ACTOR_DICT={
    "booking": {
        "voyager_booking_scraper": {
        "name": "voyager/booking-scraper",
        "params" : {
            "currency": "USD",
            "language": "en-gb",
            "maxItems": 10,
            "minMaxPrice": "0-999999",
            "minScore": "5",
            "propertyType": "Hotels",
            "search": "New York",
            "sortBy": "distance_from_search",
            "starsCountFilter": "any"
        }
        },
        "voyager_fast_booking_scraper": {
            "name":"voyager/fast-booking-scraper",
            "params":{
            "currency": "USD",
            "flexWindow": "0",
            "language": "en-gb",
            "maxItems": 200,
            "minMaxPrice": "5-999999",
            "minScore": "5",
            "propertyType": "Hotels",
            "rooms": 1,
            "search": "New York",
            "sortBy": "distance_from_search",
            "starsCountFilter": "any"
        }
        }

        },
    "expedia":{
        "jupri_expedia_hotels" :{
            "name": "jupri/expedia-hotels",
            "params":{
                "dev_dataset_clear": False,
                "dev_no_strip": False,
                "includes:amenities": False,
                "includes:availability": False,
                "includes:calendar": False,
                "includes:description": False,
                "includes:faq": False,
                "includes:gallery": False,
                "includes:landmarks": False,
                "includes:location": False,
                "includes:offers": False,
                "includes:policies": False,
                "includes:review": False,
                "language": "EN_US",
                "limit": 5,
                "location": "New York",
                "rewards.member_only": False,
                "rewards.vip": False,
                "site": "1",
                "types": [
                    "hotel"
                ]
            },
            "custom_params_map":{
        }   
        }
    },

    "hotels":{
        "jeremy_frost_hotels_com_scraper" : {
        "name": "jeremy_frost/hotels-com-scraper",
        "params": {
            "max_depth": 500,
            "min_stars": "0",
            "place": "Spain"
            }
        },
        "custom_params_map":{
            "limits": "max_depth",
            "place": "location"
        }
    }
}


