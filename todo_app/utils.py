

def simple_validation(*argv):

    error = False

    for arg in argv:
        if not arg or not arg.strip():
            error = True
    return error