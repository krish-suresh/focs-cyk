terminals = ["a", "b"]

non_terminals = ["S", "A", "B"]
start = "S"
rules = {"S": ("AB", "BC"), 
         "A": ("BA", "a"), 
         "B": ("CC", "b"), 
         "C": ("AB", "a")
         }
         
w = "baaba"
n = len(w)
T = [[set() for _ in range(n - y)] for y in range(n)]
for i in range(n):
    for r, a in rules.items():
        for b in a:
            if w[i] == b:
                T[0][i].add(r)

for word_size in range(2, n + 1):
    for start_elem in range(0, n - word_size + 1):
        for left_size in range(1, word_size):
            right_size = word_size - left_size
            left_cell = T[left_size - 1][start_elem]
            right_cell = T[right_size - 1][start_elem + left_size]
            for r, a in rules.items():
                for b in a:
                    if b in terminals:
                        continue
                    if b[0] in left_cell and b[1] in right_cell:
                        T[word_size - 1][start_elem].add(r)

for l in reversed(T):
    print(l)

if start in T[n - 1][0]:
    print("Sentence is valid")
else:
    print("Sentence is not valid")