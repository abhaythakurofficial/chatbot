import streamlit as st
import requests
import json

url = "https://openrouter.ai/api/v1/chat/completions"
api = st.secrets("Chatbot_Api")

def chat(user_input):
    headers = {
        "Authorization": f"Bearer {api}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "mistralai/mistral-small-3.1-24b-instruct:free",
        "messages": [
            {"role": "user", "content": user_input}
        ],
        "reasoning": {
            "effort": "high"
        }
    }
    response = requests.post(url, headers=headers, data=json.dumps(payload))

    str_resp = json.dumps(response.json())

    dic_resp = json.loads(str_resp)
    
    result = dic_resp["choices"][0]["message"]["content"]
    
    return result

if "message" not in st.session_state:
    st.session_state.message=[]

for mess in st.session_state.message:
    if mess['role'] =='user':
        st.write(f"🥰 You: {mess['content']}")
    else:
        st.write(f"😉 Bot: {mess['content']}")


user_input = st.chat_input("ask somethinkg...")
if user_input:
    bot_response = chat(user_input)
    st.session_state.message.append({'role':'user','content':user_input})
    st.write(f"🥰 You:{user_input}")
    st.session_state.message.append({'role':'bot','content':bot_response})
    st.write(f"😉 Bot: {bot_response}")
    
    


