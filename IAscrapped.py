from openai import OpenAI

class JobDescriptionWriter:
    def __init__(self, ollama_base_url="http://localhost:11434/v1", model_name="qwen3-vl:8b"):
        """
        Initialize the JobDescriptionWriter with Ollama.
        
        Args:
            ollama_base_url: The base URL for your local Ollama instance (default: http://localhost:11434/v1)
            model_name: The name of the Llama model to use (default: qwen3-vl:8b)
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
        MUST BE HONEST - reference only actual work, projects, and metrics from Patrick's CV.
        NO EXAGGERATION. NO FABRICATION. SPECIFIC EXAMPLES ONLY.
        """
        cv = self.read_cv()
        print(cv)
        completion = self.client.chat.completions.create(
            model=self.model_name,
            messages=[
                {
                    "role": "system", 
                    "content": """You write honest, direct cover letters. RULES:
1. Reference ONLY actual projects and metrics from the CV provided
2. Use specific names: Singularity, ScrollStudio3D, AURELIAN, Motif, Pat's Pools, Leslie's Pool
3. Use actual numbers: 15% revenue increase, 8% shrink reduction, 20% defect reduction, 90+ weekly services
4. Use real technologies: GSAP, Three.js, WebGL, React, Node.js
5. NO corporate jargon like "innovative," "passionate," "cutting-edge"
6. 3 paragraphs MAX
7. Story-driven, specific to the job
8. Direct tone - no fluff
9. Address what Patrick can SOLVE for them, not generic promises
10. If job doesn't fit Patrick's actual profile, say so honestly
NEVER exaggerate. NEVER fabricate. NEVER claim skills not in the CV."""
                },
                {
                    "role": "user", 
                    "content": f"""CV:
{cv}

JOB DESCRIPTION:
{description}

Write a cover letter for Patrick applying to this role.
Be honest. Reference real work only. Use specific examples.
Maximum 3 paragraphs."""
                }
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
                {"role": "user", "content": f"You are a highly experienced human resource manager responsible for evaluating and analyzing CVs for various job positions. Today, you have been assig[...]"}
            ],
            temperature=0.7,
            top_p=0.9
        )
        return completion.choices[0].message.content
