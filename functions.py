def most_frequent(str1):
    dic={}
    for i in str1:
        dic[i]=dic.get(i,0)+1
    srt=sorted(dic.items(),key=lambda x:x[1], reverse=True)
    for i in srt:
        print(i[0],' = ',i[1])

word=input('Please enter a string: ')
str1=word.lower()
most_frequent(str1)
