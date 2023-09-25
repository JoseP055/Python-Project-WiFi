import subprocess

def show_passw():
    # Obtener la lista de perfiles de las redes wifi almacenadas
    profiles = subprocess.check_output(["netsh", "wlan", "show", "profiles"]).decode("UTF-8").split("\n") #Obtiene los perfiles ejecutando un comando desde el cmd

    # Extraer los nombres de los perfiles wifi y eliminar las cadenas vacías
    profiles_names = [i.split(":")[1].strip() for i in profiles if "All User Profile" in i]

    # Mostrar las contraseñas
    for profile_name in profiles_names:
        result = subprocess.run(["netsh", "wlan", "show", "profile", profile_name, "key=clear"], capture_output=True, text=True)
        if result.returncode == 0:
            password = [line.split(":")[1].strip() for line in result.stdout.split("\n") if "Key Content" in line]
            print(f"Red: {profile_name} - Password: {password[0] if password else 'No se encontró la contraseña'}")
        else:
            print(f"Red: {profile_name} - No se pudo recuperar la contraseña")

show_passw()
