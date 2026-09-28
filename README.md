# genpark-voronoi-diagram-delaunay-dual-skill

Agent Skill implementing **Voronoi Diagram construction from Delaunay Triangulation dual graphs**, computing circumcenters and orthogonal bisector adjacency.

## Architectural Overview
```mermaid
flowchart TD
    Sites["Planar Generator Sites"] --> Delaunay["Bowyer-Watson Delaunay Triangulation"]
    Delaunay --> Circumcenters["Calculate Triangle Circumcenters (Voronoi Vertices)"]
    Delaunay --> Adjacency["Map Shared Triangle Edges"]
    Circumcenters & Adjacency --> Voronoi["Construct Dual Voronoi Edges & Cells"]
```
