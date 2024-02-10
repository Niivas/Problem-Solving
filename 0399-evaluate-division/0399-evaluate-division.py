class Solution:
    def answer(self, current, end, scalar):
        if current == end:
            return scalar

        self.visited.add(current)

        if current in self.graph:
            for i in self.graph[current]:
                if i[0] not in self.visited:
                    # Recursive call with updated variables
                    a = self.answer(i[0], end, scalar * i[1])

                    if a != -1:
                        return a

        return -1

    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        self.graph = {}  # Initialize the graph dictionary
        self.visited = set()  # Initialize the set of visited nodes

        # Build the graph
        for i, item in enumerate(equations):
            if item[0] not in self.graph:
                self.graph[item[0]] = []
            if item[1] not in self.graph:
                self.graph[item[1]] = []

            # Add two entries for each equation and value
            self.graph[item[0]].append((item[1], 1 / values[i]))
            self.graph[item[1]].append((item[0], values[i]))

        v = []  # Initialize the result list

        # Process the queries
        for i in queries:
            self.visited = set()  # Reset the set of visited nodes

            if i[0] not in self.graph or i[1] not in self.graph:
                # If any variable is not present in the graph, append -1 to the result
                v.append(-1)
                continue

            if i[0] == i[1]:
                # If both variables are the same, append 1 to the result
                v.append(1)
            else:
                # Call the answer function and append the result
                v.append(1 / self.answer(i[0], i[1], 1))

        return v
