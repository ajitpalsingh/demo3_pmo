import streamlit as st
import pandas as pd
import openai
from genai_engine import prompt_engine

# === Set API key securely ===
openai.api_key = st.secrets["openai_api_key"]

# === UI Layout ===
st.set_page_config(page_title="Gen AI PMO Engine", layout="wide")
st.title("🔍 Gen AI PMO Demo Engine")

# === File Upload ===
uploaded_file = st.file_uploader("📂 Upload your PMO Excel file", type=["xlsx"])

if uploaded_file:
    try:
        # Load all sheets into a dictionary
        df_dict = pd.read_excel(uploaded_file, sheet_name=None)
        sheet_names = list(df_dict.keys())

        # Use Case selection
        use_case = st.selectbox("📊 Choose a Use Case", sheet_names)
        df = df_dict[use_case]

        # Display selected data
        st.subheader("📋 Input Data")
        st.dataframe(df, use_container_width=True)

        # Run Gen AI
        if st.button("🚀 Run Gen AI Analysis"):
            with st.spinner("⏳ Analyzing with GPT-4..."):
                try:
                    csv_text = df.to_csv(index=False)
                    output = prompt_engine(use_case, csv_text)

                    st.subheader("🧠 Gen AI Output")
                    st.markdown(output)

                    # Provide download link
                    st.download_button(
                        label="📥 Download Output",
                        data=output,
                        file_name=f"{use_case}_analysis.txt",
                        mime="text/plain"
                    )
                except Exception as e:
                    st.error(f"❌ OpenAI Error: {str(e)}")

    except Exception as e:
        st.error(f"❌ Excel Read Error: {str(e)}")
else:
    st.info("⬆️ Upload a `.xlsx` file containing PMO sheets like Financials, Timeline, Risks, etc.")