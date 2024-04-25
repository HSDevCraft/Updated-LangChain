from fastapi import FastAPI, Request
import uvicorn
from langchain_community.llms import Ollama, CTransformers
from langchain.prompts import ChatPromptTemplate
from langserve import add_routes
import os


app = FastAPI(
    title = "LangChain Server",
    version = "1.0",
    description = "This is a LangChain Server"
)

llama_llm = CTransformers(model='TheBloke/Llama-2-7B-GGUF', model_file='llama-2-7b.Q4_K_M.gguf')
gpt2_llm = CTransformers(model="marella/gpt-2-ggml")

# llama_llm = Ollama(model = "llama2")
# phi_llm = Ollama(model = "phi")
# qwen_llm = Ollama(model = "qwen")

prompt = ChatPromptTemplate.from_template("{query}")

print(prompt)

add_routes(
    app,
    prompt|llama_llm,
    path = "/llama"
)

add_routes(
    app,
    prompt|gpt2_llm,
    path = "/gpt2"
)

# add_routes(
#     app,
#     prompt|phi_llm,
#     path = "/phi"
# )

# add_routes(
#     app,
#     prompt|qwen_llm,
#     path = "/qwen"
# )

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=5000)

