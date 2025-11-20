def remove_punctuation(raw:str)->str:
    return "".join([c for c in raw if c.isalnum or c==' '])
def to_lower(raw:str)->str:
    return raw.lower()
def remove_stopwords(text:str,stopwords:list[str])->str:
    word_list=text.split()
    filterword=[word for word in word_list if word not in stopwords]
    return "".join(filterword)
def pipeline(raw:str,fuction)->str:
    for f in function:
        s=f(s)
    return s
def count_words(s: str) -> dict:
    word_list = s.split()
    res = dict()
    for word in word_list:
        res[word] = res.get(word, 0) + 1
    return res
text1 = input()
print(remove_punctuation(text1))

text2 = input()
print(to_lower(text2))

text3 = input()
stopword = input().split(", ")
print(remove_stopwords(text3, stopword))

text4 = input()
stop = input().split(", ")
print(pipeline(text4,  [remove_punctuation, to_lower, lambda x: remove_stopwords(x, stop)]))

text5= input()
print(count_words(text5))