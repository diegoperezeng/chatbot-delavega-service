from enum import Enum

class MessageRole(str, Enum):
    """
    Enum para os diferentes papéis em uma conversa.
    """
    USER = "user"
    ASSISTANT = "assistant"
    SYSTEM = "system" 