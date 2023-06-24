def main(s,n):
    """
    The s string variable is given. n Return the character in the index, otherwise return False.
    Args:
        s(str): parameter
    Returns:
        str: answer
    """
    if len(s)>=n:
        return s[n]
    if len(s)<n:
        return False
s,n = "salom",4
print(main(s,n))
s,n = "codeacademy",14
print(main(s,n))
