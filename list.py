L = [123, 'text', 1.23]
print(len(L))
print(L[0])
print(L[:-1])
print(L + [4, 5, 6])
print(L * 2)

L.append('Py')
print(L.pop(2))
print(L)

M = ['bb', 'aa', 'cc']
M.sort()
print(M)

M = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9],]
print(M)
print(M[2][2])

col2 = [row[1] for row in M]
print(col2)

N = [row[1] + 1 for row in M]
print(N)
N = [row[1] for row in M if row[1] % 2 == 0]
print(N)
print(M)
diag = [M[i][i] for i in [2]]
print(diag)

doubles = [c * 2 for c in 'hack']
print(doubles)

print(list(range(4)))
print(list(range(-6, 7, 2)))
print([[x ** 2, x ** 3]for x in range(4)])
print([[x, x // 2, x * 2]for x in range(-6, 7, 2)if x > 0])

G = (sum(row) for row in M)
print(next(G))
print(next(G))
print(next(G))

print({sum(row) for row in M})
print({i: sum(M[i]) for i in range(3)})