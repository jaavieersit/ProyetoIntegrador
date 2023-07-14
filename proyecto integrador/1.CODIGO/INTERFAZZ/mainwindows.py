import csv
from PyQt6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox, QMainWindow, QApplication, QFormLayout, QDateEdit
from PyQt6.QtCore import Qt, QDate

class RegistrarWindow(QWidget):
    def __init__(self, login_window):
        super().__init__()
        self.setWindowTitle("Registro de pacientes")
        self.setGeometry(200, 200, 400, 300)

        self.login_window = login_window

        self.registrar_label = QLabel("Registro de pacientes")
        self.registrar_label.setStyleSheet("font-size: 24px; margin-bottom: 20px;")

        self.genero_label = QLabel("Género del paciente:")
        self.edad_label = QLabel("Edad del paciente:")
        self.hipertension_label = QLabel("Hipertensión del paciente (0=NO/1=SI):")
        self.cardiopatia_label = QLabel("Cardiopatía del paciente (0=NO/1=SI):")
        self.historialfumador_label = QLabel("Historial de fumador del paciente (0=NO/1=SI):")
        self.IMC_label = QLabel("IMC del paciente:")
        self.NivelHnA1c_label = QLabel("Nivel de HnA1c:")
        self.glucosa_label = QLabel("Glucosa del paciente:")
        self.diabetes_label = QLabel("Diabetes del paciente (0=NO/1=SI):")

        self.genero_input = QLineEdit()
        self.edad_input = QLineEdit()
        self.hipertension_input = QLineEdit()
        self.cardiopatia_input = QLineEdit()
        self.historialfumador_input = QLineEdit()
        self.IMC_input = QLineEdit()
        self.NivelHnA1c_input = QLineEdit()
        self.glucosa_input = QLineEdit()
        self.diabetes_input = QLineEdit()

        self.añadir_button = QPushButton("Añadir")
        self.añadir_button.clicked.connect(self.registrar_paciente)
        self.añadir_button.setStyleSheet("font-size: 18px; padding: 10px 20px;")

        self.back_button = QPushButton("Volver")
        self.back_button.clicked.connect(self.volver)
        self.back_button.setStyleSheet("font-size: 18px; padding: 10px 20px;")

        self.form_layout = QFormLayout()
        self.form_layout.addRow(self.genero_label, self.genero_input)
        self.form_layout.addRow(self.edad_label, self.edad_input)
        self.form_layout.addRow(self.hipertension_label, self.hipertension_input)
        self.form_layout.addRow(self.cardiopatia_label, self.cardiopatia_input)
        self.form_layout.addRow(self.historialfumador_label, self.historialfumador_input)
        self.form_layout.addRow(self.IMC_label, self.IMC_input)
        self.form_layout.addRow(self.NivelHnA1c_label, self.NivelHnA1c_input)
        self.form_layout.addRow(self.glucosa_label, self.glucosa_input)
        self.form_layout.addRow(self.diabetes_label, self.diabetes_input)
        self.form_layout.addRow(self.añadir_button, self.back_button)

        layout = QVBoxLayout()
        layout.addWidget(self.registrar_label, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addLayout(self.form_layout)
        layout.addStretch()

        self.setLayout(layout)

    def registrar_paciente(self):
        gender = self.genero_input.text()
        age = self.edad_input.text()
        hypertension = self.hipertension_input.text()
        heart_disease = self.cardiopatia_input.text()
        smoking_history = self.historialfumador_input.text()
        bmi = self.IMC_input.text()
        HbA1c_level = self.NivelHnA1c_input.text()
        blood_glucose_level = self.glucosa_input.text()
        diabetes = self.diabetes_input.text()

        with open('Dataset.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([gender, age, hypertension, heart_disease, smoking_history, bmi, HbA1c_level, blood_glucose_level, diabetes])
        #mensaje el cual avisa si el registro fue exitoso
        QMessageBox.information(self, "reistro exitoso", "El paciente ha sido registrado correctamente.")
    
    def volver(self):
        self.login_window.show()
        self.close()    

class MainWindow(QMainWindow):
    def __init__(self): 
        super().__init__()
        self.setWindowTitle("Dataset de Diabetes")
        self.setGeometry(200, 200, 800, 600) 

        self.register_button = QPushButton("Registrar paciente nuevo")
        self.register_button.clicked.connect(self.open_register_window)
        self.register_button.setStyleSheet("font-size: 18px; padding: 10px 20px;")

        layout = QVBoxLayout()
        layout.addSpacing(80)
        layout.addWidget(self.register_button)
        layout.addStretch()

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        self.register_window = None
    
    def open_register_window(self):
        self.register_window = RegistrarWindow(self)
        self.hide()
        self.register_window.show()