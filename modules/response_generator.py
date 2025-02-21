def generate_response(user_input: str, model_response: str) -> str:
    """
    Formats the response string to be returned to the user.
    """
    return f"Bot: {model_response}"