def float2bin():
    """ This function returns the binary value of the floating point number entered. lazy stuff . if you enter negative number , you will see a b in the beginning. else the same stuff!"""
    number=float(input("\nenter the floating point number:"))
    numberstring=str(number)
    numbersplit=numberstring.split(".")
    integer=numbersplit[0]
    floating=numbersplit[1]
    intint=int(integer)
    integerbinary=bin(intint)
    arr=[]
    arr.append(integerbinary)
    arr.append(".")
    res="0."
    newnumber=res+floating
    newnumberint=float(newnumber)
    n=int(input("enter the numer of bits for fractional part (enter at least 1 ) :"))
    if n<1:
        print('what part of "at least one" is hard to comprehend?')
        return
    else:
        for x in range(n):
            newnumberint=newnumberint*2
            string=str(newnumberint)
            s=string.split(".")
            s0=s[0]
            s1=s[1]
            arr.append(s0)
            strs1=str(s1)
            conc=res+strs1
            newnumberint=float(conc)
    fstr=""
    for x in arr:
        fstr+=str(x)
    lasfstr=fstr[2:]
    print("\n")
    print("the binary equivalent is:",lasfstr)
float2bin()
