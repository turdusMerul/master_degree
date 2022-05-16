# Python program to print the data
bingo_card = {
    "B": [12, 9, 14, 7, 8],
    "I": [17, 21, 28, 19, 29],
    "N": [34, 33, 34, 31, 39],
    "G": [52, 49, 59, 51, 54],
    "O": [65, 75, 68, 69, 63]
}

scheme = "{:<5} {:<5} {:<5} {:<5} {:<5}"
print(scheme.format("B", "I", "N", "G", "O"))
for nums in bingo_card.values():
    n1, n2, n3, n4, n5 = nums
    print(scheme.format(n1, n2, n3, n4, n5))