#string_times
def string_times(str, n):
  return n * str

#front_times
def front_times(str, n):
  if (len(str) < 3):
    return str * n
  else:
    return str[:3] * n

#string_bits
def string_bits(str):
  res = ""
  for i in range(len(str)):
    if (i % 2 == 0):
      res += str[i]
  return res  

#String_splosion
def string_splosion(str):
  output=""
  for x in range(len(str)):
    output += str[:x]
  return output + str


#Last2
def last2(str):
  if(len(str)<2):
    return 0
  twochar=str[-2:]
  output=0
  for x in range(len(str)-2):
    if(twochar==str[x:x+2]):
      output+=1
  return output
    

#Array_count9
def array_count9(nums):
  output=0
  for x in range(len(nums)):
    if nums[x]==9:
      output+=1
      
  return output

#Array_front9
def array_front9(nums):
  output=0
  for x in range(len(nums)):
    if(x<4):
      if nums[x]==9:
        return True
      
  return False

#array123
def array123(nums):
 for i in range(len(nums)-2):
   if (nums[i:i+3] == [1, 2, 3]):
     return True
 return False

#String_match 
def string_match(a, b):
  counter = 0
  for i in range(len(a)-1):
    if (a[i:i+2] == b[i:i+2]):
      counter += 1
  return counter



