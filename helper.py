import requests


class ArabicHelp():

    def __init__(self, surah, verse):
        self.surah = surah
        self.verse = verse


    def getVerse(self):
        url = 'http://api.alquran.cloud/v1/ayah/' + str(self.surah) + ':' + str(self.verse)
        # url2 = 'http://api.alquran.cloud/ayah/'+ str(surah) + ':' + str(verse) +'/editions/quran-uthmani,en.pickthall'
        json_data = requests.get(url).json()
        # print(json_data)
        verse_a = json_data['data']['text']
        # json_data = requests.get(url2).json()
        # verse_e= json_data['data']['text']
        print(verse_a)
        return verse_a




