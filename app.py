#from recommendation.core import get_genre_recommendations
from flask import Flask, jsonify, request
from supabase import create_client, Client

from IA.api_chat import IA_consulta
import os 
from dotenv import load_dotenv
import datetime
#instanciamos servidor con flask

app = Flask(__name__)

load_dotenv()

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(url, key)

@app.route('/consulta', methods=['GET'])
def consulta_IA():
    try:
            
        recommendations = IA_consulta()
        print(recommendations)
          

        #Funcion para insertar en la base de datos ( falta implementar segun formato de respuesta de IA)
        recommended_movie_titles = recommendations["respuesta"]

       

        return jsonify("recommended_movie_titles"), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 404



def create_app():
    return app

if __name__ == '__main__':
    app.run(debug=True,port=5001)
