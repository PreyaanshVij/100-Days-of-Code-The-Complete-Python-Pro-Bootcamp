print("Welcome To The Tip Calculator.")

a = int(input("What Is The Total Bill? : $"))
b = int(input("What Percentage Of Tip Would You Like To Give? 10, 12 or 15? : "))
c = int(input("How Many People To Split The Bill? "))
d = (a + a*b/100)/c

print(f"Each Person Should Pay {d}$.")