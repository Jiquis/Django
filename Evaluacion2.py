import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class Main(QMainWindow):
    def __init__(self, parent=None, *args):
        super(Main, self).__init__(parent=parent)
        self.radio_buttons()       
        self.creacion_objetos()
        self.CrearImagenes()
        
    def creacion_objetos(self):
        self.setFixedSize(900, 600)
        self.setWindowTitle("Evaluacion Unidad 2")

        label = QLabel("Evaluacion segunda unidad Graficación \n Operacion de Escalacion, traslacion y rotacion", self)
        lblNombre = QLabel("Covarrubias Rosales Luis Humberto-20212393", self)
        label.setGeometry(0, 0, 900, 200)
        label.setStyleSheet("background:#424242; color:fff")
        fuente = label.font()
        fuenteNombre = lblNombre.font()
        fuente.setPointSize(28)
        fuenteNombre.setPointSize(10)
        fuente.setBold(True)
        fuenteNombre.setBold(True)
        label.setFont(fuente)
        lblNombre.setFont(fuenteNombre)
        label.setAlignment(Qt.AlignCenter)
        lblNombre.setGeometry(0, 570, 400, 30)
    ########################################### CREACION DE LOS BOTONES ####################################
        btnCrear = QPushButton('Crear', self)
        btnCrear.setGeometry(30, 485, 160, 30)
        btnLimpiar = QPushButton('Limpiar', self)
        btnLimpiar.setGeometry(200, 485, 160, 30)
        btnRotacion = QPushButton('Rotacion', self)
        btnRotacion.setGeometry(370, 485, 160, 30)
        btnTraslacion = QPushButton('Traslacion', self)
        btnTraslacion.setGeometry(540, 485, 160, 30)
        btnEscalacion = QPushButton('Escalacion', self)
        btnEscalacion.setGeometry(710, 485, 160, 30)
        btnSalir = QPushButton('Salir', self)
        btnSalir.setGeometry(30, 525, 840, 30)
        ########################################### FUNCION DE LOS BOTONES ####################################
        btnCrear.clicked.connect(self.on_btn_crear_click)
        btnSalir.clicked.connect(self.on_btn_salir_click)
        btnLimpiar.clicked.connect(self.limpiar_imagen_principal)
        btnRotacion.clicked.connect(self.rotar_imagen_principal)
        btnTraslacion.clicked.connect(self.trasladar_imagen_principal)
        btnEscalacion.clicked.connect(self.escalar_imagen_principal)
    
    def radio_buttons(self):
        ########################################### CREACION DE LOS RADIOBUTTONS ####################################
        self.cbxTriangulo = QRadioButton("Triangulo", self)
        self.cbxTriangulo.setGeometry(100, 200, 100, 100)
        self.cbxCuadrado = QRadioButton("Cuadrado", self)
        self.cbxCuadrado.setGeometry(100, 250, 100, 100)
        self.cbxPentagono = QRadioButton("Pentagono", self)
        self.cbxPentagono.setGeometry(100, 300, 100, 100)
        self.cbxImagen1 = QRadioButton("Imagen1", self)
        self.cbxImagen1.setGeometry(100, 350, 100, 100) 
        self.cbxImagen2 = QRadioButton("Imagen2", self)
        self.cbxImagen2.setGeometry(100, 400, 100, 100) 
            
        self.ButtonGroup = QButtonGroup(self)
        self.ButtonGroup.addButton(self.cbxTriangulo)
        self.ButtonGroup.addButton(self.cbxCuadrado)
        self.ButtonGroup.addButton(self.cbxPentagono)
        self.ButtonGroup.addButton(self.cbxImagen1)
        self.ButtonGroup.addButton(self.cbxImagen2)
        self.ButtonGroup.buttonClicked.connect(self.on_button_clicked)
        ########################################### CREACION DE LA IMAGEN PRINCIPAL ####################################
        self.imgPrincipal = QLabel(self)
        self.imgPrincipal.setGeometry(450, 250, 200, 200)
        self.imgPrincipal.setScaledContents(True)
        self.imgPrincipal.setStyleSheet('border: 2px solid black;')

        self.actualizar_imagen_principal()

    def CrearImagenes(self):
        ########################################### IMPLEMENTAN LAS IMAGENES ALADO DE LOS RADIOBUTTONS ####################################
        self.crear_label_imagen(25, 243, '/Users/luisa/OneDrive/Pictures/Triangulo.png')
        self.crear_label_imagen(25, 293, '/Users/luisa/OneDrive/Pictures/Cuadrado.png')
        self.crear_label_imagen(25, 343, '/Users/luisa/OneDrive/Pictures/Pentagono.png')
        self.crear_label_imagen(25, 393, '/Users/luisa/OneDrive/Pictures/Cristiano.jpg')
        self.crear_label_imagen(25, 443, '/Users/luisa/OneDrive/Pictures/Messi.jfif')

    def crear_label_imagen(self, x, y, ruta):
        label = QLabel(self)
        pixmap = QPixmap(ruta)
        label.setPixmap(pixmap)
        label.setGeometry(x, y, 40, 40)
        label.setScaledContents(True)
        label.setStyleSheet('border: 2px solid black;')

    def on_button_clicked(self, button):
        print(f"Botón clickeado: {button.text()}")

    def on_btn_crear_click(self):
        print("Botón 'Crear' clickeado")
        self.actualizar_imagen_principal()

    def actualizar_imagen_principal(self):
        pxmpPrincipal = QPixmap(self.imgPrincipal.size())
        pxmpPrincipal.fill(Qt.white)
        ############################## SE IMPLEMENTA YA SEA EL OBJETO O LA IMAGEN SELECCIONADA EN PRINCIPAL ####################################
        if self.cbxTriangulo.isChecked():
            self.dibujar_triangulo(pxmpPrincipal)
        elif self.cbxCuadrado.isChecked():
            self.dibujar_cuadrado(pxmpPrincipal)
        elif self.cbxPentagono.isChecked():
            self.dibujar_pentagono(pxmpPrincipal)
        elif self.cbxImagen1.isChecked():
            pxmpPrincipal = QPixmap('/Users/luisa/OneDrive/Pictures/Cristiano.jpg')
        elif self.cbxImagen2.isChecked():
            pxmpPrincipal = QPixmap('/Users/luisa/OneDrive/Pictures/Messi.jfif')

        if pxmpPrincipal:
            self.imgPrincipal.setPixmap(pxmpPrincipal)
        else:
            self.imgPrincipal.clear()

    def dibujar_triangulo(self, pixmap):
        painter = QPainter(pixmap)
        painter.setRenderHint(QPainter.Antialiasing)

        ########################################### SE DEFINEN LAS COORDENDADAS DEL OBJETO ####################################
        points = [QPoint(100, 100), QPoint(150, 200), QPoint(200, 100)]
        painter.drawPolygon(QPolygon(points))
        painter.end()

    def dibujar_cuadrado(self, pixmap):
        painter = QPainter(pixmap)
        painter.setRenderHint(QPainter.Antialiasing)

        ########################################### SE DEFINEN LAS COORDENDADAS DEL OBJETO ####################################
        points = [QPoint(100, 100), QPoint(200, 100), QPoint(200, 200), QPoint(100, 200)]
        painter.drawPolygon(QPolygon(points))
        painter.end()

    def dibujar_pentagono(self, pixmap):
        painter = QPainter(pixmap)
        painter.setRenderHint(QPainter.Antialiasing)

        ########################################### SE DEFINEN LAS COORDENDADAS DEL OBJETO ####################################
        points = [QPoint(100, 100), QPoint(150, 50), QPoint(200, 100),
                QPoint(175, 175), QPoint(125, 175)]
        painter.drawPolygon(QPolygon(points))
        painter.end()

    def on_btn_salir_click(self):
        print("Botón 'Salir' clickeado")
        # Cierra la aplicación
        QApplication.quit()

    def limpiar_imagen_principal(self):
        print("Botón 'Limpiar' clickeado")
        # Elimina la imagen del QLabel principal
        self.imgPrincipal.clear()

    def rotar_imagen_principal(self):
        print("Botón 'Rotacion' clickeado")
        pixmap = self.imgPrincipal.pixmap()
        ########################################### SE IMPLEMENTA LA ROTACION DEL OBJETO ####################################
        if pixmap is not None:
            pixmap = pixmap.transformed(QTransform().rotate(70))
            self.imgPrincipal.setPixmap(pixmap)

    def trasladar_imagen_principal(self):
        ########################################### SE IMPLEMENTA LA TRASLACION DEL OBJETO ####################################
        if not hasattr(self, 'trasladada') or not self.trasladada:
            current_pos = self.imgPrincipal.pos()
            new_pos = current_pos + QPoint(20, 20)  
            self.imgPrincipal.move(new_pos)
            self.trasladada = True
        else:
        ########################################### SE REGRESA A LA POSICION INICIAL EL OBJETO ####################################
            current_pos = self.imgPrincipal.pos()
            new_pos = current_pos - QPoint(20, 20)  # Ajusta las coordenadas según tu necesidad
            self.imgPrincipal.move(new_pos)
            self.trasladada = False

    def escalar_imagen_principal(self):
        ########################################### SE IMPLEMENTA LA ESCALACION DEL OBJETO ####################################
        nuevo_tamano = self.imgPrincipal.size() * 0.8  # Se le ajusta el tamaño a 0.8 de su tamaño inicial.
        self.imgPrincipal.resize(nuevo_tamano)
        print("Botón 'Escalacion' clickeado")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventanaPrincipal = Main()
    ventanaPrincipal.show()
    sys.exit(app.exec_())
