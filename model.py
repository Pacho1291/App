import random
import string as st

class Password_Generator_Model():
    def __init__(self, lenght, lower_case, uper_case, numbers, special):
        self.lenght = lenght
        self.lower_case = lower_case
        self.uper_case = uper_case
        self.numbers = numbers
        self.special = special        

    def generate_password(self):
        # Verifica si la suma de los caracteres excede la longitud de la contraseña
        if self.lower_case + self.uper_case + self.numbers + self.special > self.lenght:
            raise ValueError("The sum of the character quantities exceeds the original length of the password.")
        
        # Generación de las partes de la contraseña
        lower = [random.choice(st.ascii_lowercase) for i in range(self.lower_case)] 
        uper = [random.choice(st.ascii_uppercase) for i in range(self.uper_case)]
        num = [random.choice(st.digits) for i in range(self.numbers)]
        sp = [random.choice(st.punctuation) for i in range(self.special)]
    
        # Combinación de todas las partes generadas
        total_chars = lower + uper + num + sp

        # Si la longitud total es menor a la solicitada, completamos con caracteres aleatorios
        if len(total_chars) < self.lenght:
            remaining = self.lenght - len(total_chars)
            total_chars += [random.choice(st.ascii_lowercase + st.ascii_uppercase + st.digits + st.punctuation) for i in range(remaining)]

        # Mezclar y devolver la contraseña generada
        random.shuffle(total_chars)
        return ''.join(total_chars)

    def validate(self):
        # Validación de la longitud mínima
        if self.lenght < 8:
            raise ValueError("Password must be at least 8 characters long.")
