def totalNQueens(n):
    count = 0

    def backtrack(c, diagonals, anti_diagonals, rows):
        nonlocal count
        if c == n:
            count += 1
        for r in range(n):
            curr_diag = r - c
            curr_anti_diag = r + c
            if (r in rows or curr_diag in diagonals or curr_anti_diag in anti_diagonals):
                continue
            rows.add(r)
            diagonals.add(curr_diag)
            anti_diagonals.add(curr_anti_diag)
            backtrack(c + 1, diagonals, anti_diagonals, rows)
            rows.remove(r)
            diagonals.remove(curr_diag)
            anti_diagonals.remove(curr_anti_diag)
    backtrack(0, set(), set(), set())

    return count

