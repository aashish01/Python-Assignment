chest = {
'42': 'It is the Answer to Life the Universe and Everything.',
'666': 'If you would be a real seeker after truth, it is necessary thatat least once in your life you doubt, as far as possible, all things.',
'8': 'It is wrong always, everywhere and for everyone, to believeanything upon insufficient evidence.',
'13': 'The Truth is in the Heart.',
'0': 'Freedom is secured not by the fulfilling of ones desires, but bythe removal of desire.',
'9': 'The unexamined life is not worth living.',
'76': 'Life is a series of natural and spontaneous changes.',
'70': 'God is dead! He remains dead! And we have killed him.'
}

# Question 1
key =list([int(i) for i in list(chest.keys())])
for j in range (len(key)):
    for i in range ( len ( key ) - 1) :
        if  key [ i ] > key [ i + 1 ] :
            key [ i ] , key [ i + 1 ] =  key [ i + 1 ] , key [ i ]

sorted_keys= key
sorted_values = [chest[str(i)] for i in sorted_keys]
sorted_dict = {str(k):v for (k,v) in zip(sorted_keys,sorted_values)}
# print(sorted_dict) #Question 1 Answer

# Question no.2
first,second,last,last_second = str(sorted_keys[0]),str(sorted_keys[1]),str(sorted_keys[-1]),str(sorted_keys[-2]) #Question 2 answer

# Question no.3
concatinated_string = sorted_dict[first] + sorted_dict[second] + sorted_dict[last] + sorted_dict[last_second]       #final answer
# print(concatinated_string) # Question 3 Answer

# Question no.4
sentences = [i for i in concatinated_string.split(".") if i!=""]
each_words = [i.split(" ") for i in sentences]
first_last_words = []
first_last_words_strings = []
for i in each_words:
    for j in i:
        x = j.replace(",","")
        temp = x[0]+x[len(x)-1]
        if "," in j:
            temp = temp+","
        first_last_words.append(temp)
    first_last_words.append(".")
    first_last_words_strings.append(first_last_words)

characters = "".join(first_last_words_strings[0]) 
# print(characters) # Question 4 Answer

# Question no.5
def get_counts():
    keys = {i for i in characters}
    all_occurances = {}
    for i in keys:
        all_occurances[i] = characters.count(i)
    number_of_occurance = sorted(all_occurances.values())[::-1][:5]
    final_result = {}
    for i in number_of_occurance:
        for j,k in zip(all_occurances.keys(),all_occurances.values()):
            if i == k:
                final_result[j] = k
    return final_result,number_of_occurance
final_result, number_of_occurance = get_counts()   
# print(get_counts()) # Question 5 Answer

# Question no.6
key_list = [52,51,61,71,58] # Question 6 Answer
result = [x+y for x,y in zip(key_list,number_of_occurance)]  # Question 7 Answer 
treasure = "".join([chr(i) for i in result]) 
print(treasure)  # Question 8 Answer






