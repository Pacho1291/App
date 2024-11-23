from model import Password_Generator_Model
from view import Password_Generator_View

class Password_Controller():
    def __init__(self, view):
        self.view = view
        # Configura el comando para el botón en la vista
        self.view.generate_button.configure(command=self.controller_generator_password)

    def controller_generator_password(self):
        try:
            # Obtiene los datos ingresados a través de los métodos `get_*`
            length = self.view.get_lenght()
            lower_case = self.view.get_lower_case()
            uper_case = self.view.get_uper_case()
            numbers = self.view.get_numbers()
            special = self.view.get_special_characters()

            # Crea una instancia del modelo con los parámetros obtenidos
            model = Password_Generator_Model(length, lower_case, uper_case, numbers, special)

            # Valida que la longitud de la contraseña sea válida
            model.validate()

            # Genera la contraseña utilizando el modelo
            password = model.generate_password()

            # Actualiza la vista con la contraseña generada
            self.view.update_result(password)

        except ValueError as e:
            # Si ocurre un error (por ejemplo, longitud inválida o caracteres que exceden la longitud), muestra un mensaje de error
            self.view.update_result(f"Error: {str(e)}")

