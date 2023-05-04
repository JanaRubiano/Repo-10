def dotProduct(list1:list, list2:list) -> int: # the input are two lists.
    dot_prod = 0 # a variable dot_prod is set to zero.
    for i in range(len(list1)): # the program iterates the lenght of the list. (Any list works, because both must be the same lenght).
        dot_prod += list1[i]*list2[i] # the values at the same position in list 1 and 2 are multiplied and the added to variable dot_prod.
    return dot_prod

if __name__ == "__main__":
    n = int(input("Enter the number of real numbers both lists will contain: "))
    list1 = [int(input("Enter a number for list 1: ")) for x in range(n)]
    list2 = [int(input("Enter a number for list 2: ")) for x in range(n)]
    res = dotProduct(list1, list2)
    print(res)