# deva.rover.system
Object-oriented Python controller for an autonomous obstacle-avoiding robot rover, featuring hardware abstraction layers compatible with Raspberry Pi and Webots 3D simulations. 


# 🤖 Automatic Obstacle-Avoiding Robot Controller

An object-oriented, production-ready Python controller designed for an autonomous robotic rover. Built on the core principles of the robotics pipeline—**Sense, Think, Decide, and Act**—this software utilizes hardware abstraction, making it seamlessly compatible with both physical hardware (Raspberry Pi & HC-SR04) and 3D virtual simulators like Webots.

---

## 📊 System Architecture Overview

The flow diagram below represents the real-time decision-making matrix executed by the robot's brain to avoid obstacles and navigate autonomously:

```mermaid
graph TD
    %% Styling
    classDef startEnd fill:#f9f,stroke:#333,stroke-width:2px;
    classDef process fill:#bbf,stroke:#333,stroke-width:1px;
    classDef condition fill:#ff9,stroke:#333,stroke-width:2px;
    
    START([Start System]) --> INIT[Initialize Motors & Ultrasonic Sensor]
    INIT --> READ[Read Sensor Distance]
    READ --> CHECK{Is Distance < 20cm?}
    
    %% No Obstacle Path
    CHECK -- NO --> FORWARD[Drive Straight: Left & Right Motors at Forward Speed]
    FORWARD --> WAIT_FWD[Wait 0.5 Seconds]
    WAIT_FWD --> READ
    
    %% Obstacle Path
    CHECK -- YES --> STOP[Trigger Stop Command: Stop All Motors]
    STOP --> WAIT_STOP[Pause for 0.5 Seconds for Stabilization]
    WAIT_STOP --> TURN[Trigger Turn Left Command: Pivot Wheel Speeds]
    TURN --> WAIT_TURN[Maintain Turn for 1.0 Second]
    WAIT_TURN --> READ

    class START startEnd;
    class CHECK condition;
    class INIT,READ,FORWARD,WAIT_FWD,STOP,WAIT_STOP,TURN,WAIT_TURN process;
```

---

## 🛠️ Software Structure

As the autonomous security features scale, the project follows a clean, modular object-oriented directory structure:

```text
robot_project/
│
├── sensors/            # Handles raw distance sensor feeds
│   └── ultrasonic.py
├── motors/             # Hardware abstraction layer for motor drivers
│   └── motor_controller.py
├── navigation/         # Core obstacle avoidance & routing logic
│   └── obstacle_avoidance.py
├── vision/             # Future expansion: OpenCV human detection
│   └── camera.py
├── config/             # Threshold configurations and pin mappings
│   └── settings.py
└── main.py             # Main entry point to boot the robot controller
```

---

## 🚀 Key Features

* **Hardware Abstraction:** The core decision logic (`class Robot`) remains completely independent of the environment, ensuring quick adaptation between simulation and real-world microcontrollers.
* **Sense-Think-Decide-Act Loop:** Continuous evaluation of sensor inputs with precise timing loops to minimize physical hardware strain.
* **Fail-Safe Mechanism:** Instant wheel stabilization and stop triggers upon detecting tight-boundary breaches.

---

## 📂 Source Code
The complete functional object-oriented script logic can be found directly in the [`deva.robotic.py`](./deva.robotic.py) file within this repository.
