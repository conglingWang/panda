# !/usr/bin/env Python
# coding=gb2312
import csv
import os

import jieba

exclude_words = ['的', '怎么', '怎么', '做', '了', '是', '用', '', '有', '怎么办', '怎么回事', '怎么样', '怎么']
words = {}
original_file_name = 'D:\\怎么长尾词_1621258000.csv'
with open(original_file_name, encoding='gbk') as original_file:
    csv_reader = csv.reader(original_file)
    for row in csv_reader:
        arr = jieba.lcut(row[0])
        for word in arr:
            if len(word) > 1 and word not in exclude_words:
                if word in words:
                    words[word] = words[word] + 1
                else:
                    words[word] = 1
    words = sorted(words.items(), key=lambda d: d[1], reverse=True)
    result_file_name = 'd:\\高频_' + os.path.basename(original_file_name).split('.')[0] + ".csv"
    with open(result_file_name, 'w', encoding='gbk', newline="") as result_file:
        csv_writer = csv.writer(result_file)
        for w in words:
            if w[1] > 200:
                csv_writer.writerow([w[0], w[1]])
