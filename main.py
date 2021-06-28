from tweet import TweetQ
from ayahat import Ayah
import hadiths
import random
import schedule

TWEET_SIZE = 280
AYAHAT_SIZE = 6236
TIME = 30

def post_tweets():
    """POST a tweet to the twitter API"""

    # random 
    #chos = random.randint(1, 3)
    chos = 1
    in_quran = random.randint(1, AYAHAT_SIZE)
    t = TweetQ()

    if chos == 1:
        # checking the ayah length
        ayah = Ayah(in_quran).get_ayah()

        if check_size(ayah):
            print("Posting Ayah")
            t.tweet(ayah)   
        else:
            print("Can't post Ayah, size")
            return

    if chos == 2:
        # getting the hadith
        req_hadith = hadiths.request_hadith()
        hadith = hadiths.format_hadith()

        # sending hadith
        if check_size(hadith):
            print("Posting Hadith")
            t.tweet(hadith)
        else:
            print("Can't post hadith, size")
            return


def check_size(msg):
    if len(msg) > 280:
        return False
    return True


# run the function job() every X minutes 
schedule.every(TIME).minutes.do(post_tweets)

try:
    while True:
        schedule.run_pending()
except Exception as e:
    print("Done")
