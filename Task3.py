"""
下面的文件将会从csv文件中读取读取短信与电话记录，
你将在以后的课程中了解更多有关读取文件的知识。
"""
import csv
import re

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
任务3:
(080)是班加罗尔的固定电话区号。
固定电话号码包含括号，
所以班加罗尔地区的电话号码的格式为(080)xxxxxxx。

第一部分: 找出被班加罗尔地区的固定电话所拨打的所有电话的区号和移动前缀（代号）。
 - 固定电话以括号内的区号开始。区号的长度不定，但总是以 0 打头。
 - 移动电话没有括号，但数字中间添加了
   一个空格，以增加可读性。一个移动电话的移动前缀指的是他的前四个
   数字，并且以7,8或9开头。
 - 电话促销员的号码没有括号或空格 , 但以140开头。

输出信息:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
代号不能重复，每行打印一条，按字典顺序排序后输出。

第二部分: 由班加罗尔固话打往班加罗尔的电话所占比例是多少？
换句话说，所有由（080）开头的号码拨出的通话中，
打往由（080）开头的号码所占的比例是多少？

输出信息:
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
注意：百分比应包含2位小数。
"""
# 被叫代号列表（元素不重复）
_receiving_code_set = set()
# 被叫代号列表（元素重复）
_receiving_code_list = []


def switch_receiving_code(num):
    """
    通过正则获取所需电话号码中的代号
    Args:
        num: string 电话号码
    """
    if re.match(r'\(\d+\)', num):
        # 返回座机代号
        return re.match(r'\(\d+\)', num).group(0)
    elif re.match(r'^(7|8|9)\d+', num):
        # 返回手机代号
        return re.match(r'^(7|8|9)\d+', num).group(0)[:4]
    elif re.match(r'^140\d+$', num):
        # 电话促销员
        return re.match(r'^140\d+$', num).group(0)[:4]
    else:
        return None


def save_receiving_code(num):
    """
    存储被叫电话号码的代号
    Args:
        num: string 被叫电话号码
    """
    global _receiving_unique_code_list
    global _receiving_code_list
    matched_code = switch_receiving_code(num)
    if matched_code:
        _receiving_code_list.append(matched_code)
        _receiving_code_set.add(matched_code)


def print_receving_code(lists):
    """
    格式化输出
    Args:
        lists: list 待输出列表
    """
    print("The numbers called by people in Bangalore have codes:")
    for item in lists:
        print(item)


# 班加罗尔的区号
code = '(080)'
# part 1
for call in calls:
    if code in call[0]:
        save_receiving_code(call[1])


# 按字典排序 & 格式化输出
print_receving_code(sorted(_receiving_code_set))

# part 2
# 被叫 为班加罗尔 的数量
bangalore_receiving_code = _receiving_code_list.count(code)
proportion_bangalore = round(bangalore_receiving_code / len(_receiving_code_list), 2)
print("{:.2%} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(
    proportion_bangalore))
