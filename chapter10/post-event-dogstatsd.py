# post-event-dogstatsd.py  

from datadog import initialize, statsd 

options = { 
    'statsd_host':'127.0.0.1', 
    'statsd_port':8125 
} 

initialize(**options) 

title = "An event testing DogStatsD API" 
text = "The DogStatsD API works fine! Just wanted to confirm it." 
tags = ["event-source:dogstatsd-test"] 

statsd.event(title, text, alert_type='info', tags=tags) 
