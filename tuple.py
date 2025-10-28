T = (1, 2, 3, 4)
print(len(T))

print(T + (5, 6))
print(T[0], T[2:])

# T[0] = 2

T = (2,) + T[1:]
print(T)

T = 'hack', 3.0, [11, 22, 33]
print(T)
print(T[1])
print(T[2][1])
# print(T.append(4))