# https://www.reddit.com/r/dailyprogrammer/comments/4savyr/20160711_challenge_275_easy_splurthian_chemistry/


def check_symbol(name, symbol):
    index1 = name.find(symbol[0])
    index2 = name.find(symbol[1], index1)
    if index1 == -1 or index2 == -1:
        return"Invalid Chemical Symbol\n"
    return"Valid Chemical Symbol\n"


def bonus(name):
    symbol_list = permutations(name)
    symbol_list.sort()
    print('**** BONUS 1 AND 2 ****', end='\n \n')
    print('First symbol in alphabetical order: ' + symbol_list[0])
    print('Number of possible distinct symbols: ' + str(len(symbol_list)))


def permutations(name):
    symbol_list = []
    for i in range(len(name)):
        for j in range(i + 1, len(name)):
            symbol = name[i].upper() + name[j]
            if not symbol_list.__contains__(symbol):
                symbol_list.append(symbol)
    return symbol_list


inputName = input('Enter Chemical Name: ').lower()
inputSymbol = input('Enter Chemical Symbol: ').lower()
# Skipped the uppercase check
if len(inputSymbol) != 2:
    print('Invalid Chemical Symbol')
print(check_symbol(inputName, inputSymbol))
bonus(inputName)
