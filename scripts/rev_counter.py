from manim import *
import numpy as np 

class RevCounter(Scene):
    def construct(self):
        
        rotation_center = LEFT

        polarplane_pi = PolarPlane(
            azimuth_units="degrees",
            size=5.35,
            azimuth_label_font_size=0.1,
            azimuth_step=12,
            azimuth_direction="CCW",
            radius_config={"font_size":0.1,
                            "stroke_opacity":0.5},
            background_line_style={"stroke_opacity":0.3},
        ).add_coordinates().shift(LEFT)

        theta_tracker = ValueTracker(0.1)
        rev_label = Variable(var=0, label='rev', num_decimal_places=0).next_to(polarplane_pi, UR*0.1)
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
                                           start_angle=-250*DEGREES,
                                           angle=((theta_tracker.get_value()-360)*DEGREES),
                                           fill_opacity=0.4,
                                           color=RED).shift(LEFT)                                           

        self.add(polarplane_pi, line1, line_moving, arcFromPos, line_static, rev_label)
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

        phi.add_updater(
            lambda x: x.move_to(
                Angle(
                    line1, line_moving, radius=0.4 + 3 * SMALL_BUFF, other_angle=True
                ).point_from_proportion(0.5)
            )
        )


        arcFromPos = always_redraw(get_arc_from_pos)
        self.add(filledAngleFromPos)

        self.play(theta_tracker.animate(run_time=2.5).set_value(110))
        self.wait(2)
        self.play(LaggedStart(theta_tracker.animate(run_time=3).set_value(470),
                                rev_label.tracker.animate.set_value(1), lag_ratio=0.5))
                                                                    
        self.wait(2)
        self.play(LaggedStart(theta_tracker.animate(run_time=3).set_value(110),
                                rev_label.tracker.animate.set_value(0), lag_ratio=0.2))
        self.wait(2)
        # theta_tracker.set_value(110)
        arcFromNeg = always_redraw(get_arc_from_neg)
        filledAngleFromNeg.update()
        phi.update()
        self.add(arcFromNeg, filledAngleFromNeg, phi)
        
        self.remove(arcFromPos, filledAngleFromPos, theta)
        self.wait(2)
        
        self.play(LaggedStart(theta_tracker.animate(run_time=3).set_value(-250),
                                rev_label.tracker.animate.set_value(-1), lag_ratio=0.3))
        self.wait(2)
        self.play(LaggedStart(theta_tracker.animate(run_time=3).set_value(110),
                                rev_label.tracker.animate.set_value(0), lag_ratio=0.4))
        
        self.wait()
    
x = RevCounter()
x.render