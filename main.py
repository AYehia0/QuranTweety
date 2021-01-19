from tweet import TweetQ
from ayahat import Ayah
import random
import schedule

TWEET_SIZE = 280
AYAHAT_SIZE = 6236
TIME = 10

def post_tweets():
    in_quran = random.randint(1, AYAHAT_SIZE)
    ayah = Ayah(in_quran).get_ayah()
    tweet = TweetQ()

    if check_size(ayah):
        print(f"Sending : {len(ayah)} ayah")
        tweet.tweet_quran(ayah)   
    else:
        print("Can't Send (limit exceeded)")
        return

def check_size(ayah):
    if len(ayah) > 280:
        return False
    return True


# run the function job() every 5 minutes 
schedule.every(TIME).minutes.do(post_tweets)

try:
    while True:
        schedule.run_pending()
except Exception as e:
    print("Done")