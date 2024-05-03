import argparse
import os
import pathlib


BASE_PATH = str(pathlib.Path(__file__).absolute().parent.parent.absolute())




def main():
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('pos_arg', type=int, help='Query number')
    args = parser.parse_args()
    q_num = args.pos_arg
    q_path = BASE_PATH + f"/Q{q_num}/details.txt"

    


    if not os.path.isfile(q_path):
        print(f"{q_path} does not exist")
        exit(1)
    

    with open(q_path, 'r') as f:
        first_line = f.readline().strip()
        if not first_line.lower().startswith("agent:"):
            print("Details file must start with 'agent:'")
            exit(1)


    
    print("  All details file tests passed")
    exit(0)




if __name__ == "__main__":
    main()
