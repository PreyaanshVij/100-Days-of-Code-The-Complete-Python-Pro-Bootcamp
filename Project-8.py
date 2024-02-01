import random
def cipher():
    def solve():
        c = ""
        for i in b :
            r = 0
            if i not in a:
                c += i
            else :
                while i != a[r]:
                    r += 1

                f = s + r
                c += a[f]
        return c


    a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p'
        , 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p'
        , 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    n = input("Enter Your Message :  ")
    b = []

    for i in range(0, len(n)):
        b.append(n[i])

    d = input("Encode Or Decode :  ")
    s = int(input("Enter the shift :  "))

    if d.lower() == "encode":
        s = s % 26
        output = solve()
        print(f"The encoded message is {output}")

    elif d.lower() == "decode":
        s = s % 26
        s = s*(-1)
        output = solve()
        print(f"The decoded message is {output}")
    k = input("Do you want to continue? Yes or No :  ")
    if k.lower() == "yes":
        cipher()
    else:
        print("Have a good day.")


cipher()

