import customtkinter as ctk
class Password_Generator_View:
    def __init__(self, window):
        self.window = window

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.create_interface()

    def create_interface(self):
        self.label = ctk.CTkLabel(self.window, text="Welcome user come in! ", font=("Arial", 12), text_color="#FFFFFF")
        self.label.pack(pady = 5)

        self.label = ctk.CTkLabel(self.window, text="Please digit the lenght of the password ", font=("Arial", 12 ))
        self.label.pack(pady = 5)

        self.entry_lenght = ctk.CTkEntry(self.window, height = 20, width = 50, font = ("Arial", 12), border_width=3, border_color="#0056D2")
        self.entry_lenght.pack(pady=5)

        self.label = ctk.CTkLabel(self.window, text="Please digit the quality of the uper case ", font=("Arial", 12 ))
        self.label.pack(pady = 5)

        self.entry_uper = ctk.CTkEntry(self.window, height = 20, width = 50, font = ("Arial", 12), border_width=3, border_color="#0056D2")
        self.entry_uper.pack(pady=5)

        self.label = ctk.CTkLabel(self.window, text="Please digit the quality of the lower case ", font=("Arial", 12 ))
        self.label.pack(pady = 5)

        self.entry_lower = ctk.CTkEntry(self.window, height = 20, width = 50, font = ("Arial", 12), border_width=3, border_color="#0056D2")
        self.entry_lower.pack(pady=5)

        self.label = ctk.CTkLabel(self.window, text="Please digit the quality of the numbers ", font=("Arial", 12 ))
        self.label.pack(pady = 5)

        self.entry_numbers = ctk.CTkEntry(self.window, height = 20, width = 50, font = ("Arial", 12), border_width=3, border_color="#0056D2")
        self.entry_numbers.pack(pady=5)

        self.label = ctk.CTkLabel(self.window, text="Please digit the quality of the special characters ", font=("Arial", 12 ))
        self.label.pack(pady = 5)

        self.entry_char = ctk.CTkEntry(self.window, height = 20, width = 50, font = ("Arial", 12), border_width=3, border_color="#0056D2")
        self.entry_char.pack(pady=5)


        self.generate_button = ctk.CTkButton(self.window, text = "Password generator", font=("Arial", 12),corner_radius=5, hover_color="#0056D2")
        self.generate_button.pack(pady=10)
        
        self.result_label = ctk.CTkLabel(self.window, text="You password will appear here", font=("Arial", 12))
        self.result_label.pack(pady = 20)
        
        
    def get_lenght(self):
        return int(self.entry_lenght.get())

    def get_lower_case(self):
        return int(self.entry_lower.get())

    def get_uper_case(self):
        return int(self.entry_uper.get())

    def get_numbers(self):
        return int(self.entry_numbers.get())

    def get_special_characters(self):
        return int(self.entry_char.get())

    # Método para actualizar el resultado en la vista
    def update_result(self, password):
        self.result_label.configure(text=f"Your password is: {password}", text_color="#0056D2")


