# QuranTweety

A very simple python script to post Quran verses on twitter every X mins

Use Environment Variables To pass the secret keys to the script, you can obtain them from twitter's dev site.
The script make use of this awesome api : ```http://api.alquran.cloud/v1/ayah/...```

# Instalation

* To use twitter api:
  * ```pip install python-twitter```
* Install ```schedule``` to post every ```X``` mins or so:
  * ```pip install schedule```


# Features 

* Posts quran
* Posts hadith
* Generates poetry, special thanks to: [@hayderkharrufa](https://github.com/hayderkharrufa) for his cool vid :D, and ofc [@CodingTrain](https://github.com/CodingTrain).


# Resources 

* [Twitter's Api](https://developer.twitter.com/en/docs/twitter-api/v1/tweets/post-and-engage/overview)
* [Markov Chains](https://www.youtube.com/watch?v=eGFJ8vugIWA)


### ToDo
* more error handling 
* save send tweet's info (id, text, ...) for further plans like deleting and other stuff 
* more about twitter's API
