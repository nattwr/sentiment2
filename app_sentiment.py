import streamlit as st
import pickle

# Load the trained sentiment analysis model
with open('sentiment_pipeline_model.pkl', 'rb') as file:
    sentiment_pipeline = pickle.load(file)

# Streamlit app
st.title("Sentiment Analysis")

# Text input for sentiment analysis
text_input = st.text_area("Enter text for sentiment analysis")

if st.button("Analyze Sentiment"):
    # Predict sentiment
    predictions = sentiment_pipeline.predict([text_input])
    sentiment = predictions[0]

    # Display result as progress bars
    st.subheader("Sentiment Analysis Result:")

    if sentiment == 'pos':
        st.success(f"Positive Sentiment")
        st.progress(1.0)
    elif sentiment == 'neg':
        st.error(f"Negative Sentiment")
        st.progress(1.0)
    else:
        st.warning(f"Neutral Sentiment{sentiment}.")
        st.progress(1.0)
