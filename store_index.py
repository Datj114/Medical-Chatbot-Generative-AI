from pinecone import Pinecone, ServerlessSpec
import os
from dotenv import load_dotenv
from langchain_pinecone import PineconeVectorStore
from src.helper import text_split,load_pdf_file,download_hugging_face_embeddings


load_dotenv()
PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')
os.environ['PINECONE_API_KEY'] = PINECONE_API_KEY

pc = Pinecone(api_key=PINECONE_API_KEY)
index_name = 'medicalbot'
pc.create_index(name = index_name,dimension = 384, metric='cosine',spec = ServerlessSpec(cloud="aws",region='us-east-1'))

extract_data = load_pdf_file(data='Data/')
text_chunks = text_split(extract_data)
embeddings = download_hugging_face_embeddings()

docsearch = PineconeVectorStore.from_documents(
    documents=text_chunks,
    index_name=index_name,
    embedding = embeddings,
)