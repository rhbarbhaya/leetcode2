def isMatch(s: str, p: str) -> bool:
    for i, j in zip(s,p):
        if i.isalpha() and j != ".":
            return False
        # elif (i.isalpha() and j != "*") or (i == "" and j != "*"):
        #     return False
        elif i != j:
            return False
    return True
