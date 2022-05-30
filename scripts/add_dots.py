from manim import *
import numpy as np 


class AddDots(Scene):
    def construct(self):
        
        rotation_center = ORIGIN
        angle = 140 
        num_of_tris = 7
        sub_angle = angle / num_of_tris
        
                
        theta_tracker = ValueTracker(0.1)
        line1 = Line(ORIGIN, RIGHT*3, color=GRAY_A)
        line_moving = Line(ORIGIN, line1.get_end(), color=GRAY_A)
        line_ref = line_moving.copy()
        line_moving.rotate(
            theta_tracker.get_value() * DEGREES, about_point=rotation_center
        )
        
        
        a = Angle(line1, line_moving, radius=0.5, other_angle=False)
        circle = Circle(radius=line1.get_length())
        num_circle = Circle(radius=line1.get_length()+SMALL_BUFF*4)
        edge = Angle(line1, line_moving, circle.radius, other_angle=False, color=GRAY_A)
       
        tri_count = 0
        array_of_points = np.zeros([num_of_tris+2, 3])
        array_of_points[0,:] = circle.get_center()
        array_of_nums = np.zeros([num_of_tris+2, 3])
        while tri_count <= num_of_tris:
            array_of_points[(tri_count + 1), :] = circle.point_at_angle((tri_count * sub_angle)*DEGREES)
            array_of_nums[(tri_count + 1), :] = num_circle.point_at_angle((tri_count * sub_angle)*DEGREES)
            tri_count += 1   
        
        array_of_tris = np.zeros([num_of_tris, 3,3])       
        array_of_tris[:,0,:] = circle.get_center()
        for t in range(num_of_tris):
            array_of_tris[t,1,:] = array_of_points[t+1,:] 
            array_of_tris[t,2,:] = array_of_points[t+2,:]                               

        
        line_moving.add_updater(
            lambda x: x.become(line_ref.copy()).rotate(
                theta_tracker.get_value() * DEGREES, about_point=rotation_center
            )
        )     

        a.add_updater(
            lambda x: x.become(Angle(line1, line_moving, radius=0.5, other_angle=False))
        )        

        edge.add_updater(
            lambda x: x.become(Angle(line1, line_moving, radius=line1.get_length(), other_angle=False, color=GRAY_A))
        )
        
        

        origin = Dot(array_of_points[0])        
        first_point = Dot(array_of_points[1])
        array_of_points = np.delete(array_of_points, [0,1], 0)
             

        dots = VGroup(*[Dot(i)
                        for i in array_of_points])
        
        nums = VGroup(Integer(0).next_to(origin,DL*0.5),
                        Integer(1).next_to(first_point,RIGHT))
        nums.add(*[Integer(i).move_to(array_of_nums[i])
                                for i in range(2, num_of_tris+2)])

        
        self.add(line1, line_moving, edge)     
        self.add_foreground_mobjects(a, first_point, origin)    
        
        self.play(LaggedStart(theta_tracker.animate(run_time=2).increment_value(140),
                              LaggedStart(FadeIn(*(_ for _ in dots),lag_ratio=0.3)),
                                        lag_ratio=0.3))
        
        self.play(FadeIn(nums))
        
        self.wait(2)
        
       
        
x = AddDots()
x.render
