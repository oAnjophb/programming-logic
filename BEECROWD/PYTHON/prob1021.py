note_values = [10000, 5000, 2000, 1000, 500, 200]
cent_values = [100, 50, 25, 10, 5, 1]

notes = {d: 0 for d in note_values}
cents = {d: 0 for d in cent_values}

value = int(input().replace('.', ''))

for d in note_values:
    q = value // d
    notes[d] = q    
    value -= q * d

for d in cent_values:
    q = value // d
    cents[d] = q
    value -= q * d

print("NOTAS:")
for d in note_values:
    print(f"{notes[d]} nota(s) de R$ {d/100:.2f}")

print("MOEDAS:")
for d in cent_values:
    print(f"{cents[d]} moeda(s) de R$ {d/100:.2f}")
