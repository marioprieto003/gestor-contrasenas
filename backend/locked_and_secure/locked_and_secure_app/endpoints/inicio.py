from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from locked_and_secure_app.models import Usuarios, Grupos, Contraseñas
from locked_and_secure_app.endpoints.funciones import decrypt_1
from cryptography.fernet import Fernet
import json, bcrypt, secrets, base64

def all(request):
    if request.method != 'GET':
        return JsonResponse({"error": "Método no soportado"}, status=405)
       
   
    try:
        token = request.headers['token']
        clave = request.headers['clave']
    except KeyError:
        return JsonResponse({"error": "Faltán parámetros"}, status=400)
    

    
    try:
        usuario = Usuarios.objects.get(token_sesion=token)
    except  Usuarios.DoesNotExist:
        return JsonResponse({"error": "Usuario no encontrado"}, status=404)
    
    # Obtenemos los grupos que ha creado el usuario
    grupos = Grupos.objects.filter(usuario=usuario)
    
    lista_contraseñas_completa = []
    for grupo in grupos:
        # Obtenemos las contraseñas que el usuario ha creado en cada grupo
        contraseñas = Contraseñas.objects.filter(id_grupo=grupo)
        
        import sys 
        print(sys.path)
        lista_contraseñas_grupo = []
        for contraseña in contraseñas:
             lista_contraseñas_grupo.append(
                 {
                    "id": int(contraseña.id),
                    "contraseña": contraseña.contraseña,
                    "email": contraseña.email,
                    "usuario": contraseña.usuario,
                    "fecha": contraseña.fecha
                 }
             )
             
        lista_contraseñas_completa.append({
            "id": int(grupo.id),
            "grupo": grupo.nombre,
            "tamaño": len(lista_contraseñas_grupo),
            "contraseñas": lista_contraseñas_grupo
            }
        )
        
    return JsonResponse(lista_contraseñas_completa, safe=False, status=200)