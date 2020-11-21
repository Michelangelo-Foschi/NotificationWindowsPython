from win10toast import ToastNotifier

toaster = ToastNotifier()

toaster.show_toast("New Notification!", "Alerting You Right now!", threaded=True, icon_path=None, duration=5)

import time
while toaster.notification_active():
    time.sleep(0.1)
