# by PKHG
# see https://github.com/nortikin/sverchok/issues/459
# based on
# "author": "original for 2.49 from Andy Houston , meta-androcto, Noctumsolis,
# (later >= Bl. 2.5) PKHG ",

from numpy import matrix as npMatrix
from enum import Enum


class Geo(Enum):

    tetra_top = 0
    tetra_edge = 1
    tetra_face = 2
    octra_top = 3
    octra_edge = 4
    octra_face = 5
    icosa_top = 6
    icosa_edge = 7
    icosa_face = 8
    # >8 becomes tetraeder_top


class HedronScript(SvScriptSimpleGenerator):

    @staticmethod
    def make_hedron(type_geodesic, layer, top_x, top_y, top_z, scale):
        x = top_x * scale
        y = top_y * scale
        z = top_z * scale

        [x0, x1, x2, y0, y1, y2, z0, z1, z2, x3, y3, z3, x4, y4, z4] = [0 for i in range(15)]
        use = (x, y, z)

        if layer == 0:
            (x0, y0, z0) = use
        elif layer == 1:
            (x1, y1, z1) = use
        elif layer == 2:
            (x2, y2, z2) = use
        elif layer == 3:
            (x3, y3, z3) = use
        elif layer == 4:
            (x4, y4, z4) = use

        if (type_geodesic == Geo.tetra_top.value) or (type_geodesic > 8):
            return (
                npMatrix([
                    (x0, y0, 1.73205080757 + z0),
                    (0.0 + x1, -1.63299316185 + y1, -0.577350269185 + z1),
                    (1.41421356237 + x1, 0.816496580927 + y1, -0.57735026919 + z1),
                    (-1.41421356237 + x1, 0.816496580927 + y1, -0.57735026919 + z1)
                    ])*(1.0 + scale)).tolist()

        elif type_geodesic == Geo.tetra_edge.value:
            return (
                npMatrix([
                    (x0, -1.41421356237 + y0, 1.0 + z0),
                    (x0, 1.41421356237 + y0, 1.0 + z0),
                    (1.41421356237 + x1, 0.0 + y1, -1.0 + z1),
                    (-1.41421356237 + x1, 0.0 + y1, -1.0 + z1)
                    ])*(1.0 + scale)).tolist()

        elif type_geodesic == Geo.tetra_face.value:
            return (
                npMatrix([
                    (-1.41421356237 + x0, -0.816496580927 + y0, 0.57735026919 + z0),
                    (1.41421356237 + x0, -0.816496580927 + y0, 0.57735026919 + z0),
                    (x0, 1.63299316185 + y0, 0.577350269185 + z0),
                    (x1, y1, -1.73205080757 + z1)
                    ])*(1.0 + scale)).tolist()

        elif type_geodesic == Geo.octra_top.value:
            return (
                npMatrix([
                    (x0, y0, 1.0 + z0),
                    (x1, 1.0 + y1, z1),
                    (-1.0 + x1, y1, z1),
                    (x1, -1.0 + y1, z1),
                    (1.0 + x1, y1, z1),
                    (x2, y2, -1.0 + z2)
                    ])*(1.0 + scale)).tolist()

        elif type_geodesic == Geo.octra_edge.value:
            return (
                npMatrix([
                    (0.0 + x0, -0.707106781187 + y0, 0.707106781187 + z0),
                    (0.0 + x0, 0.707106781187 + y0, 0.707106781187 + z0),
                    (1.0 + x1, y1,  z1),
                    (-1.0 + x1, y1,  z1),
                    (0.0 + x2, -0.707106781187 + y2, -0.707106781187 + z2),
                    (0.0 + x2, 0.707106781187 + y2, -0.707106781187 + z2)
                    ])*(1.0 + scale)).tolist()

        elif type_geodesic == Geo.octra_face.value:
            return (
                npMatrix([
                    (0.408248458663 + x0, -0.707106781187 + y0, 0.577350150255 + z0),
                    (0.408248458663 + x0, 0.707106781187 + y0, 0.577350150255 + z0),
                    (-0.816496412728 + x0, 0.0 + y0, 0.577350507059 + z0),
                    (-0.408248458663 + x1, -0.707106781187 + y1, -0.577350150255 + z1),
                    (0.816496412728 + x1, 0.0 + y1, -0.577350507059 + z1),
                    (-0.408248458663 + x1, 0.707106781187 + y1, -0.577350150255 + z1)
                    ])*(1.0 + scale)).tolist()

        elif type_geodesic == Geo.icosa_top.value:
            return (
                npMatrix([
                    (0.0 + x0, 0.0 + y0, 0.587785252292 + z0),
                    (0.0 + x1, -0.525731096637 + y1, 0.262865587024 + z1),
                    (0.5 + x1, -0.162459832634 + y1, 0.262865565628 + z1),
                    (0.309016994375 + x1, 0.425325419658 + y1, 0.262865531009 + z1),
                    (-0.309016994375 + x1, 0.425325419658 + y1, 0.262865531009 + z1),
                    (-0.5 + x1, -0.162459832634 + y1, 0.262865565628 + z1),
                    (0.309016994375 + x2, -0.425325419658 + y2, -0.262865531009 + z2),
                    (0.5 + x2, 0.162459832634 + y2, -0.262865565628 + z2),
                    (0.0 + x2, 0.525731096637 + y2, -0.262865587024 + z2),
                    (-0.5 + x2, 0.162459832634 + y2, -0.262865565628 + z2),
                    (-0.309016994375 + x2, -0.425325419658 + y2, -0.262865531009 + z2),
                    (0.0 + x3, 0.0 + y3, -0.587785252292 + z3)
                    ])*(1.0 + scale)).tolist()

        elif type_geodesic == Geo.icosa_edge.value:
            return (
                npMatrix([
                    (x0, 0.309016994375 + y0, 0.5 + z0),
                    (x0, -0.309016994375 + y0, 0.5 + z0),
                    (-0.5 + x1, 0 + y1, 0.309016994375 + z1),
                    (0.5 + x1, 0 + y1, 0.309016994375 + z1),
                    (-0.309016994375 + x2, -0.5 + y2, 0 + z2),
                    (0.309016994375 + x2, -0.5 + y2, 0 + z2),
                    (0.309016994375 + x2, 0.5 + y2, 0 + z2),
                    (-0.309016994375 + x2, 0.5 + y2, 0 + z2),
                    (-0.5 + x3, 0 + y3, -0.309016994375 + z3),
                    (0.5 + x3, 0 + y3, -0.309016994375 + z3),
                    (0 + x4, 0.309016994375 + y4, -0.5 + z4),
                    (0 + x4, -0.309016994375 + y4, -0.5 + z4)
                    ])*(1.0 + scale)).tolist()

        elif type_geodesic == Geo.icosa_face.value:
            return (
                npMatrix([
                    (-0.17841104489 + x0, 0.309016994375 + y0, 0.46708617948 + z0),
                    (-0.17841104489 + x0, -0.309016994375 + y0, 0.46708617948 + z0),
                    (0.35682208977 + x0, y0, 0.467086179484 + z0),
                    (-0.57735026919 + x1, 0.0 + y1, 0.110264089705 + z1),
                    (-0.288675134594 + x2, -0.5 + y2, -0.11026408971 + z2),
                    (0.288675134594 + x1, -0.5 + y1, 0.11026408971 + z1),
                    (0.57735026919 + x2, 0.0 + y2, -0.110264089705 + z2),
                    (0.288675134594 + x1, 0.5 + y1, 0.11026408971 + z1),
                    (-0.288675134594 + x2, 0.5 + y2, -0.11026408971 + z2),
                    (-0.35682208977 + x3, 0.0 + y3, -0.467086179484 + z3),
                    (0.17841104489 + x3, -0.309016994375 + y3, -0.46708617948 + z3),
                    (0.17841104489 + x3, 0.309016994375 + y3,  -0.46708617948 + z3)
                    ])*(1.0 + scale)).tolist()

    @staticmethod
    def make_edges(type_geodesic, layer, top_x, top_y, top_z, scale):
        edgeskeleton = [(0, 1), (0, 2), (0, 3), (1, 2), (2, 3), (1, 3)]
        if type_geodesic > 2 and type_geodesic < 6:  # octaeder
            edgeskeleton = [
                (0, 1), (0, 2), (0, 3), (0, 4), (1, 2), (2, 4), (3, 4), (1, 3),
                (1, 5), (2, 5), (3, 5), (4, 5)]
            if type_geodesic == 5:
                edgeskeleton = [
                    (0, 1), (0, 2), (0, 3), (0, 4), (1, 2), (2, 3), (3, 4), (1, 4),
                    (1, 5), (2, 5), (3, 5), (4, 5)]
        elif type_geodesic == 6:  # icosaeder
            edgeskeleton = [
                (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (1, 2), (2, 3), (3, 4),
                (4, 5), (5, 1), (1, 6), (2, 6), (2, 7), (3, 7), (3, 8), (4, 8),
                (4, 9), (5, 10), (1, 10), (6, 7), (7, 8), (8, 9), (9, 10),
                (10, 6), (6, 11), (7, 11), (8, 11), (9, 11), (10, 11)]
        elif type_geodesic == 7:
            edgeskeleton = [
                (0, 1), (0, 7), (0, 2), (1, 2), (1, 4), (1, 5), (1, 3), (0, 3),
                (0, 6), (2, 7), (2, 8), (2, 4), (4, 5), (3, 5), (3, 9), (3, 6),
                (6, 7), (7, 10), (7, 8), (4, 8), (4, 11), (5, 11), (5, 9), (6, 9),
                (6, 10), (8, 10), (8, 11), (9, 11), (9, 10), (10, 11)]
        elif type_geodesic == 8:
            edgeskeleton = [
                (0, 1), (2, 1), (2, 0), (0, 3), (1, 3), (1, 4), (1, 5), (2, 5),
                (2, 6), (2, 7), (0, 7), (0, 8), (3, 9), (3, 4), (5, 4), (5, 10),
                (5, 6), (7, 6), (7, 11), (7, 8), (3, 8), (4, 9), (4, 10), (6, 10),
                (6, 11), (8, 11), (8, 9), (9, 10), (11, 10), (11, 9)]
        return edgeskeleton

    @staticmethod
    def make_faces(type_geodesic, layer, top_x, top_y, top_z, scale):
        faceskeleton = [(0, 1, 2), (0, 2, 3), (0, 1, 3), (1, 2, 3)]
        if type_geodesic > 2 and type_geodesic < 6:  # octaeder
            faceskeleton = [
                (0, 1, 2), (0, 2, 3), (0, 3, 4), (0, 4, 1), (1, 2, 5),
                (2, 3, 5), (3, 4, 5), (4, 1, 5)]
            if type_geodesic == 4:
                faceskeleton = [
                    (0, 1, 2), (0, 1, 3), (0, 2, 4), (1, 2, 5), (1, 3, 5),
                    (0, 3, 4), (2, 4, 5), (3, 4, 5)]
            elif type_geodesic == 5:
                faceskeleton = [
                    (0, 1, 2), (0, 3, 4), (0, 1, 4), (1, 4, 5), (2, 1, 5),
                    (2, 3, 5), (0, 2, 3), (3, 4, 5)]
        elif type_geodesic == 6:  # icosaeder
            faceskeleton = [
                (0, 1, 2), (0, 2, 3), (0, 3, 4), (0, 4, 5), (0, 5, 1), (1, 2, 6),
                (2, 6, 7), (2, 3, 7), (3, 7, 8), (3, 4, 8), (4, 8, 9), (4, 5, 9),
                (5, 9, 10), (5, 1, 10), (1, 10, 6), (6, 7, 11), (7, 8, 11),
                (8, 9, 11), (9, 10, 11), (10, 6, 11)]
        elif type_geodesic == 7:
            faceskeleton = [
                (0, 1, 2), (0, 1, 3), (0, 2, 7), (1, 2, 4), (1, 4, 5), (1, 3, 5),
                (0, 3, 6), (0, 6, 7), (2, 7, 8), (2, 4, 8), (3, 5, 9), (3, 6, 9),
                (7, 8, 10), (4, 8, 11), (4, 5, 11), (5, 9, 11), (6, 9, 10),
                (6, 7, 10), (8, 10, 11), (9, 10, 11)]
        elif type_geodesic == 8:
            faceskeleton = [
                (2, 0, 1), (0, 1, 3), (2, 1, 5), (2, 0, 7), (1, 3, 4), (1, 5, 4),
                (2, 5, 6), (2, 7, 6), (0, 7, 8), (0, 3, 8), (3, 4, 9), (5, 4, 10),
                (5, 6, 10), (7, 6, 11), (7, 8, 11), (3, 8, 9), (4, 9, 10),
                (6, 11, 10), (8, 11, 9), (11, 9, 10)]

        return faceskeleton

    inputs = [
        ('s', "type_geodesic", 0),
        ('s', "layer", 0),
        ('s', "top_x", 0.0),
        ('s', "top_y", 0.0),
        ('s', "top_z", 0.0),
        ('s', 'scale', 0.1)]

    outputs = [
        ("v", "Verts", "make_hedron"),
        ("s", "Edges", "make_edges"),
        ("s", "Faces", "make_faces")]
