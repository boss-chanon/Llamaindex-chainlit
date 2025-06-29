from llama_index.core import SimpleDirectoryReader, VectorStoreIndex, Settings
from llama_index.embeddings.gemini import GeminiEmbedding


GOOGLE_API_KEY = ...

DATA_DIR = "./data"
OUTPUT_DIR = "./index"

# Load documents from the directory
documents = SimpleDirectoryReader(
    input_files=["./data/IPCC_AR6_WGII_Chapter03.pdf"]
).load_data()

# Initialize the embedding model
embedding_model = GeminiEmbedding(
    model_name="models/text-embedding-004",
    api_key=GOOGLE_API_KEY,
)
Settings.embed_model = embedding_model

# Create an index
index = VectorStoreIndex.from_documents(documents, show_progress=True)

# Save index
index.storage_context.persist(OUTPUT_DIR)
