class RoverController:
    """Turns distance readings into left and right wheel commands.

    Wheel commands are normalized:
        -1.0 = full speed backward
         0.0 = stopped
         1.0 = full speed forward
    """

    def __init__(
        self,
        obstacle_distance_cm=25.0,
        turn_seconds=0.5,
        forward_speed=0.55,
        turn_speed=0.50,
    ):
        self.obstacle_distance_cm = obstacle_distance_cm
        self.turn_seconds = turn_seconds
        self.forward_speed = forward_speed
        self.turn_speed = turn_speed

        self._turn_remaining = 0.0
        self._turn_command = (0.0, 0.0)
        self._turn_right_next = True

    def update(self, distance_cm, dt_seconds):
        """Return (left_wheel, right_wheel) commands for this time step.

        A missing/invalid reading is treated as unsafe, so the rover stops.
        """
        if distance_cm is None:
            self._turn_remaining = 0.0
            return (0.0, 0.0)

        # Continue a turn already in progress.
        if self._turn_remaining > 0.0:
            self._turn_remaining = max(
                0.0, self._turn_remaining - dt_seconds
            )
            return self._turn_command

        # Begin a new turn if an obstacle is too close.
        if distance_cm <= self.obstacle_distance_cm:
            if self._turn_right_next:
                # Pivot right: left wheel forward, right wheel backward.
                self._turn_command = (
                    self.turn_speed,
                    -self.turn_speed,
                )
            else:
                # Pivot left: left wheel backward, right wheel forward.
                self._turn_command = (
                    -self.turn_speed,
                    self.turn_speed,
                )

            self._turn_right_next = not self._turn_right_next
            self._turn_remaining = self.turn_seconds
            return self._turn_command

        # No obstacle close enough: drive forward.
        return (self.forward_speed, self.forward_speed)
    
# --- main driver code (start writing from the extreme left, leavin no empty spaces) ---
if __name__ == "__main__":
    # 1. i created a robot object from the RoverController class
    my_rover = RoverController()
    
    # 2. a list of some hypothetical distances from the sensor (Simulation Data)
    test_distances = [50.0, 40.0, 20.0, 15.0, 35.0] 
    time_step = 0.1 # the time for each step (in seconds)
    
    print("--- DEVANIX ROVER SIMULATION START ---")
    
    for distance in test_distances:
        # i called the robot's update function to get the wheel speeds
        left_wheel, right_wheel = my_rover.update(distance, time_step)
        
        print(f"sensor distance: {distance} cm ->  {left_wheel},  {right_wheel}")
