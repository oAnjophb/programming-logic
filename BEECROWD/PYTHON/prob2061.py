
qtyInitPages, qtyActions= map(int, input().split())

for _ in range(qtyActions):

    action = input()

    if action == 'fechou':
        qtyInitPages += 1

    if action == 'clicou':
        qtyInitPages -= 1

print(qtyInitPages)