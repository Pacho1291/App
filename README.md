# App
My first project in python 
App: Generador de contraseñas
Objetivo: 
Diseñar una aplicación que genere contraseñas aleatorias, con distintos parámetros (mayúsculas, minúsculas, números caracteres) para obtener un mayor nivel de seguridad a nivel tecnológico, siendo estas contraseñas útiles para usarlas en cuentas bancarias, cuentas de redes sociales, configuraciones de redes entre otros ámbitos.

Descripción: 
La aplicación funciona de una manera muy sencilla, se enfoca en generar contraseñas aleatorias en base a los parámetros que el usuario elija, permitiéndole determinar la longitud, así como también, el numero de mayúsculas, minúsculas, números y caracteres especiales.
El modelo esta enfocado en todo el proceso lógico, se establecen los métodos para generar la contraseña, así como un método adicional que valide que la contraseña sea superior a 8 dígitos.
La vista esta enfocada en la parte visual, se establecen una serie de etiquetas que solicitan información al usuario, así como también sus respectivas entradas, y finalmente se determinan unos métodos que van a enlazarse con el controlador.
El controlador es el intermediario entre la vista y el modelo, se encarga de relacionar el modelo con la vista, en este apartado, se estableció un método que dejara enlazar la vista con los atributos respectivos para generar la contraseña, así como también   la respectiva instancia de los atributos estipulados en el modelo, y se determina una prueba de error que se encuentra enfocada en detectar errores en dado caso el usuario digite valores inadecuados.

Consideraciones:
Instalar el customtkinter antes de ejecutar.
--->Pip install customtkinter<---

Ejecutar el programa desde el archivo main, para apreciar la interfaz gráfica


