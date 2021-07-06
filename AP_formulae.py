import collections

x = [10, 27, 44] #input list
x.sort()
diff_lst = []
print("Input is: ", x)

for i in range(0, len(x)):
	if i < len(x) - 1:
		d = x[i+1] - x[i]
		diff_lst.append(d)

k = 0
for i in range(0, len(diff_lst)):
	if i < len(diff_lst) - 1:
		if diff_lst[i] == diff_lst[i+1]:
			k = 1
		else:
			k = 0

# y = n*d - d^2 + a1
diff = diff_lst[0]

if diff <= 47:
	r = 50
else:
	r = x[-1]

ans = []

if k == 0:
	print("Difference is not same. It is not an AP.")
else:
	for n in range(r):
		y = n*diff - diff**2 + x[0]
		if y in x:
			ans.append(y)

if collections.Counter(ans) == collections.Counter(x):
	print("\nOutput is: f(x) = x *", diff, "+ (", x[0] - diff**2, ")")
else:
	print("Couldn't find the pattern.")
