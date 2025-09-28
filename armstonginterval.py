lower = 100
upper = 2000

for no in range(lower, upper + 1):

   # order of number
   order = len(str(no))
    
   # initialize sum
   sum = 0

   temp = no
   while temp > 0:
       digit = temp % 10
       sum += digit ** order
       temp //= 10

   if no == sum:
       print(no)
