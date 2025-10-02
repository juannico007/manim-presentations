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
        # Slide 1
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
        highlight = SurroundingRectangle(col, color=RED, buff=0.1)
        highlight.set_fill(RED, opacity=0.3)
        self.play(Create(highlight))
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