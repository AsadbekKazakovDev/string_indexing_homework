def main(s):
    """
    A string of five numbers is given. Find the sum of its numbers.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
    a= s%10
    s//=10
    b= s%10
    s//=10
    c= s%10
    s//=10
    d= s%10
    s//=10
    e= s%10
    s//=10
    return a+b+c+d+e
s = 19302
print(main(s))
    
