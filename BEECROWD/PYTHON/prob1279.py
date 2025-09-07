# year = input()

# phrase = ''
# char = [int(i) for i in year]

# if int(year) % 4 == 0 and int(year) % 100 != 0 or int(year) % 400 == 0:
#     phrase += 'This is leap year.'

# elif sum(char) % 3 == 0 and (year[-1] == '0' or year[-1] == '5'):
#     phrase += '\nThis is huluculu festival year.'

# elif (year[-1] == '0' or year[-1] == '5') and int(year) % 11 == 0:
#     phrase += '\nThis is bulukulu festival year.'

# print(phrase)

year = input().strip()

phrase = ''
char = [int(i) for i in year]

if (int(year) % 4 == 0 and int(year) % 100 != 0) or int(year) % 400 == 0:
    phrase += 'This is leap year.\n'

if sum(char) % 3 == 0 and (year[-1] == '0' or year[-1] == '5'):
    phrase += 'This is huluculu festival year.\n'

if ((year[-1] == '0' or year[-1] == '5') and int(year) % 11 == 0
        and ((int(year) % 4 == 0 and int(year) % 100 != 0) or int(year) % 400 == 0)):
    phrase += 'This is bulukulu festival year.\n'

print(phrase.strip())
