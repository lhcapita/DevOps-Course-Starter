

def simple_validation(*argv):

    error = False

    for arg in argv:
        if not arg or not arg.strip():
            error = True
    return error

def reformat_due_date(date):
    if date == None:
        return None
    l = date.split("-")

    date_reformatted = l[1] + "/" + l[2] + "/" + l[0]

    return date_reformatted