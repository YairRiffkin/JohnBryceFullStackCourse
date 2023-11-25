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
# fruits = ["apple", "pear", "apricot", "bananna", "orange"]
# colors = ["red", "green", "purple", "yellow", "orange"]
# my_dict = dict.fromkeys(fruits)
# for i in range(5):
#     my_dict[fruits[i]] = colors[i]
# print(my_dict)
#### / exercise 6 / ####
# x = [x for x in range(10)]
# print(min(x))
#### / exercise 7 / ####
# x = [x for x in range(10)]
# print(max(x))
#### / exercise 8 / ####
word_input = input()
reverse_word = word_input[::-1]
print(word_input == reverse_word)