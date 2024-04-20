# Making a Snake game in Python with Tkinter

Another week, another time to practice building something new! As of classic arcade games, few titles evoke as much nostalgia and entertainment as THE timeless Snake Game. I am certain many of us spent countless hours on our old Nokia phones trying to hit a new high score. With its simple yet addictive gameplay, Snake has remained a base mobile game on various platforms since its first iterations. Today in this article, we'll see the process of developing it using Python and the basic Tkinter library for the graphics. If you wanna play around more here is the link for the GitHub repo.

## Introduction

The Snake Game, originally introduced in the 1970s, gained immense popularity with the advent of mobile phones in the late 1990s. The objective of the game is straightforward: control a snake as it moves around the game board, eating food to grow longer. However, the challenge lies in avoiding collisions with the walls of the game area and with the snake's own body. Although many other variations exists.

Python, serves as an excellent choice for developing the our project. Additionally Tkinter, Python's de facto standard GUI (Graphical User Interface) toolkit, provides a convenient way to create interactive applications with minimal effort.

![Gameplay Screenshot](gameplay.png)

## Key components

### 1. Game logic

At the heart of the game lies the game logic, responsible for managing the snake's movement, food generation, scoring, and collision detection. This logic forms the backbone of the game and ensures a seamless and engaging experience for the player.

```python
# Game Logic

class Game:
    """
    Represents the game logic.
    """

    def __init__(self, canvas: Canvas, label: Label) -> None:
        """
        Initializes the Game object.
        """
        self.canvas: Canvas = canvas
        self.label: Label = label
        self.score: int = 0
        self.direction: str = "down"
        self.snake: Snake = Snake(canvas)
        self.food: Food = Food(canvas)
        self.game_over_text_id = None
        self.restart_button = None
```

### 2. Graphics rendering

Using Tkinter's canvas widget, we can render the game graphics, including the snake, food, and game board. Tkinter's basic drawing capabilities give us the chance to create a visually appealing and interactive game interface.

```python
# Graphics Rendering

class Snake:
    """
    Represents the Snake in the game.
    """

    def __init__(self, canvas: Canvas) -> None:
        """
        Initializes the Snake object.
        """
        self.body_size: int = BODY_PARTS
        self.coordinates: List[Tuple[int, int]] = []
        self.squares: List[int] = []

        for _ in range(0, BODY_PARTS):
            self.coordinates.append([0, 0])

        for x, y in self.coordinates:
            square = canvas.create_rectangle(
                x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tag="snake"
            )
            self.squares.append(square)
```

### 3. User interaction

User interaction is essential for the player to control the snake's movement. By capturing keyboard input, we enable players to guide the snake across the game board, adding an element of skill and strategy to the gameplay.

```python
# User Interaction

def change_direction(self, new_direction: str) -> None:
    """
    Changes the direction of the snake.
    """
    if new_direction == "left" and self.direction != "right":
        self.direction = new_direction
    elif new_direction == "right" and self.direction != "left":
        self.direction = new_direction
    elif new_direction == "up" and self.direction != "down":
        self.direction = new_direction
    elif new_direction == "down" and self.direction != "up":
        self.direction = new_direction
```

## The development process

### 1. Initialization

Here we begin by setting up the game window, defining constants such as the game board dimensions, speed, and colors. Additionally, we initialize the game elements, including the snake, food, and score display.

```python
# Initialization

def initialize_game(window: Tk) -> None:
    """
    Initializes the game.
    """
    window.title("SNAKE GAME")
    window.resizable(False, False)

    label = Label(window, text="Score:0", font=("consolas", 40))
    label.pack()

    canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
    canvas.pack()

    # Update window geometry
    window.update()
    window_width = window.winfo_width()
    window_height = window.winfo_height()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = int((screen_width / 2) - (window_width / 2))
    y = int((screen_height / 2) - (window_height / 2))
    window.geometry(f"{window_width}x{window_height}+{x}+{y}")

    # Bind arrow keys
    game = Game(canvas, label)
    window.bind("<Left>", lambda event: game.change_direction("left"))
    window.bind("<Right>", lambda event: game.change_direction("right"))
    window.bind("<Up>", lambda event: game.change_direction("up"))
    window.bind("<Down>", lambda event: game.change_direction("down"))

    game.start()
```

### 2. Game loop

The game loop forms the core of the game, executing continuously to update the game state, handle user input, and redraw the game graphics. As we are iterating through each game tick, we are ensuring a smooth and responsive gameplay.

```python
# Game Loop

def next_turn(self) -> None:
        """
        Moves the snake and updates the game state.
        """
        x, y = self.snake.coordinates[0]

        if self.direction == "up":
            y -= SPACE_SIZE
        elif self.direction == "down":
            y += SPACE_SIZE
        elif self.direction == "left":
            x -= SPACE_SIZE
        elif self.direction == "right":
            x += SPACE_SIZE

        self.snake.coordinates.insert(0, (x, y))

        square = self.canvas.create_rectangle(
            x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR
        )

        self.snake.squares.insert(0, square)

        if x == self.food.coordinates[0] and y == self.food.coordinates[1]:
            self.score += 1
            self.label.config(text=f"Score:{self.score}")
            self.canvas.delete("food")
            self.food = Food(self.canvas)  # Pass canvas to Food constructor
        else:
            del self.snake.coordinates[-1]
            self.canvas.delete(self.snake.squares[-1])
            del self.snake.squares[-1]

        if self.check_collisions():
            self.game_over()
        else:


            self.canvas.after(SPEED, self.next_turn)
```

### 3. Game over handling

After detecting a collision, we need to trigger the game over sequence, displaying a game over message and offering the player the option to restart the game. This feedback loop enhances player engagement, and just looks better than the restarting of the whole script.

```python
# Game Over Handling

def game_over(self) -> None:
        """
        Displays game over message and restart button.
        """
        if self.game_over_text_id is None:
            self.game_over_text_id = self.canvas.create_text(
                self.canvas.winfo_width() / 2,
                self.canvas.winfo_height() / 2,
                font=("consolas", 70),
                text="GAME OVER",
                fill="red",
                tag="gameover",
            )

            self.restart_button = Button(
                self.canvas,
                text="Restart",
                font=("consolas", 20),
                command=self.restart_game,
            )
            self.canvas.create_window(
                self.canvas.winfo_width() / 2,
                self.canvas.winfo_height() / 2 + 100,
                window=self.restart_button,
                tag="restart_button",
            )

def restart_game(self) -> None:
    """
    Restarts the game.
    """
    self.canvas.delete("gameover")
    self.canvas.delete("restart_button")
    self.canvas.delete("all")
    self.score = 0
    self.label.config(text=f"Score:{self.score}")
    self.snake = Snake(self.canvas)
    self.food = Food(self.canvas)
    self.game_over_text_id = None
    self.restart_button = None
```

## Conclusion

In conclusion, developing this game in Python yielded a rewarding and educational experience. - At least for me! - Also a good practice if you want to get back into Python development. We showed that we can create a captivating but still simple game that pays homage to the classics while showcasing some standard modern development techniques. This Game project provides an excellent opportunity to learn, experiment, and have fun for everyone. So why wait? Try it yourself!
