numbers = [1, 2, 3, 4, 5]
numbers.append(6)  # Adding an element to the end of the list
numbers.insert(0, 6)  # Inserting 6 element at the 0 index of the list
numbers[0] = 0  # Modifying the first element of the list
numbers[-2]# access the second-to-last element of the list
numbers[-1]  # access the last element of the list
numbers.remove(3)  # Removing the element with value 3 from the list
numbers.pop()  # Removing the last element from the list
numbers.pop(0)  # Removing the first element from the list
numbers.index(4)  # Finding the index of the element with value 4
numbers.count(2)  # Counting how many times the value 2 appears in the list
numbers.sort()  # Sorting the list in ascending order   
numbers.reverse()  # Reversing the order of the list
print(numbers)  # Output the final state of the list