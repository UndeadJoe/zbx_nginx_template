#!/usr/bin/python

zabbix_host = '127.0.0.1'   # Zabbix server IP
zabbix_port = 10051         # Zabbix server port
hostname = 'Zabbix Agent'   # Name of monitored host, like it shows in zabbix web ui
time_delta = 1              # grep interval in minutes

# URL to nginx stat (http_stub_status_module)
stat_url = 'https://nginx.server/nginx_stat'

# Nginx log file path
nginx_log_file_path = '/var/log/nginx/access.log'

# Optional Basic Auth
username = 'user'
password = 'pass'

# Temp file, with log file cursor position
seek_file = '/tmp/nginx_log_stat'