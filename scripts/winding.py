from manim import *
import numpy as np 

class Winding(Scene):
    def construct(self):
        
        rotation_center = LEFT

        theta_tracker = ValueTracker(0.1)
        line1 = Line(LEFT, RIGHT)
        line_moving = Line(LEFT, RIGHT)
        line_ref = line_moving.copy()
        line_moving.rotate(
            theta_tracker.get_value() * DEGREES, about_point=rotation_center
        )
        line_static = Line(LEFT, RIGHT, color=YELLOW)
        line_static.rotate(
            110 * DEGREES, about_point=rotation_center
        )

        angleFromPos = Angle(line1,line_moving,radius=line1.get_length(), color=BLUE)
        angleFromNeg = Angle(line1,line_moving,radius=line1.get_length(), other_angle=True, color=RED)
        arcFromPos = Angle(line1, line_moving, radius=0.5, other_angle=False, color=BLUE)
        arcFromNeg = Angle(line1, line_moving, radius=0.5, other_angle=True, color=RED)
        theta = MathTex(r"\theta", color=BLUE).move_to(
            Angle(
                line1, line_moving, radius=0.5 + 3 * SMALL_BUFF, other_angle=False
            ).point_from_proportion(0.5)
        )
        # q1 = angleFromPos.points        
        # q2 = line_moving.reverse_points().points
        # q3 = line1.points
        # points = np.concatenate([q1,q2, q3])
        # mfill = VMobject()
        # mfill.set_points(points).set_fill(BLUE,opacity=0.5)
        filledAngleFromPos = AnnularSector(inner_radius=0,
                                           outer_radius=line1.get_length(),
                                           angle=(theta_tracker.get_value()*DEGREES),
                                           fill_opacity=0.4,
                                           color=BLUE).shift(LEFT)
        filledAngleFromNeg = AnnularSector(inner_radius=0,
                                           outer_radius=line1.get_length(),
                                           start_angle=-250*DEGREES,
                                           angle=((theta_tracker.get_value()-360)*DEGREES),
                                           fill_opacity=0.4,
                                           color=RED).shift(LEFT)                                           

        self.add(line1, line_moving, arcFromPos, line_static)
        self.add_foreground_mobject(theta)
        self.wait()

        line_moving.add_updater(
            lambda x: x.become(line_ref.copy()).rotate(
                theta_tracker.get_value() * DEGREES, about_point=rotation_center
            )
        )
        # angleFromPos.add_updater(
        #     lambda x: x.become(Angle(line1, line_moving, radius=line1.get_length(), color=BLUE))
        # )
        
        filledAngleFromPos.add_updater(
            lambda x: x.become(AnnularSector(inner_radius=0,
                                           outer_radius=line1.get_length(),
                                           angle=(theta_tracker.get_value()*DEGREES),
                                           fill_opacity=0.4,
                                           color=BLUE).shift(LEFT))
        )

        # angleFromNeg.add_updater(
        #     lambda x: x.become(Angle(line1, line_moving, radius=line1.get_length(), other_angle=True, color=RED))
        # )

        
        def get_arc_from_pos():
            if theta_tracker.get_value() >= 360:
                return arcFromPos.become(Circle(radius=0.5, color=BLUE).shift(LEFT))
            else:
                return arcFromPos.become(Angle(line1, line_moving, radius=0.5, color=BLUE, other_angle=False))

        def get_arc_from_neg():
            if theta_tracker.get_value()-360 <= -360:
                return arcFromNeg.become(Circle(radius=0.5, color=RED).shift(LEFT))
            else:
                return arcFromNeg.become(Angle(line1, line_moving, radius=0.5, color=RED, other_angle=True))
            

        filledAngleFromNeg.add_updater(
            lambda x: x.become(AnnularSector(inner_radius=0,
                                           outer_radius=line1.get_length(),
                                           angle=((theta_tracker.get_value()-360)*DEGREES),
                                           fill_opacity=0.4,
                                           color=RED).shift(LEFT) )
        )


        theta.add_updater(
            lambda x: x.move_to(
                Angle(
                    line1, line_moving, radius=0.5 + 3 * SMALL_BUFF, other_angle=False
                ).point_from_proportion(0.5)
            )
        )

        arcFromPos = always_redraw(get_arc_from_pos)
        self.add(filledAngleFromPos)

        self.play(theta_tracker.animate.set_value(110))
        self.wait(2)
        self.play(theta_tracker.animate.set_value(470))
        self.wait(2)
        self.play(theta_tracker.animate.set_value(110))
        # self.wait(2)
        # theta_tracker.set_value(110)
        arcFromNeg = always_redraw(get_arc_from_neg)
        filledAngleFromNeg.update()
        self.add(arcFromNeg, filledAngleFromNeg)
        
        self.remove(arcFromPos, filledAngleFromPos)
        self.wait(2)
        
        self.play(theta_tracker.animate.set_value(-250))
        self.wait(2)
        self.play(theta_tracker.animate.set_value(110))
        # self.play(theta_tracker.animate.set_value(-610))
        # x = r.copy()
                
        # r.rotate_about_origin(140*DEGREES)
        
        # dot = Dot(r.get_end())
        
        # a = Angle(x,r, radius=0.5)
        # angleFromPos = Angle(x,r,radius=r.get_length())
        
        
        # self.add(mfill)
        # self.add(r,x,a,dot,angleFromPos) 

        # TODO: Show revolution count and angle values
        self.wait()
    
x = Winding()
x.render