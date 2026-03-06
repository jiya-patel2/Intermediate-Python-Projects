---

## 📂 Project Architecture

The game logic is divided into four main components to ensure the code is "DRY" (Don't Repeat Yourself) and easy to maintain:

* **`main.py`**: The "Brain." It manages the game loop, screen updates, and collision logic between the ball and other objects.
* **`paddle.py`**: Handles paddle creation, positioning, and boundary-limited movement (preventing paddles from leaving the screen).
* **`ball.py`**: Manages the ball's trajectory. Includes `bounce_x()` and `bounce_y()` methods to handle directional changes.
* **`scoreboard.py`**: A specialized `Turtle` subclass that writes and clears the score on the screen in real-time.

---

## 🧪 Technical Details

The game uses a coordinate system where the center of the screen is $(0,0)$.

* **Screen Dimensions**: $800 \times 600$ pixels.
* **Frame Refresh**: Controlled via `screen.tracer(0)` and `screen.update()` to eliminate flickering and ensure smooth animation.
* **Ball Physics Logic**:
    * **Vertical Bounce**: Triggered when the ball's Y-coordinate is $|y| > 280$ (hitting top or bottom walls).
    * **Paddle Bounce**: Triggered when the distance between the ball and paddle is $< 60$ pixels and the X-coordinate exceeds $|330|$.
    * **Velocity**: The `move_speed` starts at $0.1$ and reduces (speeds up) by $10\%$ with every successful paddle hit.

---

## 🚀 Future Improvements

- [ ] **Start Screen**: Add a landing page with instructions before the game loop begins.
- [ ] **SFX**: Integrate the `winsound` or `pygame` mixer for bounce and score sound effects.
- [ ] **Win State**: Implement a logic check (e.g., `if score == 10`) to trigger a "Game Over" message and stop the loop.
- [ ] **AI Opponent**: Create a simple tracking logic for the left paddle to allow for single-player mode.

---

**Developed with Python Turtle Graphics** 🐍