import os
import openai


class Gpt_generator:
    def __init__(self, api_key=None, model='gpt-4'):
        """
        Inicializa a classe GptGenerator com a chave da API e o modelo padrão.
        """
        self.api_key = api_key or self.get_api_key()
        self.model = model
        
        # Configura a chave da API
        openai.api_key = self.api_key

    def get_api_key(self, file_path='openai_key.txt'):
        """
        Lê a chave da API de um arquivo.
        """
        try:
            with open(file_path, 'r') as file:
                api_key = file.read().strip()
                return api_key
        except FileNotFoundError:
            raise FileNotFoundError(f"Arquivo '{file_path}' não encontrado. Por favor, forneça uma chave de API válida.")
        except Exception as e:
            raise Exception(f"Erro ao ler a chave da API: {e}")
        
    def set_model(self, model):
        """
        Atualiza o modelo utilizado para as chamadas.
        """
        self.model = model

    def invoke(self, prompt):
        """
        Envia um prompt ao modelo configurado e retorna a resposta.
        """
        try:
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=[
                    {
                        "role": "user",
                        "content": prompt,
                    }
                ],
            )
            return response['choices'][0]['message']['content'].strip()
        except Exception as e:
            raise Exception(f"Erro ao invocar o modelo: {e}")