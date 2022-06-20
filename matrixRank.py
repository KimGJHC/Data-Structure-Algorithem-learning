def matrixRank(matrix):
    m, n = len(matrix), len(matrix[0])
    import collections
    dict_matrix = collections.defaultdict(list)
    for i in range(m):
        for j in range(n):
            dict_matrix[matrix[i][j]].append((i, j))

    res = [[0] * n for _ in range(m)]
    row_rank_max, col_rank_max = [0] * m, [0] * n
    dict_matrix = sorted(dict_matrix.items(), key=lambda k_v: k_v[0])

    for cur_val, positions in dict_matrix:
        if len(positions) == 1:
            x, y = positions[0]
            res[x][y] = 1 + max(row_rank_max[x], col_rank_max[y])
            row_rank_max[x] = res[x][y]
            col_rank_max[y] = res[x][y]
        else:
            # determine the best rank based on partitions
            partition = []
            for x, y in positions:
                find_set = False
                for i in range(len(partition)):
                    if x in partition[i][0] or y in partition[i][1]:
                        partition[i][0].add(x)
                        partition[i][1].add(y)
                        partition[i][2].append((x, y))
                        find_set = True
                        break
                if not find_set:
                    partition.append([set([x]), set([y]), [(x, y)]])


            for _, _, part in partition:
                row_rank_max_copy = row_rank_max.copy()
                col_rank_max_copy = col_rank_max.copy()
                rank_candidate_max = 0
                for x, y in part:
                    rank_candidate = 1 + max(row_rank_max_copy[x], col_rank_max_copy[y])
                    if rank_candidate > rank_candidate_max:
                        rank_candidate_max = rank_candidate
                for x, y in part:
                    res[x][y] = rank_candidate_max
                    row_rank_max[x] = res[x][y]
                    col_rank_max[y] = res[x][y]
    return res


