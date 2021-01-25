import requests
import sys

#list of subdomains to use (save in program file location)
sub_list = open("subdomains-1000.txt").read()
subs = sub_list.splitlines()

#loop through subdomains via url args
for sub in subs:
	url_to_check = f"http://{sub}.{sys.argv[1]}" 

	try:
		requests.get(url_to_check)
#skip any errors
	except requests.ConnectionError:
		pass
#display valid domains
	else:
		print("Valid domain: ", url_to_check)