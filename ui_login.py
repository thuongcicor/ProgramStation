# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loginlSZqHc.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QTabWidget,
    QTextBrowser, QWidget)
import icons_rc

class Ui_FormLogin(object):
    def setupUi(self, FormLogin):
        if not FormLogin.objectName():
            FormLogin.setObjectName(u"FormLogin")
        FormLogin.resize(752, 359)
        icon = QIcon()
        icon.addFile(u":/ui/Logo Team TEST.png", QSize(), QIcon.Normal, QIcon.Off)
        FormLogin.setWindowIcon(icon)
        self.pushButton_OK = QPushButton(FormLogin)
        self.pushButton_OK.setObjectName(u"pushButton_OK")
        self.pushButton_OK.setGeometry(QRect(80, 270, 101, 41))
        font = QFont()
        font.setPointSize(14)
        self.pushButton_OK.setFont(font)
        self.label = QLabel(FormLogin)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 50, 41, 20))
        font1 = QFont()
        font1.setPointSize(10)
        self.label.setFont(font1)
        self.lineEdit_MSNV = QLineEdit(FormLogin)
        self.lineEdit_MSNV.setObjectName(u"lineEdit_MSNV")
        self.lineEdit_MSNV.setGeometry(QRect(80, 40, 231, 31))
        self.lineEdit_MSNV.setFont(font)
        self.lineEdit_MSNV.setLayoutDirection(Qt.LeftToRight)
        self.lineEdit_MSNV.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(FormLogin)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 110, 51, 20))
        self.label_2.setFont(font1)
        self.lineEdit_LotNo = QLineEdit(FormLogin)
        self.lineEdit_LotNo.setObjectName(u"lineEdit_LotNo")
        self.lineEdit_LotNo.setGeometry(QRect(80, 100, 231, 31))
        self.lineEdit_LotNo.setFont(font)
        self.lineEdit_LotNo.setLayoutDirection(Qt.LeftToRight)
        self.lineEdit_LotNo.setAlignment(Qt.AlignCenter)
        self.label_3 = QLabel(FormLogin)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 190, 51, 41))
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(False)
        self.label_3.setFont(font2)
        self.comboBox_Project = QComboBox(FormLogin)
        self.comboBox_Project.setObjectName(u"comboBox_Project")
        self.comboBox_Project.setGeometry(QRect(80, 190, 231, 41))
        font3 = QFont()
        font3.setPointSize(12)
        self.comboBox_Project.setFont(font3)
        self.pushButton_Cancel = QPushButton(FormLogin)
        self.pushButton_Cancel.setObjectName(u"pushButton_Cancel")
        self.pushButton_Cancel.setGeometry(QRect(210, 270, 101, 41))
        self.pushButton_Cancel.setFont(font)
        self.tabWidget = QTabWidget(FormLogin)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(340, 30, 291, 281))
        self.tabWidget.setFont(font)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.textBrowser_2 = QTextBrowser(self.tab)
        self.textBrowser_2.setObjectName(u"textBrowser_2")
        self.textBrowser_2.setGeometry(QRect(0, 0, 291, 251))
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.textBrowser = QTextBrowser(self.tab_2)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(0, 0, 291, 251))
        self.tabWidget.addTab(self.tab_2, "")
        self.label_4 = QLabel(FormLogin)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(640, 230, 91, 81))
        self.label_4.setPixmap(QPixmap(u":/ui/Logo Team TEST.png"))
        self.label_4.setScaledContents(True)
        self.QRCodecheck = QCheckBox(FormLogin)
        self.QRCodecheck.setObjectName(u"QRCodecheck")
        self.QRCodecheck.setEnabled(True)
        self.QRCodecheck.setGeometry(QRect(80, 150, 81, 16))
        self.QRCodecheck.setFont(font1)
        self.QRCodecheck.setChecked(True)
        self.QRCodecheck.setTristate(False)
        QWidget.setTabOrder(self.lineEdit_MSNV, self.lineEdit_LotNo)
        QWidget.setTabOrder(self.lineEdit_LotNo, self.QRCodecheck)
        QWidget.setTabOrder(self.QRCodecheck, self.comboBox_Project)
        QWidget.setTabOrder(self.comboBox_Project, self.pushButton_OK)
        QWidget.setTabOrder(self.pushButton_OK, self.pushButton_Cancel)
        QWidget.setTabOrder(self.pushButton_Cancel, self.tabWidget)
        QWidget.setTabOrder(self.tabWidget, self.textBrowser)
        QWidget.setTabOrder(self.textBrowser, self.textBrowser_2)

        self.retranslateUi(FormLogin)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(FormLogin)
    # setupUi

    def retranslateUi(self, FormLogin):
        FormLogin.setWindowTitle(QCoreApplication.translate("FormLogin", u"Login", None))
        self.pushButton_OK.setText(QCoreApplication.translate("FormLogin", u"OK", None))
        self.label.setText(QCoreApplication.translate("FormLogin", u"MSNV:", None))
        self.label_2.setText(QCoreApplication.translate("FormLogin", u"LOT NO:", None))
        self.label_3.setText(QCoreApplication.translate("FormLogin", u"Project:", None))
        self.pushButton_Cancel.setText(QCoreApplication.translate("FormLogin", u"Cancel", None))
        self.textBrowser_2.setHtml(QCoreApplication.translate("FormLogin", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'MS Shell Dlg 2'; font-size:16pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2';\">1. Input employee number</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -q"
                        "t-block-indent:0; text-indent:0px; font-family:'MS Shell Dlg 2';\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2';\">2. Scan QRCode LotNo</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'MS Shell Dlg 2';\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2';\">3. Select the program</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'MS Shell Dlg 2';\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS "
                        "Shell Dlg 2';\">4. Press the button &quot;OK&quot; to start</span></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("FormLogin", u"Instruction", None))
        self.textBrowser.setHtml(QCoreApplication.translate("FormLogin", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'MS Shell Dlg 2'; font-size:16pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2';\">1. Nh\u1eadp m\u00e3 s\u1ed1 nh\u00e2n vi\u00ean</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0"
                        "px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'MS Shell Dlg 2';\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2';\">2. Scan QRCode LotNo</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'MS Shell Dlg 2';\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2';\">3. Ch\u1ecdn ch\u01b0\u01a1ng tr\u00ecnh</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'MS Shell Dlg 2';\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-in"
                        "dent:0px;\"><span style=\" font-family:'MS Shell Dlg 2';\">4. Nh\u1ea5n &quot;OK&quot; \u0111\u1ec3 b\u1eaft \u0111\u1ea7u</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'MS Shell Dlg 2';\"><br /></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("FormLogin", u"H\u01b0\u1edbng d\u1eabn", None))
        self.label_4.setText("")
        self.QRCodecheck.setText(QCoreApplication.translate("FormLogin", u"QRCode", None))
    # retranslateUi

