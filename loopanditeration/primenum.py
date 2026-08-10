def prime(n):
    if n < 2:
        return False    
    for i in range(2, n):
            if n%i == 0:
                 return False
    return True
def main():
    count =0
    for n in range(1,21):
        if prime(n):
            count += 1
            if count % 2!= 0:
                 print(n,end=" ")
main()