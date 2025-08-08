cases = int(input())

for _ in range(cases):
    firstWord, lastWord = map(str, input().split())

    newWord = ''
    
    for i in range(max(len(firstWord), len(lastWord))):
        newWord += firstWord[i:i+1] + lastWord[i:i+1]

    print(newWord)