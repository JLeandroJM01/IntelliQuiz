# IntelliQuiz

## Instalación
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Estado

No se ha terminado de hacer la conexion con openai
Se termino conexion con SUPABASE, se puede probar conexcion corriendo BD/connection.py

Las variables de entorno:

1) debes crear un archivo .env en el directorio principal
2) Pon esto ahi
```bash
SUPABASE_KEY="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImdhY2podWphZmpzemV4bmJwbmxjIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MDI5NjAzODUsImV4cCI6MjAxODUzNjM4NX0.n5dpARt6Rsq45_xy5UxzAARcNKQoFb6957XNJXsqWD0"
API_KEY="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"
SUPABASE_URL="https://gacjhujafjszexnbpnlc.supabase.co"
```