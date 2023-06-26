def get_response(message: str) -> str:
    p_message = message.lower()

    if p_message == "hello":
        return "Quack Quack!"

    if p_message == "!help":
        return "`Here comes the help`"

    return "Quack!"
