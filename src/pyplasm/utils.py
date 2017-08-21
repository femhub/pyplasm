# ===================================================
# FLATTEN
# ===================================================

# takes lists (possibly including other lists) and returns one plain list
def flatten(*args):
    output = []
    for arg in args:
        if hasattr(arg, '__iter__'):
            output.extend(flatten(*arg))
        else:
            output.append(arg)
    return output
