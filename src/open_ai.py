import sys
import openai

# Define tu clave de API de OpenAI
openai.api_key = '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'

# Variables para mantener el estado de la conversación
ULTIMA_CONSULTA = ""  # Almacena la última consulta realizada
BUFFER_CONVERSACION = []  # Buffer para almacenar consultas y respuestas anteriores

def invocar_chat_gpt(consulta):
    """
    Invoca el modelo de ChatGPT de OpenAI para generar una respuesta dada una consulta.

    Parameters:
        consulta (str): La consulta para la cual se solicita una respuesta.

    Returns:
        str: La respuesta generada por el modelo de ChatGPT.
    """
    try:
        # Llamada a la API de OpenAI para generar una respuesta de ChatGPT
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-0125",
            messages=[
                {"role": "system", "content": "Contexto de inicio"},
                {"role": "user", "content": consulta}
            ],
            temperature=1,
            max_tokens=150,
            stop=["\n"]
        )
        return response.choices[0].message['content']  # Devuelve el contenido de la respuesta generada
    except openai.OpenAIError as e:
        return f"Error al invocar el modelo de chatGPT: {e}"

def main():
    """
    Función principal del programa.
    """
    global ULTIMA_CONSULTA, BUFFER_CONVERSACION
    
    # Verifica si se ha pasado el argumento "--convers"
    modo_conversacion = "--convers" in sys.argv
    
    while True:
        try:
            # Solicita al usuario que ingrese una consulta
            consulta_usuario = input("Ingresa tu consulta (o 'salir' para terminar): ")
            
            # Verifica si el usuario quiere salir del programa
            if consulta_usuario.lower() == 'salir':
                print("¡Adiós!")
                break
            
            # Verifica si la consulta del usuario está vacía
            if consulta_usuario.strip():
                # Imprime la consulta del usuario con el prefijo "You:"
                print("You:", consulta_usuario)
                
                # Almacena la última consulta realizada
                ULTIMA_CONSULTA = consulta_usuario
                
                # Agrega la consulta al buffer de conversación si está en modo conversación
                if modo_conversacion:
                    BUFFER_CONVERSACION.append(("You:", consulta_usuario))
                
                try:
                    # Genera una respuesta de ChatGPT basada en la consulta del usuario
                    if modo_conversacion:
                        # Si está en modo conversación, utiliza la última consulta realizada para generar una respuesta
                        respuesta_chat_gpt = invocar_chat_gpt(" ".join(BUFFER_CONVERSACION[-1][1:]))
                    else:
                        # Si no está en modo conversación, genera una respuesta basada en la consulta actual
                        respuesta_chat_gpt = invocar_chat_gpt(consulta_usuario)
                    
                    # Imprime la respuesta de ChatGPT con el prefijo "chatGPT:"
                    print("chatGPT:", respuesta_chat_gpt)
                    
                    # Agrega la respuesta al buffer de conversación si está en modo conversación
                    if modo_conversacion:
                        BUFFER_CONVERSACION.append(("chatGPT:", respuesta_chat_gpt))
                    
                except openai.OpenAIError as e:
                    print(f"Error al obtener respuesta de chatGPT: {e}")
            else:
                print("Por favor, ingresa una consulta válida.")
        
        except KeyboardInterrupt:  # Captura la excepción cuando se presiona "cursor Up"
            # Recupera la última consulta cuando se presiona "cursor Up"
            print("\nConsulta anterior recuperada:", ULTIMA_CONSULTA)
            continue
        
        except Exception as e:
            print(f"Error durante la ejecución: {e}")

if __name__ == "__main__":
    main()
