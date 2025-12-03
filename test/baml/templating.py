from app.baml_client import b
from typing import TypedDict, List

from app.prompting.prompts import Prompts


class Content(TypedDict):
    text: str

class Input(TypedDict):
    content: List[Content]

class Result(TypedDict):
    input: List[Input]

resume = """
  Vaibhav Gupta
  vbv@boundaryml.com

  Experience:
  - Founder at BoundaryML
  - CV Engineer at Google
  - CV Engineer at Microsoft

  Skills:
  - Rust
  - C++
"""




if __name__ == "__main__":
    print(b.request.ExtractResume(resume))
    prompts = Prompts(b)
    print(prompts.extract_resume(resume))

    print(prompts.visual_verifier)

    print(prompts.analysis_description)