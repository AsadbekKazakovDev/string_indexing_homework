from math import*
def main(s):
    """
    Given a variable s string of length five. Determine the number of digits involved in this variable.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
    return s[0].isdigit()+s[1].isdigit()+s[2].isdigit()+s[3].isdigit()+s[4].isdigit()
s = "32xz2"
print(main(s))
s = "1934z"
print(main(s))