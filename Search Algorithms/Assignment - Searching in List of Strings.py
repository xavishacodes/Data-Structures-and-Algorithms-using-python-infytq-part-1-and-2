#lex_auth_0127667326864670723497
#PROBLEM_STATEMENT
# Mary is a kindergarten teacher. She has given a task to the children after teaching them a list of words. The task is to find the unknown words (other than the words they already know) from the given text. Write a python function which accepts the text and the known list of words and returns the set of unknown words found.

 

# Return -1 if there are no unknown words.

 

# Sample Input

# Expected Output

# Text: "the sun rises in the east"
# Vocabulary: ["sun","in","east","doctor","day"]

# {'rises', 'the'}
import re

def find_unknown_words(text,vocabulary):
    #Remove pass and write your logic here
    # pass
    text = text.split(" ")
    unknown = []
    for word in text:
        if word not in vocabulary:
            unknown.append(word)
            
    if len(unknown)==0:
        return -1
    return set(unknown)
    # for i in vocabulary:
    #     if (len(re.findall(vocabulary,text))==0):
    #         continue
    #     else:
    #         unknown_words.append(vocabulary)
    # return unknown_words

#Pass different values of text and vocabulary to the function and test your program
text="The sun rises in the east and sets in the west."
vocabulary = ["sun","in","rises","the","east"]
unknown_words=find_unknown_words(text,vocabulary)
print("The unknown words in the file are:",unknown_words)