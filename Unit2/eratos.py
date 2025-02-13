upto = int(input("Numbers up to: "))
nums = [x+1 for x in range(upto)]
ded = [1]

def Printallnums():
    for x in nums:
        c = 1
        if x in ded:
            c = 31
        
        if len(str(x)) < len(str(upto)):
            print(f"\u001b[{c}m{'0'*(len(str(upto))-len(str(x)))}\u001b", end="")
        print(f"\u001b[{c}m{x}\u001b", end="\u001b[0m | \u001b")
        if x%10 == 0:
            print()

for num in range(upto):
    n = num+1
    if n in ded:
        continue
    elif n*n > upto:
        break

    for n2 in nums[num+1:]:
        if n2%n == 0:
            ded.append(n2)
    Printallnums()
    print("\n")

print("all prime numbers")
for x in nums:
    if not x in ded:
        print(x,end=", ")
print()