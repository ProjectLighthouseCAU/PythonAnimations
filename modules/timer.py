import time

class Timer():
    def __init__(self, duration: float = 1.0):
        self.duration = duration
        self.start_time = time.monotonic()  # monotonic für Zeitmessung ohne Probleme durch Systemzeit-Änderungen

    def has_expired(self) -> bool:
        """
        Checks if the timer has expired.

        Returns:
            bool: true when expired
        """
        return (time.monotonic() - self.start_time) >= self.duration

    def reset(self) -> None:
        """
        Resets the timer and returns 
        """
        self.start_time = time.monotonic()
        
    def remaining_time(self) -> float:
        """
        Returns the remaining time in seconds.

        Returns:
            float: Remaining time
        """
        return max(0.0, time.monotonic() - self.start_time)
        
    def reset_if_expired(self) -> bool:
        """
        Checks if the timer has expired and resets it in that case.

        Returns:
            bool: true when expired
        """
        expired = (time.monotonic() - self.start_time) >= self.duration
        if expired: self.start_time = time.monotonic()
        return expired