import sys
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QPushButton,
    QVBoxLayout,
    QFileDialog,
    QLabel,
)
from PyQt6.QtCore import Qt
from NoPS import process_single, process_folder

class ImageApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("NoPS")
        self.setFixedSize(500,500)
        self.lable = QLabel("select a file or folder to process")
        self.lable.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.btn_file = QPushButton("Process single image")
        self.btn_folder = QPushButton("Process folder")

        self.btn_file.clicked.connect(self.pick_file)
        self.btn_folder.clicked.connect(self.pick_folder)

        layout = QVBoxLayout()
        layout.addWidget(self.lable)
        layout.addWidget(self.btn_file)
        layout.addWidget(self.btn_folder)

        self.setLayout(layout)

    def pick_file(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Select Image",
            "",
            "Images (*.jpg *.jpeg *.png *.webp)"
        )
        if file_path:
            out_path, _ = QFileDialog.getSaveFileName(
                self,
                "save output as",
                "",
                "JPEG(*.jpg)"   
            )
        if out_path:
            try:
                process_single(file_path, out_path)
                set.lable.setText("Image Procesed successfuly!")
            except Exception as e:
                self.label.setText(f"Error: {e}")

    def pick_folder(self):
        folder_path = QFileDialog.getExistingDirectory(
                self,
                "Select Input Folder"
            )
        if folder_path:
            out_folder = QFileDialog.getExistingDirectory(
                self,
                "Select Output Folder"
            )
        if out_folder:
            try:
                process_folder(folder_path, out_folder)
                self.lable.setText("Folder proccessed successfully.")
            except Exception as e:
                self.label.setText(f"Error: {e}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ImageApp()
    window.show()
    sys.exit(app.exec())
    
