# This is mean to get your started
# Accelerated Computer Science @ BDFZ Spring 2017
# Assignment: Word Counting

file = open(r"lear.txt", "r", encoding="utf-8-sig")

wordcount={}

words = file.read().lower().replace(',', '').replace('.','').replace('-',' ').replace('!','').replace('?','').replace(';','').replace('*','').replace('"','').replace("'",'').split()



for word in words:
    if word not in wordcount:
        wordcount[word] = 1
    else:
        wordcount[word] += 1

copy = []

for k,v in wordcount.items():
    copy.append((v, k))

copy = sorted(copy, reverse=True)

for k in copy:
        print (k[1], k[0])