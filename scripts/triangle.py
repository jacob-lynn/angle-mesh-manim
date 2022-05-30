
from manim import *
from manim.mobject.geometry.tips import ArrowTriangleTip
import numpy as np

class Triangle(Scene):  
    def construct(self):
                
        vertices = np.zeros([3,3])
        vertices[0,:] = LEFT
        vertices[1,:] = UP+0.5*RIGHT
        vertices[2,:] = RIGHT
        dots = VGroup(*[Dot(i)
                        for i in vertices])
        dots2 = dots.copy()

        tri = (Polygon(vertices[0,:],vertices[1,:],vertices[2,:]).set_fill(BLUE, opacity=0.5)).shift(2*LEFT)
        tri2 = (Polygon(vertices[0,:],vertices[2,:],vertices[1,:])).shift(2*RIGHT)
        
        circle_a = Circle(radius=0.5).move_to(LEFT)
        circle_b = Circle(radius=0.5).move_to(RIGHT*3)
        
        text_a = Text('A',font_size=30).move_to(LEFT*2).shift(UP*2)
        text_b = Text('B',font_size=30).move_to(RIGHT*2).shift(UP*2)
        
        indices_a = Text('[0,2,1]',font_size=30).next_to(tri,DOWN*2)
        indices_b = Text('[0,1,2]',font_size=30).next_to(tri2,DOWN*2)
        
        curve_a = CurvedArrow(circle_a.point_at_angle(70*DEGREES),circle_a.point_at_angle(90*DEGREES), tip_shape=ArrowTriangleTip, angle=-340*DEGREES).move_to(text_a).scale(0.3)
        curve_b = CurvedArrow(circle_b.point_at_angle(110*DEGREES),circle_b.point_at_angle(90*DEGREES), tip_shape=ArrowTriangleTip, angle=340*DEGREES).move_to(text_b).scale(0.3)
        
        

        labels = VGroup(Text('0',font_size=20).next_to(dots[0], SMALL_BUFF*DL),
                        Text('2',font_size=20).next_to(dots[1], SMALL_BUFF*UR),
                        Text('1',font_size=20).next_to(dots[2], SMALL_BUFF*DR))
        labels2 = labels.copy()
        
        self.add(text_a,text_b,curve_a,curve_b)
              

        self.add(labels.shift(2*LEFT),labels2.shift(2*RIGHT))
        self.add_foreground_mobjects(dots.shift(2*LEFT),dots2.shift(2*RIGHT))
        self.play(LaggedStart(DrawBorderThenFill(tri),FadeIn(indices_a),lag_ratio=1))
        self.play(LaggedStart(DrawBorderThenFill(tri2),FadeIn(indices_b),lag_ratio=1))   
        self.wait(2)

t = Triangle()
t.render()
