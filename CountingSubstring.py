def count_substring(string,substring):
    word_length = len(substring)

    if substring not in string:
        return 0
    else:
        count=0
        while substring in string:
            try:
                count+=1
                new_index=string.index(substring)+1
                string=string[new_index:]
                                         
            except:
                break
        return count

if __name__ == "__main__":
    string=input("Enter a string : ")
    substring=input("Enter the substring to find within the string : ")
    frequency=(count_substring(string, substring))

    if frequency==1:
        print("The string is found 1 time")
    else:
        print("The string is found {} times".format(frequency)) 