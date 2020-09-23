## TODO: complete the function "lowest_terms" below

def lowest_terms(x):
    """
    This function will divide two number by their highest common factor

    return: the lowest terms seperated by an '/'

    """
    # Split the string into a list of 2 numbers
    y = x.split("/")
    # Assign the numbers to a variable each and convert to integers from strings
    n1 = int(y[0])
    n2 = int(y[1])
    # Set the lower number to be used as range number division
    range_stop = abs(min([n1,n2]))+1
    
    # Check if both numbers are not equal to 0
    if n1 == 0 and n2 == 0:
        # Iterate through the range of the lowest number in reverse 
        for i in reversed(range(range_stop)):
            # Check that for factor of both numbers 
            if n1%i == 0 and n2%i == 0:
                # Return the result of dividing the numbers by the factor 
                return "{}/{}".format(n1//i,n2//i)
