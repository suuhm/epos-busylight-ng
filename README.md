# epos-busylight-ng

![grafik](https://github.com/user-attachments/assets/06080bde-8963-4066-98bc-efa04ef6084b)


python implementation of sennheiser epos connect busylight bl20 with ms-teams status checker beta.  
Inspired by the reverse engeneering of https://github.com/EthyMoney/Sennheiser-EPOS-USB-BusyLight-Control


### ***Works on Windows, Linux and MacOS***

## Overview

This project provides a Python implementation for controlling the Sennheiser EPOS Connect Busylight BL20. It integrates with Microsoft Teams to set the busylight color based on the user's current status in MS Teams.

The busylight is used to indicate the user's status (like available, busy, do not disturb, etc.) through different colors of the light. This integration allows automatic updating of the busylight based on the user's status in MS Teams, providing a visual indicator for others in your environment.

This is a beta release, and some features may be subject to change in future versions.

## Features

- **MS Teams Status Detection (beta):** Automatically detects your status in Microsoft Teams (e.g., Available, Busy, Do Not Disturb).
- **Busylight Color Control:** Changes the color of the EPOS Busylight BL20 based on your MS Teams status:
  - Green for Available
  - Red for Busy / Do Not Disturb
  - Yellow for Away (WIP!)
  - Purple for Custom/Inactive states (WIP!)
- **Speaker Integration:** Can trigger the speaker of the Busylight to play sounds at high volume when certain events occur.
- **Rainbow Mode:** A pulsating rainbow light effect for visual aesthetic.
  
## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/suuhm/epos-busylight-ng.git
   cd epos-busylight-ng
   ```

2. **Install dependencies:**

   Make sure you have Python 3.6+ installed, then install the necessary Python packages:

   ```bash
   pip install -r requirements.txt
   ```

   You'll need the `hid` library for communicating with the Busylight device.

3. **Install Microsoft Teams (Optional):**

   You may need to register a Azure APP for full status access at the moment of Teams Version 2

## Usage

### Command-Line Interface (CLI)

Once the dependencies are installed, you can run the program using the following commands:

- **Set the LED color to a specific state:**

   ```bash
   python epos-busylight-ng.py [color] [--on]
   ```

   Supported colors:
   - `red`
   - `green`
   - `blue`
   - `yellow`
   - `orange`
   - `purple`
   - `cyan`
   - `white`
   - `off`
   - `rainbow`

   Example: To set the light to "green" for Available status:

   ```bash
   python epos-busylight-ng.py green --on
   ```

- **Trigger the speaker (high volume sound):**

   ```bash
   python epos-busylight-ng.py speaker
   ```

   This will trigger the high volume sound from the Busylight device.

- **Activate Rainbow effect:**

   ```bash
   python epos-busylight-ng.py rainbow
   ```

   This will start a pulsating rainbow effect on the Busylight.

# Integrating with Microsoft Teams (Beta)

- The script checks your MS Teams status and adjusts the Busylight color automatically based on your current status. For this to work, ensure you have configured the necessary integrations to get the MS Teams status.

## Example Usage

```bash
python teams2busylight.py
```

You can set up your light to follow your MS Teams status by running the script in Background.


## Requirements

- Python 3.6+
- `hid` library (for controlling the Busylight)
- `psutil`
- `pygetwindow`


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Feel free to modify this according to your specific project needs!
