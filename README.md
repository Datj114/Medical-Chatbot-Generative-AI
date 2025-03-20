Dưới đây là phiên bản trình bày lại file `README.md` của bạn, rõ ràng và dễ đọc hơn:  

---

# **Medical Chatbot Generative AI**  

🚀 **Medical-Chatbot-Generative-AI** là một chatbot y tế sử dụng AI tổng hợp, hỗ trợ xử lý ngôn ngữ tự nhiên (NLP) để phân tích và phản hồi câu hỏi liên quan đến y tế.  

## **🚀 Cài đặt Môi Trường**  

### **1️⃣ Tạo môi trường Conda**  
```bash
conda create -n medibot python=3.10 -y
```

### **2️⃣ Kích hoạt môi trường Conda**  
```bash
conda activate medibot
```

### **3️⃣ Cài đặt các thư viện cần thiết**  
```bash
pip install -r requirements.txt
```

---

## **📦 Danh sách Thư viện Sử Dụng**  

| 📌 **Thư viện**               | 🔍 **Chức năng** |
|-------------------------------|------------------------------------------------|
| **sentence-transformers==2.2.2**  | Xử lý văn bản, tạo embedding, hỗ trợ NLP. |
| **langchain**                  | Xây dựng ứng dụng AI dùng LLM, hỗ trợ RAG. |
| **flask**                      | Framework web để triển khai API chatbot. |
| **pypdf**                      | Đọc, trích xuất văn bản từ file PDF. |
| **python-dotenv**               | Quản lý biến môi trường `.env`, bảo mật API key. |
| **pinecone[grpc]**              | Cơ sở dữ liệu vector để tìm kiếm embedding nhanh. |
| **langchain-pinecone**          | Kết nối LangChain với Pinecone để tìm kiếm dữ liệu. |
| **langchain_community**         | Các công cụ mở rộng cho LangChain. |
| **langchain_openai**            | Kết nối LangChain với API OpenAI (GPT-4, GPT-3.5). |
| **langchain_experimental**      | Các tính năng thử nghiệm mới của LangChain. |

---

## **🚀 Hướng Dẫn Sử Dụng**  
1️⃣ **Chạy server Flask**  
```bash
python app.py
```
2️⃣ **Gửi request API đến chatbot** (Ví dụ với `cURL`)  
```bash
curl -X POST "http://localhost:5000/chat" -H "Content-Type: application/json" -d '{"message": "Triệu chứng của cảm cúm là gì?"}'
```
3️⃣ **Nhận phản hồi từ AI** 🎯  

---

## **📌 Ứng Dụng Thực Tế**  
✅ Hỗ trợ tư vấn y tế tự động.  
✅ Tìm kiếm tài liệu y khoa theo ngữ nghĩa.  
✅ Tích hợp vào hệ thống chatbot chăm sóc sức khỏe.  

📌 **Cần hỗ trợ?** Đóng góp ý tưởng hoặc báo lỗi [tại đây](#). 🚀