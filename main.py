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

    action = inquirer.select(
        message="Select an action:",
        choices=[
            Choice(value=0, name="Start server"),
            Choice(value=1, name="Configure SecuriCard™"),
            Choice(value=None, name="Exit"),
        ],
        default=None,
    ).execute()

    match action:
        case 0:
            start_server()
        case 1:
            configure()
        case _:
            exit()


def start_server() -> None:
    while True:
        time = datetime.now()
        log_types = ["LOG", "FRD"]
        log_type: str = choices(log_types, weights=(90, 10))[0]
        log_msg = "Sample server log."
        if log_type == "FRD":
            log_msg = "Potential fraud detected. Bank has been alerted successfully."

        log_line = f'{time.strftime("%m/%d/%Y %H:%M:%S")} {log_type}: {log_msg}'
        print(log_line)
        sleep(1)


def configure() -> None:
    config_action = inquirer.select(
        message="Select config option:",
        choices=[
            Choice(value=0, name="Set notification endpoint"),
            Choice(value=1, name="Set bank db endpoint"),
            Choice(value=2, name="Detect db schema"),
            Choice(value=3, name="Delete audit logs"),
        ],
        default=None,
    ).execute()

    match config_action:
        case 0:
            print("Notification endpoint set")
        case 1:
            print("Bank db endpoint set")
        case 2:
            print("Db schema set")
        case 3:
            print("Audit logs deleted")
        case _:
            exit()


if __name__ == "__main__":
    main()
