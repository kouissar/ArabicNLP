import random

from arabic_nlp import Arabic_helper




ara = Arabic_helper()

#usage for tokenize
result = ara.tokenize(u'مكتبة برمجية تجمع في طياتها خصائص ووظائف يحتاجها المبرمج للتعامل مع النصوص العربية. لكثير من وظائف النصوص العربية')
# print(result)

#usage for count_word_occurence
result2= ara.count_word_occurence(u'لا إن شعر المتنبي جيد جودة الخمر الجيدة، جميلٌ جمال الغواني الغاويات، ساحرٌ سحر بابل. كون الخمر حراماً لا يعني أن معاقريها لا ينتشون غبطةً، وكون التبغ قاتلاً لا يعني'
                                  u' أنه  يوهم مدخنيه بالمتعة.','لا')
# print(result2)


# usage for bring_verse
aya = random.randint(1,6237)
# print(aya)
link = ara.get_random_verse(aya)
# print(link[0])
# print(link[1])
# print(link[2])

# usage for get_verse
# result3 = ara.get_verse(13, 10)
# print(result3)


# full_verse = ara.getVerse(1,2)

count=ara.word_count("ذهب الطالب الى المدرسة")
print(count)