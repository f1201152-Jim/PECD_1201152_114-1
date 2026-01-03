import tkinter as tk
import random

ROWS = 5
COLS = 5
MINES = 5

window = tk.Tk()
window.title("踩地雷 V3")

mines = [[False]*COLS for _ in range(ROWS)]
flags = [[False]*COLS for _ in range(ROWS)]
buttons = []

# 放地雷
count = 0
while count < MINES:
    r = random.randint(0, ROWS - 1)
    c = random.randint(0, COLS - 1)
    if not mines[r][c]:
        mines[r][c] = True
        count += 1

def count_mines(r, c):
    total = 0
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < ROWS and 0 <= nc < COLS:
                if mines[nr][nc]:
                    total += 1
    return total

def game_over():
    for r in range(ROWS):
        for c in range(COLS):
            if mines[r][c]:
                buttons[r][c].config(text="💣", bg="red")

def left_click(r, c):
    if flags[r][c]:
        return

    if mines[r][c]:
        game_over()
        print("Game Over")
    else:
        n = count_mines(r, c)
        buttons[r][c].config(text=str(n), state="disabled")

def right_click(event, r, c):
    if buttons[r][c]["state"] == "disabled":
        return

    if not flags[r][c]:
        buttons[r][c].config(text="🚩")
        flags[r][c] = True
    else:
        buttons[r][c].config(text="")
        flags[r][c] = False

for r in range(ROWS):
    row = []
    for c in range(COLS):
        btn = tk.Button(window, width=4, height=2)
        btn.grid(row=r, column=c)

        btn.config(command=lambda r=r, c=c: left_click(r, c))
        btn.bind("<Button-3>", lambda e, r=r, c=c: right_click(e, r, c))

        row.append(btn)
    buttons.append(row)

window.mainloop()
