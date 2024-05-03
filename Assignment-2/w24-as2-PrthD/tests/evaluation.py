"""
Author: Mohammadreza PourrezA
Date: 2023-07-30
"""
import sqlparse
import random
import json
from typing import Tuple, List, Set, Any
from itertools import product
from collections import defaultdict
from sqlalchemy import create_engine, text

def remove_distinct(query: str):
    toks = [t.value for t in list(sqlparse.parse(query)[0].flatten())]
    return ''.join([t for t in toks if t.lower() != 'distinct'])

def unorder_row(row: Tuple) -> Tuple:
    return tuple(sorted(row, key=lambda x: str(x) + str(type(x))))

def quick_rej(result1: List[Tuple], result2: List[Tuple], order_matters: bool) -> bool:
    s1 = [unorder_row(row) for row in result1]
    s2 = [unorder_row(row) for row in result2]
    if order_matters:
        return s1 == s2
    else:
        return set(s1) == set(s2)

def get_constraint_permutation(tab1_sets_by_columns: List[Set], result2: List[Tuple]):
    num_cols = len(result2[0])
    perm_constraints = [{i for i in range(num_cols)} for _ in range(num_cols)]
    if num_cols <= 3:
        return product(*perm_constraints)

    # we sample 20 rows and constrain the space of permutations
    for _ in range(20):
        random_tab2_row = random.choice(result2)

        for tab1_col in range(num_cols):
            for tab2_col in set(perm_constraints[tab1_col]):
                if random_tab2_row[tab2_col] not in tab1_sets_by_columns[tab1_col]:
                    perm_constraints[tab1_col].remove(tab2_col)
    return product(*perm_constraints)

# return whether two bag of relations are equivalent
def multiset_eq(l1: List, l2: List) -> bool:
    if len(l1) != len(l2):
        return False
    d = defaultdict(int)
    for e in l1:
        d[e] = d[e] + 1
    for e in l2:
        d[e] = d[e] - 1
        if d[e] < 0:
            return False
    return True

def permute_tuple(element: Tuple, perm: Tuple) -> Tuple:
    assert len(element) == len(perm)
    return tuple([element[i] for i in perm])

def postprocess(query: str) -> str:
    query = query.replace('> =', '>=').replace('< =', '<=').replace('! =', '!=')
    return query

def result_eq(result1: List[Tuple], result2: List[Tuple], order_matters: bool) -> bool:
    if len(result1) == 0 and len(result2) == 0:
        return True
    # if length is not the same, then they are definitely different bag of rows
    if len(result1) != len(result2):
        return False

    num_cols = len(result1[0])
    # if the results do not have the same number of columns, they are different
    if len(result2[0]) != num_cols:
        return False

    # unorder each row and compare whether the denotation is the same
    # this can already find most pair of denotations that are different
    if not quick_rej(result1, result2, order_matters):
        return False

    # the rest of the problem is in fact more complicated than one might think
    # we want to find a permutation of column order and a permutation of row order,
    # s.t. result_1 is the same as result_2
    # we return true if we can find such column & row permutations
    # and false if we cannot
    tab1_sets_by_columns = [{row[i] for row in result1} for i in range(num_cols)]

    # on a high level, we enumerate all possible column permutations
    # that might make result_1 == result_2
    # we decrease the size of the column permutation space by
    # the function get_constraint_permutation
    # if one of the permutation make result_1, result_2 equivalent,
    # then they are equivalent
    for perm in get_constraint_permutation(tab1_sets_by_columns, result2):
        if len(perm) != len(set(perm)):
            continue
        if num_cols == 1:
            result2_perm = result2
        else:
            result2_perm = [permute_tuple(element, perm) for element in result2]
        if order_matters:
            if result1 == result2_perm:
                return True
        else:
            # in fact the first condition must hold if the second condition holds
            # but the first is way more efficient implementation-wise
            # and we use it to quickly reject impossible candidates
            if set(result1) == set(result2_perm) and multiset_eq(result1, result2_perm):
                return True
    return False

def execute_sql_command(engine: Any, sql_command: str) -> List[Tuple]:
    """
    Execute an SQL command using the given SQLAlchemy engine.

    Parameters:
    engine (sqlalchemy.engine.Engine): The SQLAlchemy engine connected to the database.
    sql_command (str): The SQL command to be executed.

    Returns:
    list: The result of the SQL query as a list of tuples.
    """
    sql_command = sqlparse.format(sql_command, strip_comments=True).strip() # Added By Arash
    commands = sqlparse.split(sql_command) # Added By Arash
    try:
        # Establish a connection to the database
        connection = engine.connect()
        for command in commands:
        # Execute the SQL command
            result = connection.execute(text(command))

        # Close the connection
        connection.close()

        return result.fetchall()

    except Exception as e:
        # Handle any exceptions that may occur during execution
        print(f"Error occurred: {e}")
        return []
    
def json_to_list_of_tuples(input_list: List[dict]) -> List[Tuple]:
    """
    Convert a JSON object to a list of tuples.

    Parameters:
    json (dict): The JSON object to be converted.

    Returns:
    list: The list of tuples.
    """
    if not input_list:
        return []

    keys = input_list[0].keys()
    tuple_list = [tuple(d[key] for key in keys) for d in input_list]
    return tuple_list


def evaluate(db_uri: str, generated_sql: str, gold_json_path: str):
    """
    Evaluate the generated SQL query against the gold query.

    Parameters:
    db_uri (str): The URI of the database to connect to.
    generated_sql (str): The generated SQL query.
    gold_json_path (str): The path to the gold JSON file.
    """
    # Load the gold JSON file
    gold_json = []
    with open(gold_json_path, 'r') as jsonl_file:
        for line in jsonl_file:
            data = json.loads(line.strip())
            gold_json.append(data)

    # Connect to the database
    engine = create_engine('sqlite:///'+db_uri)

    # Execute the generated SQL query
    generated_sql = generated_sql.strip()

    # order_matters = 'order by' in generated_sql.lower()

    g_denotation = json_to_list_of_tuples(gold_json)
    p_denotation = execute_sql_command(engine, generated_sql)

    equivalence = result_eq(
                g_denotation,
                p_denotation,
                order_matters=False)
    return equivalence    
