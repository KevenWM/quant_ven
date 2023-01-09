import PyPDF2 as p2
import pandas as pd

#EMPRESA#

ticker = "pcar3"

url = r'C:/Users/keven.mendes/Desktop/Python Algos/BuzzWord/'+ticker+'.pdf'

pdf = open(url, 'rb')

pdf_reader = p2.PdfFileReader(pdf)

n = pdf_reader.numPages

a = "INICIO"
for i in range(n):
    pageObj = pdf_reader.getPage(i-1)
    words = pageObj.extractText()
    a = a + " " + str(words)

a = a.lower()

new_a = ""
for char in a:
    if char not in ('.', ")", "(", ",", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "-", "%", ":", ";", "@", "'", "/", "", "&", "$", "#", "+", "-"):
        new_a += char

new_b = ' '.join([w for w in new_a.split() if len(w) > 2])

words_list = new_b.split()

words_to_remove = ['com', 'que', 'das', 'dos', 'por', 'nos', 'pela', 'para', 'sobre', 'nas',
                   'foi', 'como', 'sendo', 'pelo', 'uma', 'sua', 'sem', 'aos', 'são', 'vez', 'deve', 'está', 'além', 'foram', 'entre']

for occur in words_to_remove:
    while occur in words_list:
        words_list.remove(occur)

d = {}

for word in words_list:
    d[word] = d.get(word, 0) + 1

word_freq = []
for key, value in d.items():
    word_freq.append((value, key))

word_freq.sort(reverse=True)

df = pd.DataFrame(word_freq, columns=['Frequência', 'Palavra'])

url_exp = r'C:/Users/keven.mendes/Desktop/Python Algos/BuzzWord/export_'+ticker+'.xlsx'

df.to_excel(url_exp,
            index=False, header=True)
