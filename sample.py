


sample_list1 =  [1,2,3,4,5]
sample_list2 =  [10,20,30,40,50]

fianl = sample_list1 + sample_list2
print(fianl)

combine = []
for item1, item2 in zip(sample_list1,sample_list2):
    combine.append(item1+item2)

print(combine)