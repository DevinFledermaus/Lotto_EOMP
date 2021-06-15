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

from uuid import uuid4

students = ["piet", "jan", "koos", "donny"]

for students in students:
    player_id = str(uuid4())
    print('{} : {}'.format(students, player_id))
