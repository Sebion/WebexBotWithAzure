from webex_bot.models.command import Command
from webex_bot.models.response import Response
import openai

class gpt(Command):

    messages = []
    messages.append({"role":"system","content":"You are an AI assistant that helps people find information."})

    def __init__(self):
        super().__init__()

    def execute(self, message, attachment_actions, activity):

        openai.api_type = "azure"
        openai.api_version = "2023-03-15-preview" # for example: 2020-07-01-preview
        openai.api_base = "https://cs-gpt3-research.openai.azure.com/"
        openai.api_key = "fae147496ee146708bac9f46159154a3"

        self.messages.append({"role": "user", "content": message})
        completion = openai.ChatCompletion.create(
        engine="cs-gpt35-turbo",
        messages=self.messages)

        gpt_response=completion.choices[0].message.content
        self.messages.append({"role": "assistant", "content": message})
        return(gpt_response)
