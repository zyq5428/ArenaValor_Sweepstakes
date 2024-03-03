import sys
import random
import tkinter as tk

class LotteryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("抽奖程序")
        self.root.geometry("400x300")

        self.participants = ["张三", "李四", "王五", "赵六", "钱七", "孙八"]
        self.is_running = False
        self.winner = ""

        self.label = tk.Label(root, text="即将开始", font=("Arial", 20))
        self.label.pack(pady=20)

        self.start_button = tk.Button(root, text="开始抽奖", command=self.start_lottery)
        self.start_button.pack()

        self.stop_button = tk.Button(root, text="停止抽奖", command=self.stop_lottery, state=tk.DISABLED)
        self.stop_button.pack()

    def start_lottery(self):
        if not self.is_running:
            self.is_running = True
            self.start_button.config(state=tk.DISABLED)
            self.stop_button.config(state=tk.NORMAL)
            self.roll()

    def stop_lottery(self):
        if self.is_running:
            self.is_running = False
            self.start_button.config(state=tk.NORMAL)
            self.stop_button.config(state=tk.DISABLED)
            self.label.config(text=f"中奖者：{self.winner}")

    def roll(self):
        self.winner = random.choice(self.participants)
        self.label.config(text=self.winner)
        if self.is_running:
            self.root.after(100, self.roll)

if __name__ == "__main__":
    root = tk.Tk()
    app = LotteryApp(root)
    root.mainloop()
