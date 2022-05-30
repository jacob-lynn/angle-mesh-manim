from manim import *
import numpy as np 

class AddZVals(ThreeDScene):
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
            
            nums.shift(RIGHT)   
         
             
            tri_nums = VGroup()
            tri_nums.add(*[Integer(i).set_color(BLUE).move_to(tri_num_arc.point_from_proportion((i * 1/int(num_of_tris))+ 0.5*(1/int(num_of_tris))))
                                    for i in range(num_of_tris)])  
            tri_nums[0].set_color(RED)
            tri_nums[1].set_color(GREEN)
            tri_nums[2].set_color(PURPLE)  
            self.add(tri_nums)    
            
         
            
            angle_group = VGroup(line1, line_moving, tris, tri_nums, edge,a, dots)
            
            self.add_foreground_mobjects(angle_group.shift(RIGHT)) 
            
            plane = NumberPlane(x_range=[-20,20],
                                y_range=[-20,20],                                
                                background_line_style={
                                    'stroke_opacity':0.75}).set_z_index(0)
            self.add(plane.get_x_axis_label("x").move_to([self.camera.frame_width/2-MED_SMALL_BUFF,MED_SMALL_BUFF,0],aligned_edge=RIGHT))
            self.add(plane.get_y_axis_label("y").shift(UP*0.6))
            
           
            coords_2d = VGroup()
            for d in dots:
                coords_2d.add(Text('(',font_size=25), DecimalNumber(d.get_x(),num_decimal_places=1), Text(',',font_size=25), DecimalNumber(d.get_y(),num_decimal_places=1),Text(')',font_size=25))
           
            coords_2d.scale(0.75)
            
            coords_2d_0 = coords_2d[0:5].arrange_in_grid(rows=1, cell_alignment=[0,-1,0], buff=(SMALL_BUFF)).move_to(nums[0],UR*2)
            coords_2d_1 = coords_2d[5:10].arrange_in_grid(rows=1, cell_alignment=[0,-1,0], buff=(SMALL_BUFF)).next_to(nums[1],UP,aligned_edge=DL)
            coords_2d_2 = coords_2d[10:15].arrange_in_grid(rows=1, cell_alignment=[0,-1,0], buff=(SMALL_BUFF)).move_to(nums[2],aligned_edge=DL)
            coords_2d_3 = coords_2d[15:20].arrange_in_grid(rows=1, cell_alignment=[0,-1,0], buff=(SMALL_BUFF)).move_to(nums[3])
            coords_2d_4 = coords_2d[20:25].arrange_in_grid(rows=1, cell_alignment=[0,-1,0], buff=(SMALL_BUFF)).next_to(nums[4],LEFT*0.4,aligned_edge=DR)
            
            z_val_0 = VGroup(Text(',', font_size=25), DecimalNumber(0.0, num_decimal_places=1, color=YELLOW)).scale(0.75).arrange_in_grid(rows=1, cell_alignment=[0,-1,0], buff=(SMALL_BUFF)).move_to(coords_2d_0[3])
            z_val_1 = VGroup(Text(',', font_size=25), DecimalNumber(0.0, num_decimal_places=1, color=YELLOW)).scale(0.75).arrange_in_grid(rows=1, cell_alignment=[0,-1,0], buff=(SMALL_BUFF)).next_to(coords_2d_1[3],buff=SMALL_BUFF)
            z_val_2 = VGroup(Text(',', font_size=25), DecimalNumber(0.0, num_decimal_places=1, color=YELLOW)).scale(0.75).arrange_in_grid(rows=1, cell_alignment=[0,-1,0], buff=(SMALL_BUFF)).next_to(coords_2d_2[3],buff=SMALL_BUFF)
            z_val_3 = VGroup(Text(',', font_size=25), DecimalNumber(0.0, num_decimal_places=1, color=YELLOW)).scale(0.75).arrange_in_grid(rows=1, cell_alignment=[0,-1,0], buff=(SMALL_BUFF)).next_to(coords_2d_3[3],buff=SMALL_BUFF)
            z_val_4 = VGroup(Text(',', font_size=25), DecimalNumber(0.0, num_decimal_places=1, color=YELLOW)).scale(0.75).arrange_in_grid(rows=1, cell_alignment=[0,-1,0], buff=(SMALL_BUFF)).move_to(coords_2d_4[3])
            
            z_vals = VGroup(z_val_0,z_val_1,z_val_2,z_val_3,z_val_4)
            
            self.add(plane,coords_2d_0,coords_2d_1,coords_2d_2,coords_2d_3,coords_2d_4) 
            config.frame_width=16
            
            
            axes_3d = ThreeDAxes(x_length=0,                                 
                                 y_length=0,   
                                 z_length=11,
                                 tips = False,   
                                 x_axis_config={
                                    "include_ticks" : False
                                 },   
                                 y_axis_config={
                                     "include_ticks" : False
                                 },                         
                                 z_axis_config={
                                    "include_tip"   : True,
                                     "include_ticks": False
                                }                 
            )
            
            self.add(axes_3d.get_z_axis_label("z",rotation=PI/2, rotation_axis=UP).move_to([0,MED_SMALL_BUFF,axes_3d.z_length/2 - 0.4]))#.rotate(PI,RIGHT))
            self.play(FadeIn(axes_3d.set_z_index(2)))
           
            self.move_camera(phi=-45*DEGREES,theta=-160*DEGREES,gamma=-90*DEGREES)
            self.wait(0.5)
            self.move_camera(phi=0*DEGREES,theta=-90*DEGREES,gamma=0*DEGREES)
            self.play(coords_2d_1[4].animate.next_to(z_val_1,RIGHT*SMALL_BUFF),
                      coords_2d_2[4].animate.next_to(z_val_2,RIGHT*SMALL_BUFF),
                      coords_2d_3[4].animate.next_to(z_val_3,RIGHT*SMALL_BUFF),
                      coords_2d_4[0:4].animate.next_to(z_val_4,LEFT*SMALL_BUFF),
                      coords_2d_0[0:4].animate.next_to(z_val_0,LEFT*SMALL_BUFF),
                      FadeIn(z_vals),
                      )
            self.play(z_vals.animate.set_color(WHITE))
            self.wait(2)
            
 
            
x = AddZVals()
x.render()