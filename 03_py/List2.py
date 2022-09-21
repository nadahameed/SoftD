# count_evens
# Return the number of even ints in the given array. Note: the % "mod" operator computes the remainder, e.g. 5 % 2 is 1.
def count_evens(nums):
  ans = 0
  for e in range(len(nums)):
    if nums[e] % 2 == 0:
      ans +=1
  return ans

print(count_evens([2, 1, 2, 3, 4])) #3
print(count_evens([2, 2, 0]))  #3

#big_diff
#Given an array length 1 or more of ints, return the difference between the largest and smallest values in the array. Note: the built-in min(v1, v2) and max(v1, v2) functions return the smaller or larger of two values.
def big_diff(nums):
  return max(nums) - min(nums)

print(big_diff([10, 3, 5, 6])) #7
print(big_diff([7, 2, 10, 9])) #8

#centered_average
#Return the "centered" average of an array of ints, which we'll say is the mean average of the values, except ignoring the largest and smallest values in the array. If there are multiple copies of the smallest value, ignore just one copy, and likewise for the largest value. Use int division to produce the final average. You may assume that the array is length 3 or more.
def centered_average(nums):
  maxvalue = max(nums)
  minvalue = min(nums)
  nums.remove(maxvalue) 
  nums.remove(minvalue)
  return sum(nums) / len(nums)

print(centered_average([1, 2, 3, 4, 100])) #3
print(centered_average([1, 1, 5, 5, 10, 8, 7]) ) #5

#sum13
#Return the sum of the numbers in the array, returning 0 for an empty array. Except the number 13 is very unlucky, so it does not count and numbers that come immediately after a 13 also do not count.
def sum13(nums):
  sum = 0
  if len(nums) > 0 and nums[0] is not 13:
    sum += nums[0]
  for e in range(len(nums)):
    if nums[e] is not 13:
      if e > 0 and nums[e - 1] is not 13:
        sum += nums[e]
  return sum

print(sum13([1, 2, 2, 1])) #6
print(sum13([1, 1])) #2

#sum67
#Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 7 (every 6 will be followed by at least one 7). Return 0 for no numbers.
def sum67(nums):
  ans = 0
  value = True
  for e in range(len(nums)):
    if nums[e] == 6:
      value = False
    elif value == False and nums[e] == 7:
      value = True
      e += 1
    else:
      if value == True:
        ans += nums[e]
  return ans

print(sum67([1, 2, 2])) #5
print(sum67([1, 2, 2, 6, 99, 99, 7])) #5

#has22
#Given an array of ints, return True if the array contains a 2 next to a 2 somewhere.
def has22(nums):
  for e in range(len(nums) - 1):
    if nums[e] == 2 and nums[e + 1] == 2:
      return True
  return False

print(has22([1, 2, 2])) #T
print(has22([1, 2, 1, 2])) #F