# You are given n words. Some words may repeat. For each word, output its number of occurrences. 
# The output order should correspond with the input order of appearance of the word. See the sample input/output for clarification.
# Note: Each input line ends with a "\n" character

# Input Format
# The first line contains the integer, .
# The next  lines each contain a word.

# Output Format
# Output  lines.
# On the first line, output the number of distinct words from the input.
# On the second line, output the number of occurrences for each distinct word according to their appearance in the input.

def get_words(num_words):
    word_entries=[]
    for i in range(num_words):
        word=input()
        word_entries.append(word)
    return word_entries

def get_frequency(words):
    result={}
    for word in words:
        if word not in result:
            result[word]=0
        result[word]+=1
    return result

if __name__ == "__main__":
    
    num_words=int(input())
    words=get_words(num_words)
    frequency=get_frequency(words)

    distinct=len(frequency.keys())
    output_string=[str(i) for i in frequency.values()]
    
    print(distinct)
    print(', '.join(output_string))

 