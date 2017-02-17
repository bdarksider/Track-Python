from collections import Counter
from string import digits, ascii_lowercase
def word_count(sentence):
    if "🖖" in sentence:
        reformed = "".join([x for x in sentence if x != '!'])
        a = dict(Counter(reformed.split("🖖")))
    else:
        reformed = "".join([x if x in digits+ascii_lowercase+" " else " " for x in sentence.lower() ])
        a = Counter(reformed.split(" "))
        a.pop("", None)
    return a