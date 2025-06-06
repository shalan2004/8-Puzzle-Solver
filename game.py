import heapq
import tkinter as tk
from collections import deque
import time

GOAL = [1, 2, 3, 4, 5, 6, 7, 8, 0]

def manhattan(state):
    return sum(
        abs((val - 1) // 3 - i // 3) + abs((val - 1) % 3 - i % 3)
        for i, val in enumerate(state) if val
    )

def is_solvable(puzzle):
    inv = sum(
        1 for i in range(len(puzzle)) for j in range(i + 1, len(puzzle))
        if puzzle[i] and puzzle[j] and puzzle[i] > puzzle[j]
    )
    return inv % 2 == 0

def get_moves(state):
    i = state.index(0)
    r, c = divmod(i, 3)
    moves = []
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < 3 and 0 <= nc < 3:
            ni = nr * 3 + nc
            new = state[:]
            new[i], new[ni] = new[ni], new[i]
            moves.append(new)
    return moves

def greedy(start):
    heap = [(manhattan(start), 0, start, [])]
    visited = set()

    while heap:
        _, cost, curr, path = heapq.heappop(heap)
        if curr == GOAL:
            return path

        t = tuple(curr)
        if t in visited:
            continue
        visited.add(t)

        for next_state in get_moves(curr):
            if tuple(next_state) not in visited:
                heapq.heappush(heap, (manhattan(next_state), cost + 1, next_state, path + [next_state]))
    return []

def bfs(start):
    queue = deque([(start, [])])
    visited = set()

    while queue:
        curr, path = queue.popleft()
        if curr == GOAL:
            return path

        t = tuple(curr)
        if t in visited:
            continue
        visited.add(t)

        for next_state in get_moves(curr):
            if tuple(next_state) not in visited:
                queue.append((next_state, path + [next_state]))
    return []

class PuzzleGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("8 Puzzle Solver")
        self.tiles = []
        self.state = GOAL.copy()

        self.frame = tk.Frame(root)
        self.frame.pack(padx=10, pady=10)

        for i in range(9):
            btn = tk.Button(self.frame, text=str(self.state[i]) if self.state[i] != 0 else '',
                            width=6, height=3, font=('Arial', 24),
                            command=lambda i=i: self.move_tile(i))
            btn.grid(row=i // 3, column=i % 3, padx=5, pady=5)
            self.tiles.append(btn)

        self.controls = tk.Frame(root)
        self.controls.pack(pady=10)

        self.entry = tk.Entry(self.controls, font=('Arial', 14), width=20)
        self.entry.grid(row=0, column=0, padx=5)

        self.solve_button = tk.Button(self.controls, text="Solve", command=self.start_solving, font=('Arial', 14))
        self.solve_button.grid(row=0, column=1, padx=5)

        self.algo_var = tk.StringVar(value="Greedy")
        self.algo_menu = tk.OptionMenu(self.controls, self.algo_var, "Greedy", "BFS")
        self.algo_menu.config(font=('Arial', 14))
        self.algo_menu.grid(row=0, column=2, padx=5)

    def move_tile(self, index):
        zero_index = self.state.index(0)
        r1, c1 = divmod(index, 3)
        r0, c0 = divmod(zero_index, 3)
        if abs(r1 - r0) + abs(c1 - c0) == 1:
            self.state[zero_index], self.state[index] = self.state[index], self.state[zero_index]
            self.update_board()

    def update_board(self):
        for i, val in enumerate(self.state):
            self.tiles[i].config(text=str(val) if val != 0 else '')

    def start_solving(self):
        raw = self.entry.get().strip()
        try:
            nums = list(map(int, raw.split()))
            if sorted(nums) != list(range(9)):
                print("Invalid input: Please enter 9 unique numbers from 0 to 8.")
                return
            if not is_solvable(nums):
                print("Unsolvable puzzle.")
                return

            self.state = nums
            self.update_board()

            algo = self.algo_var.get()

            start_time = time.perf_counter()
            if algo == "Greedy":
                path = greedy(self.state)
            else:
                path = bfs(self.state)
            end_time = time.perf_counter()

            if path is not None:
                duration = end_time - start_time
                self.result_info = (algo, duration, len(path))  # Store for later print
                self.animate_solution(path)
            else:
                print("No solution found.")
        except Exception:
            print("Invalid input format.")

    def animate_solution(self, path):
        if not path:
            return
        def step(i=0):
            if i >= len(path):
                algo, duration, moves = self.result_info
                print(f"{algo} took {duration:.6f} seconds and {moves} moves.")
                return
            self.state = path[i]
            self.update_board()
            self.root.after(50, step, i + 1)
        step()

if __name__ == "__main__":
    root = tk.Tk()
    app = PuzzleGUI(root)
    root.mainloop()
