multi_list = [[1,2,3],
              [4,5,6],
              [7,8,9]]

# diagnol

print([multi_list[i][i] for i in range(len(multi_list))] )

# row 1

print([multi_list[i][1] for i in range(len(multi_list))] )
print([col[1] for col in multi_list])

