#!/usr/bin/python
import csv
import time
import datetime

with open('src/resources/data/transactions.csv','r') as csvinput:
    with open('src/resources/data/transactionsTTL.csv', 'w') as csvoutput:
        writer = csv.writer(csvoutput, delimiter='~', lineterminator='\n')
        reader = csv.reader(csvinput, delimiter='~')

        current_time = datetime.datetime.utcnow()
        all = []
        row = next(reader)
#		adds column header
        row.append('ttl')
        row.append('timestamp')
        all.append(row)

        for row in reader:
#		get transaction_initiation_date which is column 80
#		and convert to writetime format which is microseconds since
#	        december 1 1970 
            trans_time = datetime.datetime.strptime(row[80], "%Y-%m-%d  %H:%M:%S")
#		TTL is 6 months, assuming 30 days in a month, 15552000 seconds
#			but must subract difference in seconds from transaction
#			initiation and current time
 	    trans_past_delta = (current_time - trans_time).total_seconds() 
	    ttl_seconds = max(int(15552000-trans_past_delta),1)
            row.append(ttl_seconds)
#		this is the transaction_initiation_date
            row.append(row[80])

            all.append(row)

        writer.writerows(all)
