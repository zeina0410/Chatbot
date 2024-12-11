from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import json

model_name = "facebook/blenderbot-400M-distill"
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

conversation_history = []

def handle_prompt(data):
    data = json.loads(data)
    input_text = data['prompt']

    history = "\n".join(conversation_history)

    inputs = tokenizer.encode_plus(history, input_text, return_tensors="pt")

    outputs = model.generate(**inputs, max_length= 60) 
    
    print("hello")
    response = tokenizer.decode(outputs[0], skip_special_tokens=True).strip()

    conversation_history.append(input_text)
    conversation_history.append(response)

    return response