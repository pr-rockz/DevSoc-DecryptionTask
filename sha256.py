# Hash a single string with hashlib
import hashlib
a_string = input("Enter your roll number: ")
print()
hashed_string = hashlib.sha256(a_string.encode('utf-8')).hexdigest()
print(hashed_string)

print()
hashed_string = hashed_string[-6:]
print("the last 6 digit of the string is : " + hashed_string)
