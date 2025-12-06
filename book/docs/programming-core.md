---
title: Core Programming for Humanoids
---

```markdown
# Chapter 3: Core Programming for Humanoids: Movement and Perception

**Learning Objectives:**

*   Understand the fundamental concepts of controlling humanoid movement using code.
*   Learn how to process sensor data (simulated) for environmental awareness.
*   Implement basic walking gaits and obstacle avoidance algorithms.
*   Gain experience in integrating movement and perception for simple tasks.

## 3.1 Introduction to Humanoid Control

Programming a humanoid robot requires understanding how to translate high-level commands (e.g., "walk forward", "turn left") into low-level motor commands. This chapter focuses on simulating these principles without delving into the complexities of real-world hardware. We will use simple mathematical models and Python code to control a simulated humanoid.

## 3.2 Basic Movement: Joint Control and Gait Cycles

Humanoid movement is achieved by controlling the angles of individual joints. A 'gait cycle' refers to the repetitive sequence of movements required for walking or running.  We'll start with a simplified gait where we alternate lifting and moving each leg.

```python
# Simplified Gait Cycle Example (Python)

def move_joint(joint_name, angle_degrees):
    """Simulates moving a joint to a specified angle."""
    print(f"Moving joint {joint_name} to {angle_degrees} degrees")
    # In a real robot, this would send a command to the motor controlling the joint.

def walk_forward_step():
    """Simulates one step forward."""
    print("--- Taking a step ---")
    move_joint("Left Hip", 10)  # Lift left leg slightly
    move_joint("Left Knee", -20) # Bend left knee
    move_joint("Right Hip", -5)  # Move right leg slightly back
    move_joint("Right Knee", 5)  # Straighten right knee a bit
    # ... (More joint movements for balance and forward motion)
    print("Step completed.")

# Example usage:
for _ in range(3): # Take three steps
    walk_forward_step()
```

This is a very basic example. Real gaits involve complex coordination of multiple joints to maintain balance and stability.

## 3.3 Perception: Simulated Sensors and Data Processing

Humanoids need to perceive their environment to navigate and interact with it. We'll simulate sensors to provide data that our robot can process.

```python
# Simulated Sensor Data Example

def get_distance_reading(sensor_name):
    """Simulates a distance sensor reading."""
    # In a real robot, this would read the data from the sensor.
    # Here, we simulate it with a random value.
    import random
    distance = random.randint(50, 200) # Distance in cm, range 50-200
    print(f"Sensor {sensor_name} reading: {distance} cm")
    return distance

def check_for_obstacle():
  """Uses sensor data to detect obstacles."""
  distance = get_distance_reading("Front Distance Sensor")
  if distance < 80: # Obstacle detected if closer than 80cm
      print("Obstacle detected! Stopping.")
      return True
  else:
      print("No obstacle detected.")
      return False

# Example Usage:
if check_for_obstacle():
  # Implement obstacle avoidance behavior (e.g., turn away)
  print("Initiating obstacle avoidance...")
else:
  print("Continuing forward movement.")
```

This example shows how to simulate a distance sensor and use its data to detect obstacles. In reality, robots use a variety of sensors, such as cameras, lidar, and sonar, and employ sophisticated algorithms to process the data.

## 3.4 Simple Obstacle Avoidance

Combining movement and perception allows for simple obstacle avoidance.

```python
# Obstacle Avoidance Example

def turn_left():
  """Simulates turning the robot left."""
  print("Turning left...")
  move_joint("Left Hip", -5) # Adjust hip angles to turn
  move_joint("Right Hip", 5)
  # ... (Other joint adjustments for turning)
  print("Turn completed.")


def main_loop():
    """Main loop for controlling the humanoid."""
    while True: # Run indefinitely (or until stopped)
        if check_for_obstacle():
            turn_left()
        else:
            walk_forward_step()
        # time.sleep(1) # Simulate a delay between steps (optional)

# Start the main loop (uncomment to run)
# main_loop()
```

This code combines obstacle detection with a turning action to avoid obstacles.  A real-world implementation would require more complex path planning and control algorithms.

**Key Takeaways:**

*   Humanoid control involves coordinating joint movements to achieve desired actions.
*   Gait cycles are repetitive patterns of movement for locomotion.
*   Sensors provide data about the environment, enabling perception and decision-making.
*   Integrating movement and perception is crucial for autonomous behavior.
*   The examples presented are simplified simulations, and real-world humanoid control is significantly more complex.
```
