from modules.base_animation import BaseAnimation

class ExampleAnimation(BaseAnimation):
    def __init__(self, x_size=14, y_size=28):
        super().__init__(x_size, y_size)
        self.frame_count = 0

    def get_frame(self):
        frame = [[(self.frame_count % 256, 
                   (2 * self.frame_count + x) % 256, 
                   (3 * self.frame_count + y) % 256) 
                  for x in range(self.x_size)] for y in range(self.y_size)]
        self.frame_count += 1
        return frame

    def get_params(self):
        return {
            "FPS": 10,
            "NAME": "ExampleAnimation",
            "DURATION": 10.0
        }

    def reset(self):
        self.frame_count = 0
