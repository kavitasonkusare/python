#write a python program to create a tuple with multiple data type.
my_tuple = (42, "Hello", 3.14, True, ["apple", "banana", "cherry"], None)

print("The tuple with multiple data types:", my_tuple)

print("\nAccessing elements from the tuple:")
print("First element (integer):", my_tuple[0])
print("Second element (string):", my_tuple[1])
print("Third element (float):", my_tuple[2])
print("Fourth element (boolean):", my_tuple[3])
print("Fifth element (list inside tuple):", my_tuple[4])
print("Sixth element (None):", my_tuple[5])


print("\nLength of the tuple:", len(my_tuple))


print("\nCount of 'apple' in the tuple (inside the list):", my_tuple[4].count("apple"))


print("\nIs 'Hello' present in the tuple?", "Hello" in my_tuple)
