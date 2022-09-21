#sleep_in
def sleep_in(weekday, vacation):
  return weekday==False or vacation == True

#near_hundred
def near_hundred(n):
  return 89<n and n<111 or 189<n and n<211

#monkey_trouble
def monkey_trouble(a_smile, b_smile):
  return a_smile==b_smile

#sum_double
def sum_double(a, b):
  if(a==b):
    return 2*a + 2*b
  else:
    return a + b

#parrot_troubles
def parrot_trouble(talking, hour):
  return (hour < 7 or hour > 20) and (talking)

#front3
def front3(str):
  if (len(str) < 3):
    return str * 3
  return str[:3] * 3
  



