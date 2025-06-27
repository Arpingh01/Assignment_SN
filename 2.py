import google.generativeai as genai

genai.configure(api_key="AIzaSyB8hSdTnxtL8SpnJcgRNQIKQlM1R7tLMT4")

# Load the original text
with open("chapter1_text.txt", "r", encoding="utf-8") as file:
    original_text = file.read()

# Step 1: AI Writer
writer_prompt = f"""
You are an AI Writer. Rewrite the following chapter in modern, vivid, descriptive English.
Preserve the original meaning and scene structure. Do not add or skip content.

{original_text}
"""

# Use the lightweight model
model = genai.GenerativeModel(model_name="models/gemini-1.5-flash")

# Generate rewritten content
writer_response = model.generate_content(writer_prompt)
spun_text = writer_response.text.strip()

# Save spun text
with open("chapter1_spun.txt", "w", encoding="utf-8") as f:
    f.write(spun_text)
print("✅ Rewritten (spun) chapter saved as 'chapter1_spun.txt'.")

# Step 2: AI Reviewer
reviewer_prompt = f"""
You are an expert AI Editor. Carefully review and improve the following rewritten chapter.
Fix grammar, enhance readability, polish transitions, but do not change meaning or tone.

{spun_text}
"""

reviewer_response = model.generate_content(reviewer_prompt)
refined_text = reviewer_response.text.strip()

# Save final reviewed version
with open("chapter1_refined.txt", "w", encoding="utf-8") as f:
    f.write(refined_text)
print("chapter1_refined.txt")






