import os
try:
    from dotenv import load_dotenv
except ImportError:
    print("Error: 'python-dotenv' is not installed. Run 'pip install python-dotenv' to use this demo.")
    load_dotenv = None

def dotenv_demo():
    print("--- Python Dotenv Demonstration ---")
    
    if load_dotenv:
        # 1. Load variables from .env file
        # By default, it looks for a file named .env in the current directory
        load_dotenv()
        
        print("Loading environment variables from .env...")
        
        # 2. Access variables using os.getenv
        api_key = os.getenv("API_KEY", "default-api-key")
        db_url = os.getenv("DATABASE_URL")
        debug_mode = os.getenv("DEBUG", "False")
        
        print(f"API Key: {api_key}")
        print(f"Database URL: {db_url}")
        print(f"Debug Mode: {debug_mode}")
        
    else:
        print("Skipping demo because python-dotenv is not installed.")

    print("\nEnvironment variable access is crucial for sensitive data like passwords and keys.")

if __name__ == "__main__":
    # Create a dummy .env file for the demo if it doesn't exist
    if not os.path.exists(".env"):
        with open(".env", "w") as f:
            f.write("API_KEY=my_secret_token_123\n")
            f.write("DATABASE_URL=sqlite:///production.db\n")
            f.write("DEBUG=True\n")
        print("Created a temporary .env file for demonstration.")
        
    dotenv_demo()
