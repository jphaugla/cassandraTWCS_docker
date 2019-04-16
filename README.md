# cassandraTWCS_docker
working with TWCS with cassandra docker container
#  create tables
```
cqlsh node0 -f src/resources/cql/DDL.txt 
```
#  run the main dsbulk load
```
./src/resources/scripts/dsbulk.sh 
```

