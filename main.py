# Start your code here!
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

# Define the model to use
model = "gpt-3.5-turbo"

# Define the client
client = OpenAI(api_key=os.environ["OPENAI"])

# Start coding here
def system_msg(content):
    return {"role": "system", "content": f"{content}"}


def user_msg(content):
    return {"role": "user", "content": f"{content}"}


def assist_msg(content):
    return {"role": "assistant", "content": f"{content}"}


conversation = [
system_msg("You are a travel specialist and concierge for Paris, France who politely answers questions from vacationers. You help Parisian tourists learn how to spend their time wisely by providing information on the most popular attractions, and how to plan their routes in order to create travel itineraries. You possess knowledge of the culture, art, buildings, and attractions of Paris to understand what they should visit and how to get there once they arrive."),
user_msg("how far away (in miles) is the Eiffel Tower from Versailles?"),
assist_msg("The Eiffel Tower is about 11 miles away from Versailles. It's a long enough distance that travel by car or rideshare is ideal which is about a 40 minute drive"),
user_msg("Where is the Louvre Museum?"),
assist_msg("The Louvre Museum is located on the Right Bank of the Seine in the city's 1st arrondissement (district or ward). Right in Paris' city center, the address is '75001 Paris, France' and it's about a 15 minute walk from the Sainte-Chapelle"),
user_msg("What are some famous artworks in Paris?"),
assist_msg("Famous artworks in Paris include: 'Les Nympheas' - Claude Monet (1914-1926) located in the Tuileries museum, 'The Frame'- Frida Khalo (1938) located at the Louvre Museum, and 'Antonia' - Amadeo Modigliani (1915) located in the Musée de l’Orangerie")]

user_questions = ["How far away is the Louvre from the Eiffel Tower (in miles) if you are driving?", "Where is the Arc de Triomphe?", "What are the must-see artworks at the Louvre Museum?"]

for question in user_questions:
    message = user_msg(question)
    conversation.append(message)
    response = client.chat.completions.create(
        model = model,
        messages = conversation,
        max_tokens = 100,
        temperature = 0.0
    )
    assistant_response = response.choices[0].message.content
    conversation.append(assist_msg(assistant_response))
    print(assistant_response)