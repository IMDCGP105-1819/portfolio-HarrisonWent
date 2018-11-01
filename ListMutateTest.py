def remove_dups (L1, L2):
    ToKeep = []
    for e in L1:
        if e not in L2:
            ToKeep.append(e)
    return ToKeep
L1 = [1,2,3,4]
L2 = [1,2,5,6]
print(remove_dups(L1,L2))