def square_dict():
    square ={}
    for i in range(1,11):
        square[i] = i*i
    return square   
def main():
    result = square_dict()
    print(f"squares dictionary: {result}")
main()