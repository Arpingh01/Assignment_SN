import google.generativeai as genai

# Gemini API key
genai.configure(api_key="AIzaSyB8hSdTnxtL8SpnJcgRNQIKQlM1R7tLMT4")

#original chapter text
with open("chapter1_text.txt", "r", encoding="utf-8") as file:
    original_text = file.read()

model = genai.GenerativeModel("models/gemini-1.5-flash")

# Agent Functions #
def ai_writer(input_text):
    prompt = f"""You are an AI Writer. Rewrite the following chapter in modern, vivid, descriptive English. 
    Preserve the original meaning and scene structure. Do not add or skip content.\n\n{input_text}"""
    response = model.generate_content(prompt)
    spun_text = response.text.strip()
    with open("chapter1_spun.txt", "w", encoding="utf-8") as f:
        f.write(spun_text)
    return spun_text

def ai_reviewer(spun_text):
    prompt = f"""You are an expert AI Reviewer. Refine the following rewritten chapter by fixing grammar, 
    enhancing flow, and polishing transitions. Do not change meaning.\n\n{spun_text}"""
    response = model.generate_content(prompt)
    refined_text = response.text.strip()
    with open("chapter1_refined.txt", "w", encoding="utf-8") as f:
        f.write(refined_text)
    return refined_text

def human_editor(refined_text):
    # Simulate final human edit
    final_text = refined_text + "\n\n[Final edit complete. Ready for versioning.]"
    with open("chapter1_final.txt", "w", encoding="utf-8") as f:
        f.write(final_text)
    return final_text

# Agentic Pipeline #
def run_pipeline(input_text):
    spun = ai_writer(input_text)
    reviewed = ai_reviewer(spun)
    final = human_editor(reviewed)
    return final

# Run the pipeline
final_output = run_pipeline(original_text)
print("chapter1_final.txt")

