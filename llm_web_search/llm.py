import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

def call_gemini(prompt):
    
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
    model = genai.GenerativeModel("gemini-2.5-flash")
    response = model.generate_content(prompt)
    
    # Extract usage metadata
    usage = response.usage_metadata
    
    # Print detailed token information
    print(f"Model: gemini-1.5-flash")
    print(f"Input tokens: {usage.prompt_token_count}")
    print(f"Output tokens: {usage.candidates_token_count}")
    print(f"Total tokens: {usage.total_token_count}")
    print("-" * 50)
    
    return response.text

def context_combine_prompt(context_from_logs, topic):
    """
    Create a prompt that combines context from logs with a question
    
    Args:
        context_from_logs (str): The context content from scraped logs
        topic (str): The question/topic to ask about
    
    Returns:
        str: The combined prompt for the LLM
    """

    prompt = ("Take this context " + context_from_logs + 
              " now answer this question based on the context given. dont make anything up by yourself, answer "
              " strictly based on the context given. "
              " "
              " Qn : " + topic)
    
    return prompt

result = call_gemini("Explain autoregressive language models.")
print(result)