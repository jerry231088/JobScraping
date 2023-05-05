import json


def store_data_to_json(scraped_data):
    with open('scraped_jobs_data.json', 'w') as fp:
        json.dump(scraped_data, fp)
