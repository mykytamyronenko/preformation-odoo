# For this challenge you will determine if a stream of digits occurs in a string.

"""
have the function NumberStream(str) take the str parameter being passed which
will contain the numbers 2 through 9, and determine if there is a consecutive
stream of digits of at least N length where N is the actual digit value. If so,
return the string true, otherwise return the string false. For example: if str is
"6539923335" then your program should return the string true because there is a consecutive
stream of 3's of length 3. The input string will always contain at least one digit.
"""

"""
traverse the string
have a temp string that will increase if values are consecutive
if the next value is not the same as current consecutive values
break and analyze the length of the temp string
if the length matches the digit value than return true
else continue until the string has been fully traversed
"""

def NumberStream(stream):
    if len(stream) == 1:
        return False
    tmp = stream[0]

    for i in range(1,len(stream)):
        if stream[i] == stream[i-1]:
            tmp += stream[i]
        else:
            tmp = stream[i]

        if len(tmp) == int(stream[i]):
            return True

    return False

# print(NumberStream("5556293383563665")) # False
# print(NumberStream("5788888888882339999")) # True
# print(NumberStream("6539923335")) # True

# print("\n\n")

# def NumberStream(stream):
#     count = 1

#     for i in range(1,len(stream)):
#         if stream[i] == stream[i-1]:
#             count += 1
#         else:
#             count = 1

#         if int(stream[i]) <= count:
#             return "true"

#     return "false"

print(NumberStream("5556293383563665")) # False
print(NumberStream("5788888888882339999")) # True
print(NumberStream("6539923335")) # True
print(NumberStream("2566848658999999999849")) # True
print(NumberStream("24949892")) # False
print(NumberStream("225958596")) # True
print(NumberStream("22")) # True
print(NumberStream("33")) # False
print(NumberStream("333")) # True
print(NumberStream("123")) # False
print(NumberStream("2")) # False

# print("\n\n")

# def NumberStream2(str):
#     if len(str) == 1:
#         return "false"

#     temp = str[0]

#     for x in range(1, len(str)):
#         if not temp:
#             temp += str[x]
#             continue

#         # If values are the same, add it to temp string
#         if str[x] == temp[0]:
#             temp += str[x]
#         else:
#             # Clear the temp string
#             temp = ""

#         # Condition to analyze length of temp string
#         # If length matches the consecutive values, it is valid
#         if len(temp) > 1 and len(temp) + 48 == ord(temp[0]):
#             return "true"

#     return "false"


# print(NumberStream2("5556293383563665"))  # false
# print(NumberStream2("5788888888882339999"))  # true
# print(NumberStream2("6539923335"))  # true
