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
# 通话记录主叫集合
# 通过list comprehension 生成 list 学到了
possible_phone_list = [x[0] for x in calls]
# 通过二维list与空list求和转换成一维list：[[1,2]] + [] = [1,2] 很厉害的思路
impossible_phone_list = sum([[x[0], x[1]] for x in texts], []) + [x[1] for x in calls]
# sorted 函数能对可迭代的对象排序
telemarketers = sorted(set(possible_phone_list) - set(impossible_phone_list))

print("These numbers could be telemarketers: ")
for x in telemarketers:
    print(x)
