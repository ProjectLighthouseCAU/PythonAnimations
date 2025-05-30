# PythonAnimations
Python based animations for the Christian Albrecht Universities zu Kiel's Lighthouse Project

## Usage
### Before first run
- Create a virtual environment in this programs root directory with 'python3 -m venv venv'
- Activate the virtual environment with 'source ./venv/bin/activate'
- Install the requirements with 'pip install -r requirements.txt'

### Otherwise
- Activate the virtual environment with 'source ./venv/bin/activate'
- Run the animation with 'python ./python_animations/main.py {TIME} {Optional Parameters}'

## Adding animations
The animations to be imported need to be classes.
Each class needs to provide a 'get_frame()' function, which then generates a frame and then increase
the simulation by a timestep.
The return value of the get_frame function needs to be of the format list[list[tuple[int, int, int]]].  
  
Each class also needs to provide a 'get_params()' function which returns a dictionary with optional parameters:
- "FPS": int | float
  - Allowed range: 1 .. 180
  - Tells the animation controller how fast the animation is to be run. If not provided, a default value is used.
- "NAME": str
  - Tells the animation controller how the animation is named. Needed for useful console output/logging.
- "LENGTH": int | float
  - Unit: Seconds
  - Provides the animation controller with the exact length of the animation. Useful for scrolling texts 
    that have a certain, set length. If not set, a default value from the animation controller will be used.
