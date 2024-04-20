from tkinter import *
import random
from typing import List, Tuple

# Constants
GAME_WIDTH: int = 800
GAME_HEIGHT: int = 800
SPEED: int = 200  # Lower the number faster the game
SPACE_SIZE: int = 50
BODY_PARTS: int = 4
SNAKE_COLOR: str = "green"
FOOD_COLOR: str = "orange"
BACKGROUND_COLOR: str = "black"


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
class Food:
    """
    Represents the food in the game.
    """

    def __init__(self, canvas: Canvas) -> None:
        """
        Initializes the Food object.
        """
        x: int = random.randint(0, (GAME_WIDTH // SPACE_SIZE) - 1) * SPACE_SIZE
        y: int = random.randint(0, (GAME_HEIGHT // SPACE_SIZE) - 1) * SPACE_SIZE

        self.coordinates: List[int] = [x, y]

        canvas.create_oval(
            x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag="food"
        )

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

    def start(self) -> None:
        """
        Starts the game loop.
        """
        self.canvas.after(SPEED, self.next_turn)

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

    def check_collisions(self) -> bool:
        """
        Checks for collisions with walls or itself.
        """
        x, y = self.snake.coordinates[0]

        if x < 0 or x >= GAME_WIDTH:
            return True
        if y < 0 or y >= GAME_HEIGHT:
            return True

        for body_part in self.snake.coordinates[1:]:
            if x == body_part[0] and y == body_part[1]:
                return True
        return False

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
        self.start()


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

def main() -> None:
    """
    Main function to start the game.
    """
    window = Tk()
    initialize_game(window)
    window.mainloop()


if __name__ == "__main__":
    main()
