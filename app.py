import chainlit as cl

from llama_index.core import StorageContext, load_index_from_storage
from llama_index.core import Settings

from llama_index.llms.gemini import Gemini
from llama_index.embeddings.gemini import GeminiEmbedding

GOOGLE_API_KEY = "AIzaSyD4K9-x9lx8pef5zVr5wzHTcl47u7_pZlk"


# Chainlit session setting
@cl.on_chat_start
async def start():
    # Setting llama index llm and embedding
    embed_model = GeminiEmbedding(
        model_name="models/text-embedding-004",
        api_key=GOOGLE_API_KEY,
    )
    llm = Gemini(
        model="models/gemini-2.5-flash",
        api_key=GOOGLE_API_KEY,
    )
    Settings.llm = llm
    Settings.embed_model = embed_model

    # Create vector database
    storage_context = StorageContext.from_defaults(persist_dir="./index")
    index = load_index_from_storage(storage_context)

    # Store the index globally to use in other parts of the app
    cl.user_session.set("index", index)


# Query the index with user input and return a response
@cl.on_message
async def message(message: cl.Message):
    # Retrieve the stored index
    index = cl.user_session.get("index")

    # Create a query engine
    chat_engine = index.as_chat_engine(streaming=True, similarity_top_k=10)

    # Run the query
    response = chat_engine.query(message.content)

    # Stream the response in Chainlit
    msg = cl.Message(content="")
    for token in response.response:
        await msg.stream_token(token)
    await msg.send()
