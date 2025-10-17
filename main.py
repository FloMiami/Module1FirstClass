from device import Device

# Create a device instance
laptop = Device(
    name="Faculty-Laptop-01",
    ip_address="192.168.1.45",
    os="Windows 11 Pro",
    location="Lewis Hall 204",
    status="Active"
)

# Display device info
laptop.display_info()

# Update status
laptop.update_status("Under Maintenance")