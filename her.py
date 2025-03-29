import os

from typing import List
from openai import OpenAI

from dotenv import load_dotenv
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

role = """
You are a helpful assistant that helps with writing emails.
In you role, you are responsible for reading the title and description of a
a few papers and then showing interest in the author's work.

you will receive the resume of the applicant and your summary and the output
must relate the background of the applicant to the papers and show interest
in the author's work and say it's a good fit for the author's work.
"""

prompt = """

here's the resume of the applicant:

{resume}

here's the title and abstract of the papers:

{papers}

Use the resume information and the abstract and title of the papers to write 50 words that will be sent to the author.

in these 50 words, you must mentions the author's works and how my background is a good fit for the author's research.
you sentences must be just related to this and not anything else.

Just write these 50 words, don't write anything else.

"""


class Her:
    def __init__(self):
        self.client = OpenAI(api_key=OPENAI_API_KEY)

    def write_email(self, resume: str, papers: List[dict[str, str]]) -> str:
        
        papers_str = ""
        for paper in papers:
            papers_str += f"Title: {paper['title']}\Abstract: {paper['description']}\n\n"
        
        context = resume
        query = prompt.format(resume=resume, papers=papers_str)
        
        response = self.client.chat.completions.create(
            model="gpt-4o",
            messages=[
            {"role": "system", "content": role},
            {"role": "user",
              "content": f"Context: {context}\n\n{query}"}
            ]
        )
        return response.choices[0].message.content
