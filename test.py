# !/usr/bin/env Python
# coding=gb2312
import csv
import os

import jieba

exclude_words = ['的', '怎么', '怎么', '做', '了', '是', '用', '', '有', '怎么办', '怎么回事', '怎么样', '怎么']
words = {}
result_file_name = 'd:\\分析结果.csv'
for root, dirs, files in os.walk('d:\\cwc'):
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
                    for word in arr:
                        if len(word) > 1 and word not in exclude_words and word not in original_exclude_words:
                            word = original_file_base_name + " " + word
                            if words.__contains__(word):
                                words[word] = words[word] + 1
                            else:
                                words[word] = 1
words = sorted(words.items(), key=lambda d: d[1], reverse=True)
with open(result_file_name, 'w', encoding='gbk', newline="") as result_file:
    csv_writer = csv.writer(result_file)
    for w in words:
        if w[1] > 200:
            csv_writer.writerow([w[0], w[1]])
