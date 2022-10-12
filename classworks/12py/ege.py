p= {i for i in range(25,38)}
q= {i for i in range(29,44)}
for a in range(1,1000):
	s = p or ((not q) and a)
	if s == False:
		print(a)

