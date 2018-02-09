"""
下面的文件将会从csv文件中读取读取短信与电话记录，
你将在以后的课程中了解更多有关读取文件的知识。
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
任务1：
短信和通话记录中一共有多少电话号码？每个号码只统计一次。
输出信息：
"There are <count> different telephone numbers in the records."
"""
# 存储所有电话号码的集合
_phone_number_set = set()


def add_phone_numbers(lists):
    """
    向全局变量"_phone_number_set"中添加电话号码
    lists[0]:主叫
    lists[1]：被叫
    Args:
        lists: 短信或电话列表
    """
    # use global variable
    global _phone_number_set
    for item in lists:
        _phone_number_set.add(item[0])
        _phone_number_set.add(item[1])


# 添加短信号码
add_phone_numbers(texts)
print(_phone_number_set)

# 添加通话记录号码
add_phone_numbers(calls)
print(_phone_number_set)
print("There are {} different telephone numbers in the records.".format(str(len(_phone_number_set))))
