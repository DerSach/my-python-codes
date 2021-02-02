#Codewars - 6 kyu
#Let's assume that a song consists of some number of words (that don't contain WUB).
#To make the dubstep remix of this song, the DJ inserts a certain number of words "WUB" before the first word of the
#song (the number may be zero), after the last word (the number may be zero), and between words (at least one
#between any pair of neighbouring words), and then the boy glues together all the words, including "WUB",
#in one string and plays the song at the club.
#For example, a song with words "I AM X" can transform into a dubstep remix as "WUBWUBIWUBAMWUBWUBX" and cannot
#transform into "WUBWUBIAMWUBX".
#Input
#   The input consists of a single non-empty string, consisting only of uppercase English letters,
#the string's length doesn't exceed 200 characters
#Output
# Return the words of the initial song that Polycarpus used to make a dubsteb remix.
#Separate the words with a space.


import re
def song_decoder(song):
    return re.compile(r'(WUB)+').sub(' ',song).strip()
