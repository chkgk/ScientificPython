def flattenList(pList, pFlatList = []):
	if isinstance(pList, list):
		for e in pList:
			flattenList(e, pFlatList)
	else:
		pFlatList.append(pList)
	return pFlatList


def flist2(pList, pFlatList = []):
	for e in pList:
		if isinstance(e, list):
			flattenList(e, pFlatList)
		else:
			pFlatList.append(e)
	return pFlatList


myList = [[1,2], [4,5,[6,7,[8,9],5,2],2],[1,2,[3,2],5]]
print(flattenList(myList))
print(flist2(myList))