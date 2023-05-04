def zerosAtTheEnd(lst:list) -> list: # the input is a list.
    for i in range(len(lst)): # the program iterates the lenght of the list.
        if lst[i] == 0: # if it founds a zero, it removes it from the position and adds it at the end.
            lst.pop(i)
            lst.append(0)
    return lst

if __name__ == "__main__":
    n = int(input("Enter the number of real numbers the list will contain: "))
    lst = [int(input("Enter a number: ")) for x in range(n)]
    res = zerosAtTheEnd(lst)
    print(res)
