from openai import AzureOpenAI
import os

#Client is a variable
client = AzureOpenAI(
	api_key = os.getenv("AZURE_KEY"),
	azure_endpoint = os.getenv("AZURE_ENDPOINT"),
	api_version = "2023-10-01-preview" 
)

#BOT response
#"Pink is the best-pink"

def get_response(question):
	my_messages = [
	{"role":"system","content":"Tell me your answer, then after a hyphen, say the selected color as one word"},
	{"role":"user","content":question}
	]

	response = client.chat.completions.create(
		model = "GPT-4",
		messages = my_messages
	)

	return response.choices[0].message.content