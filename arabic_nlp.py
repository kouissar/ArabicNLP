import string

import pyarabic.araby as araby
import pyarabic.number as number
import random
import requests
import nltk
import pyarabic.named as named


class Arabic_helper:

    def tokenize(self, text):
        words = araby.tokenize(text)
        return words

    def count_word_occurence(self, text, word):
        count = text.count(word)
        return count

    def getVerse(self, surah, verse):
        url = 'http://api.alquran.cloud/v1/ayah/' + str(surah) + ':' + str(verse)
        # url2 = 'http://api.alquran.cloud/ayah/'+ str(surah) + ':' + str(verse) +'/editions/quran-uthmani,en.pickthall'
        json_data = requests.get(url).json()
        # print(json_data)
        verse_a = json_data['data']['text']
        # json_data = requests.get(url2).json()
        # verse_e= json_data['data']['text']
        print(verse_a)
        return verse_a



############################################################
# This code displays random verse from the Quran both in   #
# Arabic original and English translation (Pickthall)      #
# -------------------------------------------------------- #
# API from http://api.alquran.cloud                        #
# Author: Abdul Baqi                                       #
# Date: Oct 2018                                           #
# ##########################################################

# This function takes a random number
# between 1 and 6237 (which are the total number of verses in the Quran
# and returns:
# verse_a : verse in arabic
# verse_en: verse in English (Pickthall translation)
# sura: Name of surah in english, then number of sura and after : the number of verse
# example: Taa-Haa(20):108

    def get_random_verse(self, verse):
        url = 'http://api.alquran.cloud/ayah/' + str(verse) + '/editions/quran-uthmani,en.pickthall'
        #print(url)
        json_data = requests.get(url).json()
        print(json_data)
        verse_a = json_data['data'][0]['text']
        verse_en = json_data['data'][1]['text']
        sura = json_data['data'][0]['surah']['name']
        sura_en = json_data['data'][0]['surah']['englishName']
        number = json_data['data'][0]['surah']['number']
        number_in_sura=json_data['data'][0]['numberInSurah']
        page=json_data['data'][0]['page']

        # sura = json_data['data'][0]['surah']['englishName'] + \
        #        '(' + str(json_data['data'][0]['surah']['number']) + '):' + \
        #        str(json_data['data'][0]['numberInSurah'])
        type= json_data['data'][0]['surah']['revelationType']
        return [verse_a, verse_en, sura, sura_en, number, number_in_sura, type, page]

    def get_verse(self, surah, verse):
        url = 'http://api.alquran.cloud/v1/ayah/' + str(surah) + ':' + str(verse)
        #url2 = 'http://api.alquran.cloud/ayah/'+ str(surah) + ':' + str(verse) +'/editions/quran-uthmani,en.pickthall'
        json_data = requests.get(url).json()
        # print(json_data)
        verse_a = json_data['data']['text']
        #json_data = requests.get(url2).json()
        #verse_e= json_data['data']['text']
        # print(verse_a)
        return verse_a
       # print(verse_e)

    def word_count(self, str):
       words=str.split(" ")
       count = len(words)
       return count

    def freq_dist(self, str):
        words = araby.tokenize(str)
        # print(words)
        freq = nltk.FreqDist(words)
        for key, val in freq.items():
            print(str(key) + ':' + str(val))
        return str(key) + ':' + str(val)

    def get_name(self, str):
        names=named.extract_named(str)
        return names

    def get_letter_count(self, str):
        lcount= len(str)
        return lcount