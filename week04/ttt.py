import random
s = 3                      
pl = ["X", "0"]          
d = "Draw"                 
ck = "y"            
    
win_lines = []
for r in range(s):
    win_lines.append([r * s + c for c in range(s)])             
for c in range(s):
    win_lines.append([r * s + c for r in range(s)])             
win_lines.append([i * s + i for i in range(s)])                 
win_lines.append([i * s + (s - 1 - i) for i in range(s)])    

total_squares = s * s           
width = len(str(total_squares))
results = []                  

playing = True
while playing:
    board = [str(n) for n in range(1, total_squares + 1)]
    turn = 0
    round_winner = None

    while round_winner is None:
        player = pl[turn % len(pl)]

        print()
        for r in range(s):
            line = " " + " | ".join(cell.rjust(width) for cell in board[r * s:(r + 1) * s])
            print(line)
            if r < s     - 1:
                print("-" * len(line))
        print()

        if player == "X":
            while True:
                choice = input(f"Player X, choose a square (1-{total_squares}): ")
                if not choice.isdigit() or not 1 <= int(choice) <= total_squares:
                    print(f"Please enter a number from 1 to {total_squares}.")
                elif board[int(choice) - 1] in pl:
                    print("That square is taken, try again.")
                else:
                    board[int(choice) - 1] = player
                    break
        else:
            available = [i for i, cell in enumerate(board) if cell not in pl]
            choice = random.choice(available)
            board[choice] = player
            print(f"Computer chooses square {choice + 1}.")

        for line in win_lines:
            first = board[line[0]]
            if first in pl and all(board[i] == first for i in line):
                round_winner = first

        if round_winner is None and all(cell in pl for cell in board):
            round_winner = d

        turn += 1

    print()
    for r in range(s):
        print(" " + " | ".join(cell.rjust(width) for cell in board[r * s:(r + 1) * s]))
    print()
    if round_winner == d:
        print("It's a draw!")
    else:
        print(f"Player {round_winner} wins!")

    results.append(round_winner)

    again = input(f"Play another round? ({ck}/n): ").strip().lower()
    playing = again == ck

print("\n FINAL SCORE ")
for p in pl:
    print(f"Player {p}: {results.count(p)}")
print(f"{d}s: {results.count(d)}")

print("\nRound by round:")
for i, winner in enumerate(results, start=1):
    print(f"  Round {i}: {winner}")
