def ispalindrom(str):
    if str == str[::-1]:
        return str

list_of_strings = ['aba', 'bababab', 'dsf', 'kekllol']
palindrom_list = list(filter(ispalindrom, list_of_strings))

print(palindrom_list)