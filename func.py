def Control(x, y, max_X, max_Y, min_X = 0, min_Y = 0):
    if (min_X <= x <= max_X) and (min_Y <= y <= max_Y):
        return True
    return False


def Equals(A1, A2):
    if (len(A1) != len(A2)):
        return False
    
    for b in A1:
        if not (b in A2):
            return False
        
    return True


# ---

def Grey(x: int):
    return (x, x, x)

def Change(num: int):
    match num:
        case 9:
            return ((230, 70, 70), (170, 10, 10))
        case 0:
            return ((230, 230, 230), (170, 170, 170))
        case _:
            return (((255 / 8) * num, 0, 0), (30 * num + 10 - 20, 0, 0))
        