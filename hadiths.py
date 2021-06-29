"""
This Fetches Hadith from Sunnah API using their default key : 
    SqD712P3E82xnwOAEOkGd5JZH8s9wRR24TqNFzjk 
"""

import requests
import json

# Max tweet length : 280
max_tweet = 280

def request_hadith():
    '''Get random hadith'''

    payload = "{}"
    headers = {'x-api-key': 'SqD712P3E82xnwOAEOkGd5JZH8s9wRR24TqNFzjk'}
    url = "https://api.sunnah.com/v1/hadiths/random"

    res = requests.request("GET", url, data=payload, headers=headers)
    res_json = json.loads(res.text)

    # Here i assume no errors happen, only receiving a valid response,, gonna change it later.
    try :  
        if res_json["message"] == "Too Many Requests":
            return None
    except Exception as e:
        #No errors
        pass

    return res_json

def format_hadith(res):
    '''Return a formatted hadith from the response'''

    # Checking for errors 
    if res is None:
        return None 

    # The ar in index: 1
    hadith_body_ar = res['hadith'][1]["body"].replace("<p>", "")
    formatted_hadith =  hadith_body_ar[:len(hadith_body_ar)-4]

    return formatted_hadith.lstrip("-")



