# Passo 01 - Criar ferramenta
from langchain.chat_models import init_chat_model
from langchain.tools import BaseTool, tool
from langchain_core.messages import (
    BaseMessage,
    HumanMessage,
    SystemMessage,
)
from rich import print

from dotenv import load_dotenv

load_dotenv()


@tool()
def multiply(a: float, b: float) -> float:
    """Multipy a * b and return the result
    Args:
        a (float): The first number
        b (float): The second number
    Returns:
        float: The resulting foat of the equation a * b"""
    return a * b


llm = init_chat_model("gpt-4o-mini", temperature=0)


system_message = SystemMessage(
    content=""" Você é um assistente de matemática prestativo. Você tem acesso a ferramentas. 
                Quando o usuário pedir algo, primeiro verifique se você possui uma ferramenta que resolva esse problema."""
)
human_message = HumanMessage("Oi eu sou Goku, quanto é 12.5 multiplicado por 3.4?")
messages: list[BaseMessage] = [
    system_message,
    human_message,
]
tools: list[BaseTool] = [
    multiply,
]

llm_with_tools = llm.bind_tools(tools)

if __name__ == "__main__":
    result = llm_with_tools.invoke(messages)
    print(result)
