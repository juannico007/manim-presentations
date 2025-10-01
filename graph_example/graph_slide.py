from manim import *

config.background_color = BLACK





def create_edge(a, b):
    return Line(start=a, end=b, stroke_color=PURE_RED, stroke_width=12).set_z_index(-0.5)



class GraphAnimation(MovingCameraScene):

    def construct(self):

        # Create the nodes
        node_positions = [[-5, -3, 0], [0, -3, 0], [5, -3, 0]]
        nodes = self.create_nodes(node_positions)
        self.wait(2)
        self.play(*[GrowFromCenter(node) for node in nodes])
        self.wait(2)
        lines = self.create_edges(node_positions)
        for l in lines:
            self.add(l)
        self.add(create_edge([2.5, 1, 0], [0, 1, 0]))
        self.add(create_edge([5, 1, 0], [2.5, 1, 0],))
        anchestral_node = [[2.5, 1, 0]]
        a_node = self.create_nodes(anchestral_node)
        self.play(*[GrowFromCenter(a_node[0])])
        self.wait(2)

    def create_edges(self,node_pos):
        lines = []
        for node in node_pos:
            line_length = [0, 4, 0]
            lines.append(create_edge(node, [a+b for a, b in zip(node, line_length)]))
        return lines
    def create_nodes(self, node_positions):
        """Create nodes at specified positions."""
        nodes = []
        for position in node_positions:
            # Create a circle for the node
            node_circle = Circle(
                radius=0.5,
                fill_color=TEAL_B,
                fill_opacity=1,
                color=DARK_BLUE,
                stroke_width=5.6
            )
            node_circle.move_to(position)
            nodes.append(node_circle)
        return nodes

'''
        # Create the edges
        edges, edge_list = self.create_edges(node_positions)

        # Store the original edges for later transformation back
        original_edges = [edge.copy() for edge in edge_list]

        # Add nodes and edges to the scene
        self.play(*[GrowFromCenter(node) for node in nodes.values()])
        self.play(*[GrowFromCenter(edge) for edge in edge_list])

        self.wait(2)

        self.play(self.camera.frame.animate.scale(1.2).shift(RIGHT * 1.43).shift(DOWN * 0.66))

        stack = Stack().next_to(nodes["D"], RIGHT).shift(RIGHT * 0.8)
        stack.push(self, "A")
        self.play(FadeOut(stack[0]))
        set1 = AnimatedSet().next_to(stack, DOWN).shift(DOWN * 0.7).shift(LEFT * 2.7)

        self.play(Create(stack))
        self.play(Create(set1))

        self.wait(2)

        a = stack.pop(self)
        self.wait(2)
        set1.push("A", self)


        self.play(nodes["A"][1].copy().animate.next_to(nodes["F"], DOWN).shift(LEFT * 1.6).shift(DOWN * 0.45))
        self.play(nodes["A"][0].animate.set_fill(PURPLE))

        self.wait(2)

        self.play(FadeOut(a, ))

        self.wait(2)

        self.play(Indicate(nodes["B"], color=PURE_GREEN), Indicate(nodes["C"], color=PURE_GREEN))
        self.wait(2)

        stack.push(self, "C")
        stack.push(self, "B")

        self.wait(2)

        b = stack.pop(self)
        self.wait(2)
        set1.push("B", self)


        self.play(nodes["B"][1].copy().animate.next_to(nodes["F"], DOWN).shift(LEFT * 0.6).shift(DOWN * 0.45))
        self.play(nodes["B"][0].animate.set_fill(PURPLE))


        self.wait(2)

        self.play(FadeOut(b, ))

        self.wait(2)

        self.play(Indicate(nodes["A"], color=PURE_GREEN), Indicate(nodes["G"], color=PURE_GREEN))
        stack.push(self, "G")

        self.wait(2)

        g = stack.pop(self)

        set1.push("G", self)



        self.play(nodes["G"][1].copy().animate.next_to(nodes["F"], DOWN).shift(RIGHT * 0.4).shift(DOWN * 0.45))
        self.play(nodes["G"][0].animate.set_fill(PURPLE))

        self.play(FadeOut(g, ))

        self.wait(2)

        self.play(Indicate(nodes["C"], color=PURE_GREEN), Indicate(nodes["F"], color=PURE_GREEN),
                  Indicate(nodes["B"], color=PURE_GREEN))

        stack.push(self, "C")
        stack.push(self, "F")

        self.wait(2)

        f = stack.pop(self)

        set1.push("F", self)



        self.play(nodes["F"][1].copy().animate.next_to(nodes["F"], DOWN).shift(RIGHT * 1.4).shift(DOWN * 0.45))
        self.play(nodes["F"][0].animate.set_fill(PURPLE))

        self.play(FadeOut(f, ))

        self.wait(2)

        self.play(Indicate(nodes["C"], color=PURE_GREEN), Indicate(nodes["E"], color=PURE_GREEN),
                  Indicate(nodes["G"], color=PURE_GREEN))

        self.wait(1)

        stack.push(self, "E")
        stack.push(self, "C")

        self.wait(1)

        c = stack.pop(self)

        set1.push("C", self)



        self.play(nodes["C"][1].copy().animate.next_to(nodes["F"], DOWN).shift(RIGHT * 2.4).shift(DOWN * 0.45))
        self.play(nodes["C"][0].animate.set_fill(PURPLE))

        self.play(FadeOut(c, ))

        self.wait(2)

        self.play(Indicate(nodes["A"], color=PURE_GREEN), Indicate(nodes["G"], color=PURE_GREEN),
                  Indicate(nodes["F"], color=PURE_GREEN))

        self.wait(2)

        e = stack.pop(self)

        set1.push("E", self)

        self.play(nodes["E"][1].copy().animate.next_to(nodes["F"], DOWN).shift(RIGHT * 3.4).shift(DOWN * 0.45))
        self.play(nodes["E"][0].animate.set_fill(PURPLE))

        self.play(FadeOut(e, ))

        self.wait(2)

        self.play(Indicate(nodes["D"], color=PURE_GREEN),
                  Indicate(nodes["F"], color=PURE_GREEN))

        self.wait()

        stack.push(self, "D")

        self.wait(2)

        d = stack.pop(self)

        set1.push("D", self)

        self.play(nodes["D"][1].copy().animate.next_to(nodes["F"], DOWN).shift(RIGHT * 4.4).shift(DOWN * 0.45))
        self.play(nodes["D"][0].animate.set_fill(PURPLE))

        self.play(FadeOut(d))

        self.wait(2)

        c = stack.pop(self)
        self.play(FadeOut(c))
        c = stack.pop(self)
        self.play(FadeOut(c))

        self.wait(2)
'''