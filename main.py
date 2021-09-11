from tweet import TweetQ
from ayahat import Ayah
from poems import *

import hadiths
import random
import schedule
import time

TWEET_SIZE = 280
AYAHAT_SIZE = 6236

# time in mins : runs every 3h
TIME = 180

def post_tweets():
    """POST a tweet to the twitter API"""

    # random 
    chos = random.randint(1, 3)

    res = ensure_get(chos)
    #print(f"Message: {res} ,Size:{len(res)}")

    #More Error handling, in case of something went wrong, CASE: res size == 0
    if res is not None:
        if len(res) > 0:
            t = TweetQ()
            t.tweet(res)

def ensure_get(search_key):
    """Ensure getting a valid response, when size exceeds the tweet's size"""

    valid_response = False

    while not valid_response:

        #Ayah
        if search_key == 1:
            in_quran = random.randint(1, AYAHAT_SIZE)
            res = Ayah(in_quran).get_ayah()

            if check_size(res):
                valid_response = True
        
        #Hadith
        if search_key == 2:
            # getting the hadith
            req_hadith = hadiths.request_hadith()
            res = hadiths.format_hadith(req_hadith)

            if res is None:
                return

            if check_size(res):
                valid_response = True
            else:
                # To avoid too many requests
                time.sleep(8)

        if search_key == 3:

            # getting poem
            #res = get_random_lines(5)
            res = generate_poem()

            if res:
                if check_size(str(res)):
                    valid_response = True

    return res

def check_size(msg):
    """Check the size of the tweet"""

    if len(msg) > TWEET_SIZE:
        return False
    return True


# run the function job() every X minutes 
schedule.every(TIME).minutes.do(post_tweets)

try:
    while True:
        schedule.run_pending()
except Exception as e:
    print(f"Error: {e}")
