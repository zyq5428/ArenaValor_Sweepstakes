# 加载 Tk 库
from tkinter import *
# 子模块 tkinterttktkinter
from tkinter import ttk

# 如果我们显式更改与小部件关联的文本变量的值（正如我们所做的一样，它被附加到我们的标签上），
# 小部件将自动 使用变量的当前内容进行更新
def calculate(*args):
    try:
        value = float(feet.get())
        meters.set(int(0.3048 * value * 10000.0 + 0.5)/10000.0)
    except ValueError:
        pass

# 设置主应用程序窗口
root = Tk()
# 设置窗口标题
root.title("Feet to Meters")

# 创建内容框架(使用“主题”框架小部件来保存内容可确保 背景是正确的)
# 填充 left: 3, top: 3, right: 12, bottom: 12
mainframe = ttk.Frame(root, padding="3 3 12 12") 
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# 设置标签(创建小部件本身，然后将其放置在屏幕上)
feet = StringVar()
# 指定它的父级,条目显示的宽度为7个字符
feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
# 网格选项描述了小部件应如何 使用罗盘方向在网格单元格内对齐，（西-东）表示将其连接到左右两侧
feet_entry.grid(column=2, row=1, sticky=(W, E))

# 标签将显示我们计算的结果（米）
meters = StringVar()
ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))

# “计算”按钮，按下该按钮来执行计算
ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)

# 三个静态文本标签来明确如何使用该应用程序
ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

# 对用户界面进行了一些最后的润色
for child in mainframe.winfo_children(): 
    # 设置每个小部件的内边距，所有小部件周围添加一点填充物，这样它们就不会那么挤在一起
    child.grid_configure(padx=5, pady=5)

# 告诉Tk将焦点放在我们的入口小部件上。这样光标将从该字段开始，因此用户在开始键入之前不必单击它
feet_entry.focus()
# 如果用户按Return键（在Windows上为 Enter），它应该调用我们的计算例程，就像他们按下“计算”按钮一样
root.bind("<Return>", calculate)

root.mainloop()