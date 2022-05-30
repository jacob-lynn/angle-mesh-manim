
from manim import *
import numpy as np 

class AddVars(Scene):
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
            
            self.add(theta_tracker.set_value(140))
            self.add(line1, line_moving, tris, edge)     
            self.add_foreground_mobjects(a, dots, nums)    
             
            
            tri_nums = VGroup()
            tri_nums.add(*[Integer(i).set_color(BLUE).move_to(tri_num_arc.point_from_proportion((i * 1/int(num_of_tris))+ 0.5*(1/int(num_of_tris))))
                                    for i in range(num_of_tris)])    
            
            tri_nums[0].set_color(RED)
            tri_nums[1].set_color(GREEN)
            tri_nums[2].set_color(PURPLE)
            
            self.add(tri_nums)    
            
            self.camera.frame_center = (RIGHT*2.5)
                
            
            horizontal_line = Line(LEFT*3,RIGHT*2).next_to(circle,UR+RIGHT*6)
            vertical_line = Line(horizontal_line.get_midpoint()+UP*0.5, horizontal_line.get_midpoint()+DOWN*2)
            
            left_text = Text('Triangle',font_size=25).move_to(horizontal_line.point_from_proportion(0.25),aligned_edge=DOWN)
            right_text = Text('Indices',font_size=25).move_to(horizontal_line.point_from_proportion(0.75),aligned_edge=DOWN).align_to(left_text,UP)
            
            self.add(horizontal_line,vertical_line,left_text,right_text)
            
            tri_table_nums = tri_nums.copy().arrange_in_grid(rows=num_of_tris, col=1, cell_alignment=[0,-1,0], buff=(MED_SMALL_BUFF*1.21)).next_to(horizontal_line.point_from_proportion(0.25),DOWN, aligned_edge=UP, buff=MED_SMALL_BUFF)
            
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
            self.add(tri_table_nums)
            self.add(table_nums)    
            
            triangles_var = VGroup()
            triangles_var.add(Text('[',font_size=25), Integer(0,color=RED), Text(',',font_size=25), Integer(1, color=GREEN), Text(',',font_size=25), Integer(2, color=PURPLE), Text(']',font_size=25))
            triangles_var.arrange_in_grid(rows=1, col=num_of_tris, cell_alignment=[0,-1,0], buff=(MED_SMALL_BUFF*1.21)).move_to(RIGHT*3.5).shift(DOWN*2)
            triangles_label = Text('triangles =', font_size=25).next_to(triangles_var, LEFT)
            
            indices_var = VGroup(Text('[',font_size=25))            
            for i in range(num_of_tris):     
                if (i==0):
                    color=RED_C
                if (i==1):
                    color=GREEN_C
                if (i==2):
                    color=PURPLE_C           
                indices_var.add(Integer(0,color=color), Text(',',font_size=25), Integer(i+2,color=color), Text(',',font_size=25), Integer(i+1,color=color), Text(',',font_size=25))
            indices_var.remove(indices_var[num_of_tris*6])
            indices_var.add(Text(']',font_size=25))
            indices_var.arrange_in_grid(rows=1, cell_alignment=[0,-1,0], buff=MED_SMALL_BUFF).next_to(triangles_var,DOWN)
            indices_var_label = Text('indices =', font_size=25).next_to(indices_var,LEFT)
            
            
            def move_tri_nums_to_var():
                tri_nums_to_var_anim = []
                for i in range(num_of_tris):
                    tri_nums_to_var_anim.append(TransformFromCopy(tri_table_nums[i],triangles_var[i*2+1]))
                return tri_nums_to_var_anim
            
            def move_vert_nums_to_var():
                filtered_table_nums = []
                vert_nums_to_var_anim = []
                even = False
                for i in range(num_of_tris*7):
                    if (i%7 == 0 and i !=0):
                        if even:
                            even = False
                        else:
                            even = True
                        continue
                    if (even):
                        if(i%2 == 0):
                            filtered_table_nums.append(table_nums[i])
                    else: 
                        if(i%2 !=0):
                            filtered_table_nums.append(table_nums[i])    
                for i in range(num_of_tris*3):
                    vert_nums_to_var_anim.append(TransformFromCopy(filtered_table_nums[i], indices_var[i*2+1])) 
                return vert_nums_to_var_anim
           
            def fade_in_tri_brackets():
                tri_brackets_anim = [] 
                for i in range(num_of_tris*2+1):
                    if(i%2 == 0):
                        tri_brackets_anim.append(FadeIn(triangles_var[i]))
                return tri_brackets_anim        
               
            def fade_in_vert_brackets():
                vert_brackets_anim = []
                for i in range(num_of_tris*5 +4):
                    if (i%2 == 0): 
                        vert_brackets_anim.append(FadeIn(indices_var[i]))
                return vert_brackets_anim
                    
            
            self.play(LaggedStart(*move_tri_nums_to_var(),lag_ratio=0.2),
                      FadeIn(triangles_label),
                      LaggedStart(*(_ for _ in fade_in_tri_brackets()),lag_ratio=0.2))
            
            self.play(LaggedStart(*(move_vert_nums_to_var()),lag_ratio=0.2),
                      FadeIn(indices_var_label),
                      LaggedStart(*(_ for _ in fade_in_vert_brackets()),lag_ratio=0.2))
            
            braces = VGroup()
            braces.add(Brace(indices_var[1:6],UP,color=RED))
            braces.add(Brace(indices_var[7:12],UP,color=GREEN))
            braces.add(Brace(indices_var[13:18],UP,color=PURPLE))
            self.play(triangles_var.animate.arrange_in_grid(rows=1, cell_alignment=[0,-1,0], buff=LARGE_BUFF*1.03).shift(UP*0.4),
                      triangles_label.animate.shift(LEFT*2.17).shift(UP*0.4),
                      FadeIn(braces))
            self.wait(2)
           
x = AddVars()
x.render() 
            
            
            
            
