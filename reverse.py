def reverse_list(l):
    return [l[i] for i in range(len(l)-1, -1, -1)]

i=reverse_list(range(6))
print (i)