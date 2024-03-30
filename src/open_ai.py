import openai

# Define tu clave de API de OpenAI
key = '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'
openai.api_key = key

ultima_consulta = ""  # Variable para almacenar la última consulta

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
    global ultima_consulta  # Declarar la variable global
    
    while True:
        try:
            consulta_usuario = input("Ingresa tu consulta (o 'salir' para terminar): ")
            
            if consulta_usuario.lower() == 'salir':
                print("¡Adiós!")
                break
            
            if consulta_usuario.strip():  # Verifica si la consulta tiene texto
                print("You:", consulta_usuario)  # Imprime la consulta del usuario con el prefijo "You:"
                ultima_consulta = consulta_usuario  # Almacena la última consulta
                
                try:
                    respuesta_chatGPT = invocar_chatGPT(consulta_usuario)  # Invoca la función para obtener la respuesta de chatGPT
                    
                    print("chatGPT:", respuesta_chatGPT)  # Imprime la respuesta de chatGPT con el prefijo "chatGPT:"
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
