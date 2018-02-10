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
任务2: 哪个电话号码的通话总时间最长? 不要忘记，用于接听电话的时间也是通话时间的一部分。
输出信息:
"<telephone number> spent the longest time, <total time> seconds, on the phone during
September 2016.".

提示: 建立一个字典，并以电话号码为键，通话总时长为值。
这有利于你编写一个以键值对为输入，并修改字典的函数。
如果键已经存在于字典内，为键所对应的值加上对应数值；
如果键不存在于字典内，将此键加入字典，并将它的值设为给定值。
"""
_phone_number_dicts = {}

def sum_number_duration_time(num, time):
    """
    计算单个号码的通话时间并存储到'_phone_number_dicts'字典中
    Args:
        num: string 电话号码
        time: string 通话时间
    """
    global _phone_number_dicts
    if num in _phone_number_dicts:
        _phone_number_dicts[num] += int(time)
    else:
        _phone_number_dicts[num] = int(time)

# 该函数可用内置max函数替代
# def longest_duration_time():
#     """
#     计算最长通话时间并返回对应的字典键，如果出现多个最长记录取第一个
#     """
#     global _phone_number_dicts
#     longest_time = 0
#     longest_time_key = None
#     for key in _phone_number_dicts:
#         if _phone_number_dicts[key] > longest_time:
#             longest_time = _phone_number_dicts[key]
#             longest_time_key = key
#     return longest_time_key


# 遍历通话记录计算每个电话的通话时间
for call in calls:
    calling = call[0]
    receiving = call[1]
    duration_time = call[3]
    # 主叫通话时间
    sum_number_duration_time(calling, duration_time)
    # 被叫通话时间
    sum_number_duration_time(receiving, duration_time)
# 获取最长通话时间对应的字典键与值
# longest_time_key = longest_duration_time()
longest_time_key = max(_phone_number_dicts, key=_phone_number_dicts.get)
longest_time = _phone_number_dicts[longest_time_key]

print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(
    longest_time_key,
    str(longest_time)
))
