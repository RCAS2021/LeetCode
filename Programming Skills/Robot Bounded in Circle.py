class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        # Initializes direction facing north
        direction = (0, 1)
        # Initializes position
        pos = [0, 0]

        # For each insctruction
        for i in instructions:
            # If instruction = G, pos.x and pos.y += dir.x and dir.y
            if i == "G":
                pos[0] += direction[0]
                pos[1] += direction[1]
            # If instruction = L, dir.x = -dir.y and dir.y = dir.x
            elif i == "L":
                direction = (-direction[1], direction[0])
            # If instruction = R, dir.x = dir.y and dir.y = -dir.x
            elif i == "R":
                direction = (direction[1], -direction[0])

            print(f"after {i}, new pos ={pos}")
            print(f"after {i}, new dir ={direction}")
        # If pos == [0, 0] (initial position) or direction != (0, 1) (north)
        return pos == [0, 0] or direction != (0, 1)
