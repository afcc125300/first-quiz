from question2 import run_swapper 

def swapper(t):
    # Check if the input is a tuple with exactly two items
    if isinstance(t, tuple) and len(t) == 2:
        return (t[1], t[0])  # Swap the items and return a new tuple
    else:
        return t  # Return the input as is if it's not a valid tuple

def run_swapper(list_of_tuples):
    return list(map(swapper, list_of_tuples))
