def main(s):
    """
    a single character string is given. Convert it to int type, return -1 if not possible.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
    if s.isdigit()==True:
        return s
    return -1
s = "16"
print(main(s))
s = "s"
print(main(s))