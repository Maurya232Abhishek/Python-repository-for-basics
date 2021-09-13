from nltk.corpus import stopwords as sw
"""words=[] #55532500887
count=[]

dict={}
while True:
    #sort

    for i in range(1, len(count)):
        #print(i, count)
        tempc = count[i]
        tempw = words[i]
        j = i - 1
        while j >= 0:
            if count[j] > tempc:
                count[j + 1] = count[j]
                words[j + 1] = words[j]
            else:
                break
            j -= 1
        j += 1
        #print(i, j, tempc)
        count[j] = tempc
        words[j] = tempw

    if len(words) >= 5:
        print("Trending:\n",words[-1],":",count[-1]," ",words[-2],":",count[-2]," ",words[-3],":",count[-3]," ",words[-4],":",count[-4]," ",words[-5],":",count[-5]," ")
    x = input("Enter the word: ")
    if x in sw.words('english'):
        continue
    if x == "0":
        break
    if x not in words:
        dict[x] = 1
        words=[x] + words
        count=[1] + count
    else:
        flag = -1
        dict[x] += 1
        for i in range(len(words)):
            if words[i] == x:
                flag = i
        if flag != -1:
            count[flag] += 1
            tempc = flag
        
print(dict)
print(words)
print(count)"""

"""max1 = 0
word1 = ""
max2 = 0
word2 = ""
max3 = 0
word3 = ""
max4 = 0
word4 = ""
max5 = 0
word5 = """""
dict={}
n=7 # n top words
max=[]
word =[]
for i in range(n):
    max.append(0)
    word.append("")

while True:
    print("Trending")
    for i in range(n):
        print(word[i],":",max[i])
    x = input("Enter the words:")
    x = x.strip()
    if x in sw.words('english'):
        continue
    if x == "0":
        break
    if x not in dict.keys():
        dict[x] = 1
    else:
        dict[x] += 1
    tempw = x
    tempc = dict[x]

    if tempw in word:
        if word[0] == tempw:
            max[0] = dict[tempw]
        else:
            pos = -1
            for i in range(n):
                if tempw == word[i]:
                    pos=i
                    break

            j=pos-1
            while j>=0:
                if max[j]>=tempc:
                    break
                max[j+1]=max[j]
                word[j+1] = word[j]
                j -= 1
            j+=1
            lmax[j]=tempc
            word[j]=tempw
    else:
        for i in range(n):
            if tempc > max[i]:
                w=tempw
                c=tempc
                tempw=word[i]
                tempc=max[i]
                max[i] = c
                word[i] = w
                if tempw == w:
                    break

print(max)
print(word)



