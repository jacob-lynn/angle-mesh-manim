
from manim import *
import numpy as np

class MovingAngleSeries(Scene):
    def construct(self):
        
        angle = 140  
        theta_tracker = ValueTracker(0.1)        
        
        plane = NumberPlane(x_range=[-50,50],
                            y_range=[-50,50]).shift(LEFT)
        
        def angle_factory(num_of_tris, center=[0,0,0]):
            
            sub_angle = angle / num_of_tris
                 
            line1 = Line(center, (center+RIGHT*3))
            line_moving = Line(center, line1.get_end())
            line_ref = line_moving.copy()
            line_moving.rotate(
                theta_tracker.get_value() * DEGREES, about_point=center
            )

            a = Angle(line1, line_moving, radius=0.5, other_angle=False)
            circle = Circle(radius=line1.get_length()).move_to(center)     
            edge = ArcBetweenPoints(line1.get_end(), line_moving.get_end(), radius=circle.radius)
            
            tri_count = 0
            array_of_points = np.zeros([num_of_tris+2, 3])
            array_of_points[0,:] = circle.get_center()
            
            while tri_count <= num_of_tris:
                array_of_points[(tri_count + 1), :] = circle.point_at_angle((tri_count * sub_angle)*DEGREES)
                tri_count += 1   
            
            array_of_tris = np.zeros([num_of_tris, 3,3])       
            array_of_tris[:,0,:] = circle.get_center()
            for t in range(num_of_tris):
                array_of_tris[t,1,:] = array_of_points[t+1,:] 
                array_of_tris[t,2,:] = array_of_points[t+2,:]                               

            
            line_moving.add_updater(
                lambda x: x.become(line_ref.copy()).rotate(
                    theta_tracker.get_value() * DEGREES, about_point=center
                )
            )     
            
            origin = Dot(array_of_points[0])
            first_point = Dot(array_of_points[1])
            array_of_points = np.delete(array_of_points, [0,1], 0)
             

            dots = VGroup(*[Dot(i)
                        for i in array_of_points])

            tris = VGroup(*[Polygon(t[0,:],t[2,:],t[1,:]).set_fill(BLUE, opacity=0.2)
                        for t in array_of_tris])
            
            label = Text(str(num_of_tris)).next_to(center, UP*15)
            
            dots_and_tris_anim = [] 
            for t,d in zip(tris,dots):  
                dots_and_tris_anim.append(AnimationGroup(DrawBorderThenFill(t,run_time=1,rate_func=rush_into),
                                                                        FadeIn(d, run_time=1.01)))
                
            a.add_updater(
                lambda x: x.become(Angle(line1, line_moving, radius=0.5, other_angle=False))
            )        

            edge.add_updater(
                lambda x: x.become(Angle(line1, line_moving, radius=line1.get_length(), other_angle=False))
            )
            
            angle_group = VGroup(line1, line_moving, origin, first_point,a,edge, label,dots,tris)
            
            return angle_group, dots_and_tris_anim
        
    
        group1, anim1 = angle_factory(1, LEFT*13)
        group2, anim2 = angle_factory(2, LEFT*7)
        group3, anim3 = angle_factory(3, LEFT)
        group4, anim4 = angle_factory(4, RIGHT*5)
        group5, anim5 = angle_factory(5, RIGHT*11)

        groups = VGroup(group1,group2,group3,group4,group5)
        
         
        config.frame_width = 40
        self.add(plane)
        
        self.add_foreground_mobjects(groups)
        
        self.play(LaggedStart(theta_tracker.animate(run_time=2).increment_value(140),
                             (AnimationGroup(LaggedStart(*(i for i in anim1),
                                                        lag_ratio=0.2),
                                              LaggedStart(*(i for i in anim2),
                                                        lag_ratio=0.2),
                                              LaggedStart(*(i for i in anim3),
                                                        lag_ratio=0.2),
                                              LaggedStart(*(i for i in anim4),
                                                        lag_ratio=0.2),
                                              LaggedStart(*(i for i in anim5),
                                                        lag_ratio=0.2))),
                             lag_ratio=0.25))
        
        
        self.wait(2)
        
      
x = MovingAngleSeries()
x.render()                    
        


    
