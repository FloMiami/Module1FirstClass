class Device:
    def __init__(self, name, ip_address, os, location, status):
        self.name = name
        self.ip_address = ip_address
        self.os = os
        self.location = location
        self.status = status

    def update_status(self, new_status):
        self.status = new_status
        print(f"Status updated to: {self.status}")

    def display_info(self):
        print("Device Information:")
        print(f"Name: {self.name}")
        print(f"IP Address: {self.ip_address}")
        print(f"Operating System: {self.os}")
        print(f"Location: {self.location}")
        print(f"Status: {self.status}")