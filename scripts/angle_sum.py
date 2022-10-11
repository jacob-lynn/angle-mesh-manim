from manim import *
import numpy as np 

class AngleSum(Scene):
    def construct(self):
        
        rotation_center = LEFT

        theta_tracker = ValueTracker(110)
        line1 = Line(LEFT, RIGHT)
        line_moving = Line(LEFT, RIGHT)
        line_ref = line_moving.copy()
        line_moving.rotate(
            theta_tracker.get_value() * DEGREES, about_point=rotation_center
        )

        angleFromPos = Angle(line1,line_moving,radius=line1.get_length(), color=BLUE)
        angleFromNeg = Angle(line1,line_moving,radius=line1.get_length(), other_angle=True, color=RED)
        a = Angle(line1, line_moving, radius=0.5, other_angle=False, color=BLUE)
        b = Angle(line1, line_moving, radius=0.4, other_angle=True, color=RED)
        theta = MathTex(r"\theta", color=BLUE).move_to(
            Angle(
                line1, line_moving, radius=0.5 + 3 * SMALL_BUFF, other_angle=False
            ).point_from_proportion(0.5)
        )

        phi = MathTex(r"\phi", color=RED).move_to(
            Angle(
                line1, line_moving, radius=0.4 + 3 * SMALL_BUFF, other_angle=True
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
                                           angle=((360-theta_tracker.get_value())*-DEGREES),
                                           fill_opacity=0.4,
                                           color=RED).shift(LEFT)                                           

        self.add(filledAngleFromPos, filledAngleFromNeg, line1, line_moving, a, b, theta, phi, angleFromNeg, angleFromPos)
        self.wait()

        line_moving.add_updater(
            lambda x: x.become(line_ref.copy()).rotate(
                theta_tracker.get_value() * DEGREES, about_point=rotation_center
            )
        )
        angleFromPos.add_updater(
            lambda x: x.become(Angle(line1, line_moving, radius=line1.get_length(), color=BLUE))
        )
        
        filledAngleFromPos.add_updater(
            lambda x: x.become(AnnularSector(inner_radius=0,
                                           outer_radius=line1.get_length(),
                                           angle=(theta_tracker.get_value()*DEGREES),
                                           fill_opacity=0.4,
                                           color=BLUE).shift(LEFT))
        )

        angleFromNeg.add_updater(
            lambda x: x.become(Angle(line1, line_moving, radius=line1.get_length(), other_angle=True, color=RED))
        )

        filledAngleFromNeg.add_updater(
            lambda x: x.become(AnnularSector(inner_radius=0,
                                           outer_radius=line1.get_length(),
                                           angle=((360-theta_tracker.get_value())*-DEGREES),
                                           fill_opacity=0.4,
                                           color=RED).shift(LEFT) )
        )

        a.add_updater(
            lambda x: x.become(Angle(line1, line_moving, radius=0.5, other_angle=False, color=BLUE))
        )

        b.add_updater(
            lambda x: x.become(Angle(line1, line_moving, radius=0.4, other_angle=True, color=RED))
        )
        

        theta.add_updater(
            lambda x: x.move_to(
                Angle(
                    line1, line_moving, radius=0.5 + 3 * SMALL_BUFF, other_angle=False
                ).point_from_proportion(0.5)
            )
        )

        phi.add_updater(
            lambda x: x.move_to(
                Angle(
                    line1, line_moving, radius=0.4 + 3 * SMALL_BUFF, other_angle=True
                ).point_from_proportion(0.5)
            )
        )

        
        self.play(theta_tracker.animate.set_value(40))
        self.play(theta_tracker.animate.increment_value(140))
        # self.play(tex.animate.set_color(RED), run_time=0.5)
        self.play(theta_tracker.animate.set_value(320))
        
        # r = Line(ORIGIN, RIGHT*3)
        # x = r.copy()
                
        # r.rotate_about_origin(140*DEGREES)
        
        # dot = Dot(r.get_end())
        
        # a = Angle(x,r, radius=0.5)
        # angleFromPos = Angle(x,r,radius=r.get_length())
        
        
        # self.add(mfill)
        # self.add(r,x,a,dot,angleFromPos) 
        self.wait()
        
        
        
        
x = AngleSum()
x.render