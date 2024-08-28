import erniebot


# List supported models
models = erniebot.Model.list()

print(models)
# ernie-3.5               文心大模型（ernie-3.5）
# ernie-3.5-8k            文心大模型（ernie-3.5-8k）
# ernie-lite              文心大模型（ernie-lite）
# ernie-4.0               文心大模型（ernie-4.0）
# ernie-4.0-turbo-8k      文心大模型（ernie-4.0-turbo-8k）
# ernie-speed             文心大模型（ernie-speed）
# ernie-speed-128k        文心大模型（ernie-speed-128k）
# ernie-tiny-8k           文心大模型（ernie-tiny-8k）
# ernie-char-8k           文心大模型（ernie-char-8k）
# ernie-text-embedding    文心百中语义模型
# ernie-vilg-v2           文心一格模型

# Set authentication params
erniebot.api_type = "aistudio"
erniebot.access_token = "371eb4f8adc3b9df566d884c6621f2a326a8a1aa"

# Create a chat completion
# response = erniebot.ChatCompletion.create(model="ernie-3.5", messages=[{"role": "user", "content": "你好，请介绍下你自己"}])

# print(response.get_result())

# from erniebot.client import ErnieClient

# def get_ernie_response(prompt):
#     ernie_client = ErnieClient(api_key="your_api_key_here")
#     response = ernie_client.generate_text(
#         prompt=prompt,
#         max_tokens=100,
#         temperature=0.7,
#         top_p=0.9,
#         num_return_sequences=1
#     )
#     return response.generated_text[0]


def get_ernie_response(prompt):
    # erniebot.ChatCompletion.create(model="ernie-3.5", messages=[{"role": "user", "content": "你好，请介绍下你自己"}])
    response = erniebot.ChatCompletion.create(
        model="ernie-3.5",
        messages=[{"role": "user", "content": prompt}],
        max_output_tokens=100,
        temperature=0.7,
        top_p=0.9
    )
    print(response.get_result())
    return response.get_result()

# get_ernie_response("你好呀")