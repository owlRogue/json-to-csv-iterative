import requests
import json
import os

def run_flat_json(config_file, csv_file):
	# Set the rquest parameters.
	headers = {}
	headers['content-type'] = 'application/json'
	headers['authorization'] = 'Bearer Token'
	req = requests.get('URL', headers=headers)
	res_raw = req.text

	# Unparse the request json.
	res_obj = json.loads(res_raw)

	# Grap the 'data' attribute and write to file.
	data = res_obj['data']
	with open("./temp.json", "w") as f:
		f.write(json.dumps(data))

	# Use json2csv to parse the data and flatten it given the config path.
	os.system("json2csv -i ./temp.json -F /PATH/" + config_file + " > /PATH/" + csv_file)

	# Clean up temp json file.
	os.system("rm ./temp.json")

# This only runs if you run this file.
if __name__ == "__main__":
	run_flat_json("fieldsConfig.json", "curl_results-flat.csv")
