# ---------------------------------------------
# Imports and Setup
# ---------------------------------------------
import json
import sys

from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException
from llm_helper import llm  # This should provide a configured LLM object from LangChain

# Reconfigures the terminal output encoding to UTF-8 (especially useful on Windows systems)
sys.stdout.reconfigure(encoding='utf-8')


# ---------------------------------------------
# Function: process_post
# Purpose:
# - Process raw LinkedIn post data.
# - Extract metadata using extract_metadata().
# - Unify tags using get_unified_tags().
# - Save the processed/enriched data to a JSON file.
# ---------------------------------------------
def process_post(raw_file_path, processed_file_path="data/processed_posts.json"):
    enriched_posts = []  # List to hold posts after metadata enrichment

    # Step 1: Read raw post data from the specified file
    with open(raw_file_path, encoding="utf-8") as file:
        posts = json.load(file)

        for post in posts:
            # Step 2: Extract metadata from each post's text
            metadata = extract_metadata(post['text'])

            # Step 3: Merge original post data with extracted metadata
            post_with_metadata = post | metadata  # Dictionary merge operator
            enriched_posts.append(post_with_metadata)

    # Step 4: Unify tags across all posts
    unified_tags = get_unified_tags(enriched_posts)

    for post in enriched_posts:
        current_tags = post['tags']
        # Step 5: Replace current tags with unified tags
        new_tags = {unified_tags[tag] for tag in current_tags}
        post['tags'] = list(new_tags)

    # Step 6: Write the final enriched data to a new JSON file
    with open(processed_file_path, 'w', encoding='utf-8') as outfile:
        json.dump(enriched_posts, outfile, indent=4)


# ---------------------------------------------
# Function: get_unified_tags
# Purpose:
# - Collect all tags from enriched posts.
# - Use an LLM to unify similar/related tags into a consistent set.
# - Return a mapping of original tags to unified tags.
# ---------------------------------------------
def get_unified_tags(posts_with_metadata):
    tags = set()  # To collect unique tags from all posts

    for post in posts_with_metadata:
        tags.update(post.get('tags', []))

    unique_tags_list = ', '.join(tags)  # Convert tag set to a comma-separated string
    print(f"Unified Tags: {unique_tags_list}")  # Optional: Display all unique tags

    # Prompt template to instruct the LLM to unify tags
    template = '''I will give you a list of tags. You need to unify tags with the following requirements,
    1. Tags are unified and merged to create a shorter list. 
        Example 1: "Jobseekers", "Job Hunting" can be all merged into a single tag "Job Search". 
        Example 2: "Motivation", "Inspiration", "Drive" can be mapped to "Motivation"
        Example 3: "Personal Growth", "Personal Development", "Self Improvement" can be mapped to "Self Improvement"
        Example 4: "Scam Alert", "Job Scam" etc. can be mapped to "Scams"
    2. Each tag should be follow title case convention. example: "Motivation", "Job Search"
    3. Output should be a JSON object, No preamble
    4. Output should have mapping of original tag and the unified tag. 
        For example: {"Jobseekers": "Job Search",  "Job Hunting": "Job Search", "Motivation": "Motivation"}

    Here is the list of tags: 
    {tags}
    '''

    pt = PromptTemplate.from_template(template)
    chain = pt | llm  # Combine the prompt with the LLM to form a LangChain chain
    response = chain.invoke(input={"tags": str(unique_tags_list)})

    try:
        json_parser = JsonOutputParser()
        res = json_parser.parse(response.content)
    except OutputParserException:
        raise OutputParserException("Context too long. Please shorten the input text.")

    return res  # Return tag mapping dictionary


# ---------------------------------------------
# Function: extract_metadata
# Purpose:
# - Extract metadata from a single LinkedIn post using LLM.
# - Extracted metadata includes:
#   1. line_count (number of lines in the post)
#   2. language (English or Hinglish)
#   3. tags (max 2 tags related to the post)
# - Returns a JSON-compatible dictionary.
# ---------------------------------------------
def extract_metadata(post):
    template = '''
    You are given a Linkedin post. You need to extract number of lines, Languages of the post and tags.
    1. Return a valid JSON. No preamble.
    2. JSON object should have exactly three keys: line_count, language, tags.
    3. tags is an array of text tags. Extract maximum two tags.
    4. language should be english or hinglish( Hinglish means a mix of Hindi and English).

    Here is the actual post on which you need to perform this task:
    {post}
    '''

    pt = PromptTemplate.from_template(template)
    chain = pt | llm  # Create a LangChain chain with the prompt and LLM
    response = chain.invoke(input={"post": post})

    try:
        json_parser = JsonOutputParser()
        res = json_parser.parse(response.content)
    except OutputParserException:
        raise OutputParserException("Context too long. Please shorten the input text.")

    return res  # Return metadata dictionary


# ---------------------------------------------
# Entry Point of the Script
# Purpose:
# - This block runs only when the script is executed directly.
# - Calls process_post() with paths to raw and processed files.
# ---------------------------------------------
if __name__ == "__main__":
    process_post("data/raw_post.json", "data/processed_posts.json")
