# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'programV22mJGHcm.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPlainTextEdit,
    QProgressBar, QPushButton, QSizePolicy, QTabWidget,
    QTextBrowser, QWidget)
import icons_rc

class Ui_FormProgram(object):
    def setupUi(self, FormProgram):
        if not FormProgram.objectName():
            FormProgram.setObjectName(u"FormProgram")
        FormProgram.setEnabled(True)
        FormProgram.resize(758, 494)
        icon = QIcon()
        icon.addFile(u":/ui/Logo Team TEST.png", QSize(), QIcon.Normal, QIcon.Off)
        FormProgram.setWindowIcon(icon)
        self.lineEdit_QRCode = QLineEdit(FormProgram)
        self.lineEdit_QRCode.setObjectName(u"lineEdit_QRCode")
        self.lineEdit_QRCode.setEnabled(True)
        self.lineEdit_QRCode.setGeometry(QRect(40, 60, 231, 31))
        font = QFont()
        font.setPointSize(14)
        self.lineEdit_QRCode.setFont(font)
        self.lineEdit_QRCode.setAlignment(Qt.AlignCenter)
        self.label = QLabel(FormProgram)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(41, 31, 61, 31))
        font1 = QFont()
        font1.setPointSize(10)
        self.label.setFont(font1)
        self.pushButton_Program = QPushButton(FormProgram)
        self.pushButton_Program.setObjectName(u"pushButton_Program")
        self.pushButton_Program.setGeometry(QRect(40, 130, 231, 51))
        font2 = QFont()
        font2.setPointSize(16)
        self.pushButton_Program.setFont(font2)
        self.pushButton_Result = QPushButton(FormProgram)
        self.pushButton_Result.setObjectName(u"pushButton_Result")
        self.pushButton_Result.setEnabled(False)
        self.pushButton_Result.setGeometry(QRect(40, 210, 231, 81))
        font3 = QFont()
        font3.setPointSize(20)
        self.pushButton_Result.setFont(font3)
        self.progressBar = QProgressBar(FormProgram)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(40, 430, 601, 31))
        font4 = QFont()
        font4.setPointSize(12)
        self.progressBar.setFont(font4)
        self.progressBar.setValue(0)
        self.progressBar.setAlignment(Qt.AlignCenter)
        self.tabWidget = QTabWidget(FormProgram)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(310, 50, 331, 351))
        self.tabWidget.setFont(font)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.textBrowser_2 = QTextBrowser(self.tab)
        self.textBrowser_2.setObjectName(u"textBrowser_2")
        self.textBrowser_2.setGeometry(QRect(0, 0, 331, 321))
        self.textBrowser_2.setFont(font)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.textBrowser = QTextBrowser(self.tab_2)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(0, 0, 331, 321))
        self.textBrowser.setFont(font)
        self.tabWidget.addTab(self.tab_2, "")
        self.label_Project = QLabel(FormProgram)
        self.label_Project.setObjectName(u"label_Project")
        self.label_Project.setGeometry(QRect(40, 100, 231, 20))
        self.label_Project.setFont(font1)
        self.label_2 = QLabel(FormProgram)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(650, 320, 91, 81))
        self.label_2.setPixmap(QPixmap(u":/ui/Logo Team TEST.png"))
        self.label_2.setScaledContents(True)
        self.plainTextResult = QPlainTextEdit(FormProgram)
        self.plainTextResult.setObjectName(u"plainTextResult")
        self.plainTextResult.setGeometry(QRect(40, 310, 231, 91))
        QWidget.setTabOrder(self.lineEdit_QRCode, self.pushButton_Program)
        QWidget.setTabOrder(self.pushButton_Program, self.plainTextResult)
        QWidget.setTabOrder(self.plainTextResult, self.tabWidget)
        QWidget.setTabOrder(self.tabWidget, self.textBrowser)
        QWidget.setTabOrder(self.textBrowser, self.pushButton_Result)
        QWidget.setTabOrder(self.pushButton_Result, self.textBrowser_2)

        self.retranslateUi(FormProgram)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(FormProgram)
    # setupUi

    def retranslateUi(self, FormProgram):
        FormProgram.setWindowTitle(QCoreApplication.translate("FormProgram", u"Program", None))
        self.label.setText(QCoreApplication.translate("FormProgram", u"QRCode:", None))
        self.pushButton_Program.setText(QCoreApplication.translate("FormProgram", u"PROGRAM", None))
        self.pushButton_Result.setText(QCoreApplication.translate("FormProgram", u"RESULT", None))
        self.progressBar.setFormat(QCoreApplication.translate("FormProgram", u"%p%", None))
        self.textBrowser_2.setHtml(QCoreApplication.translate("FormProgram", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'MS Shell Dlg 2';\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2';\">1. Scan QRCode DUT</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text"
                        "-indent:0px; font-family:'MS Shell Dlg 2';\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2';\">2. Put on DUT into the fixture</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'MS Shell Dlg 2';\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2';\">3. Close the fixture</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'MS Shell Dlg 2';\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2';"
                        "\">4. Press the button &quot;PROGRAM&quot;</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'MS Shell Dlg 2';\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2';\">5. Waiting for the result PASS/ FAIL</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'MS Shell Dlg 2';\"><br /></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("FormProgram", u"Instruction", None))
        self.textBrowser.setHtml(QCoreApplication.translate("FormProgram", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'MS Shell Dlg 2';\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2';\">1. Scan QRCode board m\u1ea1ch</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-in"
                        "dent:0; text-indent:0px; font-family:'MS Shell Dlg 2';\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2';\">2. \u0110\u1eb7t board m\u1ea1ch v\u00e0o g\u00e1 test</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'MS Shell Dlg 2';\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2';\">3. \u0110\u00f3ng g\u00e1</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'MS Shell Dlg 2';\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><sp"
                        "an style=\" font-family:'MS Shell Dlg 2';\">4. Nh\u1ea5n n\u00fat &quot;PROGRAM&quot;</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'MS Shell Dlg 2';\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2';\">5. \u0110\u1ee3i k\u1ebft qu\u1ea3 PASS/ FAIL</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'MS Shell Dlg 2';\"><br /></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("FormProgram", u"H\u01b0\u1edbng d\u1eabn", None))
        self.label_Project.setText(QCoreApplication.translate("FormProgram", u"Project", None))
        self.label_2.setText("")
        self.plainTextResult.setPlainText("")
    # retranslateUi

