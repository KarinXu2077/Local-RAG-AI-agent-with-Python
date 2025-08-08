from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector import retriever

model = OllamaLLM(model="llama3.2")

template = """
You are an expert career advisor on new-grad-friendly tech companies

Here are some relevant company profiles: {profiles}

Here is the question to answer: {question}
"""
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

while True:
    print("\n\n-------------------------------")
    question = input("Ask your question about companies (q to quit): ")
    print("\n\n")
    if question == "q":
        break
    
    profiles = retriever.invoke(question)
    result = chain.invoke({"profiles": profiles, "question": question})
    print(result)
