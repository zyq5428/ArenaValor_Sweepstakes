# 加载 Tk 库
from tkinter import *
# 子模块 tkinterttktkinter
from tkinter import ttk, font
# 用于转换为tkinter支持的.png 或 .gif 格式的图片
from PIL import ImageTk, Image
import random

# 图片路径列表（替换成你自己的图片路径）
image_paths = ["./image/海月_幻泉雾影.jpg",
               "./image/海月_浮梦罗烟_海报.png",
               "./image/海月_王牌新星_海报.jpg"
               ]
current_image_index = 0

def show_image(*args):
    global current_image_index
    image_path = image_paths[current_image_index]
    img = Image.open(image_path)
    img = img.resize((392, 200))  # 调整图片大小
    img_tk = ImageTk.PhotoImage(img)
    skin_display.configure(image=img_tk)
    skin_display.image = img_tk

def sweep_stakes(*args):
    global current_image_index
    current_image_index = random.randint(0, len(image_paths) - 1)
    show_image()

# 设置主应用程序窗口
root = Tk()
# 设置窗口标题
root.title("王者荣耀")

# 创建内容框架(使用“主题”框架小部件来保存内容可确保背景是正确的)
# 填充 left: 3, top: 3, right: 12, bottom: 12
mainframe = ttk.Frame(root, padding="3 3 12 12") 
mainframe.grid(column=0, row=0, sticky=(N, S, W, E))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# 英雄皮肤展示界面
skin_display = ttk.Label(mainframe)
skin_display.grid(column=1, row=1, sticky=(N, S, W, E))
# skin_image = PhotoImage(file='./image/海月_幻泉雾影.jpg')
# skin_display['image'] = skin_image
show_image()

# 奖池界面
prize_frame = ttk.Frame(mainframe, borderwidth=5, relief="ridge", width=100, height=200)
prize_frame.grid(column=2, row=1, sticky=(N, S, W, E))
style = ttk.Style()
style.configure("BW.TLabel", foreground="gold")
prize1 = ttk.Label(prize_frame, text="英雄皮肤1", style="BW.TLabel")
prize1.grid(column=1, row=1, sticky=(W, E))
prize2 = ttk.Label(prize_frame, text="英雄皮肤2", style="BW.TLabel")
prize2.grid(column=1, row=2, sticky=(W, E))
# prize3 = ttk.Label(prize_frame, text="英雄皮肤3", style="BW.TLabel", anchor="center")
prize3 = ttk.Label(prize_frame, text="英雄皮肤3", style="BW.TLabel")
prize3.grid(column=1, row=3, sticky=(W, E))

# 皮肤介绍界面
skin_introduce = ttk.Label(mainframe, text="皮肤介绍", anchor="center")
skin_introduce.grid(column=1, row=2, sticky=(N, S, W, E))

# “抽奖”按钮，按下该按钮来执行计算
image = PhotoImage(file='./image/立即领取.png')
# style.configure('TButton', font=font.Font(family='华文楷体', size=24, weight='bold'), foreground="gold", background="white")
# lucky = ttk.Button(mainframe, text="开始抽奖", style='TButton', command=sweep_stakes)
lucky = ttk.Button(mainframe, command=sweep_stakes)
lucky['image'] = image
lucky.grid(column=2, row=2, sticky=(N, S, W, E))


# 对用户界面进行了一些最后的润色
for child in mainframe.winfo_children(): 
    # 设置每个小部件的内边距，所有小部件周围添加一点填充物，这样它们就不会那么挤在一起
    child.grid_configure(padx=5, pady=5)

# 自适应宽度
mainframe.columnconfigure(1, weight=1)
mainframe.columnconfigure(2, weight=1)
mainframe.rowconfigure(1, weight=1)
mainframe.rowconfigure(2, weight=1)

# 告诉Tk将焦点放在我们的入口小部件上。这样光标将从该字段开始，因此用户在开始键入之前不必单击它
lucky.focus()
# 如果用户按Return键（在Windows上为 Enter），它应该调用我们的计算例程，就像他们按下“计算”按钮一样
root.bind("<Return>", sweep_stakes)

root.mainloop()