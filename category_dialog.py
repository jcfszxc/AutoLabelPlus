# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'category_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CategoryDialog(object):
    def setupUi(self, CategoryDialog):
        CategoryDialog.setObjectName("CategoryDialog")
        CategoryDialog.resize(300, 400)
        self.verticalLayout = QtWidgets.QVBoxLayout(CategoryDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit = QtWidgets.QLineEdit(CategoryDialog)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.autoLabelCheckBox = QtWidgets.QCheckBox(CategoryDialog)
        self.autoLabelCheckBox.setObjectName("autoLabelCheckBox")
        self.horizontalLayout.addWidget(self.autoLabelCheckBox)
        self.buttonBox = QtWidgets.QDialogButtonBox(CategoryDialog)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayout.addWidget(self.buttonBox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.categoryList = QtWidgets.QListWidget(CategoryDialog)
        self.categoryList.setObjectName("categoryList")
        item = QtWidgets.QListWidgetItem()
        self.categoryList.addItem(item)
        self.verticalLayout.addWidget(self.categoryList)

        self.retranslateUi(CategoryDialog)
        QtCore.QMetaObject.connectSlotsByName(CategoryDialog)

    def retranslateUi(self, CategoryDialog):
        _translate = QtCore.QCoreApplication.translate
        CategoryDialog.setWindowTitle(_translate("CategoryDialog", "AutoLabelPlus"))
        self.autoLabelCheckBox.setText(_translate("CategoryDialog", "Auto Label"))
        __sortingEnabled = self.categoryList.isSortingEnabled()
        self.categoryList.setSortingEnabled(False)
        item = self.categoryList.item(0)
        item.setText(_translate("CategoryDialog", "person"))
        self.categoryList.setSortingEnabled(__sortingEnabled)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CategoryDialog = QtWidgets.QDialog()
    ui = Ui_CategoryDialog()
    ui.setupUi(CategoryDialog)
    CategoryDialog.show()
    sys.exit(app.exec_())