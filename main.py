above18 = totalMen = totalWomenUnder20 = 0
while True:
    age = int(input('Age: '))
    gender = ' '
    while gender not in 'MF':
        gender = str(input('Gender: [M/F] ')).strip().upper()[0]
    if age >= 18:
        above18 += 1
    if gender == 'M':
        totalMen += 1
    if gender == 'F' and age < 20:
        totalWomenUnder20 += 1
    answer = ' '
    while answer not in 'YN':
        answer = str(input('Do you want to continue? [\033[1;32mY\033[m/\033[1;31mN\033[m] ')).strip().upper()[0]
    if answer == 'N':
        break
print(f'Total \033[1;37mPEOPLE\033[m above \033[1;32m18\033[m years old: \033[1;33m{above18}\033[m .')
print(f'Total \033[1;34mMEN\033[m registered: \033[1;33m{totalMen}\033[m .')
print(f'Total \033[1;35mWOMEN\033[m under \033[1;32m20\033[m years old: \033[1;33m{totalWomenUnder20}\033[m .')
