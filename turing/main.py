from collections import deque
import sys


class TuringMachine:
    def __init__(self, tape: list[str], program: list[list[str]]):
        self.tape = list(tape)
        self.program = program

    def get_transitions(self, state: str, symbol: str):
        return [rule for rule in self.program if rule[0] == state and rule[1] == symbol]

    def run(self):
        queue: deque[tuple[list[str], int, str, list[str]]] = deque()
        queue.append((self.tape[:], 0, 'init', []))
        visited = set()

        while queue:
            tape, head, state, path = queue.popleft()

            if head < 0:
                tape = ["_"] + tape
                head += 1
            elif head >= len(tape):
                tape.append("_")

            tape_snapshot = "".join(tape)
            pointer_line = " " * head + "^"
            current_output = f"{tape_snapshot} {state}\n{pointer_line}\n"
            new_path = path + [current_output]

            if (tuple(tape), head, state) in visited:
                continue
            visited.add((tuple(tape), head, state))

            if state.startswith('halt'):
                print("".join(new_path))
                return

            symbol = tape[head]
            transitions = self.get_transitions(state, symbol)

            if not transitions:
                continue

            for trans in transitions:
                _, read_sym, write_sym, direction, next_state = trans
                new_tape = tape[:]
                new_tape[head] = write_sym
                head_change = 0
                if direction == 'R':
                    head_change = 1
                elif direction == 'L':
                    head_change = -1
                new_head = head + head_change
                queue.append((new_tape, new_head, next_state, new_path))

        print("No halting path found.")


def main():
    if len(sys.argv) != 3:
        print(f"Usage: python {sys.argv[0]} <tape> <function_file>")
        return
    tape = [symbol for symbol in sys.argv[1]]
    function_file = sys.argv[2]
    try:
        with open(function_file, 'r') as file:
            function_code = [line.strip().split() for line in file]
    except FileNotFoundError:
        print(f"Error: Function file '{function_file}' not found.")
        return
    except Exception as e:
        print(f"Error executing function file: {e}")
        return
    turing = TuringMachine(tape, function_code)
    turing.run()


if __name__ == "__main__":
    main()
