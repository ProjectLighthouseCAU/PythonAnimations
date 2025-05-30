from modules.base_animation import BaseAnimation
from modules.timer import Timer
from time import sleep

class AnimationController():
    def __init__(self, animations: list[BaseAnimation] = [], 
                 target_duration: float = 30.0, 
                 speed_multiplier: float = 1.0):
        self.animations: list[BaseAnimation] = animations
        self.target_duration: float          = target_duration
        self.speed_multiplier: float         = speed_multiplier
        self.is_running                      = True

    def _extract_params(self,  animation: BaseAnimation) -> tuple[str, float, float, float]:
        params = animation.get_params()
        name        = str(params.get("NAME", "Unkown Animation"))
        framerate   = max(1.0, min(180, float(params.get("FPS", 30.0))))
        interval    = 1/framerate
        duration    = max(1.0, float(params.get("DURATION", 30.0)))
        return(name, interval, framerate, duration)
    
    def _send_to_lh(self, frame: list[list[tuple[int, int, int]]]) -> None:
        # TODO: Implement
        pass

    def _handle_animation(self, animation: BaseAnimation) -> None:
        name, interval, framerate, duration = self._extract_params(animation)
        print(f"Playing animation {name} for {duration} seconds...")
        stop_after_frames = duration // framerate
        frame_count       = 0
        frame_timer       = Timer(interval)
        while self.is_running and frame_count < stop_after_frames:
            frame = animation.get_frame()
            if not frame or not type(frame) == list[list[tuple[int, int, int]]]: 
                return
            self._send_to_lh(frame)
            sleep(frame_timer.remaining_time())
            frame_timer.reset()

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