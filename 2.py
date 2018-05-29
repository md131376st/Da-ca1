def mergeSort(alist):
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)
        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1

def analize_(mylist):
    # complisity nlogn
    if len(mylist) == 0:
        return
    newlist = mylist[:]
    mergeSort(newlist)
    for i in xrange(len(mylist)):
        want=newlist.index(mylist[0])
        print want,
        del newlist[want]
        del mylist[0]


def reading_input():
    count = int(raw_input())
    mylist=map(int, raw_input().split())
    return count,mylist
    pass

count,mylist=reading_input()
analize_(mylist)