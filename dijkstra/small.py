from manim import *

# Set the resolution and aspect ratio
config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 28
config.frame_width = 8
config.disable_caching = True


class Small(Scene):
    def construct(self):

        # Create vertices
        vertices = {
            "A": [0, 4, 0],
            "B": [2, 2, 0],
            "C": [-2, 2, 0],
            "D": [0, 0, 0],
            "E": [2, -2, 0],
            "F": [-2, -2, 0],
            "G": [0, -4, 0],
        }

        # Create edges with weights
        edges = [
            ("A", "B", 6),
            ("A", "C", 2),
            ("B", "D", 8),
            ("C", "D", 5),
            ("D", "E", 10),
            ("D", "F", 15),
            ("E", "G", 2),
            ("F", "G", 6),
        ]

        # Create vertex objects
        vertex_objects = {
            name: LabeledDot(
                Text(name, font_size=20, color=PURE_GREEN, font="Arial"),
                point=pos,
                color=BLACK,
                # fill_opacity=0.2,
                radius=0.3,
                stroke_color=PURE_GREEN,
                stroke_width=2,
            ).set_z_index(1)
            for name, pos in vertices.items()
        }

        # Draw vertices
        for vertex in vertex_objects.values():
            self.add(vertex)

        # Create edge objects
        edge_objects = {}
        for start, end, weight in edges:
            edge = Line(
                vertex_objects[start].get_center(),
                vertex_objects[end].get_center(),
                color=WHITE,
            )
            weight_label = Text(str(weight), font_size=18).next_to(
                edge.get_center(), UP
            )
            edge_objects[(start, end)] = (edge, weight_label)
            edge_objects[(end, start)] = (
                edge,
                weight_label,
            )  # Because the graph is undirected
            self.add(edge)
            self.add(weight_label)

        # Dijkstra's algorithm visualization
        start_vertex = "A"
        unvisited = set(vertices.keys())
        distances = {vertex: float("inf") for vertex in vertices}
        distances[start_vertex] = 0
        previous_vertices = {vertex: None for vertex in vertices}

        # Show initial distances
        distance_labels = {
            vertex: Text(f"∞", font_size=24)
            .next_to(vertex_objects[vertex], DOWN)
            .set_z_index(2)
            for vertex in vertices
        }
        for label in distance_labels.values():
            self.add(label)

        while unvisited:
            # Find the unvisited vertex with the smallest distance
            current_vertex = min(unvisited, key=lambda vertex: distances[vertex])
            unvisited.remove(current_vertex)

            # Update distances to neighbors
            for start, end, weight in edges:
                if start == current_vertex and end in unvisited:
                    new_distance = distances[start] + weight
                    if new_distance < distances[end]:
                        distances[end] = new_distance
                        previous_vertices[end] = start
                        self.play(
                            Transform(
                                distance_labels[end],
                                Text(f"{new_distance}", font_size=24, color=PURE_GREEN)
                                .next_to(vertex_objects[end], DOWN)
                                .set_z_index(2),
                            ),
                            run_time=1,
                        )

        # Highlight the shortest path
        current_vertex = "G"
        edges = []
        while previous_vertices[current_vertex] is not None:
            start = previous_vertices[current_vertex]
            edge, weight_label = edge_objects[(start, current_vertex)]
            self.play(edge.animate.set_color(PURE_GREEN), run_time=0.1)
            edges.append(edge.animate.set_stroke(width=10))

            current_vertex = start

        self.play(*edges, run_time=0.5)

        self.wait(2)
