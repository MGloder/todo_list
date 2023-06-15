import os
from dotenv import load_dotenv

from app.app import app

# Load environment variables from .env file
load_dotenv()


def run():
    # Get the port number from the environment variable, or use the default value 5000
    port = int(os.getenv('PORT', 5000))
    app.run(debug=True, port=port)


if __name__ == '__main__':
    run()
