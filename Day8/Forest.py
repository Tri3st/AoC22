# Forest class

class Forest:

    def __init__(self, data):
        self.data = data
        self.highest_centric = 0
        self.dim_x = len(self.data[0])
        self.dim_y = len(self.data)
        self.grid = [[0 for _ in range(self.dim_x)] for _ in range(self.dim_y)]
        self.visible = (2 * self.dim_x) + (2 * self.dim_y) - 4
        self.populate()
        self.calc()

    def populate(self):
        y = 0
        for row in self.data:
            x = 0
            for column in row:
                self.grid[y][x] = column
                x += 1
            y += 1

    def calc(self):
        for y in range(1, self.dim_y - 1):
            for x in range(1, self.dim_x - 1):
                if self.calc_visible(x, y):
                    self.visible += 1

    def calc_visible(self, x, y):
        all_xs = [self.grid[y][xs] for xs in range(self.dim_x)]
        # split it
        xs_l = all_xs[:x]
        xs_l.reverse()
        xs_l_c = self.centric_val(self.grid[y][x], xs_l)
        xs_r = all_xs[x + 1:]
        xs_r_c = self.centric_val(self.grid[y][x], xs_r)
        visible_l = len([i for i in xs_l if i >= self.grid[y][x]]) == 0
        visible_r = len([i for i in xs_r if i >= self.grid[y][x]]) == 0
        all_ys = [self.grid[ys][x] for ys in range(self.dim_y)]
        # split it
        ys_u = all_ys[:y]
        ys_u.reverse()
        ys_u_c = self.centric_val(self.grid[y][x], ys_u)
        ys_d = all_ys[y + 1:]
        ys_d_c = self.centric_val(self.grid[y][x], ys_d)
        visible_u = len([i for i in ys_u if i >= self.grid[y][x]]) == 0
        visible_d = len([i for i in ys_d if i >= self.grid[y][x]]) == 0
        total_centric = xs_l_c * xs_r_c * ys_u_c * ys_d_c
        if total_centric > self.highest_centric:
            self.highest_centric = total_centric
        return visible_l or visible_r or visible_u or visible_d

    def centric_val(self, val, my_list):
        cent = len(my_list)
        for i in range(len(my_list)):
            if my_list[i] >= val:
                return i + 1
        return cent

    def __str__(self):
        res = ""
        y = 0
        for row in range(self.dim_y):
            x = 0
            for column in range(self.dim_x):
                res += str(self.grid[y][x])
                x += 1
            res += "\n"
            y += 1
        return res
