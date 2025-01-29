edges = [[3,7],[1,4],[2,8],[1,6],[7,9],[6,10],[1,7],[2,3],[8,9],[5,9]]
all_nums = [num for sublist in edges for num in sublist]

def findRedundantConnection():
    node_dict = {}

    redundant = []
    num_set = set()
    for edge in edges:
        current_list = node_dict.get(edge[0], [])
        current_list.append(edge[1])
        node_dict.update({edge[0]: current_list})
    print(node_dict)

    for key, values in node_dict.items():

        for value in values:

            if value in node_dict.keys() and len(node_dict[value]) == 1:
                redundant.append(value)
            else:
                num_set.add(value)
    return redundant, node_dict

# findRedundantConnection([[1, 2], [1, 3], [2, 3]])
redundant_nums, node_dict = findRedundantConnection()
filtered_edges = []

print(redundant_nums)
def backtrack():

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

"""for edge in edges[::-1]:
    if edge in final_edges:
        print(f"::{edge}")

print(final_edges[-1])
 """