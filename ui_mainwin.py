# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwinKjGrxb.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QHBoxLayout,
    QLabel, QListWidget, QListWidgetItem, QMainWindow,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(700, 500)
        MainWindow.setMinimumSize(QSize(700, 500))
        font = QFont()
        font.setPointSize(12)
        MainWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u"tray.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.magnet_listwidget = QListWidget(self.groupBox)
        self.magnet_listwidget.setObjectName(u"magnet_listwidget")
        self.magnet_listwidget.setFont(font)
        self.magnet_listwidget.setWordWrap(True)

        self.verticalLayout.addWidget(self.magnet_listwidget)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.adress_label = QLabel(self.groupBox)
        self.adress_label.setObjectName(u"adress_label")

        self.horizontalLayout.addWidget(self.adress_label)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.user_label = QLabel(self.groupBox)
        self.user_label.setObjectName(u"user_label")

        self.horizontalLayout.addWidget(self.user_label)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"QBWebUi\u63a8\u9001\u5de5\u5177", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u63a8\u9001\u5386\u53f2", None))
        self.adress_label.setText(QCoreApplication.translate("MainWindow", u"QBWebUi\u63a8\u9001\u5de5\u5177", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Ver 0.1 ", None))
        self.user_label.setText(QCoreApplication.translate("MainWindow", u"\u767b\u5f55\u4e2d...", None))
    # retranslateUi

