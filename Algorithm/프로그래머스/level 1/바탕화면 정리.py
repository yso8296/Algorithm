def solution(wallpaper):
    lux = 51
    luy = 51
    rdx = 0
    rdy = 0
    h = len(wallpaper)
    w = len(wallpaper[0])
    for i in range(h):
        for j in range(w):
            if wallpaper[i][j] == '#':
                lux = min(lux, i)
                luy = min(luy, j)
                rdx = max(rdx, i)
                rdy = max(rdy, j)
    array = [lux, luy, rdx + 1, rdy + 1]
    return array