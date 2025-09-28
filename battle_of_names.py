even_set = set()
odd_set = set()

num = int(input())
for i in range(1, num+1):
    name = input()
    curr_num = sum(ord(ch) for ch in name) // i

    if curr_num % 2 == 0:
        even_set.add(curr_num)
    else:
        odd_set.add(curr_num)
odd_sum = sum(odd_set)
even_sum = sum(even_set)

if odd_sum == even_sum:
    result = odd_set | even_set
elif odd_sum > even_sum:
    result = odd_set - even_set
else:
    result = odd_set ^ even_set

print(", ".join(str(x) for x in result))