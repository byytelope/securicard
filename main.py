from os import system
from datetime import datetime
from time import sleep
from random import choices

from InquirerPy import inquirer
from InquirerPy.base.control import Choice


def main() -> None:
    system("clear")
    print(
        r"""
  _____                      _  _____              _
 / ____|                    (_)/ ____|            | |
| (___   ___  ___ _   _ _ __ _| |     __ _ _ __ __| |
 \___ \ / _ \/ __| | | | '__| | |    / _` | '__/ _` |
 ____) |  __/ (__| |_| | |  | | |___| (_| | | | (_| |
|_____/ \___|\___|\__,_|_|  |_|\_____\__,_|_|  \__,_|
"""
    )
    print("Thank you for using SecuriCard™")

    inquirer.text(message="Company username:").execute()
    inquirer.secret(message="Password for user:").execute()

    menu_action = inquirer.select(
        message="Select an action:",
        choices=[
            Choice(value=0, name="Start server"),
            Choice(value=1, name="Configure SecuriCard™"),
            Choice(value=None, name="Exit"),
        ],
        default=None,
    ).execute()

    match menu_action:
        case 0:
            start_server()
        case 1:
            configure()
        case _:
            exit()


def start_server() -> None:
    show_init = 0

    while True:
        time = datetime.now()
        log_types = ["LOG", "FRD"]
        log_type: str = choices(log_types, weights=(90, 10))[0]
        log_msg = "Sample server log."
        if log_type == "FRD":
            log_msg = "Potential fraud detected and alerted."

        if show_init == 0:
            log_msg = "Starting SecuriCard™ server..."

        log_line = f'{time.strftime("%m/%d/%Y %H:%M:%S")} {log_type}: {log_msg}'
        print(log_line)
        show_init = 1
        sleep(1)


def configure() -> None:
    config_action = inquirer.select(
        message="Select config option:",
        choices=[
            Choice(value=0, name="Set notification endpoint"),
            Choice(value=1, name="Set bank db endpoint"),
            Choice(value=2, name="Manage audit logs"),
        ],
        default=None,
    ).execute()

    match config_action:
        case 0:
            set_notif_endpoint()
        case 1:
            set_bank_db_endpoint()
        case 2:
            manage_audit_logs()
        case _:
            exit()


def set_notif_endpoint() -> None:
    endpoint_action = inquirer.text(
        message="Enter endpoint for notification system:"
    ).execute()

    print(f"Notification endpoint set to: {endpoint_action}")


def set_bank_db_endpoint() -> None:
    endpoint_action = inquirer.text(message="Enter endpoint for bank db:").execute()

    print(f"Bank db endpoint set to: {endpoint_action}")
    print(f"Bank db schema detected and validated")


def manage_audit_logs() -> None:
    endpoint_action = inquirer.select(
        message="Select audit log action",
        choices=[
            Choice(value=0, name="Clear logs"),
            Choice(value=1, name="Re-scan logs"),
            Choice(value=2, name="Mark for review"),
            Choice(value=3, name="Delete logs"),
        ],
    ).execute()

    match endpoint_action:
        case 0:
            print("Logs cleared")
        case 1:
            print("Logs re-scanned")
        case 2:
            print("Admin called for log review")
        case 3:
            print("Logs deleted")
        case _:
            exit()


if __name__ == "__main__":
    main()
