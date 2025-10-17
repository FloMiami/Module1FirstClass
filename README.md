
# 💻 DeviceManager

A Python application that models and manages endpoint devices in an IT environment. This project demonstrates object-oriented programming principles including inheritance, interface abstraction, and reflection. It builds on the base `Device` class by introducing a more advanced `ManagedDevice` class with additional functionality for compliance tracking and technician assignment.

---

## 📁 Project Structure

```
DeviceManager/
├── device.py             # Base class definition for Device
├── device_interface.py   # Abstract interface enforcing print_properties()
├── managed_device.py     # Extended class with added functionality
├── main.py               # Container app that instantiates and interacts with ManagedDevice
└── README.md             # Project overview and instructions
```

---

## 🧠 Class Overview

### 🔹 `Device` (Base Class)
Represents a basic endpoint device with the following properties:
- `name`
- `ip_address`
- `os`
- `location`
- `status`

Includes methods:
- `update_status(new_status)`
- `display_info()`

### 🔹 `ManagedDevice` (Extended Class)
Inherits from `Device` and implements `DeviceInterface`. Adds:
- `compliance_status`
- `technician`

Includes methods:
- `assign_technician(name)`
- `print_properties()` — uses reflection to print all attributes dynamically

### 🔹 `DeviceInterface`
Defines a required method:
- `print_properties()` — ensures consistent property output across device types

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

- Extending a base class using inheritance
- Designing a simple interface to enforce structure
- Using reflection to dynamically print object properties
- Building toward a scalable system for device or compliance management


