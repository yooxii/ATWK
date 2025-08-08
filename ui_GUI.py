# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'GUISYPYXj.ui'
##
## Created by: Qt User Interface Compiler version 6.8.3
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
from PySide6.QtWidgets import (QApplication, QButtonGroup, QCheckBox, QComboBox,
    QDialog, QHBoxLayout, QLabel, QLayout,
    QLineEdit, QPushButton, QRadioButton, QSizePolicy,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(640, 480)
        Dialog.setMinimumSize(QSize(640, 480))
        self.verticalLayoutWidget = QWidget(Dialog)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(50, 30, 531, 441))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_model = QLabel(self.verticalLayoutWidget)
        self.label_model.setObjectName(u"label_model")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_model.sizePolicy().hasHeightForWidth())
        self.label_model.setSizePolicy(sizePolicy)
        self.label_model.setMinimumSize(QSize(60, 30))

        self.horizontalLayout_5.addWidget(self.label_model)

        self.model_name = QComboBox(self.verticalLayoutWidget)
        self.model_name.setObjectName(u"model_name")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.model_name.sizePolicy().hasHeightForWidth())
        self.model_name.setSizePolicy(sizePolicy1)
        self.model_name.setMinimumSize(QSize(150, 0))
        self.model_name.setEditable(True)

        self.horizontalLayout_5.addWidget(self.model_name)


        self.horizontalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_class = QLabel(self.verticalLayoutWidget)
        self.label_class.setObjectName(u"label_class")
        sizePolicy.setHeightForWidth(self.label_class.sizePolicy().hasHeightForWidth())
        self.label_class.setSizePolicy(sizePolicy)
        self.label_class.setMinimumSize(QSize(60, 30))

        self.horizontalLayout_3.addWidget(self.label_class)

        self.class_a = QRadioButton(self.verticalLayoutWidget)
        self.classbtns = QButtonGroup(Dialog)
        self.classbtns.setObjectName(u"classbtns")
        self.classbtns.addButton(self.class_a)
        self.class_a.setObjectName(u"class_a")
        self.class_a.setMinimumSize(QSize(0, 30))
        self.class_a.setChecked(True)

        self.horizontalLayout_3.addWidget(self.class_a)

        self.class_b = QRadioButton(self.verticalLayoutWidget)
        self.classbtns.addButton(self.class_b)
        self.class_b.setObjectName(u"class_b")
        self.class_b.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_3.addWidget(self.class_b)


        self.horizontalLayout.addLayout(self.horizontalLayout_3)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_method = QLabel(self.verticalLayoutWidget)
        self.label_method.setObjectName(u"label_method")
        sizePolicy.setHeightForWidth(self.label_method.sizePolicy().hasHeightForWidth())
        self.label_method.setSizePolicy(sizePolicy)
        self.label_method.setMinimumSize(QSize(60, 30))

        self.horizontalLayout_2.addWidget(self.label_method)

        self.power_load_uut = QRadioButton(self.verticalLayoutWidget)
        self.methodbtns = QButtonGroup(Dialog)
        self.methodbtns.setObjectName(u"methodbtns")
        self.methodbtns.addButton(self.power_load_uut)
        self.power_load_uut.setObjectName(u"power_load_uut")
        self.power_load_uut.setMinimumSize(QSize(0, 30))
        self.power_load_uut.setCheckable(True)
        self.power_load_uut.setChecked(True)

        self.horizontalLayout_2.addWidget(self.power_load_uut)

        self.load_power_uut = QRadioButton(self.verticalLayoutWidget)
        self.methodbtns.addButton(self.load_power_uut)
        self.load_power_uut.setObjectName(u"load_power_uut")
        self.load_power_uut.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_2.addWidget(self.load_power_uut)

        self.power_uut_load = QRadioButton(self.verticalLayoutWidget)
        self.methodbtns.addButton(self.power_uut_load)
        self.power_uut_load.setObjectName(u"power_uut_load")
        self.power_uut_load.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_2.addWidget(self.power_uut_load)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_power = QLabel(self.verticalLayoutWidget)
        self.label_power.setObjectName(u"label_power")
        sizePolicy.setHeightForWidth(self.label_power.sizePolicy().hasHeightForWidth())
        self.label_power.setSizePolicy(sizePolicy)
        self.label_power.setMinimumSize(QSize(60, 30))

        self.horizontalLayout_6.addWidget(self.label_power)

        self.power_110V = QCheckBox(self.verticalLayoutWidget)
        self.power_110V.setObjectName(u"power_110V")
        self.power_110V.setChecked(True)
        self.power_110V.setTristate(False)

        self.horizontalLayout_6.addWidget(self.power_110V)

        self.power_220V = QCheckBox(self.verticalLayoutWidget)
        self.power_220V.setObjectName(u"power_220V")
        self.power_220V.setChecked(True)

        self.horizontalLayout_6.addWidget(self.power_220V)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.label_lisn = QLabel(self.verticalLayoutWidget)
        self.label_lisn.setObjectName(u"label_lisn")
        sizePolicy1.setHeightForWidth(self.label_lisn.sizePolicy().hasHeightForWidth())
        self.label_lisn.setSizePolicy(sizePolicy1)

        self.horizontalLayout_7.addWidget(self.label_lisn)

        self.lisn_l = QCheckBox(self.verticalLayoutWidget)
        self.lisn_l.setObjectName(u"lisn_l")
        self.lisn_l.setChecked(True)

        self.horizontalLayout_7.addWidget(self.lisn_l)

        self.lisn_n = QCheckBox(self.verticalLayoutWidget)
        self.lisn_n.setObjectName(u"lisn_n")
        self.lisn_n.setChecked(True)

        self.horizontalLayout_7.addWidget(self.lisn_n)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_7)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout_12.addWidget(self.label)

        self.pathEdit = QLineEdit(self.verticalLayoutWidget)
        self.pathEdit.setObjectName(u"pathEdit")
        self.pathEdit.setMinimumSize(QSize(0, 25))

        self.horizontalLayout_12.addWidget(self.pathEdit)

        self.btnSavepath = QPushButton(self.verticalLayoutWidget)
        self.btnSavepath.setObjectName(u"btnSavepath")
        self.btnSavepath.setMinimumSize(QSize(0, 25))

        self.horizontalLayout_12.addWidget(self.btnSavepath)


        self.verticalLayout.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_sn = QLabel(self.verticalLayoutWidget)
        self.label_sn.setObjectName(u"label_sn")
        sizePolicy.setHeightForWidth(self.label_sn.sizePolicy().hasHeightForWidth())
        self.label_sn.setSizePolicy(sizePolicy)
        self.label_sn.setMinimumSize(QSize(60, 30))

        self.horizontalLayout_9.addWidget(self.label_sn)

        self.sn = QTextEdit(self.verticalLayoutWidget)
        self.sn.setObjectName(u"sn")
        self.sn.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.sn.sizePolicy().hasHeightForWidth())
        self.sn.setSizePolicy(sizePolicy2)
        self.sn.setMinimumSize(QSize(0, 90))
        self.sn.setMaximumSize(QSize(16777215, 90))
        self.sn.setSizeIncrement(QSize(0, 90))
        self.sn.setBaseSize(QSize(0, 90))

        self.horizontalLayout_9.addWidget(self.sn)


        self.verticalLayout.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_load = QLabel(self.verticalLayoutWidget)
        self.label_load.setObjectName(u"label_load")
        sizePolicy.setHeightForWidth(self.label_load.sizePolicy().hasHeightForWidth())
        self.label_load.setSizePolicy(sizePolicy)
        self.label_load.setMinimumSize(QSize(60, 30))

        self.horizontalLayout_8.addWidget(self.label_load)

        self.load = QLineEdit(self.verticalLayoutWidget)
        self.load.setObjectName(u"load")
        self.load.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_8.addWidget(self.load)


        self.verticalLayout.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_exclude = QLabel(self.verticalLayoutWidget)
        self.label_exclude.setObjectName(u"label_exclude")
        sizePolicy.setHeightForWidth(self.label_exclude.sizePolicy().hasHeightForWidth())
        self.label_exclude.setSizePolicy(sizePolicy)
        self.label_exclude.setMinimumSize(QSize(60, 30))

        self.horizontalLayout_10.addWidget(self.label_exclude)

        self.exclude_items = QTextEdit(self.verticalLayoutWidget)
        self.exclude_items.setObjectName(u"exclude_items")
        self.exclude_items.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.exclude_items.sizePolicy().hasHeightForWidth())
        self.exclude_items.setSizePolicy(sizePolicy2)
        self.exclude_items.setMinimumSize(QSize(0, 90))
        self.exclude_items.setMaximumSize(QSize(16777215, 90))
        self.exclude_items.setSizeIncrement(QSize(0, 90))
        self.exclude_items.setBaseSize(QSize(0, 90))

        self.horizontalLayout_10.addWidget(self.exclude_items)


        self.verticalLayout.addLayout(self.horizontalLayout_10)

        self.horizontalWidget = QWidget(self.verticalLayoutWidget)
        self.horizontalWidget.setObjectName(u"horizontalWidget")
        self.horizontalLayout_11 = QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.btn_start = QPushButton(self.horizontalWidget)
        self.btn_start.setObjectName(u"btn_start")
        self.btn_start.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.btn_start.sizePolicy().hasHeightForWidth())
        self.btn_start.setSizePolicy(sizePolicy2)
        self.btn_start.setMinimumSize(QSize(0, 30))
        self.btn_start.setMaximumSize(QSize(80, 30))

        self.horizontalLayout_11.addWidget(self.btn_start)

        self.btn_quit = QPushButton(self.horizontalWidget)
        self.btn_quit.setObjectName(u"btn_quit")
        self.btn_quit.setMinimumSize(QSize(0, 30))
        self.btn_quit.setMaximumSize(QSize(80, 30))

        self.horizontalLayout_11.addWidget(self.btn_quit)


        self.verticalLayout.addWidget(self.horizontalWidget)


        self.retranslateUi(Dialog)
        self.btn_quit.clicked.connect(Dialog.close)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"ELEKTRA_AutoTest", None))
        self.label_model.setText(QCoreApplication.translate("Dialog", u"\u673a\u79cd\u540d\u79f0\uff1a", None))
        self.label_class.setText(QCoreApplication.translate("Dialog", u"\u6d4b\u8bd5\u7c7b\u578b\uff1a", None))
        self.class_a.setText(QCoreApplication.translate("Dialog", u"Class A", None))
        self.class_b.setText(QCoreApplication.translate("Dialog", u"Class B", None))
        self.label_method.setText(QCoreApplication.translate("Dialog", u"\u6d4b\u8bd5\u65b9\u6cd5\uff1a", None))
        self.power_load_uut.setText(QCoreApplication.translate("Dialog", u"\u7535\u538b>\u8d1f\u8f7d>\u5355\u4f53", None))
        self.load_power_uut.setText(QCoreApplication.translate("Dialog", u"\u8d1f\u8f7d>\u7535\u538b>\u5355\u4f53", None))
        self.power_uut_load.setText(QCoreApplication.translate("Dialog", u"\u7535\u538b>\u5355\u4f53>\u8d1f\u8f7d", None))
        self.label_power.setText(QCoreApplication.translate("Dialog", u"\u8f93\u5165\u7535\u538b\uff1a", None))
        self.power_110V.setText(QCoreApplication.translate("Dialog", u"110V", None))
        self.power_220V.setText(QCoreApplication.translate("Dialog", u"220V", None))
        self.label_lisn.setText(QCoreApplication.translate("Dialog", u"LISN:", None))
        self.lisn_l.setText(QCoreApplication.translate("Dialog", u"L", None))
        self.lisn_n.setText(QCoreApplication.translate("Dialog", u"N", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u4fdd\u5b58\u4f4d\u7f6e\uff1a", None))
        self.btnSavepath.setText(QCoreApplication.translate("Dialog", u"\u6d4f\u89c8", None))
        self.label_sn.setText(QCoreApplication.translate("Dialog", u"\u5e8f\u5217\u53f7\uff1a", None))
        self.label_load.setText(QCoreApplication.translate("Dialog", u"\u8d1f\u8f7d\uff1a", None))
        self.label_exclude.setText(QCoreApplication.translate("Dialog", u"\u6392\u9664\u9879\u76ee\uff1a", None))
        self.btn_start.setText(QCoreApplication.translate("Dialog", u"\u5f00\u59cb", None))
        self.btn_quit.setText(QCoreApplication.translate("Dialog", u"\u9000\u51fa", None))
    # retranslateUi

