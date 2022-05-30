
from manim import *
import numpy as np 

class TriNums(MovingCameraScene):
    def construct(self):        
        
        rotation_center = LEFT
        angle = 140 
        num_of_tris = 3
        sub_angle = angle / num_of_tris
            
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
        tri_num_arc = ArcBetweenPoints(line1.point_from_proportion(0.6), [-2.37888  ,  1.1570177,  0.       ], radius=line1.get_length()*0.6)
       
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

        tris[0].set_fill(RED_C,opacity=0.4)
        tris[1].set_fill(GREEN_C,opacity=0.4)
        tris[2].set_fill(PURPLE_C,opacity=0.4)
        
        nums = VGroup(Integer(0).next_to(dots[0],DL*0.5),
                        Integer(1).next_to(dots[1],RIGHT))
        nums.add(*[Integer(i).move_to(array_of_nums[i])
                                for i in range(2, num_of_tris+2)])
        

        self.add(line1, line_moving, tris, edge)     
        self.add_foreground_mobjects(a, dots, nums)    
        self.add(theta_tracker.set_value(140))   
        
        
       
        tri_nums = VGroup()
        tri_nums.add(*[Integer(i).set_color(BLUE).move_to(tri_num_arc.point_from_proportion((i * 1/int(num_of_tris))+ 0.5*(1/int(num_of_tris))))
                                for i in range(num_of_tris)]) 
        tri_nums[0].set_color(RED)
        tri_nums[1].set_color(GREEN)
        tri_nums[2].set_color(PURPLE)
        self.add(tri_nums)    
        
       
        self.camera.frame_center = dots[0].get_center()
               
        
        horizontal_line = Line(LEFT*3,RIGHT*2).next_to(circle,UR+RIGHT*6)
        vertical_line = Line(horizontal_line.get_midpoint()+UP*0.5, horizontal_line.get_midpoint()+DOWN*2)
        
        left_text = Text('Triangle',font_size=25).move_to(horizontal_line.point_from_proportion(0.25),aligned_edge=DOWN)
        right_text = Text('Indices',font_size=25).move_to(horizontal_line.point_from_proportion(0.75),aligned_edge=DOWN).align_to(left_text,UP)
        
        self.wait()
        self.play(LaggedStart(self.camera.frame.animate.move_to(RIGHT*2.5), FadeIn(horizontal_line,vertical_line,left_text,right_text), lag_ratio=0.5))
        
        tri_table_nums = tri_nums.copy().arrange_in_grid(rows=num_of_tris, col=1, cell_alignment=[0,-1,0], buff=(MED_SMALL_BUFF*1.21)).next_to(horizontal_line.point_from_proportion(0.25),DOWN, aligned_edge=UP, buff=MED_SMALL_BUFF)
        tri_table_nums[0].set_color(RED)
        tri_table_nums[1].set_color(GREEN)
        tri_table_nums[2].set_color(PURPLE)
        
        
        table_nums = VGroup()
        for i in range(num_of_tris):
            if (i==0):
                color=RED_C
            if (i==1):
                color=GREEN_C
            if (i==2):
                color=PURPLE_C
            table_nums.add(Text('[',font_size=25), Integer(0,color=color), Text(',',font_size=25), Integer(i+2,color=color), Text(',',font_size=25), Integer(i+1,color=color), Text(']',font_size=25))
        table_nums.arrange_in_grid(rows=num_of_tris, col=7, cell_alignment=[0,-1,0], buff=(SMALL_BUFF,MED_SMALL_BUFF)).next_to(vertical_line, RIGHT, buff=MED_LARGE_BUFF).align_to(tri_table_nums, UP)
        
        def highlight_tri_and_tri_num_anims(i):            
                return AnimationGroup(Indicate(tris[i],scale_factor=1),Indicate(tri_nums[i]))    
            
        def highlight_dots_and_nums_anims(i):
                return AnimationGroup(Indicate(dots[0]),Indicate(nums[0]),Indicate(dots[i+2]),Indicate(nums[i+2]),Indicate(dots[i+1]),Indicate(nums[i+1]))
            
        def move_tri_num(i):
                return AnimationGroup(TransformFromCopy(tri_nums[i],tri_table_nums[i]))
        
        def move_nums_and_fade_brackets(i):
                return AnimationGroup(FadeIn(table_nums[i*7],table_nums[i*7+2],table_nums[i*7+4],table_nums[i*7+6]),
                                        TransformFromCopy(nums[0], table_nums[i*7+1]),
                                        TransformFromCopy(nums[i+2], table_nums[i*7+3]),
                                        TransformFromCopy(nums[i+1], table_nums[i*7+5]))
            
        per_tri_anim_group = np.zeros(shape=(num_of_tris,4),dtype=AnimationGroup)
        for i in range(num_of_tris):            
            per_tri_anim_group[i,0] = highlight_tri_and_tri_num_anims(i)
            per_tri_anim_group[i,1] = highlight_dots_and_nums_anims(i)
            per_tri_anim_group[i,2] = move_tri_num(i)
            per_tri_anim_group[i,3] = move_nums_and_fade_brackets(i)
            
                           
        
        self.play(per_tri_anim_group[0,0])
        self.play(per_tri_anim_group[0,1])
        self.play(per_tri_anim_group[0,2])
        self.play(per_tri_anim_group[0,3])
        self.play(per_tri_anim_group[1,0])
        self.play(per_tri_anim_group[1,1])
        self.play(per_tri_anim_group[1,2])
        self.play(per_tri_anim_group[1,3])
        self.play(per_tri_anim_group[2,0])
        self.play(per_tri_anim_group[2,1])
        self.play(per_tri_anim_group[2,2])
        self.play(per_tri_anim_group[2,3])
        
       
x = TriNums()
x.render()                    
        


    