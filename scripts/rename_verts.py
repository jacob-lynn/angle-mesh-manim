
from manim import *
import numpy as np 

class RenameVerts(MovingCameraScene):
    def construct(self):    
            self.camera.frame.set(width=20).shift(DOWN)
            
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
            
            nums.shift(RIGHT)    
           
            tri_nums = VGroup()
            tri_nums.add(*[Integer(i).move_to(tri_num_arc.point_from_proportion((i * 1/int(num_of_tris))+ 0.5*(1/int(num_of_tris))))
                                    for i in range(num_of_tris)])    
            tri_nums[0].set_color(RED)
            tri_nums[1].set_color(GREEN)
            tri_nums[2].set_color(PURPLE) 
            self.add(tri_nums)    
            
            angle_group = VGroup(line1, line_moving, tris, tri_nums, edge,a, dots)
            
            self.add_foreground_mobjects(angle_group.shift(RIGHT)) 
            
            triangles_var = VGroup()
            triangles_var.add(Text('[',font_size=25), Integer(0,color=RED), Text(',',font_size=25), Integer(1, color=GREEN), Text(',',font_size=25), Integer(2, color=PURPLE), Text(']',font_size=25))
            triangles_var.arrange_in_grid(rows=1, col=num_of_tris, cell_alignment=[0,-1,0], buff=(MED_SMALL_BUFF*1.21)).move_to(RIGHT).shift(DOWN*2.5)
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
            indices_var.arrange_in_grid(rows=1, cell_alignment=[0,-1,0], buff=MED_SMALL_BUFF).next_to(triangles_var,DOWN*0.5).scale(0.75)
            indices_var_label = Text('indices =', font_size=25).next_to(indices_var,LEFT).scale(0.75)
            
            plane = NumberPlane(x_range=[-20,20],
                                y_range=[-20,20],                                
                                background_line_style={
                                    'stroke_opacity':0.75})
           
            def redraw_axis_labels():
                return  VGroup(plane.get_x_axis_label("x").move_to([self.camera.frame_width/2-MED_SMALL_BUFF,MED_SMALL_BUFF,0],aligned_edge=RIGHT),
                                plane.get_y_axis_label("y").move_to(self.camera.frame_center + [MED_SMALL_BUFF,self.camera.frame_height/2 - MED_SMALL_BUFF,0]))
            axis_labels = always_redraw(redraw_axis_labels)    
            
            coords_3d = []
            for d in dots:
                coords_3d.append(VGroup(Text('(',font_size=25),
                                     DecimalNumber(d.get_x(),num_decimal_places=1),
                                     Text(',',font_size=25),
                                     DecimalNumber(d.get_y(),num_decimal_places=1),
                                     Text(',',font_size=25),
                                     DecimalNumber(0.0, num_decimal_places=1),
                                     Text(')',font_size=25)))
            for c in coords_3d:
                c.scale(0.75)
            
            coords_3d_0 = coords_3d[0].arrange_in_grid(rows=1, cell_alignment=[0,-1,0], buff=(SMALL_BUFF)).move_to(nums[0]).move_to(nums[0],UR*2)
            coords_3d_1 = coords_3d[1].arrange_in_grid(rows=1, cell_alignment=[0,-1,0], buff=(SMALL_BUFF)).move_to(nums[1]).next_to(nums[1],UP,aligned_edge=DL)
            coords_3d_2 = coords_3d[2].arrange_in_grid(rows=1, cell_alignment=[0,-1,0], buff=(SMALL_BUFF)).move_to(nums[2]).move_to(nums[2],aligned_edge=DL)
            coords_3d_3 = coords_3d[3].arrange_in_grid(rows=1, cell_alignment=[0,-1,0], buff=(SMALL_BUFF)).move_to(nums[3]).move_to(nums[3]).shift(RIGHT*SMALL_BUFF*3.2)
            coords_3d_4 = coords_3d[4].arrange_in_grid(rows=1, cell_alignment=[0,-1,0], buff=(SMALL_BUFF)).move_to(nums[4]).next_to(nums[4],LEFT*0.4,aligned_edge=DR)
            
            vertices_var = VGroup(Text('[',font_size=25))
           
            for i in range(num_of_tris+2):
                vertices_var.add(coords_3d[i].copy(),Text(',',font_size=25))
            vertices_var.remove(vertices_var[-1])
            vertices_var.add(Text(']',font_size=25))
            
            self.add(plane,coords_3d_0, coords_3d_1, coords_3d_2, coords_3d_3, coords_3d_4)
            
            triangles_var.arrange_in_grid(rows=1, cell_alignment=[0,-1,0], buff=LARGE_BUFF*1.03).shift(UP*0.4).scale(0.75)
            triangles_label.next_to(triangles_var,LEFT).scale(0.75)
            vertices_var.arrange_in_grid(rows=1,cell_alignment=[0,-1,0], buff=MED_SMALL_BUFF).next_to(indices_var, DOWN*4).scale(0.75)    
            vertices_label = Text('vertices =', font_size=25).next_to(vertices_var, LEFT).scale(0.75)
        
            braces_2 = VGroup()
            for i in range(vertices_var.__len__()):
                if (i%2!=0):
                    braces_2.add(Brace(vertices_var[i],UP))
           
            black_rectangle = Rectangle(color=BLACK, fill_opacity=1 ,height=3,width=13).shift(DOWN*3.25)
            black_rectangle_2 = Rectangle(color=BLACK, fill_opacity=1 ,height=1.25,width=13).shift(DOWN*2.35)
                  
            self.add(axis_labels)
            
            self.add(black_rectangle,triangles_var,triangles_label,indices_var,indices_var_label,braces_2)
               
            self.add(vertices_label,vertices_var)
            
            self.add(triangles_label.align_to(vertices_label,RIGHT),
                     indices_var_label.align_to(vertices_label,RIGHT),
                     indices_var.arrange_in_grid(rows=1, cell_alignment=[0,-1,0], buff=MED_LARGE_BUFF*0.97),
                     triangles_var.arrange_in_grid(rows=1, cell_alignment=[0,-1,0], buff=LARGE_BUFF*1.66))
            
            braces = VGroup()
            braces.add(Brace(indices_var[1:6],UP,color=RED_C))
            braces.add(Brace(indices_var[7:12],UP,color=GREEN_C))
            braces.add(Brace(indices_var[13:18],UP,color=PURPLE_C))
            
            red_lines = VGroup(Line(indices_var[1].get_bottom(),braces_2[0].get_tip(),buff=SMALL_BUFF,color=RED),
                               Line(indices_var[3].get_bottom(),braces_2[2].get_tip(),buff=SMALL_BUFF,color=RED),
                               Line(indices_var[5].get_bottom(),braces_2[1].get_tip(),buff=SMALL_BUFF,color=RED))
            
            green_lines = VGroup(Line(indices_var[7].get_bottom(),braces_2[0].get_tip(),buff=SMALL_BUFF,color=GREEN),
                               Line(indices_var[9].get_bottom(),braces_2[3].get_tip(),buff=SMALL_BUFF,color=GREEN),
                               Line(indices_var[11].get_bottom(),braces_2[2].get_tip(),buff=SMALL_BUFF,color=GREEN))
            
            purple_lines = VGroup(Line(indices_var[13].get_bottom(),braces_2[0].get_tip(),buff=SMALL_BUFF,color=PURPLE),
                               Line(indices_var[15].get_bottom(),braces_2[4].get_tip(),buff=SMALL_BUFF,color=PURPLE),
                               Line(indices_var[17].get_bottom(),braces_2[3].get_tip(),buff=SMALL_BUFF,color=PURPLE))
           
            self.add(red_lines,green_lines,purple_lines,braces)
            
            self.wait()
            self.play(FadeOut(triangles_var,braces,tri_nums))
            self.remove(tri_nums)
            self.play(triangles_label.animate.move_to(indices_var_label).align_to(vertices_label,RIGHT),FadeOut(indices_var_label))
            self.play(FadeOut(red_lines,green_lines,purple_lines,braces_2))
            self.play(indices_var.animate.shift(UP),
                      vertices_var.animate.shift(UP*1.75),
                      vertices_label.animate.shift(UP*1.75),
                      triangles_label.animate.shift(UP),                      
                      black_rectangle.animate.become(black_rectangle_2))
            
            self.wait(3)
            
x = RenameVerts()
x.render()
