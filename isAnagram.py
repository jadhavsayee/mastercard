def isAnagram(str1, str2):

    # initialize dictionary
    freq_str1 = {}
    freq_str2 = {}

    # Compare str1 and str2 length
    if len(str1) != len(str2):
        return False
 
    # maintain counter for each character of str1 in dictionary freq_str1
    for i in range(len(str1)):
        freq_str1[str1[i]] = freq_str1.get(str1[i], 0) + 1
 
    # maintain counter for each character of str2 in dictionary freq_str2
    for i in range(len(str2)):
        freq_str2[str2[i]] = freq_str2.get(str2[i], 0) + 1
 
    # return true if dictionary freq_str1 and dictionary freq_str2 
    return freq_str1 == freq_str2

string1 = input('Enter 1st string: ')
string2 = input('Enter 2nd string: ')

print(isAnagram(string1,string2))
