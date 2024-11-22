import streamlit as st
from main import analyze_seo  # Import your backend functions

# Streamlit App Title
st.title("SEO Analyzer Tool")
st.write("Upload a text file to analyze its SEO metrics, including keyword density, n-grams, and readability scores.")

# File Upload Section
uploaded_file = st.file_uploader("Upload a Text File", type=["txt"])

if uploaded_file is not None:
    # Save uploaded file content as text
    text_file_path = "uploaded_file.txt"
    with open(text_file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    # Run SEO analysis
    st.write("Analyzing the uploaded file...")
    seo_results = analyze_seo(text_file_path)

    # Display Results
    st.subheader("Results")

    # Keyword Density
    st.write("### Keyword Density")
    keyword_density = seo_results["Keyword Density"]
    keyword_density_sorted = dict(sorted(keyword_density.items(), key=lambda x: x[1], reverse=True)[:10])  # Top 10 keywords
    st.table(keyword_density_sorted)

    # Top Bigrams
    st.write("### Top Bigrams")
    bigrams = seo_results["Top Bigrams"]
    st.table(bigrams)

    # Top Trigrams
    st.write("### Top Trigrams")
    trigrams = seo_results["Top Trigrams"]
    st.table(trigrams)

    # Readability Scores in Tabs
    st.write("### Readability Scores")
    readability_scores = seo_results["Readability Scores"]

    # Create Tabs for Readability Metrics
    tab1, tab2, tab3 = st.tabs(["Flesch Reading Ease", "Gunning Fog Index", "Average Sentence Length"])

    with tab1:
        st.metric(label="Flesch Reading Ease", value=readability_scores["Flesch Reading Ease"])
        st.write(
            """
            **Interpretation:**
            - 90-100: Very easy to read (e.g., for children).
            - 60-70: Standard readability (e.g., high school level).
            - 0-30: Very difficult to read (e.g., academic papers).
            """
        )

    with tab2:
        st.metric(label="Gunning Fog Index", value=readability_scores["Gunning Fog Index"])
        st.write(
            """
            **Interpretation:**
            - 6-10: Easy to read (e.g., general audience).
            - 11-15: Harder to read (e.g., college level).
            - >15: Very complex (e.g., academic or professional documents).
            """
        )

    with tab3:
        st.metric(label="Average Sentence Length", value=round(readability_scores["Average Sentence Length"], 2))
        st.write(
            """
            **Interpretation:**
            - Shorter sentences are easier to read.
            - Aim for an average sentence length of 15-20 words for general audiences.
            """
        )