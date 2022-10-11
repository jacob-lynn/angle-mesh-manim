from manim import *
import numpy as np

class Reappear(Scene):
    def construct(self): 
        angle = 140  
        rotation_center = LEFT
        
        theta_tracker = ValueTracker(110)
        num_of_tris = ValueTracker(3)
        
        line1 = Line(LEFT, RIGHT)
        line_moving = Line(LEFT, RIGHT)
        line_ref = line_moving.copy()
        circle = Circle(radius=line1.get_length()).move_to(line1.get_start())
        line_moving.rotate(
            theta_tracker.get_value() * DEGREES, about_point=rotation_center
        )

        hack_squares = VGroup((Square(side_length=0.2, fill_color=BLACK, stroke_color=BLACK, fill_opacity=1).move_to(circle.get_center()).shift(DL*SMALL_BUFF).rotate(45)))
                                    
                                    

        arc = Angle(line1, line_moving, radius=line1.get_length())

        line_moving.add_updater(
            lambda x: x.become(line_ref.copy()).rotate(
                theta_tracker.get_value() * DEGREES, about_point=rotation_center
            )
        )
        
        def get_arc():
            if (theta_tracker.get_value() > 0):
                return arc.become((Angle(line1, line_moving, radius=line1.get_length(), other_angle=False)))
            else:
                return arc.become(Angle(line1, line_moving, radius=line1.get_length(), other_angle=True))

        def get_dots_and_tris():
            array_of_points = np.zeros([int(num_of_tris.get_value())+2, 3])           
            array_of_points[0,:] = circle.get_center()
            tri_count = 0
            while tri_count <= int(num_of_tris.get_value()):
                array_of_points[(tri_count + 1), :] = arc.point_from_proportion((tri_count * 1/int(num_of_tris.get_value())))
                tri_count += 1   
            
            
            tris = get_tris(array_of_points) # call helper function
            
            dots_and_tris = VGroup(tris)
            
            return dots_and_tris  

        def get_tris(array_of_points):
                array_of_tris = np.zeros([int(num_of_tris.get_value()), 3,3])       
                array_of_tris[:,0,:] = array_of_points[0,:]
                for t in range(int(num_of_tris.get_value())):
                    array_of_tris[t,1,:] = array_of_points[t+1,:] 
                    array_of_tris[t,2,:] = array_of_points[t+2,:]       
                    
                tris = VGroup(*[Polygon(*[t[0,:],t[2,:],t[1,:]]).set_fill(BLUE, opacity=0.2)
                                for t in array_of_tris])

                return tris
              

        dots_and_tris = always_redraw(get_dots_and_tris)
        arc = always_redraw(get_arc)
        self.add(dots_and_tris, hack_squares, line1, line_moving, arc)    
        self.play(theta_tracker.animate.set_value(40))
        self.play(theta_tracker.animate.increment_value(90))
        self.wait()
        self.play(theta_tracker.animate.set_value(-100))