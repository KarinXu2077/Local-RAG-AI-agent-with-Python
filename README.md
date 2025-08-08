# 🏠 Local RAG Chatbot – “New-Grad-Friendly Companies”  
A tiny, fully-offline Retrieval-Augmented-Generation (RAG) demo built with **Python + LangChain + Ollama + ChromaDB**


## ✨ What you’ll get
| Feature | In plain English |
|---------|------------------|
| **100 % local** | No key, no cloud fees, no data leakage. Everything runs on your laptop. |
| **Ask about companies** | Queries are answered using a CSV (`ng_friendly_companies.csv`) that lists visa-sponsor / new-grad-friendly companies. |
| **RAG pipeline** | CSV 👉 text chunks 👉 embeddings (Ollama) 👉 Chroma vector store 👉 retrieved context 👉 local LLM answer. |
| **< 150 loc** | Only two Python scripts (`vector.py`, `main.py`) – easy to read, fork, or extend. |
| **Engineer-ready** | Shows how to glue together Ollama, LangChain, and Chroma – a bread-and-butter skill for any Gen-AI engineer in 2025. |

## 🔧 Project structure
├── ng_friendly_companies.csv # dataset used in the project
├── vector.py # builds / updates the local Chroma DB
├── main.py # CLI chatbot: Retrieval + LLM answer
└── README.md # you are here

Example:
Ask your question about companies (q to quit): recommend tech companies which are ng friendly and sponsor H1B   



I can help you with that. Here are some New Graduate (NG) friendly tech companies that sponsor H1B visas:

**Note:** This list may not be exhaustive, and the sponsorship status of companies can change over time.

1. **Microsoft**: Offers internships to recent graduates through their **Microsoft Internship Program**, which has been a popular choice for new grads.
2. **Amazon**: Provides various internship programs for new graduates, including the **Amazon Software Development Internship** and the **Amazon Data Science Internship**.
3. **Google**: Offers internships and full-time positions to recent graduates through their **Google Career Certificates**, which are designed to help students transition into in-demand tech careers.
4. **Facebook**: Has a variety of internship programs, including the **Facebook Engineering Internship Program**, which offers new grads the opportunity to work on real projects.
5. **Palantir**: Offers internships and full-time positions to recent graduates through their **Palantir Internship Program**, which provides hands-on experience with data analysis and software development.
6. **Salesforce**: Has a comprehensive internship program, including the **Salesforce Internship Program**, which offers new grads the chance to work on innovative projects and develop valuable skills.
7. **VMware**: Offers internships and full-time positions to recent graduates through their **VMware Internship Program**, which provides experience in software development, engineering, and more.
8. **Cisco Systems**: Provides various internship programs for new graduates, including the **Cisco Internship Program**, which offers hands-on experience with networking, cybersecurity, and other areas of interest.
9. **IBM**: Offers internships and full-time positions to recent graduates through their **IBM New Collar Internship Program**, which provides training and development opportunities in emerging tech fields.
10. **Dell Technologies**: Has a range of internship programs for new graduates, including the **Dell Technologies Internship Program**, which offers experience with software development, IT infrastructure, and more.

Please note that these companies often have specific requirements and qualifications for their internships or full-time positions, so it's essential to review their websites and job listings carefully.

🛠 Customising
you can replace csv with your own files, use any model available in ollama list, swap input loop for FastAPI, Flask or Streamlit

📚 Takeaways
1. Ollama – run biggish models locally without Docker headaches.
2. LangChain modules – how to glue an embeddings model, vector store, and LLM together.
3. ChromaDB – simplest local vector store for quick hacks.

🙏 Credits
ng_friendly_companies.csv is a hypothetical sample dataset for demo purposes only.

Feel free to fork, open issues, or submit PRs — every tweak helps solidify those skills!
