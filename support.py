from manim import *

#Camera Auto Updater
def make_camera_updater(target):
    def updater(mob):
        mob.move_to(target) #camera_updater_<...> = make_camera_updater(<...>)
                            #self.play(self.camera.frame.add_updater(camera_updater_<...>))
    return updater

#def of UpdateFromAlphaFunc -> Chữ Hồn Ma
def updatefromalphafunc(mob, alpha):
    mob.set_y(ORIGIN[1] + alpha * 0.5)
    mob.set_opacity(1 - alpha) #UpdateFromAlphaFunc(VALUE, updatefromalphafunc)