# Let's create a function that turns text into pig latin: a simple text transformation that modifies each word
# moving the first character to the end and appending "ay" to the end. 
# For example, python ends up as ythonpay

def pig_latin(text):

  # Separate the text into words
    say=""
    words=text.split()
    piglatin_words=[]

    for word in words:
        # Create the pig latin word and add it to the list
        updated_word = word[1:]+word[0]+"ay"
        piglatin_words.append(updated_word)

    
    for index,word in enumerate(piglatin_words):
        say+=word+" "
    return say

		
print(pig_latin("hello how are you")) # Should be "ellohay owhay reaay ouyay"
print(pig_latin("programming in python is fun")) # Should be "rogrammingpay niay ythonpay siay unfay"