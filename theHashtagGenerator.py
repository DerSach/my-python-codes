#Codewars - 5 kyu
#The marketing team is spending way too much time typing in hashtags.
#Let's help them with our own Hashtag Generator!

#Here's the deal:

#    It must start with a hashtag (#).
#    All words must have their first letter capitalized.
#    If the final result is longer than 140 chars it must return false.
#    If the input or the result is an empty string it must return false.




def generate_hashtag(s):
    if s == "":
        return False
    words = s.strip().split()
    for i in range(len(words)):
        words[i]=words[i].capitalize()
    hashtag = '#'+''.join(words)
    if len(hashtag)>140:
        return False
    return hashtag
