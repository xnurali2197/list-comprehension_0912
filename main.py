# 1
squares_1_10 = [i * i for i in range(1, 11)]
# 2
even_1_20 = [i for i in range(1, 21) if i % 2 == 0]
# 3
odd_10_30 = [i for i in range(10, 31) if i % 2 == 1]
# 4
word_lengths = [len(w) for w in ["apple", "banana", "pear"]]
# 5
letters_of_word = list("So'z")
# 6
cubes_1_5 = [i ** 3 for i in range(1, 6)]



print(squares_1_10)
print(even_1_20)
print(odd_10_30)
print(word_lengths)
print(letters_of_word)
print(cubes_1_5)
