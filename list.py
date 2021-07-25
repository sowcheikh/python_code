numbers = list(range(20))
# afficher tout les elements
print(numbers)
# afficher tout les elements inversement
print(numbers[::-1])
# afficher les elements par pas de 2
print(numbers[::2])


letters = ['a', 'b', 'c']
print(letters[0])
# add a letter
letters.append('d')
# insere one letter
letters.insert(0, 'y')
# remove
letters.pop(0)
letters.remove('b')
del letters[1]
# finding element index
print(letters)
print(letters.index("a"))


list_numbers = [3, 52, 2, 6, 9]
# afficher par ordre croissant
list_numbers.sort()
print(list_numbers)
# afficher par ordre décroissant
list_numbers.sort(reverse=True)
print(list_numbers)

items = [
    ("product1", 10),
    ("product2", 2),
    ("product3", 9),
    ("product4", 1),
]


# def sort_item(item):
#     return item[1]


items.sort(key=lambda item: item[1])
print(items)
