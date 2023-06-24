def main(s):
    """
    A string of length five is given. Return the index of the "*" character, return False if not present.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
    return s[0].isdigit()+s[1].isdigit()+s[2].isdigit()+s[3].isdigit()+s[4].isdigit()
s = "3**z2"
print(main(s))
s = "1**A*"
print(main(s))
        