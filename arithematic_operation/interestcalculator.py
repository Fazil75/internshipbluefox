def simple_interest(p, r, t):
    interest = (p * r * t) / 100
    return interest

p = float(input("principal: "))
r = float(input("rate: "))
t = float(input("time: "))

result = simple_interest(p, r, t)

print("Simple Interest =", result)