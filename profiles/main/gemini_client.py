import os
import google.generativeai as genai

# Set up the API key
def configure_genai():
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY is not set in environment variables.")
    genai.configure(api_key=api_key)

def send_message_to_gemini(message):
    """Sends a message to the Gemini API and returns the response."""
    configure_genai()

    # Create the model
    generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 64,
        "max_output_tokens": 8192,
        "response_mime_type": "text/plain",
    }

    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config=generation_config,
    )

    # Start chat session
    chat_session = model.start_chat(
        history=[
            {"role": "user", "parts": [message]}
        ]
    )

    # Send message and get response
    response = chat_session.send_message(message)
    return response.text
