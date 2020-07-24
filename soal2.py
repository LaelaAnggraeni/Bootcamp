input = input("Masukan angka: ")
saparator = input.split(",")
lis=[]
for i in saparator:
	if((int(i)%2)==1):
		lis.append(i)
print(lis)