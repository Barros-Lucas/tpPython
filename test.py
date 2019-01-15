import copy
from ListePriorite import ListePriorite

daltons = ListePriorite()
print(daltons.empty)  # True
print(f"priorité min = {daltons.prio_min}, priorité max = {daltons.prio_max}")  # None, None

daltons.add(5, "Joe")
daltons.add(1, "Jack")
daltons.add(3, "Averell")
daltons.add(4, "William")
daltons.add(1, "Ma")
daltons.add(10, "Jack")

print(daltons.contains("Lucky Luke"))  # False
print(daltons.contains("Averell"))  # True

print(daltons.priorities_of("Jack"))  # [1, 10]

daltons.pop()  # Supprime le dernier élément (10, "Jack")

print(daltons)  # [(1, 'Jack'), (1, 'Ma'), (3, 'Averell'),
#  (4, 'William'), (5, 'Joe')]

print(f"priorité min = {daltons.prio_min}, priorité max = {daltons.prio_max}")  # 1, 5

for elt in daltons.items():
    print(elt, end=", ")  # ((1, 'Jack'), (1, 'Ma'), (3, 'Averell'),
#  (4, 'William'), (5, 'Joe'),
print()

for val in daltons.vals():
    print(val, end=", ")  # Jack, Ma, Averell, William, Joe,
print()

print(daltons.length)  # 5

print(daltons.at(0))  # (1, "Jack")

val = daltons.pop()
print(daltons)  # [(1, 'Jack'), (1, 'Ma'), (3, 'Averell'), (4, 'William')]
print(val)  # (5, 'Joe')

print(f"priorité min = {daltons.prio_min}, priorité max = {daltons.prio_max}")  # 1, 4

outlaws = copy.deepcopy(daltons)
daltons.delete(0)
print(daltons)    # [(1, 'Ma'), (3, 'Averell'), (4, 'William')]
print(outlaws)    # [(1, 'Jack'), (1, 'Ma'), (3, 'Averell'), (4, 'William')]
