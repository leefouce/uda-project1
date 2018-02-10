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
任务4:
电话公司希望辨认出可能正在用于进行电话推销的电话号码。
找出所有可能的电话推销员:
这样的电话总是向其他人拨出电话，
但从来不发短信、接收短信或是收到来电


请输出如下内容
"These numbers could be telemarketers: "
<list of numbers>
电话号码不能重复，每行打印一条，按字典顺序排序后输出。
"""


def get_column_set(lists, column_name):
    """
    获取二维list中对应列的集合
    Args:
        lists: list 二维列表
        column_name: string 列名
    """
    column_set = set()
    for item in lists:
        column_set.add(item[column_name])
    return column_set


def print_telemarketer_list(lists):
    """
    格式化输出
    Args:
        lists: list 待输出列表
    """
    print("These numbers could be telemarketers:")
    for item in lists:
        print(item)


# 通话记录主叫集合
calling_set = get_column_set(calls, 0)
# 通话记录被叫集合
receiving_call_set = get_column_set(calls, 1)
# 短信发送集合
sending_set = get_column_set(texts, 0)
# 短信接收集合
receiving_text_set = get_column_set(texts, 1)
# 没有被叫的电话号码集合
never_receiving_numbers_set = calling_set - receiving_call_set
# 电话推销电话号码集合
telemarketer_set = never_receiving_numbers_set - sending_set - receiving_text_set
telemarketer_list = list(telemarketer_set)
# 字典排序
telemarketer_list.sort()
# 格式化输出
print_telemarketer_list(telemarketer_list)
