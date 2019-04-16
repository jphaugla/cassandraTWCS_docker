#!/usr/bin/python
#  import necessary packages 
import datetime
import csv
import time

# connect to socket to as a server 
#  keep this open until killed
while 1:
	#  open csv file holding sensors metadata 
	filename = "src/resources/data/transaction.csv"
	f = open(filename,'r') 
	#  get current time
	current_time = str(datetime.datetime.now() )
        cntr = 0
	#   use the csv reader to parse the csv file
	csv_f = csv.reader(f,delimiter='~')
	#    loop through all the transactions in the file
	for nextTran in csv_f:
		cntr += 1
		if cntr > 1:
			depth = random.randint(1, 100) + random.random()
	#   generate random humidity set
			value = random.randint(1, 100) + random.random()
	#   sensor serial number is first column in the csv
			serial_number = nextTran[0]
	#   send to the link
	#	print 'this is serial %s' % (serial_number)
			print_string =  '%s;%s;%s;%s;%s;%s\n' % (edge_id, serial_number,value,current_time,depth,value)
			print (print_string)
        		producer.send("stream_ts", print_string)
        		producer.flush()
	time.sleep(10)
# close the client socket
