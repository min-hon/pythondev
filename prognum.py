def recursion(x):
    match x:
        case 1:
            return 1
        case 2:
            return 1
        case _:
            return recursion(x-2) + recursion(x-1)