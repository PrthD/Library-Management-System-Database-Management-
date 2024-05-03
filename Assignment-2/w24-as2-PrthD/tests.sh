# pip install sqlparse==0.4.4
# pip install SQLAlchemy==2.0.19



#!/bin/bash
for i in 1 2 3 4 5 6 7 8 9 10
do
	echo "Testing Query $i"
	rm -rf tests/run_dbs
	mkdir -p tests/run_dbs
	cp -r tests/dbs/* tests/run_dbs/
	sh tests/run_query.sh $i
done

