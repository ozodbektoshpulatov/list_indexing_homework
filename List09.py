def main(list1):
    """
    A list of several elements is given. True if all items are the same, otherwise return False.
    Args:
        list1 (list): parameter
    Returns:
        bool: return answer
    """
    for i in list1[0]:
        if i !=[0]:
            return False
    return True
print(main("0,0,0,0,0,0"))
    