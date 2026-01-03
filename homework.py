import tkinter as tk
import random

# -------------------------
# 基本設定
# -------------------------
ROWS = 5
COLS = 5
MINES = 5

# 建立主視窗
window = tk.Tk()
window.title("踩地雷 V1")

# 儲存地雷位置 (True = 地雷)
mines = [[False for _ in range(COLS)] for _ in range(ROWS)]

# 隨機放地雷
count = 0
while count < MINES:
    r = random.randint(0, ROWS - 1)
    c = random.randint(0, COLS - 1)
    if not mines[r][c]:
        mines[r][c] = True
        count += 1

# 點擊事件
def click(r, c):
    if mines[r][c]:
        buttons[r][c].config(text="💣", bg="red")
        print("Game Over")
    else:
        buttons[r][c].config(text="O", state="disabled")

# 建立按鈕棋盤
buttons = []
for r in range(ROWS):
    row = []
    for c in range(COLS):
        btn = tk.Button(
            window,
            width=4,
            height=2,
            command=lambda r=r, c=c: click(r, c)
        )
        btn.grid(row=r, column=c)
        row.append(btn)
    buttons.append(row)

window.mainloop()
