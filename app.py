import streamlit as st
from openai import OpenAI

# Initialize OpenAI client
client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key="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"
)

# Streamlit UI
st.title("GPU-Powered Limerick Generator")
st.markdown("### Write a limerick about the wonders of GPU computing!")

# Input prompt
user_input = st.text_input("Enter your limerick theme:", "GPU computing")

# Generate limerick on button click
if st.button("Generate Limerick"):
    with st.spinner("Generating..."):
        completion = client.chat.completions.create(
            model="meta/llama-3.1-405b-instruct",
            messages=[{"role": "user", "content": f"Write a limerick about {user_input}"}],
            temperature=0.2,
            top_p=0.7,
            max_tokens=1024,
            stream=True
        )

        limerick = ""
        for chunk in completion:
            if chunk.choices[0].delta.content is not None:
                limerick += chunk.choices[0].delta.content

        # Display the generated limerick
        st.text_area("Generated Limerick:", limerick, height=200)
