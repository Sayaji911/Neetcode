

def reverse(input: str) -> str:
    temp = []
    reverse_string = ""
    for i in input:
        temp.append(i)
        
    for j in range(len(temp)-1,-1 , -1):
        reverse_string = reverse_string + temp[j]
        
    # return reverse_string




    temp = []
    for i in reversed(input):
        temp.append(i)
        
    reversed_string = "".join(temp)
        
    # return reversed_string

    return input[::-1]
print(reverse("ijayas navahc"))


"""
first store the elements of the string in an array

then start iterating from the last element of the array to first

join all the elements one by one in a string
"""