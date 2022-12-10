import time
import os

#while end is false, program continues to run
end = False

#returns reverse of string
def isPalindrome(s):
    return s == s[::-1]

while end == False:
    options = int(input("Enter '1' to continue, or '0' to end \n"))
    if options == 0:
        end = True
        print("Terminating Program...")
        time.sleep(2)
        print("Program Terminated.")
        break
    else:
        if options == 1:
            s = input("Enter a word: ")
            print("Checking now...")
            time.sleep(2)
            ans = isPalindrome(s)
            if (ans):
                print(f"{s} is a palindrome.")
            else:
                print(f"{s} is not a palindrome.")
        #press any key to continue        
        os.system("pause")
        time.sleep(2)
