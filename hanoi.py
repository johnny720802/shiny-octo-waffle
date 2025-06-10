# hanoi.py
# Simple Tower of Hanoi implementation.

import sys


def hanoi(n, source, target, auxiliary, moves):
    """Solve Tower of Hanoi recursively.

    Parameters
    ----------
    n : int
        Number of disks.
    source : str
        The name of the source rod.
    target : str
        The name of the target rod.
    auxiliary : str
        The name of the auxiliary rod.
    moves : list
        List to append move tuples (disk, from, to).
    """
    if n <= 0:
        return
    # Move n-1 disks from source to auxiliary
    hanoi(n - 1, source, auxiliary, target, moves)
    # Move the nth disk from source to target
    moves.append((n, source, target))
    # Move the n-1 disks from auxiliary to target
    hanoi(n - 1, auxiliary, target, source, moves)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <num_disks>")
        sys.exit(1)
    try:
        disks = int(sys.argv[1])
    except ValueError:
        print("Number of disks must be an integer.")
        sys.exit(1)

    moves = []
    hanoi(disks, "A", "C", "B", moves)
    for disk, src, dst in moves:
        print(f"Move disk {disk} from {src} to {dst}")
    print(f"Total moves: {len(moves)}")
