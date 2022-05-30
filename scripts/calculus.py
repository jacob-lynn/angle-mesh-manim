from manim import *
import numpy as np

class Calculus(Scene):
    def construct(self):    
          
            angle = 140  
               
            num_of_tris = ValueTracker(1)
            
            line1 = Line(LEFT, RIGHT*2)
            line2 = Line(LEFT, line1.get_end())           
            circle = Circle(radius=line1.get_length()).move_to(line1.get_start())       
            line2.rotate(
                angle * DEGREES, about_point=circle.get_center()
            )

            a = Angle(line1, line2, radius=0.5, other_angle=False)            
            arc = ArcBetweenPoints(line1.get_end(), line2.get_end(), radius=circle.radius)   
            
            #this is to cover a weird artifact 
            hack_squares = VGroup(Square(side_length=0.2, fill_color=BLACK, stroke_color=BLACK, fill_opacity=1).move_to(circle.get_center()).shift(DOWN*1.43*SMALL_BUFF),     
                                    (Square(side_length=0.2, fill_color=BLACK, stroke_color=BLACK, fill_opacity=1).move_to(circle.get_center()).shift(DL*SMALL_BUFF).rotate(45)),
                                    (Square(side_length=0.2, fill_color=BLACK, stroke_color=BLACK, fill_opacity=1).move_to(line1.get_end()).shift(RIGHT*1.46*SMALL_BUFF)),
                                    (Square(side_length=0.2, fill_color=BLACK, stroke_color=BLACK, fill_opacity=1).move_to(line2.get_end()).shift(UL*SMALL_BUFF).rotate(45)))
            
            circle.shift(LEFT*3)
            hack_squares.shift(LEFT*3)
            circle_vgroup = VGroup(line1, line2, a, arc).shift(LEFT*3)
            
            ax = Axes(
                x_range=[-1,10],
                y_range=[-1,10],
                tips=False,                
            ).next_to(circle.get_center()).shift(UP*1.2).shift(RIGHT).scale(0.5)
            
                       
            curve = ax.plot(lambda x: 0.1 * (x + 3-5) * (x - 3-5) * (x-5) + 5, 
                            x_range=[1,9],
                            color=WHITE)          
            
           
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
            
            def get_rects():
                riemann_area = ax.get_riemann_rectangles(curve, 
                                                        x_range=[2,8],
                                                        dx=6/int(num_of_tris.get_value()),
                                                        color=BLUE,
                                                        stroke_color=BLUE_C,
                                                        stroke_width=DEFAULT_STROKE_WIDTH,
                                                        fill_opacity=0.2)
                return riemann_area
            

            dots_and_tris = always_redraw(get_dots_and_tris)
            riemann_area = always_redraw(get_rects)
            

            self.add(circle_vgroup)
            self.add_foreground_mobjects(dots_and_tris)    
            self.add_foreground_mobjects(hack_squares)
            self.add(ax, curve, riemann_area)
            self.play(num_of_tris.animate.set_value(30.1), rate_func=rush_into, run_time=3)        
            self.wait(2)
            
x = Calculus()
x.render()
            
            
            
            
            
                   
            
        
        
