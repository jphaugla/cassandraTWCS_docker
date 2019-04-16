#!/usr/bin/env python
import time
import datetime
s = "19/10/2016 12:29:07"
utc_time = datetime.datetime.strptime(s, "%d/%m/%Y  %H:%M:%S")
init_time = datetime.datetime(1970, 1, 1)
delta_diff = (utc_time - init_time)
seconds=delta_diff.total_seconds() 
print (int(seconds*1000000))
