
while True:
    words = 'asdadsadasda'
    list_word = words.split()
    num = [str(len(word)) for word in list_word]
    result = '-'.join(num)

    if words.isnumeric:
        break

print(result)