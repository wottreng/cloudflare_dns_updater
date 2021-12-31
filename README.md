# pfsense_cloudflare_wan_updater
monitors your wan address on pfense and updates cloudflare dns entry via API if ipv4 addresses dont match

## install
* ssh into your pfense OS
  * you need to turn on ssh service in pfsense web gui. SSH option is located under `System / Advanced / Admin Access`   
* download this repository: `curl -L https://github.com/wottreng/pfsense_cloudflare_wan_updater/archive/refs/heads/main.zip --output monitor.zip`
* unzip download: `unzip monitor.zip`
* remove zip file: `rm monitor.zip`
* make script excutable: `cd pfsense_cloudflare_wan_updater/wan_addr_monitor && chmod 770 main.py`
* donwload python requests: `curl -L https://github.com/psf/requests/archive/refs/heads/main.zip --output requests.zip`
* unzip download: `unzip requests.zip`
* remove zipfile: `rm requests.zip`
* install python requests: `cd requests-main && python3.8 setup.py install`
* install nano: `pkg install nano`
* edit crontab: `nano /etc/crontab` and add `*/5	*	*	*	*	root	/root/pfsense_cloudflare_wan_updater/wan_addr_monitor/main.py`
  * this runs the service every 5 minutes
* restart cron: `service cron stop && service cron start` 



Cheers,
Mark  🍺



## Depricated commands:
* run it `nohup /root/pfsense_cloudflare_wan_updater/wan_monitor/main.py &`
