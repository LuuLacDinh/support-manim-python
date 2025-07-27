from manim import *
from support import *

class E(MovingCameraScene):
    def construct(self):
        self.camera.frame.save_state() #save camera frame
        
        #Main