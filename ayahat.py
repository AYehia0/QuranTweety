import requests as rs
import json

# Ayah Totals (1 to 6236). random.randint(1,6236)
# Twitter's max size for a tweet is 280

QURAN_API = "http://api.alquran.cloud/v1/ayah/"

class Ayah:

    def __init__(self, ayah_num):

        self.ayah_number = ayah_num
        self.q_api = QURAN_API + str(self.ayah_number)

    def get_ayah(self):
        
        ayah_json = json.loads(rs.get(self.q_api).text)
        ayah_text = ayah_json['data']['text']

        return ayah_text
