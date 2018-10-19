# For all roof / building generation functions, the lowest roof plane
# is centered at the origin.  The building portion of the object is
# extruded from this lowest roof plane to a length of
# "building_height".


# Generate flat roof building
def flatGen(roof_length,
            roof_width,
            building_height):
    xinterval = roof_length / 2
    yinterval = roof_width / 2

    vertices = [[-xinterval, yinterval, 0],
                [-xinterval, -yinterval, 0],
                [xinterval, -yinterval, 0],
                [xinterval, yinterval, 0],
                [-xinterval, yinterval, -building_height],
                [-xinterval, -yinterval, -building_height],
                [xinterval, -yinterval, -building_height],
                [xinterval, yinterval, -building_height]]

    faces = [[0, 1, 2, 3],
             [4, 7, 6, 5],
             [0, 4, 5, 1],
             [1, 5, 6, 2],
             [2, 6, 7, 3],
             [3, 7, 4, 0]]

    return vertices, faces


# Generate shed roof / building
def shedGen(roof_height,
            roof_length,
            roof_width,
            building_height):
    xinterval = roof_length / 2
    yinterval = roof_width / 2

    vertices = [[-xinterval, yinterval, 0],
                [-xinterval, -yinterval, roof_height],
                [xinterval, -yinterval, roof_height],
                [xinterval, yinterval, 0]]

    if building_height > 0:
        vertices.extend([[-xinterval, yinterval, -building_height],
                         [-xinterval, -yinterval, -building_height],
                         [xinterval, -yinterval, -building_height],
                         [xinterval, yinterval, -building_height]])

        faces = [[0, 1, 2, 3],
                 [4, 7, 6, 5],
                 [0, 4, 5, 1],
                 [1, 5, 6, 2],
                 [2, 6, 7, 3],
                 [3, 7, 4, 0]]
    else:
        vertices.extend([[-xinterval, -yinterval, 0],
                         [xinterval, -yinterval, 0]])

        faces = [[0, 1, 2, 3],
                 [0, 4, 5, 3],
                 [0, 1, 4],
                 [2, 3, 5],
                 [1, 2, 5, 4]]

    return vertices, faces


# Generate gable roof / building
def gableGen(roof_height,
             roof_length,
             roof_width,
             building_height):
    xinterval = roof_length / 2
    yinterval = roof_width / 2

    vertices = [[-xinterval, yinterval, 0],
                [-xinterval, 0, roof_height],
                [-xinterval, -yinterval, 0],
                [xinterval, -yinterval, 0],
                [xinterval, 0, roof_height],
                [xinterval, yinterval, 0]]

    if building_height > 0:
        vertices.extend([[-xinterval, yinterval, -building_height],
                         [-xinterval, -yinterval, -building_height],
                         [xinterval, -yinterval, -building_height],
                         [xinterval, yinterval, -building_height]])

        faces = [[0, 1, 4, 5],
                 [1, 2, 3, 4],
                 [0, 6, 7, 2, 1],
                 [2, 7, 8, 3],
                 [3, 8, 9, 5, 4],
                 [5, 9, 6, 0],
                 [6, 9, 8, 7]]
    else:
        faces = [[0, 1, 4, 5],
                 [1, 2, 3, 4],
                 [0, 1, 2],
                 [3, 4, 5],
                 [0, 2, 3, 5]]

    return vertices, faces


# Generate gambrel roof / building
def gambrelGen(roof_height_1,
               roof_height_2,
               roof_length,
               roof_width_1,
               roof_width_2,
               building_height):
    xinterval = roof_length / 2
    yinterval_1 = roof_width_1 / 2
    yinterval_2 = roof_width_2 / 2

    vertices = [[-xinterval, yinterval_1, 0],
                [-xinterval, yinterval_2, roof_height_1],
                [-xinterval, 0, roof_height_1 + roof_height_2],
                [-xinterval, -yinterval_2, roof_height_1],
                [-xinterval, -yinterval_1, 0],
                [xinterval, -yinterval_1, 0],
                [xinterval, -yinterval_2, roof_height_1],
                [xinterval, 0, roof_height_1 + roof_height_2],
                [xinterval, yinterval_2, roof_height_1],
                [xinterval, yinterval_1, 0]]

    if building_height > 0:
        vertices.extend([[-xinterval, yinterval_1, -building_height],
                         [-xinterval, -yinterval_1, -building_height],
                         [xinterval, -yinterval_1, -building_height],
                         [xinterval, yinterval_1, -building_height]])

        faces = [[0, 1, 8, 9],
                 [1, 2, 7, 8],
                 [2, 3, 6, 7],
                 [3, 4, 5, 6],
                 [0, 9, 13, 10],
                 [10, 13, 12, 11],
                 [11, 12, 5, 4],
                 [0, 1, 2, 3, 4, 11, 10],
                 [5, 6, 7, 8, 9, 13, 12]]
    else:
        faces = [[0, 1, 8, 9],
                 [1, 2, 7, 8],
                 [2, 3, 6, 7],
                 [3, 4, 5, 6],
                 [0, 1, 2, 3, 4],
                 [5, 6, 7, 8, 9]]

    return vertices, faces


