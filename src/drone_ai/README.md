# 🚁 Drone AI ROS Package

This project is a collaborative effort among students specializing in **AI**, **aeronautics**, **chemistry**, and **environmental monitoring**, aimed at developing a drone system to monitor commercial crops using **autonomous AI models** built on **ROS (Robot Operating System)**.

---

## 📌 Project Purpose

The goal is to build an intelligent drone that can:

- Autonomously fly over crop fields.
- Collect environmental data (e.g., temperature, humidity, chemical presence).
- Provide insights for improving agricultural productivity.
- Assist farmers and agritech industries through real-time monitoring.

---

## 👥 Team Structure

| Name         | Role                        | Specialty                   |
|--------------|-----------------------------|-----------------------------|
| Peter        | AI Developer                | MSc AI (ROS & Computer Vision) |
| Teammate A   | Hardware Designer           | Aeronautical Engineering    |
| Teammate B   | Flight Body Architect       | Aeronautical Engineering    |
| Teammate C   | Environmental Analyst       | Industrial Intern (Agritech) |
| Teammate D   | Chemical Analysis Expert    | Chemistry & Biotech         |

---

## 🛠 Technologies Used

- **ROS Noetic** (on Ubuntu)
- **Python** for AI and control logic
- **Gazebo** (optional) for simulation
- **Git & GitHub** for collaboration
- **Sensor APIs** for real-time data

---

## 📦 ROS Package Structure

```bash
drone_ai/
├── launch/
│   └── drone_ai.launch
├── scripts/
│   └── drone_ai_node.py
├── msg/
│   └── [custom messages if any]
├── CMakeLists.txt
├── package.xml
└── README.md
