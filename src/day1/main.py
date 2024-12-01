list1 = []
list2 = []

with open("list.txt", "r") as f:
    result = f.readlines()

for item in result:
    items = item.replace("\n","").split("  ")
    list1.append(int(items[0]))
    list2.append(int(items[1]))

list1.sort()
list2.sort()

result = sum([abs(list2[i] - list1[i]) for i in range(len(list1))])
print(result)

# part 2
count_list= []
for i in range(len(list1)):
    count_list.append(list2.count(list1[i]))

result = [list1[i]*count_list[i] for i in range(len(list1))]
print(sum(result))