from manim import *
import numpy as np 

class Quadrants(Scene):
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
        
        quad1_label = MathTex(r'(+, +)').shift(UR*1.5)
        quad2_label = MathTex(r'(-, +)').shift(UL*1.5)
        quad3_label = MathTex(r'(-, -)').shift(DL*1.5)
        quad4_label = MathTex(r'(+, -)').shift(DR*1.5)

        labels = VGroup(quad1_label, quad2_label, quad3_label, quad4_label)

        polarplane_pi.remove()
        self.add(polarplane_pi, labels)