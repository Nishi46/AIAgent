from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector import retriever
model = OllamaLLM(
  model = "llama3.2"
)

template = """
You are an expert in answering in questions about a pizza resturant.

Here are some relevant reviews : {reviews}

Here is the question to answer : {question}
"""

prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model 

while True:
  print("\n\n---------------------------------------")
  question = input("Ask your questions(q to quit): ")
  print("\n\n")
  if question == "q": break 
  reviews = retriever.invoke(question)
  result = chain.invoke({"reviews":reviews,"question":question})
  print(result)