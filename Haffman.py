def Hafm(dic, raspred):
    if len(dic.keys()) == 1:
        return raspred
    m1 = min(dic.values())
    char1 = ''
    for i in dic.keys():
        if(dic[i] == m1):
            char1 = i
            break
    del dic[char1]
    m2 = min(dic.values())
    char2 = ''
    for i in dic.keys():
        if(dic[i] == m2):
            char2 = i
            break
    del dic[char2]
    for i in char1:
        raspred[i] = "0" + raspred[i]
    for i in char2:
        raspred[i] = "1" + raspred[i]
    dic[char1 + char2] = m1 + m2
    return Hafm(dic, raspred)



text = "КубышкинДокажитечтоэнтропиямонеткипринимаетнаибольшеезначениедляправильноймонеткиЕфим"
text = text.lower()
chars = set(text)
alph = dict()
raspred = dict()
for char in chars:
    alph[char] = text.count(char)
    raspred[char] = ""


print(alph)

print(Hafm(alph, raspred))

