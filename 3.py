def reading_input():
    number = int(raw_input())
    my_list = map(int, raw_input().split())
    return number, my_list
    pass


def calculation(my_list,number):
    if number < 3:
        print max(my_list)
        return
    newlist=[0]*number
    newlist1 = [0] * number
    newlist[0]=my_list[0]
    newlist1[1]=my_list[1]
    for x in range(0,number-1,1):
        newlist[x]=max(my_list[x]+newlist[x-2],newlist[x-1])
        # print newlist[x],"number of x:",x,"in the list",my_list[x]
    for x in range(1,number,1):
        newlist1[x]=max(my_list[x]+newlist1[x-2],newlist1[x-1])
        # print newlist1[x], "number of x:", x, "in the list", my_list[x]
    # print newlist
    # print newlist1
    print max(max(newlist1),max(newlist))

    pass


count, my_list_ = reading_input()
calculation(my_list_,count)