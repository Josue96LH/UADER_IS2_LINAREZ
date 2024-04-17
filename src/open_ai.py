import sys
import openai

# Constantes
OPENAI_API_KEY = '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'
MODEL_NAME = "gpt-3.5-turbo-0125"
TEMPERATURE = 1
MAX_TOKENS = 150

# Variables para mantener el estado de la conversación
ULTIMA_CONSULTA = ""
BUFFER_CONVERSACION = []

# Configuración de OpenAI
openai.api_key = OPENAI_API_KEY

def invocar_chat_gpt(consulta):
    """
    Invoca el modelo de ChatGPT de OpenAI para generar una respuesta dada una consulta.

    Parameters:
        consulta (str): La consulta para la cual se solicita una respuesta.

    Returns:
        str: La respuesta generada por el modelo de ChatGPT.
    """
    try:
        response = openai.ChatCompletion.create(
            model=MODEL_NAME,
            messages=[
                {"role": "system", "content": "Contexto de inicio"},
                {"role": "user", "content": consulta}
            ],
            temperature=TEMPERATURE,
            max_tokens=MAX_TOKENS,
            stop=["\n"]
        )
        return response.choices[0].message['content']
    except openai.OpenAIError as e:
        return f"Error al invocar el modelo de chatGPT: {e}"

def obtener_consulta_usuario():
    """
    Solicita al usuario que ingrese una consulta.

    Returns:
        str: La consulta ingresada por el usuario.
    """
    return input("Ingresa tu consulta (o 'salir' para terminar): ")

def procesar_consulta(consulta_usuario, modo_conversacion):
    """
    Procesa la consulta del usuario y genera una respuesta de ChatGPT si es necesario.

    Parameters:
        consulta_usuario (str): La consulta ingresada por el usuario.
        modo_conversacion (bool): Indica si el programa está en modo conversación.

    Returns:
        str: La respuesta generada por ChatGPT, o un mensaje de error si ocurrió un problema.
    """
    if consulta_usuario.lower() == 'salir':
        return "¡Adiós!"

    if not consulta_usuario.strip():
        return "Por favor, ingresa una consulta válida."

    print("You:", consulta_usuario)
    global ULTIMA_CONSULTA
    ULTIMA_CONSULTA = consulta_usuario

    try:
        respuesta_chat_gpt = invocar_chat_gpt(" ".join(BUFFER_CONVERSACION[-1][1:])) if modo_conversacion else invocar_chat_gpt(consulta_usuario)
        print("chatGPT:", respuesta_chat_gpt)
        if modo_conversacion:
            BUFFER_CONVERSACION.append(("chatGPT:", respuesta_chat_gpt))
        return respuesta_chat_gpt
    except openai.OpenAIError as e:
        return f"Error al obtener respuesta de chatGPT: {e}"

def main():
    """
    Función principal del programa.
    """
    modo_conversacion = "--convers" in sys.argv

    while True:
        try:
            consulta_usuario = obtener_consulta_usuario()
            respuesta = procesar_consulta(consulta_usuario, modo_conversacion)
            if respuesta == "¡Adiós!":
                print(respuesta)
                break
        except KeyboardInterrupt:
            print("\nConsulta anterior recuperada:", ULTIMA_CONSULTA)
            continue
        except Exception as e:
            print(f"Error durante la ejecución: {e}")

if __name__ == "__main__":
    main()
