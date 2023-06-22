arr = [0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 1, 0, 0, 0]

"""
2 -ზე დგახართ
და უნდა იპოვოთ რამდენი ნულის დაშორებითაა 1-იანი
"""
arr = [0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0]

zeros = 0
our_index = arr.index(2)

print(arr.index(1) - arr.index(2) - 1)

for i in range(our_index + 1, len(arr)):
    if arr[i] == 1:
        break
    elif arr[i] == 0:
        zeros += 1

print(f"Chvengan 1-mde aris {zeros} nuli")