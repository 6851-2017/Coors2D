import Coors2D as c2d
points_1 = [(-2, -8), (-1, -8), (1, -8), (10, -7), (-2, -6), (-3, -6), (6, -5), (-10, -3), (-6, -2), (8, -1), (-2, 1), (3, 2), (4, 3), (-4, 7), (-6, 9)]
coors = c2d.COORS2D2Sided(points_1)

print(coors.xarray)
coors.is_sparse_x_value(-3, points_1)

