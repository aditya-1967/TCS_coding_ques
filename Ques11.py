#convert the vowels to an uppercase in a given string using
string = input('Enter a string: ')
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
string = list(string)
for i in range(len(string)):
    if string[i] in vowels:
        string[i] = string[i].upper()
print("".join(string))
