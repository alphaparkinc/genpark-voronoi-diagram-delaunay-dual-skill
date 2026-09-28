from client import VoronoiDiagram

points = [(0.0, 0.0), (1.0, 0.0), (0.0, 1.0), (1.0, 1.0), (0.5, 0.5)]
vor = VoronoiDiagram.compute_voronoi(points)

print("Voronoi Tessellation Summary:")
print(f"Generators: {vor['num_generators']}")
print(f"Voronoi Vertices: {vor['num_voronoi_vertices']}")
print(f"Internal Voronoi Edges: {vor['num_internal_voronoi_edges']}")
