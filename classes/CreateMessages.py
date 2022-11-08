import pyautogui as spam
import time


class CreateMessages:
    def __init__(self, limit: int, message: str) -> None:
        self.sleepNumber = 5
        self.limit = limit
        self.message = message

    def spam(self) -> None:
        i = 0
        time.sleep(self.sleepNumber)

        while (i < self.limit):
            spam.typewrite(message=self.message)
            spam.press("Enter")
            i += 1

        print("Success")
