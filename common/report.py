#coding=utf-8
import os


# 找出最新的报告
def Report(report):
    lists=os.listdir(report)
    lists.sort(key=lambda fn:os.path.getmtime(report+"\\"+fn))
    file=os.path.join(report,lists[-1])
    print file