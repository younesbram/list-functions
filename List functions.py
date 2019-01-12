'''
This is the get doublifylist function, which takes a two dimensional list and doubles the first 2 strings in the list
@params		a_list
@return		none
'''
def doublifylist(a_list):
	list2 = []
	for i in range(len(a_list)):
		emp_row = []
		for j in range(len(a_list)):
			emp_row.append(a_list[i][j]*2)
		list2.append(emp_row)
	print(list2)
print("\n DOUBLIFYLIST example : ")
print("[[a,b,c],[one pea, two pea, three pea]] --->",end='')
doublifylist([['a','b','c'],["one pea","two pea","three pea"]])

'''
This is the get selectsort function, which takes a list and sorts it using selection sort
@params		alist
@return		alist
'''
def selectsort(alist):
	for b in range(0,len(alist)-1):
		minindex = b
		for j in range(b+1,len(alist)):
			if alist[j] < alist[minindex]:
				minindex = j
		if minindex != b:
			alist[b], alist[minindex] = alist[minindex], alist[b]
	return alist
print("\n SELECTSORT EXAMPLE : ")
print("[1,3,5,2,3] --->", end='')
print(selectsort([1,3,5,2,3]))

'''
This is the get bubble function, which takes a list and sorts it using bubble sort
@params		a_list
@return		a_list
'''
def bubble(a_list):
    length = len(a_list) - 1
    notsorted = True
    while notsorted:
        notsorted = False
        for i in range(0,length):
             if a_list[i] > a_list[i + 1]:
                 new = a_list[i + 1]
                 a_list[i + 1] = a_list[i]
                 a_list[i] = new
                 notsorted = True
    return a_list  
print("\n BUBBLESORT EXAMPLE : ")
print("[3,3,4,5,1,3,2,5,7,8,9] --->", end='')
print(bubble([3,3,4,5,1,3,2,5,7,8,9]))

'''
This is the get listify function, which listifies a string.
@params		something
@return		listifiedlist
'''
def listify(something):
	listifiedlist = []
	for letter in something:
		listifiedlist.append(letter)
	return listifiedlist
print("\n LISTIFY EXAMPLE : ")
print("liquid --->", end='')
print(listify('liquid'))