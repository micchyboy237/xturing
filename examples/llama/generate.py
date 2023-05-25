from xturing.models.base import BaseModel

model_path = "./saved_model"

# Load the model
print(f'Load the model')
model = BaseModel.load(model_path)

# Once the model has been finetuned, you can start doing inferences
input = "Why LLM models are becoming so important?"
print(f'Generate output from input: "{input}"')
output = model.generate(texts=[input])
print("Generated output by the model: {}".format(output))
