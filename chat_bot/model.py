from groq import Groq
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.memory import ConversationBufferMemory
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from chat_bot.prompt import CUSTOM_PROMPT


class ChatbotModel:
    def __init__(self, api_key):
        self.llm = self.initialize_llm(api_key)
        self.prompt = PromptTemplate(
            input_variables=["chat_history", "question"],
            template=CUSTOM_PROMPT  # Use the imported CUSTOM_PROMPT
        )
        self.memory = ConversationBufferMemory(memory_key="chat_history")
        self.chain = self.create_chain()

    def initialize_llm(self, api_key):
        return ChatGroq(
            api_key=api_key,
            model="llama-3.3-70b-versatile",
            temperature=0,
            max_tokens=None,
            timeout=None,
            max_retries=2,
        )

    def create_chain(self):
        return LLMChain(
            llm=self.llm,
            prompt=self.prompt,
            memory=self.memory
        )

    def ask_chatbot(self, question):
        # Directly pass the question; chat history is handled by memory
        response = self.chain.run({
            "question": question,
            "chat_history": self.memory
        })
        return response