from openai import OpenAI
client = OpenAI(api_key= 'OPENAI_API_KEY')

response = client.images.generate(
  model="dall-e-3",
  prompt="a photograph of an astronaut riding a horse",
  size="1024x1024",
  quality="standard",
  n=1,
)

image_url = response.data[0].url
print(image_url)
