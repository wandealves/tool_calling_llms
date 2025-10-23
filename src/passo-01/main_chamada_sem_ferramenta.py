from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.messages import (
    BaseMessage,
    HumanMessage,
    SystemMessage,
)
from rich import print

load_dotenv()


llm = init_chat_model("gpt-4o-mini", temperature=0)
system_message = SystemMessage(
    content=""" Você é um assistente de matemática prestativo. Você tem acesso a ferramentas. 
                Quando o usuário pedir algo, primeiro verifique se você possui uma ferramenta que resolva esse problema."""
)
human_message = HumanMessage("Oi eu sou Goku")
messages: list[BaseMessage] = [
    system_message,
    human_message,
]

if __name__ == "__main__":
    result = llm.invoke(messages)
    print(result)
