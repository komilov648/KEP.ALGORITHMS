def sum_of_digits(number):
     s = 0
     for char in str(number):
         digit = int(char)
         s += digit