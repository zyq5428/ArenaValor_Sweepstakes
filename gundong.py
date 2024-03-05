import tkinter as tk

class ScrollingTextApp:
    def __init__(self, root):
        self.root = root
        self.root.title("多个文本循环上下滚动")
        self.root.geometry("400x250")

        # 创建一个滚动文本框
        self.text_widget = tk.Text(root, wrap=tk.WORD)
        self.text_widget.pack()

        # 添加文本内容
        self.text_widget.insert(tk.END, "文本1\n")
        self.text_widget.insert(tk.END, "文本2\n")
        self.text_widget.insert(tk.END, "文本3\n")
        # 添加更多文本...

        # 启动滚动
        self.scroll_text()

    def scroll_text(self):
        # 获取文本框中的内容
        text_content = self.text_widget.get("1.0", tk.END)
        # 将最后一行移到第一行
        text_content = text_content.split("\n")
        text_content.insert(0, text_content.pop())

        # 清空文本框
        self.text_widget.delete("1.0", tk.END)
        # 插入更新后的文本
        for line in text_content:
            self.text_widget.insert(tk.END, line + "\n")

        # 递归调用，实现循环滚动
        self.root.after(2000, self.scroll_text)

if __name__ == "__main__":
    root = tk.Tk()
    app = ScrollingTextApp(root)
    root.mainloop()
