# cassandraTWCS_docker
working with TWCS with cassandra docker container
# important piece is the time windowed compaction turned on in the DDL.txt file
# additionally important, is a setting in the ddl to "split_during_flush"
#  create tables
```
cqlsh node0 -f src/resources/cql/DDL.txt 
```
#  run the main dsbulk load
```
./src/resources/scripts/dsbulk.sh 
```

