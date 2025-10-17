# Module1FirstClass



---

# 💻 DeviceManager

A simple Python application that models endpoint devices in a university IT environment. This project demonstrates core object-oriented programming principles and serves as a foundation for future automation, inventory tracking, or compliance auditing.

---

## 📁 Project Structure

```
DeviceManager/
├── device.py       # Base class definition for Device
├── main.py         # Container app that instantiates and interacts with Device
└── README.md       # Project overview and instructions
```

---

## 🧠 About the `Device` Class

The `Device` class represents a managed endpoint (like a laptop or desktop) in an enterprise or academic setting. It includes:

### 🔑 Properties:
- `name`: Device name or hostname  
- `ip_address`: Network IP address  
- `os`: Operating system  
- `location`: Physical or logical location  
- `status`: Operational status (e.g., Active, Maintenance)

### ⚙️ Methods:
- `update_status(new_status)`: Updates the device’s status  
- `display_info()`: Prints all device details to the console

---

## 🚀 How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/DeviceManager.git
   cd DeviceManager
   ```

2. Run the container app:
   ```bash
   python main.py
   ```

---

## 🎯 Course Alignment


- Defining a custom object (`Device`) with five properties and two methods  
- Using a container app to instantiate and interact with the object  
- Demonstrating clean code principles and modular design

---


