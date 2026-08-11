def anagram(s1,s2):
    return sorted(s1)==sorted(s2)
def main():
    s1=input("enter the first string:")
    s2=input("enter the second string:")
    result=anagram(s1,s2)
    if result:
        print(f"{s1} and {s2} are anagrams")
    else:
        print(f"{s1} and {s2} are not anagrams")
main()