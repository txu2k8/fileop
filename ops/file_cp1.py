#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:TXU
@file:file_cp1
@time:2023/4/14
@email:tao.xu2008@outlook.com
@description:
# 待改进:
# 1.拷贝逻辑使用原生的io
# 2.针对大文件在进程内部实现多线程方式进行拷贝
"""
import time
import re
import os
import shutil
import multiprocessing
from loguru import logger

from pkgs.utils import date_str_calc


# 遍历文件夹
def walk_file(file):
    file_list = list()
    for root, dirs, files in os.walk(file):
        # 遍历文件
        for f in files:
            file_list.append(f)
    return file_list


# 计算文件数量
def get_file_count(dir):
    return len(walk_file(dir))


def copy(src, target, queue):
    target_number = 1
    if os.path.isdir(src):
        target_number = get_file_count(src)
        shutil.copytree(src, target)
    else:
        shutil.copyfile(src, target)
    # 将拷贝完成的文件数量放入队列中
    queue.put(target_number)


def copy_dir(src, desc):
    total_number = get_file_count(src)
    # 分隔符检测
    src = check_separator(src)
    desc = check_separator(desc)
    # print("src:",src)
    # print("desc:",desc)

    file_dir_list = [src + "/" + i for i in os.listdir(src)]
    if os.path.exists(desc):
        shutil.rmtree(desc)
    pool = multiprocessing.Pool(3)

    # 创建队列
    queue = multiprocessing.Manager().Queue()

    # 一个文件/目录开启一个进程去拷贝
    for f_name in file_dir_list:
        target = desc + "/" + os.path.basename(f_name[index_list("/", f_name)[1] + 1:])  # ss
        # print(target)
        # 创建target目录
        parent_path = os.path.split(target)[0]
        if not os.path.exists(parent_path):
            os.makedirs(parent_path)
        pool.apply_async(copy, args=(f_name, target, queue,))

    start = time.time()
    pool.close()
    #    pool.join()
    count = 0
    while True:
        count += queue.get()
        # 格式化输出时两个%输出一个%,不换行,每次定位到行首,实现覆盖
        print("\r拷贝进度为 %.2f %%" % (count * 100 / total_number), end="")
        if count >= total_number:
            break
    end = time.time()
    print()
    print("耗时-----", (end - start), "s")


# 查找指定字符出现的全部索引位置
def index_list(c, s):
    return [i.start() for i in re.finditer(c, s)]


# 检测目录结尾是否有 "/"
def check_separator(path):
    if path.rindex("/") == len(path) - 1:
        return path[0:path.rindex("/")]
    return path


def run_cp(src, dst, loop=1):
    idx = 0
    while True:
        if idx >= loop:
            break
        target = os.path.join(dst, date_str_calc(idx))
        logger.info(f'idx={idx}; cp {src} --> {target}')
        try:
            copy_dir(src, target)
        except Exception as e:
            logger.error(e)


if __name__ == '__main__':
    run_cp("z:/dd/", "Y:/ss/")
