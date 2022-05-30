from manim import *
import numpy as np 


class PolarScene(Scene):
    def construct(self):
        
        r = Line(ORIGIN, RIGHT*3)
        x = r.copy()
                
        r.rotate_about_origin(140*DEGREES)
        
        dot = Dot(r.get_end())
        
        a = Angle(x,r, radius=0.5)
        angle = Angle(x,r,radius=r.get_length())
        
        q1 = angle.points        
        q2 = r.reverse_points().points
        q3 = x.points
        points = np.concatenate([q1,q2, q3])
        mfill = VMobject()
        mfill.set_points(points).set_fill(BLUE,opacity=0.5)
        
        self.add(mfill)
        self.add(r,x,a,dot,angle) 
        
        
        self.play(Indicate(mfill, scale_factor=0.9), run_time=3)
        
        self.wait()
        
x = PolarScene()
x.render