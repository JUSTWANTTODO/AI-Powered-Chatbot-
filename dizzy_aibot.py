#Importing the required libraries
import os
from dotenv import load_dotenv
from langsmith import traceable
from langchain_google_genai import ChatGoogleGenerativeAI, HarmBlockThreshold, HarmCategory
from langchain.prompts import PromptTemplate, FewShotPromptTemplate
from langchain.memory import ConversationSummaryBufferMemory
from langchain.chains import LLMChain, ConversationChain
from langchain_core.output_parsers import StrOutputParser
from langchain.agents import initialize_agent, Tool, AgentType
from langchain_community.chat_message_histories import ChatMessageHistory
import speech_recognition as sr
import pyttsx3
import requests

from bs4 import BeautifulSoup

#Loading the environment variables
load_dotenv()

#Function to search the web using DuckDuckGo
def duckduckgo_search(query):
    url = f"https://duckduckgo.com/html/?q={query}"
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        search_results = []
        for result in soup.find_all("a", class_="result__a"):
            title = result.text.strip()
            link = result.get("href")
            search_results.append(f"Title: {title}, Link: {link}")

        if search_results:
            return "\n".join(search_results)  # Returning as readable text
        else:
            return "Sorry, I couldn't find relevant results."
    except Exception as e:
        print(f"Error with DuckDuckGo search: {e}")
        return "Sorry, I couldn't fetch the information from the web at the moment."

        

# %%
#Initializing the LLMChain
llm = ChatGoogleGenerativeAI(temperature = 0.7,
                             model = "gemini-1.5-flash", 
                             google_api_key = os.getenv("GOOGLE_API_KEY"),
                             safety_settings = {HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT:HarmBlockThreshold.BLOCK_NONE})


#Setting up the chat_history
chat_history = ChatMessageHistory()


#Setting up the ConversationSummaryBufferMemory
memory = ConversationSummaryBufferMemory(llm = llm, chat_history = chat_history, max_token_limit=300, return_messages = True)

tools = [
    Tool(
        name="DuckDuckGo Search",
        func=duckduckgo_search,
        description="Use this tool to search the web for therapeutic information and resources."
    )
]


agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    memory=memory,
    verbose=True
)


#Prompt template
template = """You are Dizzy, a virtual therapeutic assistant supporting people with trauma. Create a safe, empathetic, and non-judgmental space for users to share.

What to Do:
1.Validate emotions (e.g., "It’s okay to feel this way; I’m here for you.").
2.Offer gentle encouragement (e.g., "Take your time; there’s no rush.").
3.Suggest self-care tips only when asked (e.g., "How about trying deep breathing?").
4.Thank users for sharing (e.g., "That takes courage; thank you.").
5.Use positive reinforcement (e.g., "Seeking support shows your strength.").
6.Provide resources upon request without judgment.
The above are only examples; feel free to adapt based on the situation and use sentences that feel natural to you.

What to Avoid:
1.Dismissing or downplaying feelings.
2.Giving unsolicited advice.
3.Making assumptions about experiences.
4.Discussing triggering topics unless initiated.
5.Providing medical diagnoses or definitive claims. 

    Current conversation:{history}
    Friend: {input}
    Dizzy: """

prompt = PromptTemplate(input_variables = ["history", "input"], template = template)



#Setting up a conversation chain
conversation_chain = ConversationChain(llm = llm, memory = memory, prompt = prompt,verbose = True, output_parser = StrOutputParser())

@traceable(project_name= "task4")

#Function to generate a conversation
def generate_conversation(user_input):
    try:
        response = conversation_chain.invoke({"history": chat_history.messages,"input": user_input })
        # Only extract and return the response content, not the whole dictionary
        assistant_response = response['response']  # This contains the AI assistant's reply
        return assistant_response.strip()  # Remove extra spaces or newlines
    except Exception as e:
        print(f"Error in generate_conversation: {e}")
        return "I'm sorry, I couldn't process that."

#Function to recognize speech
def recognize_speech():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()
    print("Listening... (You can speak)")
    with mic as source:
        recognizer.adjust_for_ambient_noise(source, duration=1)
        try:
            audio = recognizer.listen(source)
            text = recognizer.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            print("Sorry, I didn't catch that.")
            return ""
        except sr.RequestError as e:
            print(f"Speech recognition service error: {e}")
            return ""

#Function to generate a response
def speak_response(response):
    engine = pyttsx3.init()
    try:
        # Preprocessing the text to avoid special character issues
        clean_response = ''.join(char for char in response if char.isprintable())
        engine.say(clean_response)
        engine.runAndWait()
    except KeyError as e:
        print(f"Text-to-Speech KeyError: {e}")
    except Exception as e:
        print(f"Unexpected error in TTS: {e}")
    finally:
        engine.stop()


# Main function updated to use speech recognition
if __name__ == "__main__":
    print("Therapeutic Chatbot is now active.")
    greeting = "Hey dear! I'm Dizzy! How do you do?"
    print(f"AI Assistant: {greeting}")
    speak_response(greeting)


    while True:
        try:
            user_input = recognize_speech()  # Use speech recognition

            if user_input.lower() in ["exit", "quit"]:
                farewell = "All the love and happiness in the world for you!"
                print(f"Dizzy: {farewell}")
                speak_response(farewell)
                break

            if user_input:
                output = generate_conversation(user_input)
                print(f"Friend: {user_input}")  # Print what the user said
                print(f"Dizzy: {output}")  # Print the assistant's response
                speak_response(output)
            
            if "search" in user_input.lower() or "help" in user_input.lower() or "tell" in user_input.lower():
                    print("Dizzy: Searching the web for information...")
                    agent_response = agent.run(user_input)  # The agent will decide when to invoke DuckDuckGo search
                    print(f"Dizzy: {agent_response}")
                    speak_response(agent_response)

        except KeyboardInterrupt:
            print("\nSession ended. Take care!")
            break
        
        except Exception as e:
            print(f"Error: {e}")

#To print the last human and AI messages
print("\nLast Human Message:")
print(chat_history.get_last_human_message().content if chat_history.get_last_human_message() else "No human message found.")

#To print the lastest AI message
print("\nLast AI Message:")
print(chat_history.get_last_ai_message().content if chat_history.get_last_ai_message() else "No AI message found.")



#To Getting the summarised history of the conversation
f"Conversation history/summary:", memory.load_memory_variables(inputs = {"history": chat_history.messages})

#Generating a new summary of the conversation
user_choice = input("Would you like a new summary of the conversation? (yes/no): ")
if user_choice.lower() == "yes":
    existing_summary = " "
    print(memory.predict_new_summary(chat_history.messages, existing_summary))



#Adding some context to the memory 
memory.save_context({"input": "I want to cry"}, {"output": "Try eating good food, listening to music, or talking to a friend."})


#Getting the updated conversation history
f"Updated Conversation History/summary:", memory.load_memory_variables(inputs = {"history": chat_history.messages})


#clearing chat history
chat_history.clear()
print("Chat history cleared.\n", chat_history.messages)





