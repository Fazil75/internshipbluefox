def flatten__list(n):
    flat = []
    for i in n:
        if isinstance(i, list):
            flat.extend(flatten__list(i))
        else:
            flat.append(i)
    return flat

def main():
    n = [1,[2,3],[4,[5,6]]] 
    result = flatten__list(n)
    print(f"flattened list: {result}")
main()