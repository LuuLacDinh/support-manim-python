from manim import *
from support import *

import numpy as np

class E(MovingCameraScene):
    def construct(self):
        self.camera.frame.save_state() #save camera frame
        
        #Main
        axes = Axes(
            x_range=[-10, 10, 1],
            y_range=[-1, 1, 1],
            axis_config={"color": BLUE},
            x_axis_config={
                "include_tip": False,
                "font_size": 24,
                "numbers_to_include": [-PI, -PI/2, 0, PI/2, PI]
            }
        )
        fun = axes.plot(lambda x: np.sin(x), color=GREEN)
        group = VGroup(axes, fun)
        
        self.play(Create(group), run_time=2)
        self.wait(0.25)
        self.play(ShowPassingFlash(fun, time_width=0.5, run_time=2))
        self.wait()