from abc import ABC, abstractmethod
from typing import List, Tuple, Dict, Union

class BaseAnimation(ABC):
    def __init__(self, x_size: int = 14, y_size: int = 28):
        self.x_size = x_size
        self.y_size = y_size

    @abstractmethod
    def get_frame(self) -> List[List[Tuple[int, int, int]]]:
        """
        Generates the next frame and continues the inner state of the animation by a timestep.

        Returns:
            List[List[Tuple[int, int, int]]]: Generated frame.
        """
        pass

    @abstractmethod
    def get_params(self) -> Dict[str, Union[int, float, str]]:
        """
        Returns a dictionary with parameters.
        {
          "FPS": 30,
          "NAME": "MyAnimation",
          "DURATION": 10.0
        }
        """
        return {}

    @abstractmethod
    def reset(self) -> None:
        """
        Resets the aniamtion to its initial state.
        """
        pass
