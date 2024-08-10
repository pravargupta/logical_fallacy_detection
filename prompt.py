import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(input)
    return response.text

def read_text():
    f = open("output.txt", "r")
    text = f.read()
    f.close()
    return text

default_prompt = '''You are a logical fallacy detective and should tell all the logical fallacies in the following text using some of the context here:
Types of fallacies:
1. Ad hominem -> attacking the person instead of the argument
2. Appeal to authority -> using an authority figure to validate an argument
3. False cause -> assuming a cause and effect relationship without evidence
4. Hasty generalization -> making a generalization based on insufficient evidence
5. Slippery slope -> assuming a small action will lead to a large and negative outcome
6. Strawman -> misrepresenting an argument to make it easier to attack
7. Bandwagon -> using popularity as a reason to believe something
8. Black or white -> presenting only two options when there are more
9. False dilemma -> presenting only two options when there are more
10. Red herring -> introducing irrelevant information to distract from the argument
11. Appeal to emotion -> manipulating emotions to win an argument
12. Tu quoque -> avoiding the argument by pointing out hypocrisy
13. Burden of proof -> shifting the burden of proof to the other side
14. No true Scotsman -> dismissing counterexamples by changing the definition
15. Personal incredulity -> saying something is false because you can't believe it
16. Genetic -> dismissing an argument based on its source
17. Middle ground -> assuming the middle ground between two extremes is the truth
18. Anecdotal -> using personal experience as evidence
19. Appeal to nature -> assuming something is good because it's natural
20. Appeal to tradition -> assuming something is good because it's traditional
21. Begging the question -> assuming the conclusion in the premise
22. Circular -> using the conclusion as evidence for the conclusion
23. False analogy -> assuming two things are alike in all aspects
24. Equivocation -> using the same term in different ways
25. Loaded question -> asking a question that assumes a conclusion
26. Special pleading -> applying different standards to different things
27. Appeal to fear -> using fear to win an argument
28. False balance -> presenting two sides as equally valid when they're not
 and so on ... help detect conspiracy theories, misinformation, and logical fallacies in the text below:

'''

def main():
    text = default_prompt + read_text()
    response = get_gemini_response(text)
    print(response)