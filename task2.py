m=0
def menu(i):


 print("Choose an operation")
 print("[1] check if prime ")
 print("[2] check if palindrome ")
 print("[0] to exit ")
 i = int(input("enter number"))
 if i==1 :
      prime(m)
 if i == 2 :
     palindrome(m)
 if i != 0 :
     menu(i)

def prime (m):
    m=0
    m = int(input("enter number to  check"))

    if m >= 1:
        for N in range(2, m):

            if (m % N == 0):
                print(m, "is not prime")
                break
        else:
            print(m, "is prime")


    else:
        print(m, "is not prime")

def palindrome (m) :
    m = input("enter word or numper to check palindrome")

    rev=m [::-1]
    if rev==m :
         print( m,"is palindrome")

    else:
         print(m, "is not palindrome")

i=0

menu(i)














