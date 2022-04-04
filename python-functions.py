# def sum_to(num):
#   sum = 0
#   for num in range(1, num + 1):
#     sum += num
#   print(sum)

# sum_to(6)

###################################

def largest(num):
  num.sort()
  print("Largest number is:", num[-1] )

largest([1, 2, 3, 4, 0])
largest([10, 4, 2, 231, 91, 54])