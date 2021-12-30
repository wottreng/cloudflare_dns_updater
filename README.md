# pfsense_cloudflare_wan_updater
monitors your wan address on pfense and updates cloudflare dns entry via API if ipv4 addresses dont match

## Notes
I tried to get cron to run this script every 5 minutes with `crontab -e` and could not get it to work. If anyone has insight let me know. 

## install
* ssh into your pfense OS
* download this repository: `curl -L https://github.com/wottreng/pfsense_cloudflare_wan_updater/archive/refs/heads/main.zip --output monitor.zip`
* unzip download: `unzip monitor.zip`
* remove zip file: `rm monitor.zip`
* make script excutable: `cd pfsense_cloudflare_wan_updater/wan_addr_monitor && chmod 770 main.py`
* donwload python requests: `curl -L https://github.com/psf/requests/archive/refs/heads/main.zip --output requests.zip`
* unzip download: `unzip requests.zip`
* remove zipfile: `rm requests.zip`
* install python requests: `cd requests-main && python3.8 setup.py install`
* run it `nohup /root/pfsense_cloudflare_wan_updater/wan_monitor/main.py &`

Cheers,
Mark  🍺
