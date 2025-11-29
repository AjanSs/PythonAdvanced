from PIL.ImageChops import difference

my_set = {1,2,3}
print(my_set)

set_ = set([4,5,6,6])
print(set_)

set1= {1,2,3}
set2= {3,4,5}

#UNION
union_result_method = set1.union(set2)
union_result_operator = set1 | set2

print('Union of set1 and set2 using union method:',union_result_method)
print('Union of set1 and set2 using union operator:',union_result_operator)

#intersection

intersection_method = set1.intersection(set2)
insection_operator = set1 & set2
print('Intersection of set1 and set2 using intersection method:',intersection_method)
print('Intersection of set1 and set2 using intersection operator:',insection_operator)

#difference
difference_method = set1.difference(set2)
difference_operator = set1 - set2
print('Difference of set1 and set2 using differenc method:',difference_method)
print('Difference of set1 and set2 using differenc operator:',difference_operator)

#symetric difference
symetric_method = set1.symmetric_difference(set2)
symetric_operator = set1 ^ set2
print('Symetric difference of set1 and set2 using differenc method:',symetric_method)
print('Symetric difference of set1 and set2 using differenc method:',symetric_operator)


my_set = {1,2,3}

my_set.remove(3)
print(my_set)

my_set.add(5)
print(my_set)

my_set.discard(7)
print(my_set)