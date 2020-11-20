import os
Word = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

def wordconvert(n):
    if n < 10:
        return Word[n]
    elif n >= 1_000_000_000:
        return wordconvert(n // 1_000_000_000) + ' billion ' + (wordconvert(n % 1_000_000_000) if n % 1_000_000 != 0 else '')
    elif n >= 1_000_000:
        return wordconvert(n // 1_000_000) + ' million ' + (wordconvert(n % 1_000_000) if n % 1_000_000 != 0 else '')
    elif n >= 1000:
        if n // 1000 == 1:
            return " one thousand" + (wordconvert(n % 1_000) if n % 1_000 != 0 else '')
        else:
            return wordconvert(n // 1_000) + " thousand " + (wordconvert(n % 1_000) if n % 1_000 != 0 else '')
    elif n >= 100:
        if n // 100 == 1:
            return ' one hundred ' + (wordconvert(n % 100) if n % 100 != 0 else '')
        else:
            return wordconvert(n // 100) + ' hundred ' + (wordconvert(n % 100) if n % 100 != 0 else '')
    elif n >= 20:
        if n // 10 == 2:
            return ' twenty ' + (wordconvert(n % 10) if n % 10 != 0 else '')
        if n // 10 == 3:
            return ' thirty ' + (wordconvert(n % 10) if n % 10 != 0 else '')
        if n // 10 == 4:
            return ' fourty ' + (wordconvert(n % 10) if n % 10 != 0 else '')
        if n // 10 == 5:
            return ' fifty ' + (wordconvert(n % 10) if n % 10 != 0 else '')
        if n // 10 == 8:
            return ' eighty' + (wordconvert(n % 10) if n % 10 != 0 else '')
        else:
            return wordconvert(n // 10) + 'ty' + (wordconvert(n % 10) if n % 10 !=0 else '')
    else:
        if n == 10:
            return ' ten'
        elif n == 11:
            return ' eleven'
        elif n == 12:
            return ' twelve'
        elif n == 13:
            return ' thirteen'
        elif n == 15:
            return ' fifteen'
        elif n == 18:
            return ' eighteen'
        else:
            return wordconvert(n % 10) + 'teen'        

while True:
    os.system('cls')
    print("Numbers Convert to Words")
    print("---------------------------")
    try:
        n = int(input('Numbers Pliss.. : '))
        print(f'{n:,} = {wordconvert(n)}')
    except:
        print('Please input "NUMBERS" you UNDERSTAND!')
    
    while True:
        ulang = input('Repeat?[y/n] ? ').lower()
        if ulang in ('y', 'n'):
            break
    if ulang == 'n':
        print("Thank you for using This Converter")
        break    
    os.system('pause')