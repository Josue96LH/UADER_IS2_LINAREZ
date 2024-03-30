import openai

# Define tu clave de API de OpenAI
<<<<<<< HEAD
openai.api_key = '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'

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
    while True:
        try:
            consulta_usuario = input("Ingresa tu consulta (o 'salir' para terminar): ")
            
            if consulta_usuario.lower() == 'salir':
                print("¡Adiós!")
                break
            
            if consulta_usuario.strip():  # Verifica si la consulta tiene texto
                print("You:", consulta_usuario)  # Imprime la consulta del usuario con el prefijo "You:"
                
                try:
                    respuesta_chatGPT = invocar_chatGPT(consulta_usuario)  # Invoca la función para obtener la respuesta de chatGPT
                    
                    print("chatGPT:", respuesta_chatGPT)  # Imprime la respuesta de chatGPT con el prefijo "chatGPT:"
                except Exception as e:
                    print(f"Error al obtener respuesta de chatGPT: {e}")
            else:
                print("Por favor, ingresa una consulta válida.")
        
        except Exception as e:
            print(f"Error durante la ejecución: {e}")

if __name__ == "__main__":
    main()
=======
openai.api_key = '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'

def invocar_chatGPT(consulta):
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

def main():
    while True:
        consulta_usuario = input("Ingresa tu consulta: ")
        
        if consulta_usuario.strip():  # Verifica si la consulta tiene texto
            print("You:", consulta_usuario)  # Imprime la consulta del usuario con el prefijo "You:"
            
            respuesta_chatGPT = invocar_chatGPT(consulta_usuario)  # Invoca la función para obtener la respuesta de chatGPT
            
            print("chatGPT:", respuesta_chatGPT)  # Imprime la respuesta de chatGPT con el prefijo "chatGPT:"
        else:
            print("Por favor, ingresa una consulta válida.")

if __name__ == "__main__":
    main()
>>>>>>> b08f3ecb7ef045491fb7708f05cf51c4ce081920
