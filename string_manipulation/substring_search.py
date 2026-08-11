def search(s,sub):
    return s.count(sub)
    

def main():
    s=input("enter the string:")
    sub=input("enter the substring:")
    result=search(s,sub)
    if result==0:
        print("the world not appers in the string")
    else:
        print(f"the substring '{sub}' appera {result} times in the string")
    
main()
   