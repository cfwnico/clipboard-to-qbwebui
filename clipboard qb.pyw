import json
import os
import sys

import qbittorrentapi
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from ui_mainwin import Ui_MainWindow as MainWindow


def error_msgbox(title, text, parent=None):
    QMessageBox(QMessageBox.Warning, title, text, QMessageBox.Ok, parent).exec()


class Config:
    def __init__(self, path: str):
        self.conf_path = path
        if os.path.exists(self.conf_path):
            with open(self.conf_path, "r", encoding="utf-8") as f:
                self.conf_dict = json.load(f)
        else:
            self.create_config()
            with open(self.conf_path, "r", encoding="utf-8") as f:
                self.conf_dict = json.load(f)

    def create_config(self):
        conf_dict = {
            "qb_adress": "127.0.0.1",
            "qb_port": 8080,
            "qb_user_name": "admin",
            "qb_user_pwd": "adminadmin",
            "enable": True,
            "download_msgbox": True,
            "download_notify": True,
        }
        with open(self.conf_path, "w", encoding="utf-8") as f:
            json.dump(conf_dict, f, ensure_ascii=False)

    def save_config(self):
        with open(self.conf_path, "w", encoding="utf-8") as f:
            json.dump(self.conf_dict, f, ensure_ascii=False)


class MainWin(QMainWindow, MainWindow):
    magnet_link_signal = Signal(str)
    login_qb_signal = Signal()

    def __init__(self, config: Config):
        super().__init__()
        self.config = config
        self.setupUi(self)
        self.clipboard = QClipboard()
        self.old_link = ""
        self.setup_tray()
        if self.config.conf_dict["enable"]:
            self.setup_thread()
            self.login_qb_signal.emit()
        else:
            self.user_label.setText("未启用")
        self.tray_ico = QPixmap(r"tray.ico")
        self.msg_ico = QPixmap(r"msg.ico")

    def setup_ui(self, login_states: str):
        if login_states[:12] == "qBittorrent:":
            adress = self.config.conf_dict["qb_adress"] + " "
            text = adress + login_states
            self.adress_label.setText(text)
            self.user_label.setText(self.config.conf_dict["qb_user_name"])
            self.setup_timer()
        else:
            error_msgbox("连接QBwebui错误！请检查config.json设置！", login_states, self)
            app.exit()

    def setup_tray(self):
        self.trayicon = QSystemTrayIcon()
        self.trayicon.setIcon(QIcon(r"tray.ico"))
        self.trayicon.setToolTip("qbwebui推送工具")
        self.context_menu()
        self.trayicon.show()
        self.trayicon.activated.connect(self.iconActivated)

    def setup_thread(self):
        self._thread = QThread(self)
        self.qb_thread = PushQB(self.config)
        self.qb_thread.moveToThread(self._thread)
        self.magnet_link_signal.connect(self.qb_thread.qb_download)
        self.login_qb_signal.connect(self.qb_thread.login_qb)
        self.qb_thread.download_states_signal.connect(self.show_notify)
        self.qb_thread.login_states_signal.connect(self.setup_ui)
        self._thread.start()

    def setup_timer(self):
        self.timer = QTimer(self)
        self.timer.setInterval(500)
        self.timer.timeout.connect(self.auto_check)
        if self.config.conf_dict["enable"]:
            self.timer.start()

    def show_notify(self, result: str):
        if result == "Ok.":
            if self.config.conf_dict["download_notify"]:
                self.trayicon.showMessage(
                    "qB远程推送", "已推送下载" + self.current_link, self.msg_ico
                )
        else:
            self.trayicon.showMessage("qB远程推送", str(result), self.msg_ico)

    def iconActivated(self, reason):
        if reason == QSystemTrayIcon.DoubleClick:
            if self.isHidden():
                self.show()
            else:
                self.hide()

    def auto_check(self):
        self.current_link = self.clipboard.text()
        if self.current_link == self.old_link:
            return
        if len(self.current_link) > 20:
            if self.current_link[:20] == "magnet:?xt=urn:btih:":
                if self.config.conf_dict["download_msgbox"]:
                    replay = self.download_msgbox()
                    if replay == 0:
                        self.magnet_link_signal.emit(self.current_link)
                        item = QListWidgetItem()
                        item.setText(self.current_link)
                        self.magnet_listwidget.addItem(item)
                else:
                    item = QListWidgetItem()
                    item.setText(self.current_link)
                    self.magnet_listwidget.addItem(item)
                    self.magnet_link_signal.emit(self.current_link)
        self.old_link = self.current_link

    def context_menu(self):
        context_menu = QMenu()
        quitapp = QAction("退出", self)
        quitapp.triggered.connect(self.quit_app)
        context_menu.addAction(quitapp)
        self.trayicon.setContextMenu(context_menu)

    def download_msgbox(self):
        msgBOX = QMessageBox()  # 创建一个选择对话框
        msgBOX.setWindowTitle("检测到磁力链接!")
        msgBOX.setIcon(QMessageBox.Question)
        msgBOX.setText("是否将磁力链接推送到QBwebui?")
        _ = msgBOX.addButton("是", QMessageBox.YesRole)
        no = msgBOX.addButton("否", QMessageBox.NoRole)
        msgBOX.setDefaultButton(no)  # 默认为否
        replay = msgBOX.exec()  # 是返回0，否返回1
        return replay

    def quit_app(self):
        app.exit()


class PushQB(QObject):
    login_states_signal = Signal(str)
    download_states_signal = Signal(str)

    def __init__(self, config: Config) -> None:
        super().__init__()
        self.config = config

    def login_qb(self):
        self.qbt_client = qbittorrentapi.Client(
            host=self.config.conf_dict["qb_adress"],
            port=self.config.conf_dict["qb_port"],
            username=self.config.conf_dict["qb_user_name"],
            password=self.config.conf_dict["qb_user_pwd"],
        )
        try:
            self.qbt_client.auth_log_in()
        except Exception as e:
            self.login_states_signal.emit(str(e))
            return
        text = f"qBittorrent: {self.qbt_client.app.version}"
        self.login_states_signal.emit(text)

    def qb_download(self, magnet_link):
        result = self.qbt_client.torrents_add(magnet_link)
        self.download_states_signal.emit(result)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)
    json_path = "config.json"
    config = Config(json_path)
    window = MainWin(config)
    window.show()
    app.exec()
