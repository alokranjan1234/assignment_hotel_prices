from apify_client import ApifyClient
import json
import os
from dotenv import load_dotenv
from scraper_configs import ACTOR_DICT
from pymongo import MongoClient
from datetime import datetime,timezone

def run_scraper(site,scraper_actor, custom_params=None):
    # Load environment variables
    load_dotenv(override=True)

    # Initialize the ApifyClient with your API token
    client = ApifyClient(os.getenv('APIFY_API_TOKEN'))

    # Get scraper configuration
    scraper_config = ACTOR_DICT.get(site,{}).get(scraper_actor)
    if not scraper_config:
        raise ValueError(f"Scraper '{scraper_actor}' not found in configuration.")

    # Merge default params with custom params
    run_input = scraper_config['params'].copy()
    if custom_params:
        add_params = {}
        for key in custom_params:
            custom_key = scraper_config.get("custom_params_map",{}).get(key)
            if custom_key:
                add_params[custom_key] = custom_params[key]
            else:
                add_params[key] = custom_params[key]
        run_input.update(custom_params)

    # Run the Actor
    run = client.actor(scraper_config['name']).call(run_input=run_input)

    try:
        print(run['statusMessage'])
    except:
        pass
    # Fetch and return Actor results from the run's dataset
    return client.dataset(run["defaultDatasetId"]).iterate_items()

def save_to_mongodb(data, site, scraper_actor):
    # Connect to MongoDB
    mongo_client = MongoClient(os.getenv('MONGODB_URI'))
    db = mongo_client[os.getenv('MONGODB_DB_NAME')]
    collection = db[site]

    # Add timestamp to the data
    data['timestamp'] = str(datetime.now(timezone.utc))

    # Insert the data into MongoDB
    data['actor'] = scraper_actor
    result = collection.insert_one(data)
    print(f"Inserted document with ID: {result.inserted_id}")

if __name__ == "__main__":

    # Example usage
    site ="expedia"
    scraper_actor = "jupri_expedia_hotels"
    custom_params = {
        "limit": 1000,
        "location": "Helsinki",
    }

    results = run_scraper(site,scraper_actor, custom_params)
    for item in results:
        save_to_mongodb(item, site, scraper_actor)