# 🐢 Turtle Crossing Game

A simple arcade-style **Turtle Crossing Game** built with **Python's turtle graphics module**.
The goal is to help the turtle cross the road while avoiding moving cars. Each time the turtle reaches the top, the level increases and the cars move faster.

---

## 🎮 Gameplay

* Control the turtle and try to **reach the top of the screen**.
* Avoid the **moving cars**.
* Each successful crossing:

  * Increases the **level**
  * Makes the **cars move faster**

If a car hits the turtle, the game ends.

---

## 🕹 Controls

| Key            | Action                  |
| -------------- | ----------------------- |
| **Up Arrow ↑** | Move the turtle forward |

---

## 📂 Project Structure

```
turtle_crossing/
│
├── main.py          # Main game loop
├── player.py        # Turtle player logic
├── car_manager.py   # Car creation and movement
├── scoreboard.py    # Level display and game over
└── README.md        # Project documentation
```

---

## ⚙️ How It Works

### `main.py`

Handles the **game loop**, screen setup, collision detection, and level progression.

### `player.py`

Controls the turtle player:

* Moving forward
* Resetting position when a level is completed

### `car_manager.py`

Manages the cars:

* Creates new cars
* Moves all cars across the screen
* Increases car speed when the level increases

### `scoreboard.py`

Displays:

* Current **level**
* On compeleting all **levels** **you won** message   
* **Game Over** message

---

## 🚀 How to Run the Game

1. Clone the repository

```bash
git clone https://github.com//jiya-patel2//Intermediate-Python-Projects//turtle-crossing.git
```

2. Navigate to the project folder

```bash
cd turtle-crossing-game
```

3. Run the game

```bash
python main.py
```

---

## 🧠 Concepts Practiced

This project demonstrates:

* **Object Oriented Programming (OOP)**
* Python **classes and objects**
* Game loops
* Collision detection
* Turtle graphics
* Keyboard event handling

---

## 📌 Future Improvements

* Add **start / restart screen**

---
