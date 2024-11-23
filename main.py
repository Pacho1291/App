from model import Password_Generator_Model
from view import Password_Generator_View
from controller import Password_Controller
import customtkinter as ctk

def main():
    # Configuración inicial de la ventana principal
    window = ctk.CTk()  #Instancia de la ventana principal
    window.geometry("400x500")
    window.title("Password Generator") 
    
    
    #Crea la vista
    view = Password_Generator_View(window)
    
    # Crear el controlador
    controller = Password_Controller(view)
    
    # Ejecutar la aplicación
    window.mainloop()  # Inicia el bucle principal de la interfaz gráfica


if __name__ == "__main__":
    main()
