from manim import *
import random

# Set the resolution and aspect ratio
config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 16
config.frame_width = 9
config.disable_caching = True


class Big(Scene):
    def construct(self):
        # Create 300 vertices positioned in a 12x25 grid pattern
        num_columns = 12
        num_rows = 25
        spacing_x = 0.6  # Horizontal spacing between nodes
        spacing_y = 0.6  # Vertical spacing between nodes
        vertices = {
            f"{i * num_columns + j}": [
                j * spacing_x - (num_columns - 1) * spacing_x / 2,
                (num_rows - 1) * spacing_y / 2 - i * spacing_y,
                0,
            ]
            for i in range(num_rows)
            for j in range(num_columns)
        }

        # Create random edges with weights
        edges = []
        for i in range(num_rows):
            for j in range(num_columns):
                current_node = i * num_columns + j
                # Connect to the right neighbor
                if j < num_columns - 1:
                    weight = random.randint(1, 20)
                    edges.append((f"{current_node}", f"{current_node + 1}", weight))
                # Connect to the bottom neighbor
                if i < num_rows - 1:
                    weight = random.randint(1, 20)
                    edges.append(
                        (f"{current_node}", f"{current_node + num_columns}", weight)
                    )

        # Create vertex objects
        vertex_objects = {
            name: LabeledDot(
                Text(name, font_size=8, color=GRAY_A, font="Arial"),
                point=pos,
                color=GRAY_E,
                radius=0.15,
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
            weight_label = Text(str(weight), font_size=8).move_to(
                (vertex_objects[start].get_center() + vertex_objects[end].get_center())
                / 2
            )
            edge_objects[(start, end)] = (edge, weight_label)
            edge_objects[(end, start)] = (
                edge,
                weight_label,
            )  # Because the graph is undirected
            self.add(edge)
            self.add(weight_label)

        # Dijkstra's algorithm visualization
        start_vertex = "0"
        unvisited = set(vertices.keys())
        distances = {vertex: float("inf") for vertex in vertices}
        distances[start_vertex] = 0
        previous_vertices = {vertex: None for vertex in vertices}

        # Show initial distances
        distance_labels = {
            vertex: Text(f"∞", font_size=8)
            .next_to(vertex_objects[vertex], DOWN)
            .set_z_index(2)
            for vertex in vertices
        }
        distance_labels[start_vertex] = (
            Text("0", font_size=8)
            .next_to(vertex_objects[start_vertex], DOWN)
            .set_z_index(2)
        )

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
                                Text(f"{new_distance}", font_size=8)
                                .next_to(vertex_objects[end], DOWN)
                                .set_z_index(2),
                            ),
                            run_time=0.005,
                        )

        # Highlight the shortest path to a random node
        end_vertex = "299"
        current_vertex = end_vertex
        animations = []
        path_nodes = set()
        path_edges = set()
        while previous_vertices[current_vertex] is not None:
            start = previous_vertices[current_vertex]
            edge, weight_label = edge_objects[(start, current_vertex)]
            animations.append(edge.animate.set_color(PURE_GREEN).set_stroke(width=6))
            path_edges.add(edge)
            current_vertex = start

        self.play(*animations, run_time=3)

        # Fade out all other elements except the shortest path
        path_elements = [
            obj for obj in self.mobjects if isinstance(obj, Line) and obj in path_edges
        ]
        other_elements = [obj for obj in self.mobjects if obj not in path_elements]
        self.play(FadeOut(*other_elements, run_time=3))

        self.wait(3)
