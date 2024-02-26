class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        direction = (0, 1)
        initial_pos = [0, 0]

        for i in instructions:
            if i == "G":
                initial_pos[0] += direction[0]
                initial_pos[1] += direction[1]
            elif i == "L":
                direction = (-direction[1], direction[0])
            elif i == "R":
                direction = (direction[1], -direction[0])

        print(direction)
        print(initial_pos)
        return initial_pos == [0, 0] or direction != (0, 1)
