# 💣 minesweeper-pygame-2026

An educational project — an implementation of the classic **Minesweeper** game in Python using  
**pygame** and **numpy**.

> ⚠️ Known issues — the project is **under development** and is not considered finished.

---

## 🧠 Project Goal

- Understand the internal logic of the *Minesweeper* game
- Practice working with:
  - `pygame` (graphics, events, input)
  - `numpy` (two-dimensional arrays)
  - object-oriented programming
- Create a foundation for further project development

---

## 📁 Project Structure

```text
minesweeper-pygame-2026/
├── main.py      # Main game logic
├── block.py     # Game field cell class
├── func.py      # Helper functions
├── game.py      # Menu (prototype)
└── README.md
```

---

🧱 block.py — Cell Class
This file contains the Block class, which represents a single cell of the game field.
Main responsibilities of the class:
- Rendering the cell
- Handling mouse clicks
- Displaying text (number, flag, bomb)
- Storing the cell state

🔹 Main Methods
#### onBlock(x, y)
    1. Checks whether the cursor is inside the cell.
    2. Used to determine clicks on a specific block.
####  onClick(ind)
    1. Checks for mouse button presses:
        0 — left button
        2 — right button
>📌 Polling is used (pg.mouse.get_pressed()),
so button lock protection is implemented in main.py.
#### GetPos():
    1. Returns the cell position in the format: (y, x)

> 📌 The format was deliberately chosen for compatibility with numpy,
where indexing is done as [row, column].

#### SetColor(blockColor, borderColor)
    1. Changes the color of the cell and saves the previous values 
        (used when setting and removing the flag).

#### SetText(text)
    1. Used to set text inside the cell:
        (number of mines nearby, “!”, “B”).

#### Mark()
    1. Sets or removes the flag:
        changes the cell color
        sets the “!” symbol
    2. When called again, returns the previous state

---

🧰 func.py — auxiliary functions
#### Control(x, y, max_X, max_Y)
    1. Checks whether the coordinates are within the game field.
2. Used:
    when counting bombs
    when recursively clearing empty cells

#### Equals(A1, A2)
1. Checks whether two lists contain identical elements
        (used to check for victory — all bombs are marked).

> ⚠️ The order of elements is not taken into account.

#### Grey(x)
1. Returns a shade of gray: (x, x, x)

#### Change(num)
    1. Returns the color of the cell depending on the value:
        9 — bomb
        0 — empty cell
        1–8 — number of mines nearby

---

🎮 main.py — game logic

Main steps:
- Creating the game field (numpy)
- Random generation of bombs
- Counting mines around each cell
- Creating visual blocks (Block)
- Processing clicks:
- LMB — open cell
- RMB — place/remove flag
- Victory check
- BombCounter(array, x, y)
- Counts the number of bombs around a cell
(within a radius of 1 cell).

#### CleanPlace(...)
    Recursively opens neighboring cells if the selected cell is empty (0).
    The depth of recursion is limited (i < 4).

🧪 Known issues:
- The player can lose on the first click
- The menu (game.py) is not yet integrated into the main loop

🔧 Development plans:
- Guarantee of a safe first click
- Improvement of the algorithm for clearing empty cells
- Full menu and game restart
- Separation of logic and visualization
- Improved victory check
- Customizable field size and number of bombs

🤝 Participation:
- All project code is written by the repository author
- The project is used for educational and experimental purposes
- Active development and architecture refactoring are planned
- ChatGPT's assistance was limited to writing the README file