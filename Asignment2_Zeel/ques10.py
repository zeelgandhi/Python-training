dict = {}
with open ("ques10.txt") as file:
    for line in file:
        key = line.split()
        print(key)
words = {}
for word in dict:
    if word in words:
        words[word]=1
    else:
        words[word] = words[word]+1
        print(words)
