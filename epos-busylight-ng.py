import hid
import time
import argparse

# ======================================================================
# Copyright (c) 2025 suuhm. All Rights Reserved.
# This software is provided "as is", without any warranty of any kind.
# Inspired by excellent work of:
# https://github.com/EthyMoney/Sennheiser-EPOS-USB-BusyLight-Control
# ======================================================================

# Set Vendor ID and Product ID
vendor_id = 5013
product_id = 116 

# Find the HID device
device = None
for dev in hid.enumerate(vendor_id, product_id):
    try:
        # Try to open the device
        device = hid.device()
        device.open(dev['vendor_id'], dev['product_id']) 
        print(f"Device found and opened: Vendor ID: {dev['vendor_id']}, Product ID: {dev['product_id']}")
        break
    except Exception as e:
        print(f"Error opening the device: {e}")
        device = None

if device is not None:
    try:
        def create_color_packet(red, green, blue, light_on=True):
            packet = [
                0x01, 0x12, 0x02,  # Header
                red, green, blue,   # RGB values
                red, green, blue,   # Mirror RGB values
                0x01 if light_on else 0x00,  # Light on/off
            ]
            # Fill the rest of the payload (if necessary)
            packet.extend([0x00] * (64 - len(packet)))  # Fill with zeros up to 64 bytes
            return packet

        # Function to send a packet
        def send_packet(data, description):
            print(f"Sending packet for: {description}")
            print("Packet:", [hex(x) for x in data])
            device.write(data)

        # Function for the speaker (loud / trigger)
        def speaker():
            # High volume packet
            high_volume_packet = [
                0x01, 0x04, 0x06, 0x00, 0x00, 0x00, 0x00, 0x00,
                0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
            ]
          
            trigger_packet = [
                0x01, 0x09, 0x04, 0x01, 0x03, 0x01, 0x00, 0x00,
                0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
            ]

            # Send High Volume Packet
            print("Setting high volume...")
            send_packet(high_volume_packet, "Set High Volume")

            # Send Trigger Packet with delay
            time.sleep(0.5)  # Wait before triggering the sound
            print("Triggering high volume sound...")
            send_packet(trigger_packet, "Trigger High Volume Sound")

        def set_color(color, light_on=True):
            color_map = {
                'red': (0xc0, 0x00, 0x00),
                'green': (0x00, 0xc0, 0x00),
                'blue': (0x00, 0x00, 0xc0),
                'yellow': (0xc0, 0xc0, 0x00),
                'orange': (0xc0, 0x7f, 0x00),
                'purple': (0x80, 0x00, 0x80),
                'cyan': (0x00, 0xc0, 0xc0),
                'white': (0xc0, 0xc0, 0xc0),
                'off': (0x00, 0x00, 0x00)
            }

            if color in color_map:
                red, green, blue = color_map[color]
                color_packet = create_color_packet(red, green, blue, light_on)
                send_packet(color_packet, f"Set {color} color")
            else:
                print(f"Unknown color: {color}")

        # Rainbow effect function
        def rainbow():
            rainbow_colors = [
                ('red', 0xc0, 0x00, 0x00),  # Red
                ('orange', 0xc0, 0x80, 0x00),  # Orange
                ('yellow', 0xc0, 0xc0, 0x00),  # Yellow
                ('green', 0x00, 0xc0, 0x00),  # Green
                ('cyan', 0x00, 0xc0, 0xc0),  # Cyan
                ('blue', 0x00, 0x00, 0xc0),  # Blue
                ('purple', 0x80, 0x00, 0xc0),  # Purple
            ]
            
            while True:
                for color_name, red, green, blue in rainbow_colors:
                    packet = create_color_packet(red, green, blue, light_on=True)
                    print(f"Trying to set LED to {color_name}...")
                    device.write(packet)
                    time.sleep(0.2)

        parser = argparse.ArgumentParser(description='Control LED colors and speaker.')
        parser.add_argument('action', choices=['red', 'green', 'blue', 'yellow', 'orange', 'purple', 'cyan', 'white', 'off', 'rainbow', 'speaker'], 
                            help='Action to perform (LED or Speaker)')
        parser.add_argument('--on', action='store_true', help='Turn LED on (default: off)')

        args = parser.parse_args()

        if args.action == 'speaker':
            speaker()
        elif args.action == 'rainbow':
            rainbow()  
        else:
            set_color(args.action, light_on=args.on)

    except Exception as e:
        print(f"Error sending to the device: {e}")
    finally:
        device.close()
else:
    print("No matching device found.")
