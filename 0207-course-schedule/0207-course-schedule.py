class Solution:
    def canFinish(self, num_courses: int, prerequisites: List[List[int]]) -> bool:
        # Initialize adjacency list to represent courses and their dependencies
        adjacency_list = [[] for _ in range(num_courses)]
        # Initialize indegree list to keep track of prerequisites count for each course
        indegree = [0] * num_courses
        # Initialize a list to store the order of courses that can be taken
        course_order = []

        # Populate the adjacency list and indegree list based on prerequisites
        for pair in prerequisites:
            course = pair[0]
            prerequisite = pair[1]
            adjacency_list[prerequisite].append(course)
            indegree[course] += 1

        # Initialize a queue to store courses with no prerequisites
        queue = deque()
        # Add all courses with 0 indegree to the queue
        for i in range(num_courses):
            if indegree[i] == 0:
                queue.append(i)

        # Perform topological sorting
        while queue:
            current_course = queue.popleft()
            # Add the current course to the order list
            course_order.append(current_course)

            # Process all dependent courses
            for next_course in adjacency_list[current_course]:
                # Decrement the indegree of the dependent course
                indegree[next_course] -= 1
                # If the indegree becomes 0, add it to the queue
                if indegree[next_course] == 0:
                    queue.append(next_course)

        # If all courses can be finished, the length of the order list should be equal to the total number of courses
        return len(course_order) == num_courses
