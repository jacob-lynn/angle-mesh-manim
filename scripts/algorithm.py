from manim import *
import numpy as np 

class Algorithm(Scene):
    def construct(self):
        
#         code = '''from manim import Scene, Square

# class FadeInSquare(Scene):
#     def construct(self):
#          = Square()
#         self.play(FadeIn(s))
#         self.play(s.animate.scale(2))
#         self.wait()
# '''
        # rendered_code = Code(code=code, tab_width=4, background="window",
        #                     language="cs", font="Monospace", style="Monokai")

        rotation_center = LEFT
        angle = 140
        num_of_tris = 3
        sub_angle = angle / num_of_tris

        number_plane = NumberPlane(background_line_style={"stroke_opacity":0},axis_config={"stroke_opacity":0.4}).shift(LEFT)
        
        theta_tracker = ValueTracker(angle)
        line1 = Line(LEFT, RIGHT*2)
        line_moving = Line(LEFT, line1.get_end())
        line_moving.rotate(
            theta_tracker.get_value() * DEGREES, about_point=rotation_center
        )

        a = Angle(line1, line_moving, radius=0.5, other_angle=False)
        circle = Circle(radius=line1.get_length()).shift(LEFT)
        num_circle = Circle(radius=line1.get_length()+SMALL_BUFF*4).shift(LEFT)
        edge = Angle(line1, line_moving, circle.radius, other_angle=False, color=GRAY_A)
        tri_num_arc = ArcBetweenPoints(line1.point_from_proportion(0.75), [-2.72612159,  1.44326167,  0.        ], radius=line1.get_length()*0.75)

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


        dots = VGroup(*[Dot(i)
                        for i in array_of_points])

        tris = VGroup(*[Polygon(t[0,:],t[2,:],t[1,:]).set_fill(BLUE, opacity=0.2)
                for t in array_of_tris])

        nums = VGroup(Integer(0).next_to(dots[0],DL*0.5),
                Integer(1).next_to(dots[1],RIGHT))
        nums.add(*[Integer(i).move_to(array_of_nums[i])
                        for i in range(2, num_of_tris+2)])
        
    
        bg_objects = VGroup(line1,line_moving,edge, number_plane)
        fg_objects = VGroup(a,dots,nums) 
        self.add(bg_objects)     
        self.add_foreground_mobjects(fg_objects)    
        
        tri_anims = [] 
        for t in tris:  
            tri_anims.append(DrawBorderThenFill(t,run_time=1,rate_func=rush_into))
         
        # tri_nums = VGroup()
        # tri_nums.add(*[Integer(i).set_color(BLUE).move_to(tri_num_arc.point_from_proportion((i * 1/int(num_of_tris))+ 0.5*(1/int(num_of_tris))))
        #                     for i in range(num_of_tris)])
        # for i in range(num_of_tris):               
        #        tri_nums[i].move_to(tri_num_arc.point_from_proportion((i * 1/int(num_of_tris))+ 0.5*(1/int(num_of_tris))))
    
        self.camera.frame_center = dots[0].get_center()
        self.play(LaggedStart(*(_ for _ in tri_anims),lag_ratio=0.5))
        # self.play(FadeIn(tri_nums))
        self.wait(2)
        
x = Algorithm()
x.render()                    
        
