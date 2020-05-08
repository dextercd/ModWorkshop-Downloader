import requests

workshop_list_response = requests.get('https://modworkshop.net/mws/api/modsapi.php?page=1&func=mods&count_total=1&sort=&gid=752&_=1588918349135')
workshop_list_response.raise_for_status()

workshop_list_json = workshop_list_response.json()
workshop_list = workshop_list_json['content']

for mod in workshop_list:
	print(mod)
