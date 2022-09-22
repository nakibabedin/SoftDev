#sleep_in
#The parameter weekday is True if it is a weekday, and the parameter vacation is True if we are on vacation. We sleep in if it is not a weekday or we're on vacation. Return True if we sleep in.
def sleep_in(weekday, vacation):
  return weekday==False or vacation == True

print(sleep_in(False, False)) # True
print(sleep_in(True, False)) # False
print(sleep_in(False, True)) # True


#near_hundred
# Given an int n, return True if it is within 10 of 100 or 200. Note: abs(num) computes the absolute value of a number.
def near_hundred(n):
  return 89<n and n<111 or 189<n and n<211


print(near_hundred(93) )
print(near_hundred(90) )
print(near_hundred(89) )

#monkey_trouble
# We have two monkeys, a and b, and the parameters a_smile and b_smile indicate if each is smiling. We are in trouble if they are both smiling or if neither of them is smiling. Return True if we are in trouble.
def monkey_trouble(a_smile, b_smile):

  return a_smile==b_smile

#sum_double
#Given two int values, return their sum. Unless the two values are the same, then return double their sum.
def sum_double(a, b):
  if(a==b):
    return 2*a + 2*b
  else:
    return a + b

print(sum_double(3, 2)) 
print(sum_double(1, 2))
print(sum_double(2, 2))

#parrot_troubles
# We have a loud talking parrot. The "hour" parameter is the current hour time in the range 0..23. We are in trouble if the parrot is talking and the hour is before 7 or after 20. Return True if we are in trouble.
def parrot_trouble(talking, hour):
  return (hour < 7 or hour > 20) and (talking)

print(parrot_trouble(True, 6) )
print(parrot_trouble(True, 7) )
print(parrot_trouble(False, 6))

#front3
#Given a string, we'll say that the front is the first 3 chars of the string. If the string length is less than 3, the front is whatever is there. Return a new string which is 3 copies of the front.
def front3(str):
  if (len(str) < 3):
    return str * 3
  return str[:3] * 3
  
print(front3('Java'))
print(front3('Chocolate'))
print(front3('abc'))

#diff21
# Given an int n, return the absolute difference between n and 21, except return double the absolute difference if n is over 21.
def diff21():
  if(n>21):
    return 2* (n-21)
  else:
    return 21-n

print(diff21(19))
print(diff21(10))
print(diff21(21))


#makes10
# Given 2 ints, a and b, return True if one if them is 10 or if their sum is 10.
def makes10(a,b):
  return a == 10 or b == 10 or a+b == 10

print(makes10(9, 10))
print(makes10(9, 9))
print(makes10(1, 9))

# pos_neg
# Given 2 int values, return True if one is negative and one is positive. Except if the parameter "negative" is True, then return True only if both are negative.
def pos_neg(a, b, negative):
  if(negative):
    return a < 0 and b < 0
  return ((a < 0) and (b>0)) or ((a>0) and (b<0))

print(pos_neg(1, -1, False))
print(pos_neg(-1, 1, False))
print(pos_neg(-4, -5, True))

# not_string
#Given a string, return a new string where "not " has been added to the front. However, if the string already begins with "not", return the string unchanged.
def not_string(str):
  if(str[0:2] == "not"):
    return str
  return "not " + str

print(not_string('candy'))
print(not_string('x'))
print(not_string('not bad'))


# missing_char
# Given a non-empty string and an int n, return a new string where the char at index n has been removed. The value of n will be a valid index of a char in the original string (i.e. n will be in the range 0..len(str)-1 inclusive).
def missing_char(str, n):
  str = str[:n] + str[n+1:]
  return str

print(missing_char('kitten', 1))
print(missing_char('kitten', 0) )
print(missing_char('kitten', 4) )

#front_back
# Given a string, return a new string where the first and last chars have been exchanged.
def front_back(str):
  if len(str) <= 1:
    return str
  middle = str[1:-1]
  return str[-1] + middle + str[0]

print(front_back('code') )
print(front_back('a') )
print(front_back('ab') )


