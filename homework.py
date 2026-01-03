import tkinter as tk
import random

ROWS = 5
COLS = 5
MINES = 5

window = tk.Tk()
window.title("踩地雷 V2")

mines = [[False for _ in range(COLS)] for _ in range(ROWS)]

# 放地雷
count = 0
while count < MINES:
    r = random.randint(0, ROWS - 1)
    c = random.randint(0, COLS - 1)
    if not mines[r][c]:
        mines[r][c] = True
        count += 1

# 計算周圍地雷數
def count_mines(r, c):
    total = 0
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < ROWS and 0 <= nc < COLS:
                if mines[nr][nc]:
                    total += 1
    return total

def click(r, c):
    if mines[r][c]:
        buttons[r][c].config(text="💣", bg="red")
        print("Game Over")
    else:
        number = count_mines(r, c)
        buttons[r][c].config(text=str(number), state="disabled")

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
