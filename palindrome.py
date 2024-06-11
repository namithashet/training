# def is_palindrome(num):
#     num_str = str(num)
#     if num_str == num_str[::-1]:
#         return True
#     else:
#         return False
# number = int(input("Enter a number: "))
# if is_palindrome(number):
#     print("The number is a palindrome.")
# else:
#     print("The number is not a palindrome.")


n=121
temp=n
reverse=0
while(temp>0):
    d=temp%10
    reverse=reverse*10+d
    temp=temp//10
if(n==reverse):
    print("palindrome")
else:
    print("not a palindrome")