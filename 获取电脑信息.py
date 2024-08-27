from tkinter import *
from tkinter.ttk import *
from ttkbootstrap import Style
import tkinter.font as tf
import pynvml
import psutil
import platform

# 主窗口设置
root = Tk()
root.title("获取电脑信息_制作人:半仙_qq:1668721189")
root.geometry('800x600+300+100')
root.iconbitmap('myicon.ico')

#滚动条设置
Scrollbar(root,cursor='spider').pack(side=RIGHT,fill=Y)

#设置字体
default_font = tf.nametofont('TkDefaultFont')
default_font.configure(family='微软雅黑',size=17)
          
''' 建立下拉菜单
top = Menu(root)
menuFile = Menu(top)
top.add_cascade(label='文件',menu=menuFile)
menuFile.add_command(label='打开',accelerator='Ctrl+N')
menuFile.add_command(label='保存',accelerator='Ctrl+S')
menuFile.add_separator()
menuFile.add_command(label='退出',command=root.destroy,accelerator='Ctrl+Alt')
'''


#基础信息
Label(root,text=f'\n操作系统名称:{platform.system()}').pack()
Label(root,text=f'\n操作系统版本:{platform.version()}').pack()
Label(root,text=f'\n处理器名称:{platform.processor()}').pack()
Label(root,text=f'\n处理器架构:{platform.architecture()}').pack()
#显卡信息
pynvml.nvmlInit() 
handle = pynvml.nvmlDeviceGetHandleByIndex(0) #获取显卡id信息
meminfo = pynvml.nvmlDeviceGetMemoryInfo(handle) #获取显存信息
Label(root,text=f'\n显卡个数:{pynvml.nvmlDeviceGetName(handle)}').pack()
Label(root,text=f'\n显卡驱动版本:{pynvml.nvmlSystemGetDriverVersion()}').pack()
Label(root,text=f'\n显卡个数:{pynvml.nvmlDeviceGetCount()}').pack()
Label(root,text=f'\n显存大小:{int(meminfo.total/1024/1024/1024)}GB').pack()

#内存信息
mem = psutil.virtual_memory()
Label(root,text=f'\n内存大小:{int(mem.total/1024/1024/1024)}GB',).pack()


# root.config(menu=top)
root.mainloop()
