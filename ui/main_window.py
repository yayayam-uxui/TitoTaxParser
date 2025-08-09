import os
from pathlib import Path
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QFileDialog,
    QLabel, QTableWidget, QTableWidgetItem, QMessageBox
)
from .styles import apply_styles
from modules import file_manager, exporter, ocr, parser
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("TitoTax Parser — Select • Parse • Export")
        self.folder = None
        self.files = []

        apply_styles(self)

        # UI
        self.path_label = QLabel("No folder selected")
        self.path_label.setObjectName("pathLabel")

        pick_btn = QPushButton("Choose Folder")
        pick_btn.clicked.connect(self.choose_folder)

        refresh_btn = QPushButton("Refresh")
        refresh_btn.clicked.connect(self.refresh_files)
        refresh_btn.setEnabled(False)
        self.refresh_btn = refresh_btn

        process_btn = QPushButton("Process → Excel")
        process_btn.clicked.connect(self.process_to_excel)
        process_btn.setEnabled(False)
        self.process_btn = process_btn

        top = QHBoxLayout()
        top.addWidget(self.path_label, stretch=1)
        top.addWidget(pick_btn)
        top.addWidget(refresh_btn)
        top.addWidget(process_btn)

        table = QTableWidget(0, 2)
        table.setHorizontalHeaderLabels(["File", "Type"])
        table.horizontalHeader().setStretchLastSection(True)
        self.table = table

        layout = QVBoxLayout()
        layout.addLayout(top)
        layout.addWidget(self.table)
        self.setLayout(layout)
        self.resize(900, 520)

    def choose_folder(self):
        folder = QFileDialog.getExistingDirectory(self, "Select a client folder")
        if not folder:
            return
        self.folder = Path(folder)
        self.path_label.setText(str(self.folder))
        self.refresh_btn.setEnabled(True)
        self.process_btn.setEnabled(True)
        self.refresh_files()

    def refresh_files(self):
        if not self.folder:
            return
        self.files = file_manager.list_supported_files(self.folder)
        self.table.setRowCount(0)
        for f in self.files:
            row = self.table.rowCount()
            self.table.insertRow(row)
            self.table.setItem(row, 0, QTableWidgetItem(str(f.relative_to(self.folder))))
            self.table.setItem(row, 1, QTableWidgetItem(file_manager.detect_type(f)))

    def process_to_excel(self):
        if not self.files:
            QMessageBox.warning(self, "No files", "No supported files found in this folder.")
            return
        try:
            # 1) OCR / read
            extracted = ocr.extract_batch(self.files)

            # 2) Parse to a normalized schema (stub rules for now)
            rows = parser.parse_extracted(extracted)

            # 3) Export to Excel next to the folder (data/export.xlsx)
            out_path = exporter.export_rows_to_excel(rows, base_folder=self.folder)
            QMessageBox.information(self, "Done", f"Exported to:\n{out_path}")
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))
