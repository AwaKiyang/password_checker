import string
#function to store set of already exist passwords from a file
def common_passwords(filename='wordlist.txt'):
    with open(filename, 'r', encoding='utf-8') as file:
        return set(line.strip() for line in file)
pass_list = common_passwords()
#function to check password strenth
def password():
    print('****Welcome to password strength checker input a password to test its strength****\nremember the following:\n\t-password length minimum 12+ charaters'
    '\n\t-At least 3 uppercase, lowercase, numbers and punctuations in your passwords\n\t-And lastly exclude common words')
    entry = input('Enter password to check for: ')
    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    numbers = string.digits
    punc = string.punctuation
    upcount = 0
    locount= 0
    numcount = 0
    puncount = 0
    for i in entry:
        if i in upper:
            upcount+=1
        if i in lower:
            locount+=1
        if i in numbers:
            numcount+=1
        if i in punc:
            puncount+=1
    damn = ['waar','bro']
#
    print(f'upercase : {upcount}, lowercase : {locount}, numbers: {numcount}, puntautions : {puncount}')
    if len(entry) < 12:
        return 'weak password increase length to 12 characters'
    if (upcount < 3 or locount < 3 or puncount < 3 or numcount < 3):
        return 'meduim password include atleast 3 (uppercase,lowercase,special_charaters and numbers)'
    if entry in pass_list:
        return 'password already in use'
    if (upcount >= 3 and locount >=3 and puncount >=3 and numcount >= 3):
        return 'perfect strong password'
#
print(password())
