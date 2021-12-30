#!/usr/bin/env python

import os
import requests
import time

debug = False

api_key = "12"
zone_id = "12"
account_id = "12"
email = "your.email@mail.com"
dns_api = "12"
url_id = "12"
ipv4_address = ""
domain_name = "yourDomain.com"
interface_name = "wan0"


def get_dns_addr_on_record():
    headers = {"Content-Type": "application/json", "X-Auth-Email": email, "X-Auth-Key": api_key}
    resp = requests.get(f"https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records/{url_id}", headers=headers).json()
    dns_record_ipv4 = resp["result"]["content"]
    if debug: print(dns_record_ipv4)
    return dns_record_ipv4


def update_dns_addr_on_record(new_ipv4_address):
    headers = {"X-Auth-Email": email, "X-Auth-Key": api_key, "Content-Type": "application/json"}
    data = {"type": "A", "name": domain_name, "content": new_ipv4_address, "ttl": "3600"}
    resp = requests.put(url=f"https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records/{url_id}", headers=headers, json=data).json()

    if debug: print(resp["result"]["content"])
    if resp["result"]["content"] == new_ipv4_address:
        return True
    else: return False

def get_current_wan_addr():
    ifconfig_output = os.popen(f"ifconfig | grep -A 5 {interface_name}").readlines()
    wan_addr = ifconfig_output[5].split()[1]
    if debug: print(wan_addr)
    return wan_addr

def get_cloudflare_account_info():
    print(os.popen(f"curl -X GET \"https://api.cloudflare.com/client/v4/zones\" \
    -H \"X-Auth-Email: {email}\" \
    -H \"X-Auth-Key: {api_key}\" \
    -H \"Content-Type: application/json\"").read())

def test_api_key():
    print(os.popen(f'curl -X GET "https://api.cloudflare.com/client/v4/user/tokens/verify" \
     -H "Authorization: Bearer {dns_api}" \
     -H "Content-Type:application/json"').read())

def compare_wan_addr_to_record_addr(ipv4_addr_to_compare):
    with open("wan_addr.txt","r") as doc:
        ipv4_address_on_record = doc.read().strip()
    if debug: print(ipv4_address_on_record)
    if ipv4_address_on_record == ipv4_addr_to_compare:
        if debug: print("true")
        return True
    else:
        if debug: print("false")
        with open("wan_addr.txt", "w") as doc:
            doc.write(ipv4_addr_to_compare)
        return False

def change_working_dir():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

def record_current_time():
    with open("lastRun.txt", "w") as doc:
        doc.write(str(time.time()).split(".")[0])

if __name__ == '__main__':
    while 1:
        change_working_dir()
        record_current_time()
        current_wan_ipv4_addr = get_current_wan_addr()
        result = compare_wan_addr_to_record_addr(current_wan_ipv4_addr)
        if result == False:
            # update dns ipv4
            update_dns_addr_on_record(current_wan_ipv4_addr)
        time.sleep(300)
