"""
排序算法实现
"""

"""
插入排序
直接插入 折半插入排序 希尔排序 
"""


def insert_sort(li):
    for i in range(2, len(li)):
        if li[i] < li[i-1]:
            li[0] = li[i]       # 复制为哨兵
            li[i] = li[i-1]
            j = i-1
            while li[0] < li[j]:
                li[j+1] = li[j]
                j = j-1
            li[j+1] = li[0]
    return li


def b_insert_sort(li):
    print(li)
    return li


def shell_sort(li, dk):     # dk为步长因

    return li


if __name__ == '__main__':
    test_li = [0, 3, 12, 22, 33, 55, 43, 32, 21, 5, 1, 6, 4, 9]
    li_res = insert_sort(test_li)
    print(li_res)
