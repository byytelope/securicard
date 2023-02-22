from InquirerPy import inquirer
from InquirerPy.base.control import Choice


def main() -> None:
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
    # TODO: Implement start
    print("Started")


def configure() -> None:
    # TODO: Implement config
    print("Config")


if __name__ == "__main__":
    main()
