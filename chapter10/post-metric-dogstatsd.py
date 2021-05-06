# post-metric-dogstatsd.py  

import time 
import random 

from datadog import initialize, statsd 

options = { 
    'statsd_host':'127.0.0.1', 
    'statsd_port':8125 
} 

initialize(**options) 

while(1): 
  # Get a random number to mimic the outdoor temperature. 
  temp = random.randrange(50,70) 
  statsd.gauge( 
'statsd_test.outdoor_temp', temp,  
tags=["metric-source:dogstatsd"] 

  ) 

  time.sleep(10) 
