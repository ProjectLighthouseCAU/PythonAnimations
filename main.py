import sys
from os import getenv
from modules.controller import AnimationController
from pyghthouse.ph import Pyghthouse
from modules.lh_display import Display

def main(gui: bool, remote: bool, fps: int, time_per_anim: int):
    user = getenv("LIGHTHOUSE_USER", None)
    token = getenv("LIGHTHOUSE_TOKEN", None)
    if remote and not (user and token):
        # TODO: Load user and token from file if not present as environment variables
        pass    
    
    animations = [] 
    # TODO: Implement fetching/import of animations. Maybe use files for configuration?
    
    display = None
    if gui:
        display = Display(fps)
        pass
    
    pyghthouse = None
    if remote and user and token:
        pyghthouse = Pyghthouse(user, token, frame_rate=fps)
        pyghthouse.start()
    
    controller = AnimationController(animations=animations,
                                     target_duration=time_per_anim,
                                     speed_multiplier=1.0,
                                     fallback_framerate=fps,
                                     local_display=display,
                                     pyghthouse_adapter=pyghthouse)
    controller.run()
    
    if pyghthouse:
        pyghthouse.stop()
        
    if display:
        display.stop()


def print_usage():
        print(f"Usage:\n{sys.argv[0]} [TIME] [OPTIONS]")
        print("Whereas [TIME] = time in seconds and possible options are:")
        print("--local\tRuns with local GUI only\n--gui\tRuns with both local GUI and remove connection")
        print("--fps=x\tRuns with x fps (default=60)")
    
    
if __name__ == "__main__":
    if len(sys.argv) > 1:
        time_per_anim = int(sys.argv[1])
        gui = False
        remote = True
        fps = 60
        for argument in sys.argv:
            if '--local' in argument:
                gui = True
                remote = False
            elif '--gui' in argument:
                gui = True
            elif '--fps=' in argument and len(argument) > 6 and str(argument).split('=')[1].isnumeric():
                fps = int(str(argument).split('=')[1])
        main(gui, remote, fps, time_per_anim)
    else:
        print_usage()