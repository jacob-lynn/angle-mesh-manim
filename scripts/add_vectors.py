
from manim import *
import numpy as np 

class AddVectors(MovingCameraScene):
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
            
           
             
            tri_nums = VGroup()
            tri_nums.add(*[Integer(i).set_color(BLUE).move_to(tri_num_arc.point_from_proportion((i * 1/int(num_of_tris))+ 0.5*(1/int(num_of_tris))))
                                    for i in range(num_of_tris)])    
            
            tri_nums[0].set_color(RED)
            tri_nums[1].set_color(GREEN)
            tri_nums[2].set_color(PURPLE)
            self.add(tri_nums)    
           
            
            angle_group = VGroup(line1, line_moving, tris, tri_nums, edge,a, dots, nums)
            
            self.add_foreground_mobjects(angle_group) 
            
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
                table_nums.add(Text('[',font_size=25), Integer(0,color=color), Text(',',font_size=25), Integer(i+2, color=color), Text(',',font_size=25), Integer(i+1,color=color), Text(']',font_size=25))
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
            indices_var.remove(indices_var[-1])
            indices_var.add(Text(']',font_size=25))
            indices_var.arrange_in_grid(rows=1, cell_alignment=[0,-1,0], buff=MED_SMALL_BUFF).next_to(triangles_var,DOWN)
            indices_var_label = Text('indices =', font_size=25).next_to(indices_var,LEFT)
            
            braces = VGroup()
            braces.add(Brace(indices_var[1:6],UP,color=RED), Brace(indices_var[7:12],UP,color=GREEN), Brace(indices_var[13:18],UP,color=PURPLE))
            
            self.add(triangles_var,triangles_label)
            self.add(indices_var.next_to(triangles_var,DOWN), indices_var_label.next_to(indices_var, LEFT))
            self.add(triangles_var.arrange_in_grid(rows=1, cell_alignment=[0,-1,0], buff=LARGE_BUFF*1.03).shift(UP*0.4),
                      triangles_label.shift(LEFT*2.17).shift(UP*0.4),
                      braces)
            
            plane = NumberPlane(x_range=[-20,20],
                                y_range=[-20,20],                                
                                background_line_style={
                                    'stroke_opacity':0.75}).shift(RIGHT*2.5)
           
            self.play(FadeOut(table_nums,tri_table_nums, horizontal_line, vertical_line, triangles_label,triangles_var,indices_var,indices_var_label, braces, left_text, right_text))
            self.play(LaggedStart(angle_group.animate(run_time=1.5).shift(RIGHT*3.5),
                                    FadeIn(plane, plane.get_x_axis_label("x").shift(RIGHT*3.5),plane.get_y_axis_label("y").shift(UP*0.6)),
                                    self.camera.frame.animate.set(width=16),
                                         lag_ratio=0.25))
            
          
            
            coords_2d = VGroup()
            for d in dots:
                coords_2d.add(Text('(',font_size=25), DecimalNumber(d.get_x() - 2.5,num_decimal_places=1), Text(',',font_size=25), DecimalNumber(d.get_y(),num_decimal_places=1),Text(')',font_size=25))
            
            coords_2d.scale(0.75)
          
            coords_2d_0 = coords_2d[0:5].arrange_in_grid(rows=1, cell_alignment=[0,-1,0], buff=(SMALL_BUFF)).move_to(nums[0],UR*2)
            coords_2d_1 = coords_2d[5:10].arrange_in_grid(rows=1, cell_alignment=[0,-1,0], buff=(SMALL_BUFF)).next_to(nums[1],UP,aligned_edge=DL)
            coords_2d_2 = coords_2d[10:15].arrange_in_grid(rows=1, cell_alignment=[0,-1,0], buff=(SMALL_BUFF)).move_to(nums[2],aligned_edge=DL)
            coords_2d_3 = coords_2d[15:20].arrange_in_grid(rows=1, cell_alignment=[0,-1,0], buff=(SMALL_BUFF)).move_to(nums[3])
            coords_2d_4 = coords_2d[20:25].arrange_in_grid(rows=1, cell_alignment=[0,-1,0], buff=(SMALL_BUFF)).next_to(nums[4],LEFT*0.4,aligned_edge=DR)
            
            self.play(FadeOut(nums))
            self.play(FadeIn(coords_2d_0,coords_2d_1,coords_2d_2,coords_2d_3,coords_2d_4))
            self.wait(2)
            
           
          
x = AddVectors()
x.render()
