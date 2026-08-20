# 🎯 Dodge the Bullet

A minimalist arcade-style dodging game built entirely with **Matplotlib**! Move left and right to dodge falling bullets for as long as you can.

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Animation-orange)


## 📖 About

Who says you need Pygame to make a game? This project proves that `matplotlib.animation.FuncAnimation` can power a simple, real-time, keyboard-controlled arcade game — complete with a black-themed retro look, a player sprite, and falling "bullets" you need to dodge.

## 🎮 How to Play

- A **white square** represents you (the player) at the bottom of the screen.
- A **red triangle (bullet)** falls from the top at random horizontal positions.
- Use the **Left** and **Right arrow keys** to move and dodge the bullet.
- If the bullet hits you, the game window closes — game over!
- Survive as long as possible by dodging repeated bullet drops.

## 🕹️ Controls

| Key | Action |
|------|---------|
| ⬅️ Left Arrow | Move player left |
| ➡️ Right Arrow | Move player right |

## 🛠️ Requirements

- Python 3.x
- Matplotlib

Install the dependency with:

```bash
pip install matplotlib
```

## 🚀 Getting Started

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/dodge-the-bullet.git
   cd dodge-the-bullet
   ```

2. Run the game:
   ```bash
   python dodge_the_bullet.py
   ```

3. Click on the game window to make sure it has focus, then use the arrow keys to start dodging!

## 📂 Project Structure

```
dodge-the-bullet/
│
├── dodge_the_bullet.py   # Main game script
└── README.md              # Project documentation
```

## ⚙️ How It Works

- **Rendering:** The game uses a Matplotlib figure as the game canvas, with a black background for a retro arcade feel.
- **Player & Bullet:** Both are drawn using `ax.scatter()` and updated every frame via `set_offsets()`.
- **Game Loop:** `FuncAnimation` drives the game loop, updating bullet position and checking for collisions roughly every 30ms.
- **Input Handling:** Keyboard events are captured with `fig.canvas.mpl_connect("key_press_event", move)` to move the player left or right.
- **Collision Detection:** A simple distance check between the player and bullet coordinates determines if a hit has occurred.
- **Respawning:** Once a bullet reaches the bottom of the screen without hitting the player, it respawns at the top at a new random position.

## 🔮 Possible Improvements

- [ ] Add a score counter that increases with each dodged bullet
- [ ] Increase difficulty over time (faster bullets, multiple bullets)
- [ ] Add sound effects
- [ ] Add a "Game Over" screen with restart option
- [ ] Smooth player movement instead of fixed steps

## 👤 Author

**Mohamed Afham**

## 📄 License

This project is open source, as long as i recieve the credits

---

⭐ If you liked this project, consider giving it a star on GitHub!
