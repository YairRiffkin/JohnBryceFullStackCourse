# def divide_3 (number):
#     if not number % 3:
#         return True
#     else:
#         return False
# my_number = 6
# print(my_number % 3)
# print("is the number {} dividable by 3".format(my_number), divide_3(my_number))
# for i in range(10):
#     print(i+1)
# i = 1
# while i < 11:
#     print(i, end= " ")
#     i +=1
# i = []
# i = [i for i in range(0, 101, 2)]
# print(i)
# def reverse_string(text_1):
#     return text_1[::-1]
# print(reverse_string("qwert"))
#### / exercise 5 / ####
fruits = ["apple", "pear", "apricot", "bananna", "orange"]
colors = ["red", "green", "purple", "yellow", "orange"]
my_dict = dict.fromkeys(fruits)
for i in range(5):
    my_dict[fruits[i]] = colors[i]
print(my_dict)
#### / exercise 6 / ####
# x = [x for x in range(10)]
# print(min(x))
#### / exercise 7 / ####
# x = [x for x in range(10)]
# print(max(x))
#### / exercise 8 / ####
# word_input = input()
# reverse_word = word_input[::-1]
# print(word_input == reverse_word)
#### / exercise 9 / ####
# x = "wedcvbgggngfcvbgtre"
# print(x.count("g"))
#### / exercise 10 / ####
# from random import randint
# my_string = []
# for i in range(20):
#     x = randint(97,122)
#     my_string.append(chr(x))
# print(my_string)
# vowels = ["a", "e", "i", "o", "u"]
# for i in vowels:
#     count = my_string.count(i)
#     print("There are {} occurences of {} in the list".format(count, i))
#### / exercise 11 / ####
# x = int(input())
# i = [i for i in range(x, x * 10 + 1, x)]
# print(i)
#### / exercise 12 / ####
# my_string = input()
# output = my_string.rsplit(" ")
# print(output)
#### / exercise 13 / ####
# string1 = [1, 1, 1, 1, 1, 5, 1, 4, 3]
# i = 0
# while i < len(string1):
#     print("string", string1)
#     print("i", i, string1[i])
#     if string1.count(string1[i]) > 1:
#         print("count", string1.count(string1[i]))
#         string1.pop(i)
#     else:
#         i += 1
# print("as is without duplicates", string1)
# print("sorted without duplicates", sorted(string1))
#### / exercise 14 / ####
# def longest():
#     sentence = input()
#     splited = sentence.rsplit(" ")
#     long_word = splited[0]
#     for i in splited:
#         if len(i) > len(long_word):
#             long_word = i
#     return long_word
# print(longest())    
#### / exercise 15 / ####
# this_sum = 0
# for i in range(1, 1000):
#     if not i % 3 or not i % 5:
#         this_sum = this_sum + i
# print(this_sum)

#### / exercise 16 / ####

# for i in range(1, 101):
#     if not i % 7: print(i)

#### / exercise 18 / ####

# def even_odd(number):
#     if number % 2:
#         print("{} is an odd number".format(number))
#     else:
#         print("{} is an even number".format(number))
# x = int(input())
# even_odd(x)

#### / exercise 21 / ####

# x = int(input())
# for i in range(x):
#     print("*" * (i+1)) 

#### / exercise 28 / ####

# for i in range (1, 10000):
#     if not i % 6 and not i % 7 and not i % 8 and not i % 9 and not i % 10:
#         print(i)
#         exit()

#### / exercise 29 / ####

word = input()
word = list(word)
print(word, len(word))
my_dict = dict.fromkeys(word)


for i in range(len(word)):
    my_dict[word[i]] = word.count(word[i])

print(my_dict)

