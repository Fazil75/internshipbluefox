def triangle(a,b,c):
    if a==b and b==c and c==a:
        return "equilateral"
    elif a==b or b==c or c==a:
        return "isosceles"
    else:
        return "scalene"

def main():
    a=int(input("Enter first side a of triangle: "))
    b=int(input("Enter first side b of triangle: "))
    c=int(input("Enter first side c of triangle: "))

    result= triangle(a,b,c)
    print(f"the triangle is {result}")
main()
    