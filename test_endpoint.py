from google import genai

client = genai.Client(
    vertexai=True,
    project="project-32301d32-7dfb-43f1-b1a",
    location="us-central1",
)

response = client.models.generate_content(
    model="projects/project-32301d32-7dfb-43f1-b1a/locations/us-central1/endpoints/3686869745874763776",
    contents="sepal_length: 5.1, sepal_width: 3.5, petal_length: 1.4, petal_width: 0.2"
)

print(response.text)
