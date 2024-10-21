from projeto.models.usuario import UsuarioService
from repositories.usuario_repository import UsuarioRepository
from config.connection import Session 

def main(): 
    session = Session()
    respository = UsuarioRepository(session)
    service = UsuarioService(respository)

    # Criando um usuario.
    service.criar_usuario("Marta", "marta@gmail.com", "123")

    # Listando todos os usuarios 
    print("\nListando todos os usuarios: ")
    lista_usuarios = service.listar_todos_usuarios()
    for usuario in lista_usuarios: 
        print(f"{usuario.id} - {usuario.nome} - {usuario.email} - {usuario.senha}")

if __name__ == "__main__": 
    main() # Chamada para função.