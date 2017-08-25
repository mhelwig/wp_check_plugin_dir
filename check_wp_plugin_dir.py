#!/usr/bin/python

'''
check_wp_plugin_dir

Usage: python check_wp_plugin_dir.py path/to/plugin/directory

Checks all directory names against wpvulndb.com API and lists vulnerabilities

Author: Michael Helwig (@c0dmtr1x)
License: None / Free to use
'''

import sys,os,requests,json

api="https://wpvulndb.com/api/v2/plugins/"

contents = os.listdir(sys.argv[1])
for element in contents:
    if os.path.isdir(os.path.join(sys.argv[1],element)):
        url = api + element 
        response = requests.get(url, verify=False)
        if response.ok:
            data = response.json()
            data = json.JSONDecoder('utf-8').decode(response.text)
            print "[+] " + element
            for vuln in data[element]["vulnerabilities"]:
                print "     * " + "[" + vuln.get("vuln_type") + "] " + vuln.get("title")
                print ("        Fixed in: " + vuln.get("fixed_in") if vuln.get("fixed_in") else "        ")  + (" - Published on: " + vuln.get("published_date") if vuln.get("published_date") else "")
                if "references" in vuln.keys() and isinstance(vuln.get("references"),dict) and "url" in vuln.get("references").keys():
                    for url in vuln.get("references").get("url"):
                        print "        + " + url
            if len(vuln) == 0:
                print "       No vulnerabilities found." 
        else:
            print "[-] No results for " + element

    print ""
