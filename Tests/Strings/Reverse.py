def reverse():
    rev=""
    s=input("Enter the string to reverse: ")
    print("first method Result == "+s[::-1])
    for i in range(len(s)-1,-1,-1):
        rev +=s[i]
    print("Second method result == " +rev)

reverse()