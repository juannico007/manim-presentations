from manim import *
from manim_slides import Slide

class MinimalPresentation(Slide):
    def construct(self):
        # Slide 1
        title = Text("Maximum likelihood in phylogeny")
        self.play(Create(title))
        self.next_slide()  # pause until user advances

        # Slide 2
        self.play(FadeOut(title))
        title = Text("We want to make a phylogenetic tree for 4 species").to_edge(UP)
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
        self.play(Create(species_table))
        self.next_slide()

        

        # vertices = [i for i in range(11)]
        # edges = []
        # g = Graph(vertices, edges)
        # for i in range(11):
        #     g[i].move_to([-5+i, 0, 0])
        # self.play(Create(g))
        # self.next_slide()

        # # Slide 3
        # self.play(g[2].animate.set_color(YELLOW),
        #           g[5].animate.set_color(YELLOW))
        # self.next_slide()

        # # Slide 4
        # new_vertices = [i for i in range(11, 22)]
        # layout_dict = {
        #     i : [-5+(i-11), 0.25, 0] for i in range(11,22)
        # }
        # new_edges = [(12, 0), (12, 1), (13, 2), (13, 3), (15, 4), (16, 5), (16, 6), (18, 7), (20, 8), (20, 9), (20, 10)]
        # self.play(g.animate.shift(0.25*DOWN))
        # self.play(g.animate.add_vertices(*new_vertices, positions=layout_dict),)
        # self.play(g.animate.add_edges(*new_edges))
        # self.next_slide()

        # # Slide 5
        # self.play(g[13].animate.set_color(YELLOW),
        #           g[16].animate.set_color(YELLOW),
        #           g.edges[(13, 2)].animate.set_color(YELLOW),
        #           g.edges[(16, 5)].animate.set_color(YELLOW))
        # self.next_slide()

        # # Slide 6
        # new_vertices = [i for i in range(22, 33)]
        # layout_dict = {
        #     i : [-5+(i-22), 0.5, 0] for i in range(22,33)
        # }
        # new_edges = [(23, 11), (23, 12), (25, 13), (26, 14), (26, 15), (26, 16), (28, 17), (29, 18), (29, 19), (31, 20), (31, 21)]
        # self.play(g.animate.shift(0.25*DOWN))
        # self.play(g.animate.add_vertices(*new_vertices, positions=layout_dict))
        # self.play(g.animate.add_edges(*new_edges))
        # self.next_slide()

        # # Slide 7
        # self.play(g[25].animate.set_color(YELLOW),
        #           g[26].animate.set_color(YELLOW),
        #           g.edges[(25, 13)].animate.set_color(YELLOW),
        #           g.edges[(26, 16)].animate.set_color(YELLOW))
        # self.next_slide()
        
        # # Slide 6
        # new_vertices = [i for i in range(33, 44)]
        # layout_dict = {
        #     i : [-5+(i-33), 0.75, 0] for i in range(33,44)
        # }
        # new_edges = [(33, 22), (33, 23), (35, 24), (37, 25), (37, 26), (39, 27), (39, 28), (40, 29), (41, 30), (43, 31), (43, 32)]
        # self.play(g.animate.shift(0.25*DOWN))
        # self.play(g.animate.add_vertices(*new_vertices, positions=layout_dict))
        # self.play(g.animate.add_edges(*new_edges))
        # self.next_slide()

        # # Slide 7
        # self.play(g[37].animate.set_color(YELLOW),
        #           g.edges[(37, 25)].animate.set_color(YELLOW),
        #           g.edges[(37, 26)].animate.set_color(YELLOW))
        # self.next_slide()

        # self.play(
        #     g.animate.shift(UP * 1.5)  # buff = padding from edge
        # )
        # self.next_slide()
        # Slide 4 (end)
        #thanks = Text("Thanks for watching!").scale(0.8)
        #self.play(FadeOut(g), FadeIn(thanks))
        #self.next_slide()