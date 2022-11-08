#region config

import sys
import os

if(__name__ == "__main__"):

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))
#endregion config

from classes.CreateMessages import CreateMessages as NewMessage

def main():
    limit = 0

    try:
        limit = int(input("Number of messages to repeat: "))
    except:
        print("The limit must be a natural number")
        limit = int(input("Number of messages to repeat: "))
    finally:
        if (limit < 1):
            prevLimit = limit
            limit = 1
            print(f"Limit: {prevLimit} -> {limit}",
                    "\nLimits must be greater than 0")

    message = input("Message: ")

    myMessages = NewMessage(limit, message)
    myMessages.spam()


if __name__ == "__main__":
    main()