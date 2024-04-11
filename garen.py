#!/usr/bin/python3

import asyncio
import gettext
# from PySide6.QtWidgets import QApplication
# from PySide6.QtAsyncio import QAsyncioEventLoopPolicy
import signal
import sys

# from app.asynchelper import AsyncHelper
# from app.mainwindow import MainWindow

# binName = 'rotate-video'

# if __name__ == "__main__":
#     gettext.bindtextdomain(binName)

#     app = QApplication(sys.argv)

#     main_window = MainWindow()
#     async_helper = AsyncHelper(main_window, main_window.convert)
#     main_window.show()

#     signal.signal(signal.SIGINT, signal.SIG_DFL)

#     asyncio.set_event_loop_policy(QAsyncioEventLoopPolicy())
#     asyncio.get_event_loop().run_forever()

from app.openvpn.surfshark import surfshark

surfshark()