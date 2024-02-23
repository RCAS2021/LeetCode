class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        player = 0
        grid_a, grid_b = set(), set()
        length = len(moves)
        moves = map(tuple, moves)

        # All Possible wins
        win = (
            {(0,0),(0,1),(0,2)}, {(0,0),(1,0),(2,0)},
            {(1,0),(1,1),(1,2)}, {(0,1),(1,1),(2,1)},
            {(2,0),(2,1),(2,2)}, {(0,2),(1,2),(2,2)},
            {(0,0),(1,1),(2,2)}, {(0,2),(1,1),(2,0)},
        )
        # Populating the grids
        for i in moves:
            # If player is even, then player = A, else B
            if player % 2 == 0:
                grid_a.add(i)
            else:
                grid_b.add(i)
            player += 1

        # For each possible win
        for j in win:
            # Test if A = j or bigger, example: A = (0,0) , (0,1) , (0,2) , (1,0). There is a win in j = (0,0), (0,1), (0,2).
            # There is a need to test for bigger due to there possibly having the match ((0,0) , (0,1) , (0,2)) + some other non-matching points (1,0)
            if grid_a >= j:
                return "A"
            if grid_b >= j:
                return "B"

        return "Pending" if length < 9 else "Draw"
