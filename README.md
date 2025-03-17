# Medical-Chatbot-Generative-AI
'''bash
conda create -n medibot python=3.10 -y
'''

'''bash
conda activate medibot

'''

'''bash
pip install -r requirements.txt

'''


## Thư viện
sentence-transformers==2.2.2 – Xử lý và tạo embedding từ văn bản, dùng trong tìm kiếm ngữ nghĩa và NLP.
langchain – Xây dựng ứng dụng AI dùng LLM (như OpenAI, Claude), hỗ trợ truy xuất dữ liệu.
flask – Framework web nhẹ để tạo API cho mô hình AI.
pypdf – Đọc và xử lý file PDF, trích xuất văn bản từ PDF.
python-dotenv – Quản lý biến môi trường từ file .env, giúp bảo mật API key.
pinecone[grpc] – Cơ sở dữ liệu vector để lưu và tìm kiếm embedding nhanh.
langchain-pinecone – Kết nối LangChain với Pinecone để tìm kiếm dữ liệu theo ngữ nghĩa.
langchain_community – Tập hợp các công cụ mở rộng cho LangChain.
langchain_openai – Kết nối LangChain với API của OpenAI (GPT-4, GPT-3.5).
langchain_experimental – Các tính năng thử nghiệm mới của LangChain