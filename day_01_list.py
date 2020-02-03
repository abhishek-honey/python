lst = list()
lst.append('reverse')
lst.append('pop')
lst.append('sort')
lst.append('remove')
lst.append('index')
lst.append('clear')
lst.append('copy')
lst.append('count')
lst.append('extend')
lst.append('insert')
lst.sort()
print("Original lst\t\t\t\t\t:-\t", lst)

# lst.clear()

print("Copy of the lst\t\t\t\t\t:-\t", lst.copy())

count_of_copy = lst.count("copy")
print("Count of <copy>\t\t\t\t\t:-\t", count_of_copy)

lst.extend(["append"])
print("Added <append> to the list \t\t:-\t", lst)

index_of_append = lst.index("append")
print("Index of <append>\t\t\t\t:-\t", index_of_append)

lst.pop()
print("Popped a element from the list\t:-\t", lst)

lst.insert(11, "append")
print("Inserted append at 10th index\t:-\t", lst)

lst.remove("append")
print("Removed <append> from the list\t:-\t", lst)

lst.reverse()
print("Reversed the list\t\t\t\t:-\t", lst)

int_lst_1 = list([0, 1, 2, 3, 4])
int_lst_2 = list([9, 8, 7, 6, 5])

print(sum(int_lst_1))
print([sum(pair) for pair in zip(int_lst_1, int_lst_2)])

