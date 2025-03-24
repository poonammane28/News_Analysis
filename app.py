import json
import gradio as gr
from gtts import gTTS
from transformers import pipeline
from utils import fetch_news, analyze_sentiment, translate_to_hindi

# Initialize Sentiment Analysis Model
sentiment_pipeline = pipeline("sentiment-analysis")

def process_company_news(company_name):
    articles = fetch_news(company_name)
    structured_data = []

    for article in articles[:10]:
        title, summary = article["title"], article["description"]
        sentiment = analyze_sentiment(summary, sentiment_pipeline)

        structured_data.append({"Title": title, "Summary": summary, "Sentiment": sentiment})

    # Convert Summary to Hindi Speech
    text_to_speech = "\n".join(
        [translate_to_hindi(f"{art['Title']} - {art['Summary']} - Sentiment: {art['Sentiment']}") for art in structured_data]
    )
    
    tts = gTTS(text=text_to_speech, lang="hi")
    tts.save("output.mp3")

    return json.dumps(structured_data, indent=4), "output.mp3"

# Gradio UI
iface = gr.Interface(fn=process_company_news, 
                     inputs=gr.Textbox(label="Enter Company Name"),
                     outputs=[gr.Textbox(label="News Summary (English)"), gr.Audio(label="Hindi TTS Output")])

if __name__ == "__main__":
    iface.launch()
