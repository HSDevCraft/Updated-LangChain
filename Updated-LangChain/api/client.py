import streamlit as st
import requests

def get_model_response(model_name, prompt):
    response = requests.post(f"http://localhost:5000/{model_name}/invoke", json={"input": {"topic": prompt}})
    return response.json()

st.title("Langserve API Demo")

prompt = st.text_input("Enter your prompt...")

# selected_model = st.sidebar.radio("Select Model", ("llama", "phi", "qwen"))
selected_model = st.sidebar.radio("Select Model", ("llama", "gpt2"))

if st.button("Get Response"):
    if selected_model == "llama":
        response = get_model_response("llama", prompt)
    elif selected_model == "gpt2":
        response = get_model_response("gpt2", prompt)["output"]
    else:
        response = "Invalid model selected"
    
    st.write("Response:")
    st.write(response)

# if st.button("Get Response"):
#     if selected_model == "llama":
#         response = get_model_response("llama", prompt)
#     elif selected_model == "phi":
#         response = get_model_response("phi", prompt)
#     elif selected_model == "qwen":
#         response = get_model_response("qwen", prompt)
#     else:
#         response = "Invalid model selected"
    
#     st.write("Response:")
#     st.write(response)
