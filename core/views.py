from django.http import JsonResponse
from pymongo import MongoClient

def test_mongodb(request):
    try:
        # Conectar a MongoDB
        client = MongoClient('mongodb://localhost:27017/')  # Cambia la URL si es necesario
        db = client['sppi_db']  # Reemplaza 'test' por el nombre de tu base de datos
        # Prueba listar colecciones
        collections = db.list_collection_names()
        return JsonResponse({"status": "success", "collections": collections})
    except Exception as e:
        return JsonResponse({"status": "error", "message": str(e)})
