#coding=utf-8
#! /bin/python

import ctypes
so = ctypes.CDLL("../bin/librcfile.so")
while True:
    print '请输入你的选择:\n1-显示当前目录下文件\t2-创建新文件\t3-创建新文件夹\t4-进入文件夹\t5-返回上一层\t6-删除文件\t7-删除目录\t8-显示当前目录\t9-退出'
    selection = int(raw_input())
    if selection == 1:
        fun = so.list_file
        string = ctypes.create_string_buffer(10240)
        fun(string)
        print string.value
        
    elif selection == 2:
        fun = so.new_file
        string = ctypes.create_string_buffer(10240)
        print '请输入文件名:'
        t = raw_input()
        string.value = t
        fun(t)
        
    elif selection == 3:
        fun = so.new_dir
        string = ctypes.create_string_buffer(10240)
        print '请输入目录名:'
        t = raw_input()
        string.value = t
        fun(t)
        
    elif selection == 6:
        fun = so.del_file
        string = ctypes.create_string_buffer(10240)
        print '请输入要删除的文件名:'
        t = raw_input()
        string.value = t
        fun(t)
        
    elif selection == 7:
        fun = so.del_dir
        string = ctypes.create_string_buffer(10240)
        print '请输入要删除的目录名:'
        t = raw_input()
        string.value = t
        fun(t)
    
    elif selection == 8:
        fun = so.get_dir
        string = ctypes.create_string_buffer(10240)
        fun(string)
        print string.value
    
    elif selection == 9:
        break;
    else:
        print '输入错误'
