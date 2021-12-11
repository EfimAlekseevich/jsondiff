from jsondiff import diff_dicts, diff_lists
import cProfile


def prof_dict(src, cmp):
    with cProfile.Profile() as pr:
        diff_dicts(src, cmp)
    return pr


def prof_list(src, cmp):
    with cProfile.Profile() as pr:
        diff_lists(src, cmp)
    return pr


base = 100_000

# 1 upper bound 200005 function calls in 0.063 seconds
print(1, '-'*80)
src = {i: i for i in range(base)}
cmp = {}
prof_dict(src, cmp).print_stats()

# 2 lower bound 5 function calls in 0.000 seconds
print(2, '-'*80)
src = {}
cmp = {i: i for i in range(base)}
prof_dict(src, cmp).print_stats()


# 3 7 function calls in 0.000 seconds
print(3, '-'*80)
src = {}
a = src
for i in range(997):  # 997 is limit
    a[i] = {}
    a = a[i]
cmp = {}
prof_dict(src, cmp).print_stats()

# 4 5 function calls in 0.000 seconds
print(4, '-'*80)
cmp = {}
a = cmp
for i in range(997):  # 997 is limit
    a[i] = {}
    a = a[i]
src = {}
prof_dict(src, cmp).print_stats()

# 5 6977 function calls (5981 primitive calls) in 0.033 seconds
print(5, '-'*80)
cmp = {}
a = cmp
for i in range(997):  # 997 is limit
    a[i] = {}
    a = a[i]

src = {}
a = src
for i in range(996):  # 997 is limit
    a[i] = {}
    a = a[i]

a = 3

print()
prof_dict(src, cmp).print_stats()


# 6 6972 function calls (5977 primitive calls) in 0.026 seconds
print(6, '-'*80)
cmp = {}
a = cmp
for i in range(995):  # 997 is limit
    a[i] = {}
    a = a[i]
a = 3

src = {}
a = src
for i in range(997):  # 997 is limit
    a[i] = {}
    a = a[i]

print()
prof_dict(src, cmp).print_stats()


# 01
print(1, '-'*80)
src = [[] for i in range(base)]
cmp = []
prof_list(src, cmp).print_stats()

# 02
print(2, '-'*80)
cmp = [[] for i in range(base)]
src = []
prof_list(src, cmp).print_stats()

# 03
print(3, '-'*80)
src = []
a = src
for i in range(997):  # 997 is limit
    a.append([])
    a = a[0]
cmp = []
prof_list(src, cmp).print_stats()

# 04
print(4, '-'*80)
cmp = []
a = cmp
for i in range(997):  # 997 is limit
    a.append([])
    a = a[0]
src = []
prof_list(src, cmp).print_stats()


# 05
print(5, '-'*80)
cmp = []
a = cmp
for i in range(997):  # 997 is limit
    a.append([])
    a = a[0]
src = []
a = src
for i in range(996):  # 997 is limit
    a.append([])
    a = a[0]
a = 3
prof_list(src, cmp).print_stats()