# Generate hipped roof / building
def hippedGen(roof_height,
              roof_length_1,
              roof_length_2,
              roof_width,
              building_height):

    xinterval_1 = roof_length_1 / 2
    xinterval_2 = roof_length_2 / 2
    yinterval = roof_width / 2

    vertices = [[-xinterval_1, yinterval, 0],
                [-xinterval_2, 0, roof_height],
                [-xinterval_1, -yinterval, 0],
                [xinterval_1, -yinterval, 0],
                [xinterval_2, 0, roof_height],
                [xinterval_1, yinterval, 0]]

    if building_height > 0:
        vertices.extend([[-xinterval_1, yinterval, -building_height],
                         [-xinterval_1, -yinterval, -building_height],
                         [xinterval_1, -yinterval, -building_height],
                         [xinterval_1, yinterval, -building_height]])

        faces = [[0, 1, 4, 5],
                 [1, 2, 3, 4],
                 [0, 1, 2],
                 [2, 7, 8, 3],
                 [3, 4, 5],
                 [5, 9, 6, 0],
                 [6, 9, 8, 7],
                 [0, 2, 7, 6],
                 [3, 5, 9, 8]]
    else:
        faces = [[0, 1, 4, 5],
                 [1, 2, 3, 4],
                 [0, 1, 2],
                 [3, 4, 5],
                 [0, 2, 3, 5]]

    return vertices, faces


# Generate mansard roof / building
def mansardGen(roof_height_1,
               roof_height_2,
               roof_length_1,
               roof_length_2,
               roof_length_3,
               roof_width_1,
               roof_width_2,
               building_height):
    xinterval_1 = roof_length_1 / 2
    xinterval_2 = roof_length_2 / 2
    xinterval_3 = roof_length_3 / 2
    yinterval_1 = roof_width_1 / 2
    yinterval_2 = roof_width_2 / 2

    vertices = [[-xinterval_1, yinterval_1, 0],
                [-xinterval_2, yinterval_2, roof_height_1],
                [-xinterval_3, 0, roof_height_1 + roof_height_2],
                [-xinterval_2, -yinterval_2, roof_height_1],
                [-xinterval_1, -yinterval_1, 0],
                [xinterval_1, -yinterval_1, 0],
                [xinterval_2, -yinterval_2, roof_height_1],
                [xinterval_3, 0, roof_height_1 + roof_height_2],
                [xinterval_2, yinterval_2, roof_height_1],
                [xinterval_1, yinterval_1, 0]]

    if building_height > 0:
        vertices.extend([[-xinterval_1, yinterval_1, -building_height],
                         [-xinterval_1, -yinterval_1, -building_height],
                         [xinterval_1, -yinterval_1, -building_height],
                         [xinterval_1, yinterval_1, -building_height]])

        faces = [[0, 1, 8, 9],
                 [1, 2, 7, 8],
                 [2, 3, 6, 7],
                 [3, 4, 5, 6],
                 [0, 9, 13, 10],
                 [10, 13, 12, 11],
                 [11, 12, 5, 4],
                 [1, 2, 3],
                 [0, 1, 3, 4],
                 [0, 4, 11, 10],
                 [6, 7, 8],
                 [5, 6, 8, 9],
                 [5, 9, 13, 12]]
    else:
        faces = [[0, 1, 8, 9],
                 [1, 2, 7, 8],
                 [2, 3, 6, 7],
                 [3, 4, 5, 6],
                 [1, 2, 3],
                 [0, 1, 3, 4],
                 [6, 7, 8],
                 [5, 6, 8, 9],
                 [0, 4, 5, 9]]

    return vertices, faces
