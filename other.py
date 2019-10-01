from run import run_flat_json


if __name__ == "__main__":
	jobs = {
		"json_file_1.json": "csv_file_1.csv"
		"json_file_2.json": "csv_file_2.csv"
		"json_file_3.json": "csv_file_3.csv"
		"json_file_4.json": "csv_file_4.csv"
		"json_file_5.json": "csv_file_5.csv"
	}	
	for json_file, csv_file in jobs.items():
		run_flat_json(json_file, csv_file)
