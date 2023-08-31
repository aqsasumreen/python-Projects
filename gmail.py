# email =input("Enter your Email: ")
# j,k,l=0,0,0
# if email.count(email) >= 6: #1
#     if email[0].isalpha(): #2
#         if('@' in email) and (email.count('@') == 1): #3
#             if (email[-4] == '.') ^ (email[-3] == '.'):#4
#                 for i in email:
#                     if i == i .isspace(): #5
#                         j = 1
#                     elif i.isalpha():  #5
#                         if i == i.upper():
#                             k = 1
#                     elif i.isdigit():
#                         continue
#                     elif i == '_' or i=='@' or i=='.': #5
#                         continue
#                     else:
#                         l = 1
#                 if j == 1 or k == 1 or l == 1:
#                     print("5-Wrong email")
#                 else:
#                     print("Correct")
#             else:
#                 print("4- wrong")
#         else:
#             print("3-Wrong email ")
#     else:
#         print("2-Wrong email")
# else:
#     print("1-Wrong email ")

# BY USING REGEX
# a-z
# 0-9
# @ aik br
# @ se phliy '.' ya _ aik br ho
# . back se 3, 4 pos pr ho

import re
email_condition = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

mail = input("Enter your email:")

if re.search(email_condition, mail):
    print("Right email")
else:
    print("Wrong email")
