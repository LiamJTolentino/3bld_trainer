import magiccube

solved_state = ''.join([x*9 for x in "WOGRBY"])
cube = magiccube.Cube(3,solved_state)

cube.rotate("D' B2 U' B2 L2 D2 R2 D B2 D L' D F2 L' U B2 U' R' F U L'")

print(cube)