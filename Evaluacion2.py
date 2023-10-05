import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
#Poligonos a realizar: Triangulo, Cuadrado y Pentagono
#Cargar dos imagenes diferentes
class Main(QMainWindow):
    def __init__(self, parent=None, *args):
        super(Main, self).__init__(parent=parent)

        
        def creacion_objetos():
            #width = self.frameGeometry().width() #Obtiene el largo de la ventana principal
            #height = self.frameGeometry().height() #Obtiene la altura de la ventana principal
            self.setFixedSize(900, 600) #Bloquea el tamaño a un tamaño exacto, por lo que el usuario no lo puede modificar
            self.setWindowTitle("Evaluacion Unidad 2") #Se agrega un titulo a la ventana
            label = QLabel("Evaluacion segunda unidad Graficación \n Operacion de Escalacion, traslacion y rotacion", self) #creamos el label 
            lblNombre = QLabel("Covarrubias Rosales Luis Humberto-20212393", self)
            label.setGeometry(0, 0, 900, 200)#posicion de Izq a Der, de arriba a abajo, largo y alto
            label.setStyleSheet("background:#424242; color:fff") #Estilos que se pueden aplicar al label
            fuente = label.font()
            fuenteNombre = lblNombre.font()
            fuente.setPointSize(28)
            fuenteNombre.setPointSize(10)
            fuente.setBold(True)
            fuenteNombre.setBold(True)
            label.setFont(fuente)
            lblNombre.setFont(fuenteNombre)
            #self.setCentralWidget(label) #Expandir el label al tamaño de la ventana principal
            label.setAlignment(Qt.AlignCenter ) #Posicion del texto respecto al label
            #Checkbox de los poligonos
            lblNombre.setGeometry(0, 570, 400, 30)#posicion de Izq a Der, de arriba a abajo, largo y alto
            btnCrear = QPushButton('Crear', self) #Se crea un boton con QPushButton, este boton se utiliza para Crear la imagen
            btnCrear.setGeometry(30, 485, 160, 30)
            btnLimpiar = QPushButton('Limpiar', self) #Se crea un boton con QPushButton, este boton se utiliza para limpiar la imagen
            btnLimpiar.setGeometry(200, 485, 160, 30)
            btnRotacion = QPushButton('Rotacion', self) #Se crea un boton con QPushButton, este boton se utiliza para Rotar la imagen
            btnRotacion.setGeometry(370, 485, 160, 30)
            btnTraslacion = QPushButton('Traslacion', self) #Se crea un boton con QPushButton, este boton se utiliza para Trasladar la imagen
            btnTraslacion.setGeometry(540, 485, 160, 30)
            btnEscalacion = QPushButton('Escalacion', self) #Se crea un boton con QPushButton, este boton se utiliza para Escalar la imagen
            btnEscalacion.setGeometry(710, 485, 160, 30)
            btnSalir = QPushButton('Salir', self) #Se crea un boton con QPushButton, este boton se utiliza para cerrar el programa
            btnSalir.setGeometry(30, 525, 840, 30)

        def radio_buttons():
            cbxTriangulo = QRadioButton("Triangulo", self) #Se crea un radioBUtton para las opciones de poligonos
            cbxTriangulo.setGeometry(100, 200, 100, 100) #Se le asigna la posicion en la pantalla al radiobutton
            cbxCuadrado = QRadioButton("Cuadrado", self)
            cbxCuadrado.setGeometry(100, 250, 100, 100)
            cbxPentagono = QRadioButton("Pentagono", self)
            cbxPentagono.setGeometry(100, 300, 100, 100)
            cbxImagen1 = QRadioButton("Imagen1", self)
            cbxImagen1.setGeometry(100, 350, 100, 100) 
            cbxImagen2 = QRadioButton("Imagen2", self)
            cbxImagen2.setGeometry(100, 400, 100, 100) 
            
            self.ButtonGroup = QButtonGroup(self)#Se crea un grupo de botones para juntar los radiobuttons
            self.ButtonGroup.addButton(cbxTriangulo)#Se agrega al grupo de botones el RadioButton con el poligono triangulo
            self.ButtonGroup.addButton(cbxCuadrado)#Se agrega al grupo de botones el RadioButton con el poligono cuadrado
            self.ButtonGroup.addButton(cbxPentagono)#Se agrega al grupo de botones el RadioButton con el poligono Pentagono
            self.ButtonGroup.addButton(cbxImagen1)#Se agrega al grupo de botones el RadioButton con la imagen numero 1
            self.ButtonGroup.addButton(cbxImagen2)#Se agrega al grupo de botones el RadioButton con la imagen numero 2
            self.ButtonGroup.buttonClicked.connect(on_button_clicked)
            #self.ButtonGroup.buttonClicked.connect(lambda button: crear_principal(self, button))
            
            ###################################### IMAGEN EJECUTABLE DEL PROGRAMA #############################################
            imgPrincipal = QLabel(self)
            if cbxTriangulo.isChecked(True):
                pxmpPrincipal = QPixmap('/home/luis-covarrubias/Imágenes/Triangulo.png')
            elif cbxCuadrado.isChecked(True):
                pxmpPrincipal = QPixmap('/home/luis-covarrubias/Imágenes/Cuadrado.jpeg')
            elif cbxPentagono.isChecked(True):
                pxmpPrincipal = QPixmap('/home/luis-covarrubias/Imágenes/Pentagono.png')
            elif cbxImagen1.isChecked(True):
                pxmpPrincipal = QPixmap('/home/luis-covarrubias/Imágenes/Cristiano.jgep')
            elif cbxImagen2.isChecked(True):
                pxmpPrincipal = QPixmap('/home/luis-covarrubias/Imágenes/Messi.jpeg')
            imgPrincipal.setPixmap(pxmpPrincipal)
            imgPrincipal.setGeometry(25, 403, 400, 400)
            imgPrincipal.setScaledContents(True) #La imagen se acomoda al tama;o del label en el que se encuentre
            imgPrincipal.setStyleSheet('border: 2px solid black;') #Se crea un borde alrededor de la imagen
            
        def CrearImagenes():

            imgTriangulo = QLabel(self) #Se crea un label que se utilizara para contener las imagenes
            imgCuadrado = QLabel(self)
            imgPentagono = QLabel(self)
            imgImagen1 = QLabel(self)
            imgImagen2 = QLabel(self)
            pxmpTriangulo = QPixmap('/home/luis-covarrubias/Imágenes/Triangulo.png') #Se asigna la funcion Qpixmap, que a continuacion sera utilizada para contener la imagen en el label.
            pxmpCuadrado = QPixmap('/home/luis-covarrubias/Imágenes/Cuadrado.jpeg')
            pxmpPentagono = QPixmap('/home/luis-covarrubias/Imágenes/Pentagono.png')
            pxmpImagen1 = QPixmap('/home/luis-covarrubias/Imágenes/Cristiano.jpeg')
            pxmpImagen2 = QPixmap('/home/luis-covarrubias/Imágenes/Messi.jpeg')
            imgTriangulo.setPixmap(pxmpTriangulo)#Se enlanza la funcion Pixmap con el label, para contener la imagen ahi mismo.
            imgCuadrado.setPixmap(pxmpCuadrado)
            imgPentagono.setPixmap(pxmpPentagono)
            imgImagen1.setPixmap(pxmpImagen1)
            imgImagen2.setPixmap(pxmpImagen2)
            imgTriangulo.setGeometry(25, 243, 40, 40)
            imgTriangulo.setScaledContents(True) #La imagen se acomoda al tama;o del label en el que se encuentre
            imgTriangulo.setStyleSheet('border: 2px solid black;') #Se crea un borde alrededor de la imagen
            imgCuadrado.setGeometry(25, 293, 40, 40)
            imgCuadrado.setScaledContents(True)
            imgCuadrado.setStyleSheet('border: 2px solid black;')
            imgPentagono.setGeometry(25, 343, 40, 40)
            imgPentagono.setScaledContents(True)
            imgPentagono.setStyleSheet('border: 2px solid black;')
            imgImagen1.setGeometry(25, 393, 40, 40)
            imgImagen1.setScaledContents(True)
            imgImagen1.setStyleSheet('border: 2px solid black;')
            imgImagen2.setGeometry(25, 443, 40, 40)
            imgImagen2.setScaledContents(True)
            imgImagen2.setStyleSheet('border: 2px solid black;')

###################################### IMAGEN EJECUTABLE DEL PROGRAMA #############################################
        
        def on_button_clicked(button):
            print(f"Botón clickeado: {button.text()}")
            

        radio_buttons()       
        creacion_objetos()
        CrearImagenes()
        #crear_principal(self, button= None)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventanaPrincipal = Main()
    ventanaPrincipal.show() #La ventana principal por default esta oculta
    sys.exit(app.exec_())
