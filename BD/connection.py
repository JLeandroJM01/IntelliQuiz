import os
from supabase import create_client, Client
import json
from dotenv import load_dotenv

load_dotenv()

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(url, key)

class Usuario:
    def __init__(self, email, name, password):
        self.email = email
        self.name = name
        self.password = password

    def insertar(self, user):
        data, count = supabase.table('usuarios').insert(user.__dict__).execute()
        return data

    def obtener(self):
        response = supabase.table('usuarios').select("*").execute()
        data = response.data
        formatted_data = json.dumps(data, indent=4)
        print(f'Data: {formatted_data}')

    def update(self):
        return f'Nombre: {self.nombre}\nApellido: {self.apellido}\nCorreo: {self.correo}'


usuario1 = Usuario("alejo@gmail.com", "Alejo", "chupetin23")


usuario1.insertar(usuario1)
