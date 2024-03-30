import openai
import sys

# Define tu clave de API de OpenAI
openai.api_key = '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'

ultima_consulta = ""  # Variable para almacenar la última consulta
buffer_conversacion = []  # Buffer para almacenar consultas y respuestas anteriores

def invocar_chatGPT(consulta):
    try:
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
        return response.choices[0].message['content']
    except Exception as e:
        return f"Error al invocar el modelo de chatGPT: {e}"

def main():
    global ultima_consulta, buffer_conversacion
    
    # Verifica si se ha pasado el argumento "--convers"
    if "--convers" in sys.argv:
        modo_conversacion = True
    else:
        modo_conversacion = False
    
    while True:
        try:
            consulta_usuario = input("Ingresa tu consulta (o 'salir' para terminar): ")
            
            if consulta_usuario.lower() == 'salir':
                print("¡Adiós!")
                break
            
            if consulta_usuario.strip():  # Verifica si la consulta tiene texto
                print("You:", consulta_usuario)  # Imprime la consulta del usuario con el prefijo "You:"
                ultima_consulta = consulta_usuario  # Almacena la última consulta
                
                if modo_conversacion:
                    buffer_conversacion.append(("You:", consulta_usuario))
                
                try:
                    if modo_conversacion:
                        respuesta_chatGPT = invocar_chatGPT(" ".join(buffer_conversacion[-1][1:]))  # Utiliza la última consulta realizada
                    else:
                        respuesta_chatGPT = invocar_chatGPT(consulta_usuario)  # Invoca la función para obtener la respuesta de chatGPT
                    
                    print("chatGPT:", respuesta_chatGPT)  # Imprime la respuesta de chatGPT con el prefijo "chatGPT:"
                    
                    if modo_conversacion:
                        buffer_conversacion.append(("chatGPT:", respuesta_chatGPT))
                    
                except Exception as e:
                    print(f"Error al obtener respuesta de chatGPT: {e}")
            else:
                print("Por favor, ingresa una consulta válida.")
        
        except KeyboardInterrupt:  # Captura la excepción cuando se presiona "cursor Up"
            print("\nConsulta anterior recuperada:", ultima_consulta)
            continue
        
        except Exception as e:
            print(f"Error durante la ejecución: {e}")

if __name__ == "__main__":
    main()
