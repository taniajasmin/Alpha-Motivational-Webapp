import openai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def list_available_models():
    try:
        # Initialize the OpenAI client
        client = openai.OpenAI()
        # Fetch the list of models
        models = client.models.list()
        # Count the total number of models
        model_count = len(list(models.data))
        print(f"Total number of available models: {model_count}")
        
        # Print each model ID
        print("\nAvailable model IDs:")
        for model in models.data:
            print(model.id)
    except Exception as e:
        print(f"Error fetching models: {str(e)}")

# Main execution
if __name__ == "__main__":
    list_available_models()