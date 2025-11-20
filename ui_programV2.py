# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'programV2JraiEn.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QPlainTextEdit, QProgressBar, QPushButton, QSizePolicy,
    QTabWidget, QTextBrowser, QVBoxLayout, QWidget)
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
        self.verticalLayout = QVBoxLayout(FormProgram)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.main_widget = QWidget(FormProgram)
        self.main_widget.setObjectName(u"main_widget")
        self.horizontalLayout = QHBoxLayout(self.main_widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.program_widget = QWidget(self.main_widget)
        self.program_widget.setObjectName(u"program_widget")
        self.verticalLayout_6 = QVBoxLayout(self.program_widget)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label = QLabel(self.program_widget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(10)
        self.label.setFont(font)

        self.verticalLayout_6.addWidget(self.label)

        self.lineEdit_QRCode = QLineEdit(self.program_widget)
        self.lineEdit_QRCode.setObjectName(u"lineEdit_QRCode")
        self.lineEdit_QRCode.setEnabled(True)
        font1 = QFont()
        font1.setPointSize(14)
        self.lineEdit_QRCode.setFont(font1)
        self.lineEdit_QRCode.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.lineEdit_QRCode)

        self.label_Project = QLabel(self.program_widget)
        self.label_Project.setObjectName(u"label_Project")
        self.label_Project.setFont(font)

        self.verticalLayout_6.addWidget(self.label_Project)

        self.pushButton_Program = QPushButton(self.program_widget)
        self.pushButton_Program.setObjectName(u"pushButton_Program")
        font2 = QFont()
        font2.setPointSize(16)
        self.pushButton_Program.setFont(font2)

        self.verticalLayout_6.addWidget(self.pushButton_Program)

        self.pushButton_Result = QPushButton(self.program_widget)
        self.pushButton_Result.setObjectName(u"pushButton_Result")
        self.pushButton_Result.setEnabled(False)
        font3 = QFont()
        font3.setPointSize(20)
        self.pushButton_Result.setFont(font3)

        self.verticalLayout_6.addWidget(self.pushButton_Result)

        self.plainTextResult = QPlainTextEdit(self.program_widget)
        self.plainTextResult.setObjectName(u"plainTextResult")

        self.verticalLayout_6.addWidget(self.plainTextResult)


        self.horizontalLayout.addWidget(self.program_widget)

        self.instruction_widget = QWidget(self.main_widget)
        self.instruction_widget.setObjectName(u"instruction_widget")
        self.verticalLayout_3 = QVBoxLayout(self.instruction_widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.tabWidget = QTabWidget(self.instruction_widget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setFont(font1)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.textBrowser_2 = QTextBrowser(self.tab)
        self.textBrowser_2.setObjectName(u"textBrowser_2")
        self.textBrowser_2.setGeometry(QRect(0, 0, 331, 321))
        self.textBrowser_2.setFont(font1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.textBrowser = QTextBrowser(self.tab_2)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(0, 0, 331, 321))
        self.textBrowser.setFont(font1)
        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout_3.addWidget(self.tabWidget)


        self.horizontalLayout.addWidget(self.instruction_widget)

        self.logo_widget = QWidget(self.main_widget)
        self.logo_widget.setObjectName(u"logo_widget")
        self.verticalLayout_5 = QVBoxLayout(self.logo_widget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_3 = QLabel(self.logo_widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setPixmap(QPixmap(u":/ui/Logo Team TEST.png"))
        self.label_3.setScaledContents(True)

        self.verticalLayout_5.addWidget(self.label_3, 0, Qt.AlignVCenter)


        self.horizontalLayout.addWidget(self.logo_widget)


        self.verticalLayout.addWidget(self.main_widget)

        self.processbar_widget = QWidget(FormProgram)
        self.processbar_widget.setObjectName(u"processbar_widget")
        self.verticalLayout_4 = QVBoxLayout(self.processbar_widget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.progressBar = QProgressBar(self.processbar_widget)
        self.progressBar.setObjectName(u"progressBar")
        font4 = QFont()
        font4.setPointSize(12)
        self.progressBar.setFont(font4)
        self.progressBar.setValue(0)
        self.progressBar.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.progressBar)


        self.verticalLayout.addWidget(self.processbar_widget)


        self.retranslateUi(FormProgram)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(FormProgram)
    # setupUi

    def retranslateUi(self, FormProgram):
        FormProgram.setWindowTitle(QCoreApplication.translate("FormProgram", u"Program", None))
        self.label.setText(QCoreApplication.translate("FormProgram", u"QRCode:", None))
        self.label_Project.setText(QCoreApplication.translate("FormProgram", u"Project", None))
        self.pushButton_Program.setText(QCoreApplication.translate("FormProgram", u"PROGRAM", None))
        self.pushButton_Result.setText(QCoreApplication.translate("FormProgram", u"RESULT", None))
        self.plainTextResult.setPlainText("")
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
        self.label_3.setText("")
        self.progressBar.setFormat(QCoreApplication.translate("FormProgram", u"%p%", None))
    # retranslateUi

