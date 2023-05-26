# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: b3_try_chatbot.py
@Time: 2023-03-03 16:54
@Last_update: 2023-03-03 16:54
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
import gradio as gr
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-medium")
model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-medium")


def predict(input, history=[]):
    # tokenize the new input sentence
    print(input)
    print(tokenizer.eos_token)
    new_user_input_ids = tokenizer.encode(input + tokenizer.eos_token, return_tensors='pt')

    # append the new user input tokens to the chat history
    bot_input_ids = torch.cat([torch.LongTensor(history), new_user_input_ids], dim=-1)

    # generate a response
    history = model.generate(bot_input_ids, max_length=1000, pad_token_id=tokenizer.eos_token_id).tolist()

    # convert the tokens to text, and then split the responses into lines
    response = tokenizer.decode(history[0]).split("<|endoftext|>")
    response = [(response[i], response[i + 1]) for i in range(0, len(response) - 1, 2)]  # convert to tuples of list
    return response, history


with gr.Blocks(css="#chatbot .overflow-y-auto{height:500px}") as demo:
    chatbot = gr.Chatbot(elem_id='chatbot')
    state = gr.State([])

    with gr.Row():
        txt = gr.Textbox(show_label=False, placeholder="Enter text and press enter").style(container=False)

    txt.submit(predict, [txt, state], [chatbot, state])


if __name__ == '__main__':
    demo.launch()
