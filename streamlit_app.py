import streamlit as st

st.set_page_config(page_title="TextSummary Stack", layout="wide")
st.title("🧠 TextSummary-Streamlit-HuggingFace-Stack")

providers_solutions = {
    "HuggingFace": [
        "Text Summarization",
        "Chat with Model",
        "File Upload"
    ],
    "Google": [
        "Text Summarization",
        "Natural Language Understanding",
        "Translation"
    ],
    "Microsoft": [
        "Text Summarization",
        "Language Understanding",
        "Speech-to-Text"
    ]
}

st.markdown("### Select a Solution Provider:")

for provider, solutions in providers_solutions.items():
    st.markdown(f"## 🏢 {provider}")
    cols = st.columns(3)
    for i, solution in enumerate(solutions):
        with cols[i % 3]:
            st.markdown(
                f"""
                <div style='background:#f7f7f7;padding:20px;border-radius:10px;
                           box-shadow:0 2px 5px rgba(0,0,0,0.1);text-align:center'>
                    <h4>{solution}</h4>
                    <a href="/{provider}_{solution.replace(' ', '_')}" 
                       target="_self"
                       style='text-decoration:none;color:white;'>
                        <button style='margin-top:10px;
                                       padding:10px 15px;
                                       border:none;
                                       background-color:#4CAF50;
                                       border-radius:8px;
                                       color:white;
                                       cursor:pointer;'>
                            Open
                        </button>
                    </a>
                </div>
                """,
                unsafe_allow_html=True
            )
