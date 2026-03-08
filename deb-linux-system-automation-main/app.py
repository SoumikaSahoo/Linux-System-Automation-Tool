import subprocess
import psutil
import datetime
import logging
import platform
import time
from colorama import Fore, init

init(autoreset=True)

# Logging setup
logging.basicConfig(
    filename="system_automation.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)


def run_command(command):
    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout

    except subprocess.CalledProcessError as e:
        logging.error(f"Command failed: {' '.join(command)} | Error: {e}")
        return None


def check_package_updates():

    print(Fore.CYAN + "\nChecking for package updates...\n")

    subprocess.run(
        ['sudo', 'apt', 'update'],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

    output = run_command(['apt', 'list', '--upgradable'])

    if output:
        lines = output.splitlines()

        if len(lines) > 1:

            print(Fore.YELLOW + "Available updates:\n")

            for line in lines[1:]:
                print(line)

            logging.info("Package updates available")

        else:
            print(Fore.GREEN + "System already up to date")
            logging.info("System up to date")


def update_packages():

    choice = input("\nUpdate all packages? (y/n): ")

    if choice.lower() == "y":

        print(Fore.CYAN + "\nUpdating packages...\n")

        result = subprocess.run(['sudo', 'apt', 'upgrade', '-y'])

        if result.returncode == 0:

            print(Fore.GREEN + "Packages updated successfully")
            logging.info("Packages upgraded successfully")

        else:

            print(Fore.RED + "Package upgrade failed")
            logging.error("Package upgrade failed")

    else:

        print("Update skipped")


def check_network_connection():

    print(Fore.CYAN + "\nChecking network connectivity...")

    for attempt in range(3):

        result = subprocess.run(
            ['ping', '-c', '1', '8.8.8.8'],
            stdout=subprocess.DEVNULL
        )

        if result.returncode == 0:

            print(Fore.GREEN + "Network connection OK")
            logging.info("Network working")
            return

        else:

            print(Fore.YELLOW + f"Retry {attempt+1}/3...")
            time.sleep(1)

    print(Fore.RED + "Network connection failed")
    logging.error("Network failure detected")


def monitor_system_resources():

    print(Fore.CYAN + "\nSystem Resource Monitoring\n")

    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage('/')

    print(f"CPU Usage   : {cpu}%")
    print(f"RAM Usage   : {memory.percent}%")
    print(f"Disk Usage  : {disk.percent}%")

    if disk.percent > 90:
        print(Fore.RED + "WARNING: Disk space almost full!")

    logging.info(f"CPU:{cpu}% RAM:{memory.percent}% Disk:{disk.percent}%")


def system_information():

    print(Fore.CYAN + "\nSystem Information\n")

    info = platform.uname()

    print(f"System    : {info.system}")
    print(f"Node Name : {info.node}")
    print(f"Release   : {info.release}")
    print(f"Machine   : {info.machine}")
    print(f"CPU Cores : {psutil.cpu_count(logical=True)}")
    print(f"RAM       : {round(psutil.virtual_memory().total / (1024**3),2)} GB")

    logging.info("System information viewed")


def create_system_log():

    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage('/')

    logging.info(
        f"System Log | CPU:{cpu}% RAM:{memory.percent}% Disk:{disk.percent}%"
    )

    print(Fore.GREEN + "System log recorded")


def menu():

    print(Fore.BLUE + "\n===== Linux Automation Tool =====")

    print("1. Check package updates")
    print("2. Update packages")
    print("3. Check network")
    print("4. Monitor system resources")
    print("5. Generate system log")
    print("6. System information")
    print("7. Exit")


def main():

    try:

        while True:

            menu()

            choice = input("\nSelect option: ")

            if choice == "1":
                check_package_updates()

            elif choice == "2":
                update_packages()

            elif choice == "3":
                check_network_connection()

            elif choice == "4":
                monitor_system_resources()

            elif choice == "5":
                create_system_log()

            elif choice == "6":
                system_information()

            elif choice == "7":
                print(Fore.GREEN + "\nExiting automation tool")
                break

            else:
                print(Fore.RED + "Invalid option")

    except KeyboardInterrupt:

        print(Fore.RED + "\nProgram interrupted by user")
        logging.warning("Program interrupted with CTRL+C")


if __name__ == "__main__":
    main()