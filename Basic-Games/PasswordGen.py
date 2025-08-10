import string
import random

s1 = string.ascii_lowercase
s2 = string.ascii_uppercase
s3 = string.digits
s4 = string.punctuation

plen = int(input("Enter the length of your password:"))
s = []
s.extend(s1)
s.extend(s2)
s.extend(s3)
s.extend(s4)
random_pass = random.sample(s, plen)
print("Your password is:\n", "".join(random_pass))
