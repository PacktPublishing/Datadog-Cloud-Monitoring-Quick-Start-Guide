# Based on the sample code provided in Datadog documentation. 

try: 

    from datadog_checks.base import AgentCheck 

except ImportError: 

    from checks import AgentCheck 

 

# Value set on __version__ will be shown in the Agent status page 

__version__ = "v1.0" 

 

from datadog_checks.base.utils.subprocess_output import get_subprocess_output 

 

class NginxErrorCheck(AgentCheck): 

    def check(self, instance): 

        file_info, err, retcode = get_subprocess_output(["ls", "-al","/var/log/nginx/error.log"], self.log, raise_on_empty_output=True) 

        file_size = file_info.split(" ")[4]; 

        self.gauge("kurian.nginx.error_log.size", file_size,tags=['component:nginx']) 
