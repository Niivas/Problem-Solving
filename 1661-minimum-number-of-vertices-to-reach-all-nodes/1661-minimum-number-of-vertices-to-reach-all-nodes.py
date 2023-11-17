class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        # Create a set of all vertices initially
        vertices = set(range(n))

        # Iterate through the edges
        for i in edges:
            # If the second vertex of an edge is in the set of vertices
            if i[1] in vertices:
                # Remove it from the set
                vertices.remove(i[1])

        # Convert the set of vertices to a list and return
        return list(vertices)
