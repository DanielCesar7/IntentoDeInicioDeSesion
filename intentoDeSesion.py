import requests
from time import sleep

# Configuración
url = "https://www.mitortuga.es/"  # URL del formulario de inicio de sesión
email = "prueba111@gmail.com"
password = "incorrect_password"  # Contraseña incorrecta para probar
login_data = {
    "email": email,
    "contraseña": password
}

# Parámetros de control
max_attempts = 100  # Número máximo de intentos
interval = 1  # Tiempo entre intentos en segundos (ajustado a 1 segundo)

# Función principal
def attempt_login():
    for attempt in range(max_attempts):
        try:
            # Enviar solicitud POST al formulario de inicio de sesión
            response = requests.post(url, data=login_data)

            # Verificar respuesta
            print(f"Intento {attempt + 1}: HTTP {response.status_code}")

            # Analizar respuesta en busca del mensaje de error
            if "Email o contraseña incorrectos" in response.text:
                print("Se ha encontrado un error: Email\nEmail o contraseña incorrectos.")
            else:
                print("Respuesta inesperada: Verifica si el sistema permite intentos.")
            
            # Reducción del intervalo de espera para aumentar la velocidad de los intentos
            sleep(interval)

        except requests.RequestException as e:
            print(f"Error al conectar: {e}")
            continue

# Ejecutar script
if __name__ == "__main__":
    attempt_login()