#Hint: Create a string of numbers+capital letters+small 
# letters+special characters. Take a random sample from
# the string of a length given by the user.
import random
passlen=int(input("Enter the lenght of the pasword:"))
strings_inn="abcdefghiklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPRSTUVWYZ!@#$^&*()?"
prepar="".join(random.sample(strings_inn,passlen))
print(prepar)

#output
Enter the lenght of the pasword:8
EHb!KRmN

Process finished with exit code 0
