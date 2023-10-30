from PySide2.QtWidgets import QApplication, QMainWindow, QMessageBox, QAction, QFileDialog
from PySide2.QtGui import *
from PySide2.QtCore import *
import sys
import os
from main import Ui_MainWindow
from BinProcessor import BinaryKonfigFileProcessor, BinaryDataProcessor, DataProcessor, DataExporter

class MyFileBrowser(QMainWindow):
    def __init__(self):
        super(MyFileBrowser,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("DOSConvertor")
        self.initGui()
        
        self.show()


    def initGui(self):
        self.CreateAction()

    def CreateAction(self):
        self.ui.Process_data_btn.setEnabled(False)
        self.ui.actionAboutQt.triggered.connect(self.aboutHelp)
        self.ui.actionLoadKFG.triggered.connect(self.ShowdialogKFG)
        self.ui.actionLoad.triggered.connect(self.ShowdialogData)

        self.ui.btn_load_KFG.clicked.connect(self.ShowdialogKFG)
        self.ui.btn_Load_data.clicked.connect(self.ShowdialogData)
        self.ui.btn_Save.clicked.connect(self.saveFile)

        self.ui.actionSave.triggered.connect(self.saveFile)
        self.ui.SaveData.textChanged.connect(self.check_lineedit)
        self.ui.Process_data_btn.clicked.connect(self.DataProcessing)

    def msgApp(self, title, msg):
        userinfo = QMessageBox.question(self, title, msg, QMessageBox.Yes  | QMessageBox.No)

        if userinfo == QMessageBox.Yes:
            return "Y"
        if userinfo == QMessageBox.No:
            return "N"
        self.close() 
    
    def aboutHelp(self):
        QMessageBox.about(self, "Simple convertor of binary files",
        "This editor can convert REF files to LW6 files")

    

    def ShowdialogKFG(self):
        try:
            self.fileNameKFG,_ = QFileDialog.getOpenFileName(self, "Open KFG File", "c:/")
            self.ui.LoadEditKFG.setText(self.fileNameKFG)
            self.config_file_processor = BinaryKonfigFileProcessor(self.fileNameKFG)
            if not self.fileNameKFG:
                return
        except:
            pass

    def ShowdialogData(self):
        try:
            self.folder_path = QFileDialog.getExistingDirectory(self, "Select Folder", "c:/",)
            self.ui.LoadData.setText(self.folder_path)
            self.bin_data_processor = BinaryDataProcessor(self.folder_path)
            if not self.folder_path:
                return
        except:
            pass

    def saveFile(self):
        try:
            self.Save_folder_path = QFileDialog.getExistingDirectory(self, "Select Directory")
            self.ui.SaveData.setText(self.Save_folder_path)

            if not self.Save_folder_path:
                return

            if self.Save_folder_path:
                # Specify the file path where you want to save your data
                self.Save_file_path = self.Save_folder_path + '/LW6.txt'
        except:
            pass

    def check_lineedit(self):
        # Enable the button if the QLineEdit is not empty, otherwise disable it
        if self.ui.SaveData.text():
            self.ui.Process_data_btn.setEnabled(True)
        else:
            self.ui.Process_data_btn.setEnabled(False)      

    def DataProcessing(self):
        self.combined_array = self.bin_data_processor.process_files()
        data_processor = DataProcessor(self.combined_array, self.config_file_processor.temperature_cal, self.bin_data_processor.Zeitschift, self.bin_data_processor.n_mess)
        self.result_matrix = data_processor.process_combined_array()
        
        if self.ui.CycleTime.text() != "":
            self.tcyc = int(self.ui.CycleTime.text())
        else: self.tcyc = None

        if self.ui.Sel_Cycle.text() != "":
            self.num_cycle = int(self.ui.Sel_Cycle.text())
        else: self.num_cycle = None
            
        self.data_Exporter = DataExporter(self.result_matrix, self.bin_data_processor.n_LW, self.tcyc, self.num_cycle)

    # Specify the file path and save the data
        self.data_Exporter.save_data(self.Save_file_path)
        
                    

# Main Function
if __name__ == '__main__':
# Exception Handling
    try:
        myApp = QApplication(sys.argv)
        myWindow = MyFileBrowser()
        myApp.exec_()
        sys.exit(0)
    except NameError:
        print("Name Error:", sys.exc_info()[1])
    except SystemExit:
        print("Closing Window...")
    except Exception:
        print(sys.exc_info()[1])

