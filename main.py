import requests
import time

noita_gid = 752

def download_mod(did, fid):
	args = {
		'did': did,
		'fid': fid,
		'func': 'download',
	}

	response = requests.post('https://modworkshop.net/mws/api/modsapi.php', data = args)
	response.raise_for_status()

	return response

def get_mods(page, gid):
	args = {
		'page': page,
		'func': 'mods',
		'count_total': 1, # Doesn't seem to do anything
		'sort': '',
		'gid': gid
	}

	response = requests.get('https://modworkshop.net/mws/api/modsapi.php', params = args)
	response.raise_for_status()

	return response.json()

def get_mod_file_info(did):
	args = {
		'did': did,
		'func': 'files',
	}

	response = requests.get('https://modworkshop.net/mws/api/modsapi.php', params = args)
	response.raise_for_status()

	return response.json()

page = 1

workshop_list_json = get_mods(page, noita_gid)
workshop_list = workshop_list_json['content']
page += 1

while workshop_list:
	for mod in workshop_list:
		file_info_response = get_mod_file_info(mod['did'])
		time.sleep(1)

		if not file_info_response['files']:
			continue

		file_info = file_info_response['files'][0]
		download = download_mod(mod['did'], file_info['fid'])

		with open('Download/' + file_info['name'], 'wb') as fd:
			for chunk in download.iter_content(chunk_size=128):
				fd.write(chunk)

	workshop_list_json = get_mods(page, noita_gid)
	workshop_list = workshop_list_json['content']
	page += 1
