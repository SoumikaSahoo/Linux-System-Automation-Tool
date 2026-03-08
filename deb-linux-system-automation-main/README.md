# deb-linux-system-automation

Collection of Python and Bash scripts designed to automate common system administration tasks in Debian-based Linux distributions (e.g., Ubuntu, Linux Mint, and others).

## Overview

This repository contains a set of automation scripts created to simplify system administration tasks on Debian-based Linux distributions.

The automation scripts perform the following tasks:

- **Check for System Updates:** Verify if there are available package updates for the system.
- **Upgrade System Packages:** Optionally upgrade system packages to the latest versions.
- **Test Network Connection:** Verify network connectivity by pinging a specified host.

## Why Use This Automation?

Performing system updates, package upgrades, and network checks manually can be time-consuming. This automation allows you to execute these tasks with a single command, saving time and effort. It's especially useful for ensuring that your Debian-based Linux system is up-to-date and maintaining reliable network connectivity. I will be adding more scripts soon!

## Usage

### Prerequisites

- Ensure you have Python installed on your Debian-based Linux distribution.
- Make sure you have administrative privileges (`sudo` access) for executing system update and upgrade commands.

### Steps to Run the Automation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/deb-linux-system-automation.git

2. **Go to the repository directory:**
   ```bash
   cd deb-linux-system-automation
   
3. **Run the script:**
   ```
   python3 app.py
