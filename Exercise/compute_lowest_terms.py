## TODO: complete the function "lowest_terms" below

def lowest_terms(x):
    """
    This function will divide two number by their highest common factor

    input: two integers seperated by a slash as a string type . For Example, '20/10'

    return: The integers reduced to their lowest terms, seperated by an '/'. For the example above, '2/1' for the highest factor of 10. 

    """
    # Split the string by / and assign to variables
    num,denom = x.split("/")
    #COnvert to integers
    num,denom = int(num),int(denom)

    
    # Return 0 for any numerator which is 0
    if num == 0:
        return "0"
    # Return Undefined for any denominator which is 0
    if denom == 0:
    	return "Undefined"
    # For denominators greater than 0
    elif denom > 0:
        # Iterate through from the denominator +1 to 0
        for i in reversed(range(denom+1)):
            # Check for a common factor of both numbers 
            if num%i == 0 and denom%i == 0:
                # Divide both number by their common factor
                term1,term2=num//i,denom//i
                # Return the terms     
                return "{}/{}".format(term1,term2)
    # If the denominator is a negative number 
    else:
        for i in range(denom, 0):
            # Check for a common factor of both numbers 
            if num%i == 0 and denom%i == 0:
                # Divide both number by their common factor
                term1,term2=num//i,denom//i
                # Return the terms     
                return "{}/{}".format(term1,term2)
