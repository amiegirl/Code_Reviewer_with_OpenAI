from openai import OpenAI
import streamlit as st

f = open('keys/.openai_api_key.txt')
OPENAI_API_KEY = f.read()

# Read the API key and setup a OpenAI client
client = OpenAI(api_key = OPENAI_API_KEY)

#########################################
st.snow()

# set page title
st.title(":blue[Review your Python Code with OpenAI]")
#########################################

# Take user's input
st.subheader(":lemon[Review Python Code]", divider="blue")
prompt = st.text_area("Enter your Python code here...", height=100)

# If the button is clicked, generate responses
if st.button("Review Code") == True:
    
    response = client.chat.completions.create(
      model="gpt-3.5-turbo",
      messages=[
        {"role": "system", "content": """You are a helpful AI assistant. 
                                        Given a Python code,
                                        you always generate a list of mistakes in the code
                                        and correct the mistakes in the code"""},
        {"role": "user", "content": prompt}
      ],
      max_tokens=500
    )

    # Print the responses
    st.write(response.choices[0].message.content)