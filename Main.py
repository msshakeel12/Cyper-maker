shift=13
sample_string=input("Enter text to be cyphered: ")
shifted=""
shift=int(input("Enter how many alphabets to shift: "))
x=0
for elem in sample_string:
    if elem==" ":
        shifted+=" "
        continue
    y=ord(elem)
    #print(y)
    x=ord(elem)
    #print(y)
    #if condition for only alphabets 
    if (y>=97 and y<=122):
        x=ord(elem)+shift
        #print(x)
        if (x>122):
             x=(x-122)+96
    if (y>=65 and y<=90):
        x=ord(elem)+shift
        if(x>90):
            x=(x-90)+64
    #print(x)
    shifted+=chr(x)
print("Cyphered text: ",shifted)

