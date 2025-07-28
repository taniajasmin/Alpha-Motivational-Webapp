# Alpha Motivational Webapp

Ignite your inner fire with Alpha Motivational Webapp, your daily dose of motivation crafted to propel you toward greatness with every click! This web application delivers personalized, uplifting 1-2 sentence messages, infused with a dynamic edge, and supports multiple languages to inspire a global audience.

## Overview

Alpha Motivational Webapp is built using FastAPI and powered by OpenAI's GPT models, generating tailored motivational content based on your age, name, gender, mission, tone, and grind level. With real-time personalization and a sleek interface, it’s your companion for conquering each day.

- **Language Support**: English (US), English (UK), French (FR), German (DE)
- **AI Model**: OpenAI GPT-4o (configurable in `main.py`)
- **Framework**: FastAPI
- **Current Date/Time**: Dynamically updated (e.g., 12:34 PM +06 on Monday, July 28, 2025)

## Features

- Personalized 1-2 sentence motivational messages.
- Multi-language support for a global reach.
- Dynamic user input via a web form.
- Real-time generation with current date/time context.

## Prerequisites

- Python 3.8 or higher
- An OpenAI API key

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/Alpha-Motivational-Webapp.git
   cd Alpha-Motivational-Webapp
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the project root and add your OpenAI API key:
   ```
   OPENAI_API_KEY=your-openai-api-key-here
   ```

## Usage

1. Run the FastAPI application:
   ```bash
   uvicorn main:app --reload
   ```

2. Open your browser and navigate to:
   ```
   http://127.0.0.1:8000
   ```

3. Fill out the form with your details (age, name, gender, language, mission, tone, grind level) and click "Allow and Save" to receive your motivational message.

## File Structure

- `main.py`: FastAPI application with the motivational message generator.
- `demo.html`: HTML template for the user input form.
- `requirements.txt`: List of project dependencies.
- `test_models.py`: Script to list available OpenAI GPT models (run this to see options and manually update the model name in `main.py` if needed).

## Model Configuration

- To check available GPT models, run:
  ```bash
  python test_models.py
  ```
  This will display the total number of models and their IDs. If you want to change the model (currently set to `gpt-4o` in `main.py`), manually update the `model` parameter in the `get_motivational_message` function to your preferred model ID (e.g., `gpt-3.5-turbo`).

## Acknowledgments

- Powered by OpenAI for the GPT models.
- Built with FastAPI for a robust web framework.
