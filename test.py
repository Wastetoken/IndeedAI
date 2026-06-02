from IAscrapped import JobDescriptionWriter

writer = JobDescriptionWriter()

# Real job description example
job_desc = """
Senior Frontend Engineer - Motion & Animation Focus

We're building the next generation of interactive web experiences at a high-growth fintech startup. We need someone who can ship pixel-perfect, performant animations and 3D web experiences.

Requirements:
- 5+ years React experience
- Expert with GSAP, Three.js, or similar animation libraries
- WebGL/shader experience a plus
- Portfolio of shipped work (not just concepts)
- Can lead and mentor junior developers
- Comfortable with fast-paced startup environment

Responsibilities:
- Build animation systems and motion design infrastructure
- Lead frontend architecture decisions
- Mentor team on best practices
- Ship production-grade code on tight timelines
"""

try:
    letter = writer.compose_presentation_letter(job_desc)
    print(letter)
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
