from modules.base_animation import BaseAnimation
from modules.timer import Timer
from pyghthouse.ph import Pyghthouse
from modules.lh_display import Display
from typing import Sequence
from time import sleep

class AnimationController():
    def __init__(self, animations: Sequence[BaseAnimation] = [], 
                 target_duration: float = 30.0, 
                 speed_multiplier: float = 1.0,
                 fallback_framerate: float = 30.0,
                 local_display: Display | None = None,
                 pyghthouse_adapter: Pyghthouse | None = None):
        self.animations         = animations
        self.target_duration    = target_duration
        self.speed_multiplier   = speed_multiplier
        self.fallback_framerate = fallback_framerate
        self.is_running         = True
        self.pyghthouse_adapter = pyghthouse_adapter
        self.local_display      = local_display

    def _extract_params(self,  animation: BaseAnimation) -> tuple[str, float, float, float]:
        params = animation.get_params()
        name        = str(params.get("NAME", "Unkown Animation"))
        framerate   = max(1.0, min(180, float(params.get("FPS", self.fallback_framerate))))
        interval    = 1/framerate
        duration    = max(1.0, float(params.get("DURATION", self.target_duration)))
        return(name, interval, framerate, duration)
    
    def _send_to_lh(self, frame: list[list[tuple[int, int, int]]]) -> None:
        if self.pyghthouse_adapter:
            self.pyghthouse_adapter.set_image(frame)
        if self.local_display:
            self.local_display.send_frame(frame)

    def _handle_animation(self, animation: BaseAnimation) -> None:
        name, interval, framerate, duration = self._extract_params(animation)
        print(f"Playing animation {name} for {duration} seconds...")
        stop_after_frames = duration // (framerate * self.speed_multiplier)
        frame_count       = 0
        frame_timer       = Timer(interval / self.speed_multiplier)
        while self.is_running and frame_count < stop_after_frames:
            frame = animation.get_frame()
            if not frame: 
                print("Error: No Frame!")
                return
            #if not type(frame) == list[list[tuple[int, int, int]]]:
            #    print(f"Error: Frame has wrong format {type(frame)}")
            #    return
            self._send_to_lh(frame)
            sleep(frame_timer.remaining_time())
            frame_timer.reset()
        sleep(5)

    def _main_loop(self):
        while self.is_running:
            for animation in self.animations:
                self._handle_animation(animation)

    def run(self):
        if self.animations:
            self._main_loop()
        else:
            raise Exception("Error: AnimationController was initialized without animations.") 
        print("Quitting animation controller...")