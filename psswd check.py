import re
a= input("Enter your password:")
strenght_s=0
if len(a)>= 8:
    strenght_s+=1
if re.search(r'[A-Z]',a):
    strenght_s+=1
if re.search(r'[a-z]',a):
    strenght_s+=1
if re.search(r'[0-9]',a):
    strenght_s+=1
if re.search(r'[!@#$%^&*(:"?>/)]',a):
    strenght_s+=1
if strenght_s>=5:
    print(a, "is a strong password")
elif strenght_s<3:
    print(a, "is a weak password")
else:
    print("The password can be better")
