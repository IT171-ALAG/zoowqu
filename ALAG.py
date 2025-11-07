player_x = 0
player_y = 0

treasure_x = 7
treasure_y = 3
game_running = True

print(f"Find the treasure at ({treasure_x}, {treasure_y})!")

while game_running:
    move = input("Enter move (w/a/s/d or q to quit): ")

    if move == "w":
        player_y += 1
    elif move == "s":
        player_y -= 1
    elif move == "a":
        player_x -= 1
    elif move == "d":
        player_x += 1
    elif move == "q":
        print("Game exited.")
        game_running = False
        continue
    else:
        print("Invalid input, use w/a/s/d or q only.")
        continue

    print(f"Player position: ({player_x}, {player_y})")

    if player_x == treasure_x and player_y == treasure_y:
        print("You found the treasure! You win!")
        game_running = False
