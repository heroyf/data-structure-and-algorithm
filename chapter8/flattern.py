"""
[[1,2], [1,2,3]] -> [1,2,1,2,3]
"""
def flatten(res_list):
    for i in res_list:
        if isinstance(i, list):
            for i in flatten(i):
                yield i

        else:
            yield i

print(list(flatten([[[1],2,3],[1,2,3]]))==[1,2,3,1,2,3])

