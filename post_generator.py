import llm_helper
from few_short import FewshotPosts

# Load your few-shot examples from processed posts
few_Shot = FewshotPosts()

def gen_length_str(length):
    if length == "short":
        return "1 to 5 lines"
    elif length == "medium":
        return "6 to 10 lines"
    elif length == "long":
        return "11 to 15 lines"
    else:
        raise ValueError("Invalid length specified.")

def get_prompt(length, language, tag):
    length_str = gen_length_str(length)  # Convert length to human-readable format

    prompt = f'''
Generate a LinkedIn post using the below information. No preamble.

1) Topic: {tag}
2) Length: {length_str}
3) Language: {language}
If Language is Hinglish then it means it is a mix of Hindi and English.
The script for the generated post should always be English.
'''

    examples = few_Shot.get_filtered_posts(length, language, [tag])  # tag should be a list
    if len(examples) > 0:
        prompt += "\n4) Use the writing style similar to the following examples:\n"
        for i, post in enumerate(examples):
            post_text = post['text']
            prompt += f"\n\nExample {i+1}:\n{post_text}\n"
            if i == 1:
                break  # Limit to 3 examples

    return prompt  

def generate_post(length, language, tag):
    prompt = get_prompt(length, language, tag)
    response = llm_helper.llm.invoke(prompt)  # LLM must receive a string
    return response.content

if __name__ == "__main__":
    post = generate_post("short", "English", "Criticism")
    print("\nGenerated Post:\n")
    print(post)
