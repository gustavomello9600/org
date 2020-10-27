from manimlib.imports import *

class Apótema(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=45*DEGREES, theta=-80*DEGREES)
        self.begin_ambient_camera_rotation()
        
        plane = Rectangle(color=None, height=6, width=8, fill_color=BLUE, fill_opacity=0.15)
        self.add(plane)
        
        hexagon = RegularPolygon(n=6, color=WHITE, stroke_width=1).scale(2)

        self.play(ShowCreation(hexagon), run_time=3)

        axis = DashedLine(2.5*DOWN, 2.5*UP)
        self.play(Write(axis), run_time=2)

        ponto_médio = (3**(1/2))*DOWN

        isosceles_1 = Polygon(ORIGIN, ponto_médio, ponto_médio + RIGHT, color=YELLOW, fill_color=YELLOW, fill_opacity=0.5)
        isosceles_2 = Polygon(ORIGIN, ponto_médio, ponto_médio + LEFT, color=YELLOW, fill_color=YELLOW, fill_opacity=0.5)

        self.play(DrawBorderThenFill(isosceles_1),
                  DrawBorderThenFill(isosceles_2),
                  run_time=2)

        self.wait()
        self.play(Rotate(isosceles_1, angle=PI, axis=UP, about_edge=LEFT), run_time=2)

        self.wait()
        self.play(Rotate(isosceles_1, angle=-PI, axis=UP, about_edge=RIGHT), run_time=2)
        
        radius = Line(ORIGIN, ponto_médio, color=RED, stroke_width=4)
        medida = Brace(radius, LEFT)
        nome = medida.get_tex("r")

        VGroup(medida, nome).add_updater(lambda self: self.next_to(radius, LEFT))
        self.play(Write(radius), Write(medida), Write(nome), run_time=2)

        self.wait(3)

        self.play(Rotate(radius, angle=TAU, about_point=ORIGIN), ShowCreation(Circle(radius=(3**(1/2))).rotate_about_origin(-TAU/4)), run_time=4)

        self.wait(10)

        
