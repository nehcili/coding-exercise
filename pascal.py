# the function pascal prints pascals triangle of height n.
# for example, if n = 4, it prints
#       1
#     1   1
#   1   2   1
# 1   3   3   1

# The main idea is as follows:
# we use recursion. In this recursion, we construct an invariant: triangle
# triangle is a list with all but the last element a string.
# the last element is a list of int
# triangle[:-1] contains strings of well formatted (ready to print)
# levels of pascals triangle
# its last element contains the a list whose int entries are entries into
# the last level of pascal's triangle

# the reason for the last line is only for convenience. It is much easier
# to construct the next level in pascal's triangle from a list of int,
# than to parse a string, convert it to int. Those this is a matter of taste.

# the function pascal calls pascal_aux with number of levels n passed along
# the functiona pascal_aux produces the recursive invariant triangle with
# n+1 passed. This reason for n+1 is because pascal_aux produces triangle
# whose first n entries are formatted level (ready to print) of pascal's triangle
# while the last one is a list of entries of the n+1 level. We only need the
# first n. The last one is a bit of waste. But saves me the effort to write another
# 2 lines of code.

# next_level: lst --> lst
# produces the next level of the pascal's triangle
# keeps the recursion invariant
def next_level(triangle):
    prev_level = triangle[-1]
    new_level = [1]

    for i in range(1, len(prev_level)):
        new_level.append(prev_level[i-1]+ prev_level[i])

    new_level.append(1)

    prev_level = '   '.join(str(x) for x in prev_level)
    triangle[-1] = prev_level + '\n'

    for i in range(0, len(triangle)):
        triangle[i] = '  ' + triangle[i]

    triangle.append(new_level)

    return triangle

# pascal_aux: int --> list
# produces the invariant triangle with n levels
def pascal_aux(n):
    if n == 1:
        return [[1]]
    else:
        return next_level(pascal_aux(n-1))
        
# pascal: int --> void
# prints n level pascal's triangle
def pascal(n):
    triangle = pascal_aux(n+1)
    triangle.pop()

    for level in triangle:
        print(level[2:])

while True:
    n = int(input("Enter the level of Pascal's triangle:"))
    pascal(n)
