# cloudflare_wan_updater
monitors your wan address on router/edge system and updates cloudflare dns entry via API if ipv4 addresses dont match

## install
* ssh into your router/edge OS
* download this repository: `curl -L https://github.com/wottreng/cloudflare_wan_updater/archive/refs/heads/main.zip --output monitor.zip`
* unzip download: `unzip monitor.zip`
* remove zip file: `rm monitor.zip`
* make script excutable: `cd cloudflare_wan_updater/wan_addr_monitor && chmod 770 main.py`
* donwload python requests: `curl -L https://github.com/psf/requests/archive/refs/heads/main.zip --output requests.zip`
* unzip download: `unzip requests.zip`
* remove zipfile: `rm requests.zip`
* install python requests: `cd requests-main && python3.8 setup.py install`
* install nano: `pkg install nano`
* edit crontab: `nano /etc/crontab` and add `*/5	*	*	*	*	root	/root/cloudflare_wan_updater/wan_addr_monitor/main.py`
  * this runs the service every 5 minutes
* restart cron: `service cron stop && service cron start` 



Cheers,
Mark  🍺



## Depricated commands:
* run it `nohup /root/cloudflare_wan_updater/wan_monitor/main.py &`
