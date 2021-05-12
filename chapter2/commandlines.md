# Installing the Datadog Agent on Ubuntu
```
DD_AGENT_MAJOR_VERSION=7 DD_API_KEY=<DATADOG_API_KEY> bash -c "$(curl -L https://s3.amazonaws.com/dd-agent/scripts/install_script.sh)" 
```

# Run Datadog Agent as a Docker container
```
DOCKER_CONTENT_TRUST=1 docker run -d --name dd-agent -v /var/run/docker.sock:/var/run/docker.sock:ro -v /proc/:/host/proc/:ro -v /sys/fs/cgroup/:/host/sys/fs/cgroup:ro -e DD_API_KEY=<DATADOG_API_KEY> datadog/agent:7
```

# Steps to enable Docker integration.

# 1. Add user dd-agent to the docker OS operating system group docker: 

```
usermod -a -G docker dd-agent 
```

# There would will be a sample configuration file under /etc/datadog-agent/conf.d/docker.d/conf.yaml.example. Copy or rename this file to conf.yaml and add the following settings: 

```
init_config: 

instances: 

    - url: "unix://var/run/docker.sock" 

      new_tag_names: true 
```

# Restart the Datadog Aagent: 
```
service datadog-agent restart 
```
