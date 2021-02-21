def water_trap(height):
    # given elevation map compute how much rain water is trapped
    if not height or len(height) < 2:
        return 0
    x = 0
    y = len(height) - 1
    xmax = 0
    ymax = 0
    water = 0
    while x < y:
        if height[x] < height[y]:
            if height[x] >= xmax:
                xmax = height[x]
            water += xmax - height[x]
            x += 1
        else:
            if height[y] >= ymax:
                ymax = height[y]
            water += ymax - height[y]
            y -= 1
    return water

print(water_trap([0,1,0,2,1,0,1,3,2,1,2,1]))
