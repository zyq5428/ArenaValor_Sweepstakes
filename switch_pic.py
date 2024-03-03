import tkinter as tk
import random
from PIL import Image, ImageTk

class RandomImageSwitcher:
    def __init__(self, root):
        self.root = root
        self.root.title("Random Image Switcher")

        # 图片路径列表（替换成你自己的图片路径）
        self.image_paths = ["./image/海月_幻泉雾影.jpg",
                            "./image/海月_浮梦罗烟_海报.png",
                            "./image/海月_王牌新星_海报.jpg"]
        self.current_image_index = 0

        # 创建图像界面
        self.image_label = tk.Label(root)
        self.image_label.pack()

        # 创建按钮
        self.button = tk.Button(root, text="随机切换图片", command=self.switch_image)
        self.button.pack()

        # 显示初始图片
        self.show_image()

    def show_image(self):
        image_path = self.image_paths[self.current_image_index]
        img = Image.open(image_path)
        img = img.resize((300, 300))  # 调整图片大小
        img_tk = ImageTk.PhotoImage(img)
        self.image_label.configure(image=img_tk)
        self.image_label.image = img_tk

    def switch_image(self):
        # 随机切换到下一张图片
        self.current_image_index = random.randint(0, len(self.image_paths) - 1)
        self.show_image()

if __name__ == "__main__":
    root = tk.Tk()
    app = RandomImageSwitcher(root)
    root.mainloop()
