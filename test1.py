# !/usr/bin/env Python
# coding=gb2312
import csv
import os

import jieba


def cos_vector(x, y):
    if len(x) != len(y):
        print('error input,x and y is not in the same space')
        return
    result1 = 0.0
    result2 = 0.0
    result3 = 0.0
    for i in range(len(x)):
        result1 += x[i] * y[i]  # sum(X*Y)
        result2 += x[i] ** 2  # sum(X*X)
        result3 += y[i] ** 2  # sum(Y*Y)
    return result1 / ((result2 * result3) ** 0.5)


exclude_words = ['的', '怎么', '怎么', '做', '了', '是', '用', '', '有', '怎么办', '怎么回事', '怎么样', '怎么']
arr_2 = []
result_file_name = 'd:\\分析结果.csv'
for root, dirs, files in os.walk('d:\\cwc1'):
    for original_file_name in files:
        original_file_path = root + "\\" + original_file_name
        original_file_base_name = original_file_name.split(".")[0]
        original_exclude_words = original_file_base_name.split(' ')
        if os.path.isfile(original_file_path):
            with open(original_file_path, encoding='gbk') as original_file:
                original_file.__next__()
                csv_reader = csv.reader(original_file)
                for row in csv_reader:
                    arr = jieba.lcut(row[0])
                    arr_2.append(arr)
arr_result = []
for arr1 in arr_2:
    if arr1:
        arr_result_e = [''.join(arr1)]
        for i in range(len(arr_2)):
            arr2 = arr_2[i]
            if arr1 and arr2 and arr1 != arr2:
                arr_total = arr1 + arr2
                arr_total = list(set(arr_total))
                arr1_x = []
                arr2_x = []
                for w in arr_total:
                    if w in arr1:
                        arr1_x.append(1)
                    else:
                        arr1_x.append(0)
                    if w in arr2:
                        arr2_x.append(1)
                    else:
                        arr2_x.append(0)
                cos = cos_vector(arr1_x, arr2_x)
                if cos >= 0.6:
                    arr_result_e.append(''.join(arr2))
                    arr_2[i] = []
        arr_result.append(arr_result_e)

with open(result_file_name, 'w', encoding='gbk', newline="") as result_file:
    csv_writer = csv.writer(result_file)
    for w in arr_result:
        csv_writer.writerow(w)
