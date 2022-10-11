from manim import *

class PolarPlaneExample(Scene):
    def construct(self):
        polarplane_pi = PolarPlane(
            azimuth_units="degrees",
            size=6,
            azimuth_label_font_size=0.1,
            azimuth_step=12,
            azimuth_direction="CCW",
            radius_config={"font_size":0.1,
                            "stroke_opacity":0.5},
            background_line_style={"stroke_opacity":0.3},
        ).add_coordinates()
        polarplane_pi.remove()
        self.add(polarplane_pi)
        point1 =  Dot(polarplane_pi.polar_to_point(3, PI/4), color=BLUE)
        point2, =  Dot(polarplane_pi.polar_to_point(2, 2*PI/3), color=BLUE)
        point3 =  Dot(polarplane_pi.polar_to_point(2.5, 7*PI/6), color=RED)
        point4 =  Dot(polarplane_pi.polar_to_point(3.5, 11*PI/6), color=BLUE)
        legend = MathTex(r'p=(r,\theta)').next_to(polarplane_pi, UR).shift(DR)
        point1_label = MathTex(r'(3, 45^\circ{})').next_to(point1, UR)
        point2_label = MathTex(r'(2, 480^\circ{})').next_to(point2, UL)
        point3_label = MathTex(r'(2.5, -150^\circ{})').next_to(point3, DL)
        point4_label = MathTex(r'(3.5, 330^\circ{})').next_to(point4, DR)

        points = VGroup(point1, point2, point3, point4)
        labels = VGroup(legend, point1_label, point2_label, point3_label, point4_label)

        ax = Axes()
        # line = ax.get_vertical_line(polarplane_pi.polar_to_point(3, PI/4))
        self.add(points,  labels)