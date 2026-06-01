from openai import OpenAI

class JobDescriptionWriter:
    def __init__(self, ollama_base_url="http://localhost:11434/v1", model_name="llama2"):
        """
        Initialize the JobDescriptionWriter with Ollama.
        
        Args:
            ollama_base_url: The base URL for your local Ollama instance (default: http://localhost:11434/v1)
            model_name: The name of the Llama model to use (default: llama2)
                       Available models: llama2, neural-chat, mistral, etc.
                       Make sure the model is pulled in Ollama: `ollama pull <model_name>`
        """
        self.client = OpenAI(
            api_key="ollama",  # Ollama doesn't require a real API key
            base_url=ollama_base_url
        )
        self.model_name = model_name

    def read_cv(self):
        with open('cv.txt','r') as file:
            cv = file.read()
            return cv

    def compose_presentation_letter(self, description):
        """
        Generate a personalized cover letter based on job description.
        """
        cv = self.read_cv()
        print(cv)
        completion = self.client.chat.completions.create(
            model=self.model_name,
            messages=[
                {"role": "system", "content": "You are an eloquent writer with skills to write excellent and persuasive texts. (MAXIMUM 50 WORDS.)"},
                {"role": "user", "content": f"You are a human resource expert responsible for creating presentation letters tailored to specific job descriptions. Your task is to generate a presentation letter based on the following job description:\n\n{description}\n\nJob description: {description}"}
            ],
            temperature=0.7,
            top_p=0.9
        )
        return completion.choices[0].message.content
    
    def evaluation_cv(self, cv, description):
        """
        Evaluate and personalize CV based on job description.
        """
        completion = self.client.chat.completions.create(
            model=self.model_name,
            messages=[
                {"role": "system", "content": "You are a Human resources Manager that analyze CVs for jobs requests.(MAXIMUM 50 WORDS.)"},
                {"role": "user", "content": f"You are a highly experienced human resource manager responsible for evaluating and analyzing CVs for various job positions. Today, you have been assigned to evaluate a CV for the following job description:\n\n{description}\n\nCV:\n{cv}\n\nProvide feedback on how well the CV matches the job requirements."}
            ],
            temperature=0.7,
            top_p=0.9
        )
        return completion.choices[0].message.content
