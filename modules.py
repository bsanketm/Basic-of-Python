
def module_greetings(name):
    """
    Enter a name and welcome him/her
    """
    out = 'Hi ' + str(name) + ". How are you?"
    return out

def module_sum(lst):
    """
    Enter a list of numeric data and get sum of the elements in list
    """
    sum_ = 0
    for j in lst:
        sum_ += j
    return sum_

def get_count(string):
    """
    Counts the number of characters in the given string
    """
    l =len(string)
    return l