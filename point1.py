def average(lst:list) -> int: # the input is a list of integers.
    avg = 0 # a variable avg is set to zero.
    for num in lst: # it iterates through the list, adding each number to avg.
        avg += num
    return avg / len(lst) # avg is devided into the length of the list

if __name__ == "__main__":
    n = int(input("Enter the number of real numbers the list will contain: "))
    lst = [int(input("Enter a number: ")) for x in range(n)]
    
    res = average(lst)
    print(res)
