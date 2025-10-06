from manim import *
from manim_slides import Slide

class MinimalPresentation(Slide):
    def add_common_ancestor(self, graph, labels,  node1, node2, new_label):
        new_vertex = len(graph.vertices)
        pos1 = graph[node1].get_center()
        pos2 = graph[node2].get_center()
        midpoint_x = (pos1[0] + pos2[0]) / 2
        new_pos = [midpoint_x, max(pos1[1], pos2[1]) + 0.75, 0]
        self.play(graph.animate.add_vertices(new_vertex, positions={new_vertex: new_pos}))
        label = Text('S' + str(new_vertex+1) + ',' + new_label).scale(0.5)
        label.next_to(graph[new_vertex], LEFT, buff=0.1)  # position relative to vertex
        labels.add(label)
        self.play(FadeIn(label))
        self.play(graph.animate.add_edges((node1, new_vertex), (node2, new_vertex)))

    def construct(self):
        #Slide 1
        title = Text("Maximum likelihood in phylogeny")
        self.play(Create(title))
        self.next_slide()  # pause until user advances

        # Slide 2
        self.play(FadeOut(title))
        title = Text("We have 4 species").to_edge(UP)
        self.play(Create(title))
        self.next_slide()
        


        species_1 = 'AGCCTAG'
        species_2 = 'ATACTGG'
        species_3 = 'GGCTTCG'
        species_4 = 'AACTCAG'


        species_data = [
            list(species_1),
            list(species_2),
            list(species_3),
            list(species_4)
        ]
        species_table = Table(species_data, 
                              row_labels = [Text('S1'), Text('S2'), Text('S3'), Text('S4')],
                              col_labels = [Text(str(i)) for i in range(1, len(species_1) + 1)],
                              include_outer_lines=False,  # no border
                            )
        species_table.scale(0.5)

        # Remove inner lines (make them invisible)
        for line in species_table.get_horizontal_lines() + species_table.get_vertical_lines():
            line.set_stroke(width=0)
        
    
        # Add the table to the scene
        self.add(species_table)
        self.play(FadeIn(species_table))
        self.next_slide()

        self.play(species_table.animate.to_edge(UP, buff=1.5)
                  )
        # Get the second column (index 2 because Manim counts from 1)
        col = species_table.get_columns()[2]

        # Highlight it with a background rectangle
        highlight = SurroundingRectangle(col, color=YELLOW, buff=0.1)
        highlight.set_fill(YELLOW, opacity=0.2)

        self.play(Create(highlight))
        self.next_slide()

        vertices = [i for i in range(4)]
        edges = []
        graph1_site2 = Graph(vertices, edges)
        graph1_site2[0].move_to([0, 0, 0])
        graph1_site2[1].move_to([3, 0, 0])
        graph1_site2[2].move_to([1, 0, 0])
        graph1_site2[3].move_to([2, 0, 0])

            
        graph1_site2.to_corner(DL, buff=0.5)

        labels = VGroup()
        for v in vertices:
            label = Text('S' + str(v+1)+","+str(species_data[v][1])).scale(0.5)
            label.next_to(graph1_site2[v], DOWN, buff=0.1)  # position relative to vertex
            labels.add(label)
        graph1 = VGroup(graph1_site2, labels)

        self.play(Create(graph1_site2))
        self.play(FadeIn(labels))
        self.next_slide()

        self.add_common_ancestor(graph1_site2, labels,  0, 2, "G")
        self.next_slide()

        self.add_common_ancestor(graph1_site2, labels,  3, 4, "A")
        self.next_slide()

        self.add_common_ancestor(graph1_site2, labels,  1, 5, "T")
        self.next_slide()

        highlight_graph1 = SurroundingRectangle(graph1, color=YELLOW, buff=0.1)
        highlight_graph1.set_fill(YELLOW, opacity=0.2)

        self.play(Create(highlight_graph1))
        self.next_slide()
        
        vertices2 = [i for i in range(4)]
        edges = []
        graph2_site2 = Graph(vertices2, edges)
        graph2_site2[0].move_to([-1.5, 0, 0])
        graph2_site2[1].move_to([1.5, 0, 0])
        graph2_site2[2].move_to([-0.5, 0, 0])
        graph2_site2[3].move_to([0.5, 0, 0])

        graph2_site2.to_edge(DOWN, buff=0.5)

        labels2 = VGroup()
        for v in vertices2:
            label = Text('S' + str(v+1)+","+str(species_data[v][1])).scale(0.5)
            label.next_to(graph2_site2[v], DOWN, buff=0.1)  # position relative to vertex
            labels2.add(label)
        graph2 = VGroup(graph2_site2, labels2)

        self.play(Create(graph2_site2))
        self.play(FadeIn(labels2))
        self.next_slide()

        self.add_common_ancestor(graph2_site2, labels2,  0, 2, "G")
        self.next_slide()

        self.add_common_ancestor(graph2_site2, labels2,  3, 1, "A")
        self.next_slide()

        self.add_common_ancestor(graph2_site2, labels2,  4, 5, "A")
        self.next_slide()

        highlight_graph2 = SurroundingRectangle(graph2, color=YELLOW, buff=0.1)
        highlight_graph2.set_fill(YELLOW, opacity=0.2)

        self.play(Create(highlight_graph2))
        self.next_slide()

        # Get the second column (index 6 because Manim counts from 1)
        col = species_table.get_columns()[6]
        # Highlight it with a background rectangle
        highlight_r = SurroundingRectangle(col, color=RED, buff=0.1)
        highlight_r.set_fill(RED, opacity=0.3)
        self.play(Create(highlight_r))
        self.next_slide()

        vertices3 = [i for i in range(4)]
        edges = []
        graph1_site6 = Graph(vertices3, edges)
        graph1_site6[0].move_to([0, 0, 0])
        graph1_site6[1].move_to([3, 0, 0])
        graph1_site6[2].move_to([2, 0, 0])
        graph1_site6[3].move_to([1, 0, 0])

            
        graph1_site6.to_corner(DR, buff=0.5)

        labels3 = VGroup()
        for v in vertices:
            label = Text('S' + str(v+1)+","+str(species_data[v][5])).scale(0.5)
            label.next_to(graph1_site6[v], DOWN, buff=0.1)  # position relative to vertex
            labels3.add(label)
        graph3 = VGroup(graph1_site6, labels3)

        self.play(Create(graph1_site6))
        self.play(FadeIn(labels3))
        self.next_slide()

        self.add_common_ancestor(graph1_site6, labels3,  0, 3, "A")
        self.next_slide()

        self.add_common_ancestor(graph1_site6, labels3,  2, 4, "C")
        self.next_slide()

        self.add_common_ancestor(graph1_site6, labels3,  1, 5, "G")
        self.next_slide()

        highlight_graph3 = SurroundingRectangle(graph3, color=RED, buff=0.1)
        highlight_graph3.set_fill(RED, opacity=0.2)

        self.play(Create(highlight_graph3))
        self.next_slide()

        #Slide 3
        self.play(FadeOut(VGroup(title, species_table, highlight, graph1, highlight_graph1, graph2, highlight_graph2, graph3, highlight_graph3, highlight_r)))
        title = Text("ML rescues us!").to_edge(UP)
        self.play(Create(title))
        self.next_slide()
        textv = [
            "1) We have to select a model for our data",
            "2) Start looking at different trees and calculating its likelihood",
            "3) Do a search",
            "4) Pick the one with highest ML",
        ]

        text = VGroup(*[Text(s) for s in textv])
        # Add the text to the scene
        self.add(text)
        self.next_slide()
        text.arrange(DOWN, center=False, aligned_edge=LEFT)
        text.move_to(0).to_edge(UP, buff=1)
        text.scale(0.7)
        text.arrange(DOWN, center=False, aligned_edge = LEFT, buff=0.5)
        self.play(Write(text), run_time=3)
        self.next_slide()
        self.play(FadeOut(text))

        species_1 = 'AGCCTAG'
        species_2 = 'ATACTGG'
        species_3 = 'GGCTTCG'
        species_4 = 'AACTCAG'


        species_data = [
            list(species_1),
            list(species_2),
            list(species_3),
            list(species_4)
        ]
        species_table = Table(species_data, 
                              row_labels = [Text('S1'), Text('S2'), Text('S3'), Text('S4')],
                              col_labels = [Text(str(i)) for i in range(1, len(species_1) + 1)],
                              include_outer_lines=False,  # no border
                            )
        species_table.scale(0.5)

        # Remove inner lines (make them invisible)
        for line in species_table.get_horizontal_lines() + species_table.get_vertical_lines():
            line.set_stroke(width=0)
        
    
        # Add the table to the scene
        self.add(species_table)
        self.play(FadeIn(species_table))
        self.next_slide()

        self.play(species_table.animate.to_corner(UP, buff=1.5)
                  )
        self.play(FadeOut(species_table))

        #Tree

        node_positions = [[3, -1, 0], [4, -1, 0], [5, -1, 0], [6, -1, 0]]
        node_indices = [[[0, 1]], [[4, 2]], [[3, 5]]]
        edge_indices = [[0, 4], [1, 4], [2, 5], [4, 5], [5, 6], [3, 6]]
        labels = ["S1", "S2", "S3", "S4", "P1", "P2", "Root"]
        edge_labels = ["A→A", "A→A", "G→G", "A→G", "G→A", "A→A"]
        m = self.draw_custom_tree(node_positions, node_indices, edge_indices, labels, edge_labels)
        self.next_slide()

        # Equations

        subtitle = Text("Likelihood")
        subtitle.scale(0.7)
        eq = MathTex(r"L(1) = P(A \rightarrow A) * P(A \rightarrow A) * P(A \rightarrow G) * P(G \rightarrow G) * P(G \rightarrow A) * P(A \rightarrow A)").scale(0.7)
        # self.add(eq)
        self.play(Write(subtitle.to_edge(DOWN, buff=2)))
        self.play(Write(eq.to_edge(DOWN, buff=1)))

        # Remove components
        self.next_slide()
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )



        #Slide 4
        title = Text("Questions").to_edge(UP)
        self.play(Create(title))
        self.next_slide()


        #Utils
    def draw_custom_tree(self, node_positions, node_indices, edge_indices, labels=None, edge_labels=None):
            all_labels = []
            all_edge_labels = []
            base_range = abs(node_positions[0][0] - node_positions[-1][0]) / len(node_indices)
            nodes = self.create_nodes(node_positions)
            for n in nodes:
                self.add(n)
            print(len(nodes))
            for h, layer in enumerate(node_indices):
                for i in layer:
                    node = self.create_nodes([[(node_positions[i[0]][0] + node_positions[i[1]][0]) / 2, (1 + h) * base_range + node_positions[0][1], 0]])
                    nodes += node
                    node_positions += ([nodes[-1].get_center().tolist()])
                    self.add(node[0])
            
            if labels and len(labels) >= len(nodes):
                for i, node in enumerate(nodes):
                    label = Text(labels[i], font_size=20, color=BLACK)
                    label.move_to(node.get_center())
                    all_labels.append(label)
                    self.add(label)
            
            for i, edge in enumerate(edge_indices):
                line = self.create_edge(node_positions[edge[0]], node_positions[edge[1]])
                self.add(line)
                
                if edge_labels and i < len(edge_labels):
                    start_pos = node_positions[edge[0]]
                    end_pos = node_positions[edge[1]]
                    mid_x = (start_pos[0] + end_pos[0]) / 2
                    mid_y = (start_pos[1] + end_pos[1]) / 2
                    mid_z = (start_pos[2] + end_pos[2]) / 2
                    
                    edge_label = Text(edge_labels[i], font_size=20, color=BLACK, weight=BOLD)
                    edge_label.move_to([mid_x, mid_y, mid_z])
                    
                    background = Rectangle(
                        width=edge_label.width + 0.2,
                        height=edge_label.height + 0.1,
                        fill_color=YELLOW,
                        fill_opacity=0.8,
                        stroke_color=BLACK,
                        stroke_width=2
                    )
                    background.move_to([mid_x, mid_y, mid_z])
                    
                    self.add(background)
                    self.add(edge_label)
                    all_edge_labels.append(VGroup(background, edge_label))      
            return VGroup(*nodes, *all_labels, *all_edge_labels)

    def create_nodes(self, node_positions):
        """Create nodes at specified positions."""
        nodes = []
        for position in node_positions:
            # Create a circle for the node
            node_circle = Circle(
                radius=0.35,
                fill_color=WHITE,
                fill_opacity=1,
                color=LIGHT_GREY,
                stroke_width=3.5
            )
            node_circle.move_to(position)
            nodes.append(node_circle)
        return nodes
    def create_edge(self, a, b):
        return Line(start=a, end=b, stroke_color=WHITE, stroke_width=8).set_z_index(-0.5)
