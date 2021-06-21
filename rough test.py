# import random
#
# nums = list(range(1, 49))
# random.shuffle(nums)
# lotto_draw = nums[:6]
# print(lotto_draw)
#
#
# print(lotto_draw[0])
# import rsaidnumber
# from datetime import date, datetime
# id_number = rsaidnumber.parse('9705105019082')
# print(id_number.date_of_birth)

# from datetime import date
#
#
# id_num = input("GIMME YOUR ID NO NIGGA: ")
# year = id_num[:2]
# if year >= "22":
#     year = "19" + year
# else:
#     year = "20" + year
# month = id_num[2:4]
# day = id_num[4:6]
# dob = year, month, day
# print(dob)
#
# today = date.today()
# print(today.year)

# t_year = int(today.year)
#
# age = t_year - int(year)
#
# print(age)

# age = today.year - int(year) - ((today.month, today.day) < (int(month), int(day)))
# print(age)

# import uuid
# uuid.uuid4()
# player_id = uuid.uuid4()
# print(player_id)

# from uuid import uuid4
#
# students = ["piet", "jan", "koos", "donny"]
#
# for students in students:
#     player_id = str(uuid4())
#     print('{} : {}'.format(students, player_id))
#
my_list1 = [23, 24, 39, 11]
my_list2 = [4, 23, 24, 14]
results = list(set(my_list1).intersection(my_list2))


print(results)
print(len(results))

prizes = {6: "10 000 000.00", 5: "8 584.00", 4: "2 384.00", 3: "100.50", 2: "20.00", 1: "0", 0: "0"}
my_key = len(results)
x = list({prizes.get(my_key)})
z = str(x)
print(z)

# with open('user_details.txt', 'rt') as myfile:  # Open lorem.txt for reading
#     for myline in myfile:              # For each line, read to a string,
#         print(myline)                  # and print the string.
#         print(myline[-1])

# with open('user_details.txt', 'r') as f:
#     lines = f.read().splitlines()
#     last_line = lines[-1]
#     print(last_line)
#
# import re
#
# fileToRead = 'user_details.txt'
# file = open(fileToRead, 'r')
# listLine = file.readlines()
# # print(listLine)
#
# text = str(listLine)
# print(text)
#
#
# emails = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", text)
# print(emails)
#
# print(emails[-1])

# with open('user_details.txt', "r") as x:
#     lines = x.read().splitlines()
#     last_line = lines

# from doctest import testmod
# import unittest
# import random
#
#
# def adding(x, y):
#     """
#     >>> adding(3,3)
#     6
#     >>> adding(5,7)
#     12
#     """
#     result=x+y
#     return result
#
#
# if __name__ == '__main__':
#     testmod(name='adding', verbose=True)
#
#
# def randomnumbers():
#     x = random.sample(range(1, 49), 6)
#     print(x)
#     return x
#
#
# class Randomness(unittest.TestCase):
#     def setUp(self):
#         self.a = 1
#         self.b = 49
#
#     def test_gen_age(self):
#         randomnumbers()
#         self.assertTrue(self.a >= 1 and self.b <= 20)
#         if __name__ == '__main__':
#             unittest.main()
