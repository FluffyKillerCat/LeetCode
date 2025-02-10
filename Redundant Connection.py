edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
all_nums = [num for sublist in edges for num in sublist]

def findRedundantConnection():
    node_dict = {}

    redundant = set()
    num_set = set()
    for edge in edges:
        current_list = node_dict.get(edge[0], [])
        current_list.append(edge[1])
        node_dict.update({edge[0]: current_list})
    print(node_dict)

    for key, values in node_dict.items():

        for value in values:

            if value not in node_dict.keys():
                redundant.add(value)
            else:
                num_set.add(value)
    return redundant, node_dict

# findRedundantConnection([[1, 2], [1, 3], [2, 3]])
redundant_nums, node_dict = findRedundantConnection()
filtered_edges = []
#print(redundant_nums)

res = []
def backtrack():

    for num in redundant_nums:
        count = 0
        switch = False
        for values in node_dict.values():
            count += values.count(num)
            for value in values:
                if value in node_dict.keys():
                    switch = True





        if count > 1 and switch:
            res.append(num)


for edge in edges[::-1]:
    for num in res:
        if num in edge:
            pass



backtrack()
print(res)
"""def backtrack():

    for num in redundant_nums:
        for edge in edges:
            if edge[1] == num:
                filtered_edges.append(list(edge))

backtrack()
print(filtered_edges)
index_set = set()

final_edges = []
for edge in filtered_edges:
    index_set.add(edges.index(list(edge)))

for edge in filtered_edges:
    if all_nums.count(edge[0]) != 1:
        final_edges.append(edge)

for edge in edges[::-1]:
    if edge in final_edges:
        print(f"::{edge}")

print(final_edges[-1])
 """