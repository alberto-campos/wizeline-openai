#!/usr/bin/env python3

import os
from openai import OpenAI

client = OpenAI(api_key=self.api_key)
from dotenv import load_dotenv

class ChatGPT:
    """A class to interact with OpenAI's ChatGPT model."""

    def __init__(self):
        # Load environment variables from the .env file
        load_dotenv()

        # Retrieve the OPENAI_API_KEY environment variable
        self.api_key = os.getenv("OPENAI_API_KEY")

        # Set the retrieved API key for the OpenAI library

        # A constant to describe the role or behavior of the chatbot
        self.MAIN_ROLE = "This is the behavior of chatGPT"

    def request_openai(self, message, role="system"):
        """
        Make a request to the OpenAI API.

        Args:
        - message (str): The message to be sent to the OpenAI API.
        - role (str, optional): The role associated with the message. Defaults to "system".

        Returns:
        - str: The response content from the OpenAI API.
        """

        # Create a chat completion with the provided message and role
        response = client.chat.completions.create(model="gpt-3.5-turbo",
        messages=[{"role": role, "content": message}])

        # Return the message content from the API response
        return response["choices"][0]["message"]["content"]
    
    def analyze_transcription(transcription):
        # OpenAI API call
        response = client.chat.completions.create(
            model="gpt-3.5-turbo-1106",
            temperature=1.1,
            max_tokens=200,
            messages=[
                {"role": "system", "content": "You are an English professional in linguistics, teaching English as a Second Language to Spanish-speaking individuals who seek feedback on expressing themselves in natural English. You provide explanations and use an analogy, using the Spanish language as an example. You empathize and give an example: saying 'esta computadoras están disponible' is incorrect; instead, you should say 'estas computadoras están disponibles' to further illustrate your explanation."},
                {"role": "user", "content": transcription},
            ]
        )

        # Extract the AI-generated response
        ai_response = response.choices[0].message.content
        
        return ai_response
    
    def display_recommendations(user_input, ai_output):
        display(HTML(f"<strong>User Input:</strong> {user_input}"))
        display(HTML(f"<strong>AI Output:</strong> {ai_output}"))

        # Example transcription from a Spanish-speaking user
        user_transcription = """
            Hello everyone, my name is Mr. Rodrigo Rodriguez.

            Hope your doing well. How do you call that? I want to make sure because I don't want to do a mistake.

            The bus is late, no? 

            I guess is not good that the bus is always late.


            """
        # Analyze the transcription and get AI-generated recommendations
        ai_recommendations = analyze_transcription(user_transcription)

        # Display the results
        display_recommendations(user_transcription, ai_recommendations)


# If you need to test or use this directly, you can do:
# if __name__ == "__main__":
#     chat_gpt = ChatGPT()
#     print(chat_gpt.request_openai("Hello!"))
