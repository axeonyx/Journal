from flask import Flask, render_template, request, jsonify
from transformers import AutoModelForSequenceClassification, AutoTokenizer
from torch.nn.functional import softmax
import torch

app = Flask(__name__)

model_name = "j-hartmann/emotion-english-distilroberta-base"
model = AutoModelForSequenceClassification.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

def analyze_sentiment(text):
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True, max_length=512)
    outputs = model(**inputs)
    predictions = softmax(outputs.logits, dim=-1)
    emotion_scores = {model.config.id2label[i]: score.item() for i, score in enumerate(predictions[0])}
    return emotion_scores

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    if request.method == 'POST':
        journal_text = request.form['journal']
        sentiments = analyze_sentiment(journal_text)
        return jsonify({'sentiments': sentiments})

if __name__ == '__main__':
    app.run(debug=True)
