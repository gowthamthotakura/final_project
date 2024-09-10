import requests
import json


def emotion_detector(text_to_analyze):
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(URL, json = input_json, headers=header)
    return response.text

    if response.status_code == 200:
        return formated_response
    elif response.status_code == 400:
        formated_response = {
                            'anger': anger_score,
                            'disgust': disgust_score, 
                            'fear': fear_score, 
                            'joy': joy_score, 
                            'sadness': sadness_score, 
                            'dominant_emotion': '<name of the dominant emotion>'
        }
        return formated_response
        



         

