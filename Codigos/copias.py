import copy

lst=[1,2,3,4,5,[['a'],'b','c','d']]
#list=lst.copy() copia superficial
lst1=copy.deepcopy(lst)

print(lst)
lst1[5][0]="1000"
print(lst)
print(lst1)
