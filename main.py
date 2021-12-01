from win10toast import ToastNotifier
import time

#runs the script with a self-contained 15 min timer
def activitylooptimer():
    toaster = ToastNotifier()

    x = 0
    while x != 1:
       toaster.show_toast("Do something!", "Time to do something physical right now!")
       time.sleep(900)

#Runs the notification on demand
def activityloop():
    toaster = ToastNotifier()
    toaster.show_toast("Do something!", "Time to do something physical right now!")


if __name__ == '__main__':
    activityloop()