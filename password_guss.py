"""from random import*
user_password=input("Enter your password = ")

password={'a','b','c','d','e','f','g','h','i','j','k','l',
          'm','n','o','p','q','r','s','t','u','v','w','x','y','z',
          'A','B','C','D','E','F','G','H','I','J','K','L','M','N',
          'O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2',
          '3','4','5','6','7','8','9'}

guss=""

while(guss!=user_password):
    guss=""
    for letter in range (len(user_password)):
        guess_letter = password[random.randint(0, 61)] 
              guss=str(guess_letter)+str(guss)
        print("trying ",guss)
print("Your password is: ",guss)
"""
from random import choice

user_password = input("Enter your password: ")

# সম্ভাব্য অক্ষর লিস্ট আকারে সংরক্ষণ
password_chars = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")

guss = ""

while guss != user_password:
    guss = ""  # প্রতি লুপের শুরুতে guess খালি করা
    for letter in range(len(user_password)):
        guss += choice(password_chars)  # প্রতিবার একটি এলোমেলো অক্ষর যোগ করা
    print("Trying:", guss)  # প্রতিবার কি গেস করা হচ্ছে তা দেখতে

print("Your password is:", guss)

