# PushTerm: Simplifying 3D Print Removal for Bambu Lab X1 Carbon 🖨️

![PushTerm](https://img.shields.io/badge/PushTerm-Python-blue.svg) ![GitHub Release](https://img.shields.io/badge/release-v1.0.0-orange.svg) ![3D Printing](https://img.shields.io/badge/topic-3D%20Printing-green.svg)

Welcome to the **PushTerm** repository! This Python command-line tool enhances the G-code for the Bambu Lab X1 Carbon 3D printer. By adding push-off commands, it ensures that your toolhead ejects prints after a cooldown delay. This feature helps you avoid extra hardware and simplifies the print removal process while protecting your printer.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Support](#support)

## Features 🌟

- **Easy Print Removal**: Automatically ejects prints after cooling, making it easy to remove them.
- **No Extra Hardware Needed**: Avoids the need for additional tools or modifications to your printer.
- **Customizable G-code**: Modify the G-code as per your requirements.
- **Open Source**: Contribute to the project and improve it for everyone.

## Installation ⚙️

To get started with PushTerm, you need to install it on your system. Follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/diomib/PushTerm.git
   cd PushTerm
   ```

2. **Install Required Packages**:
   Ensure you have Python installed. You can install the required packages using pip:
   ```bash
   pip install -r requirements.txt
   ```

3. **Download the Latest Release**:
   Visit the [Releases section](https://github.com/diomib/PushTerm/releases) to download the latest version. Follow the instructions provided there to execute the downloaded file.

## Usage 🛠️

Using PushTerm is straightforward. Here’s how to modify your G-code:

1. **Prepare Your G-code File**: 
   Make sure you have your G-code file ready for modification.

2. **Run PushTerm**:
   Execute the following command in your terminal:
   ```bash
   python pushterm.py path/to/your/file.gcode
   ```

3. **Check the Output**:
   After running the command, your modified G-code file will be ready. You can find it in the same directory.

4. **Load the Modified G-code**:
   Load the modified G-code file into your Bambu Lab X1 Carbon printer and start your print.

5. **Enjoy Hassle-Free Print Removal**: 
   After printing, the toolhead will automatically eject the print after the cooldown delay.

## Contributing 🤝

We welcome contributions to PushTerm! If you want to help improve the tool, follow these steps:

1. **Fork the Repository**: Click on the fork button at the top right corner of the repository page.
2. **Create a Branch**: Create a new branch for your feature or bug fix.
   ```bash
   git checkout -b feature/YourFeature
   ```
3. **Make Changes**: Implement your changes and commit them.
   ```bash
   git commit -m "Add your message here"
   ```
4. **Push to Your Branch**:
   ```bash
   git push origin feature/YourFeature
   ```
5. **Create a Pull Request**: Go to the original repository and create a pull request.

## License 📄

PushTerm is licensed under the MIT License. Feel free to use, modify, and distribute the code as you see fit.

## Support 💬

If you have any questions or issues, please check the [Releases section](https://github.com/diomib/PushTerm/releases) for troubleshooting tips. You can also open an issue in the repository, and we will be happy to help.

## Topics

- **3D Printing**: Enhance your 3D printing experience with PushTerm.
- **Automation**: Automate print removal to save time and effort.
- **Bambu Lab**: Specifically designed for the Bambu Lab X1 Carbon.
- **CNC**: Useful for CNC operations related to 3D printing.
- **Command-Line Tool**: A straightforward command-line interface for easy use.
- **G-code**: Modify G-code files with ease.
- **Open Source**: Contribute to an open-source project.
- **Printer Scripting**: Script your printer's behavior.
- **Python**: Built using Python for ease of use and flexibility.
- **Toolhead Control**: Gain better control over your printer's toolhead.

## Conclusion

PushTerm is designed to make your 3D printing experience smoother and more efficient. By automating print removal, it saves you time and protects your printer. Download the latest release from the [Releases section](https://github.com/diomib/PushTerm/releases) and start enjoying hassle-free printing today!

![3D Printing](https://images.unsplash.com/photo-1585429720134-52c1c5e40c0b) 

Happy printing!