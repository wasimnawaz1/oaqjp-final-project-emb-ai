import requests
import json

def emotion_detector(text_to_analyze):
    # URL of the emotion detector service
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    
    # Set the headers required for the API request
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # Create a dictionary with the text to be analyzed
    myobj = {"raw_document": {"text": text_to_analyze}}
    
    # Send a POST request to the API with the text and headers
    response = requests.post(url, json=myobj, headers=header)
    
    # Convert the response text to a Python dictionary
    response_dict = json.loads(response.text)
    
    # Navigate into the response JSON to extract emotions
    emotions = response_dict['emotionPredictions'][0]['emotion']
    
    # Extract the required emotions
    anger = emotions['anger']
    disgust = emotions['disgust']
    fear = emotions['fear']
    joy = emotions['joy']
    sadness = emotions['sadness']
    
    # Find the dominant emotion (highest score)
    emotion_scores = {
        'anger': anger,
        'disgust': disgust,
        'fear': fear,
        'joy': joy,
        'sadness': sadness
    }
    dominant_emotion = max(emotion_scores, key=emotion_scores.get)
    
    # Return in the required format
    return {
        'anger': anger,
        'disgust': disgust,
        'fear': fear,
        'joy': joy,
        'sadness': sadness,
        'dominant_emotion': dominant_emotion
    }
