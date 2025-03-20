from flask import Flask, render_template, jsonify, request
from langchain_community.llms import HuggingFaceHub 
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from src.prompt import *
import os
from langchain_pinecone import PineconeVectorStore
from src.helper import download_hugging_face_embeddings
from src.prompt import system_prompt

app = Flask(__name__)

load_dotenv()
PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')
HUGGINGFACEHUB_API_TOKEN=os.environ.get("HUGGINGFACEHUB_API_TOKEN")
os.environ['PINECONE_API_KEY']=PINECONE_API_KEY
os.environ['HUGGINGFACEHUB_API_TOKEN']=HUGGINGFACEHUB_API_TOKEN

index_name = 'medicalbot'
embeddings = download_hugging_face_embeddings()

docsearch = PineconeVectorStore.from_existing_index(
    index_name=index_name,
    embedding = embeddings,
)
retriever=docsearch.as_retriever(search_type="similarity",search_kwargs={"k":3})

llm = HuggingFaceHub(
    
    repo_id="mistralai/Mistral-7B-Instruct-v0.2",  # Chọn mô hình phù hợp
    model_kwargs={"temperature": 0.4, "max_length": 500},
    huggingfacehub_api_token = HUGGINGFACEHUB_API_TOKEN
)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system",system_prompt),
        ("human","{input}")
    ]
)
question_answer_chain = create_stuff_documents_chain(llm, prompt)
rag_chain = create_retrieval_chain(retriever, question_answer_chain)


@app.route('/')
def index():
    return render_template('chat.html')

@app.route('/get', methods=['POST'])
def chat():
    try:
        msg = request.form.get('msg', '').strip()  # Lấy dữ liệu từ form và loại bỏ khoảng trắng
        if not msg:
            return jsonify({"answer": "Bạn chưa nhập tin nhắn!"})

        print("User input:", msg)
        response = rag_chain.invoke({"input": msg})  # Gọi mô hình xử lý
        bot_reply = response.get('answer', 'Xin lỗi, tôi không hiểu.')  # Lấy câu trả lời từ RAG

        print("Bot response:", bot_reply)
        return jsonify({"answer": bot_reply})  # Trả về JSON

    except Exception as e:
        print("Error:", str(e))
        return jsonify({"answer": "Có lỗi xảy ra, vui lòng thử lại."})

if __name__ == "__main__":
    app.run(debug=True)