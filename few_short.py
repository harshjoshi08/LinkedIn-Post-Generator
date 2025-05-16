import json
import pandas as pd
from pandas import json_normalize

class FewshotPosts:
    """
    A class to load, process, and filter posts based on length, language, and tags.
    The posts are expected to be stored in a JSON file.
    """

    def __init__(self, file_path="data/processed_posts.json"):
        """
        Initialize the FewshotPosts class by loading the data and preparing it.
        """
        self.df = None  # DataFrame to store the posts
        self.unique_tags = None  # Set to store all unique tags
        self.load_posts(file_path)

    def load_posts(self, file_path):
        """
        Load the posts from a JSON file, normalize the data, compute post length category,
        and extract unique tags.
        """
        with open(file_path, encoding="utf-8") as file:
            posts = json.load(file)
            self.df = json_normalize(posts)  # Flatten nested JSON into a DataFrame
            
            # Categorize posts by their line count (short, medium, long)
            self.df["length"] = self.df["line_count"].apply(self.categorize_length)

            # Extract all tags and build a set of unique tag values
            all_tags = self.df['tags'].apply(lambda x: x).sum()
            self.unique_tags = set(list(all_tags))
    
    def categorize_length(self, line_count):
        """
        Categorize a post based on its line count.
        Returns: "short", "medium", or "long".
        """
        if line_count < 5:
            return "short"
        elif line_count < 10:
            return "medium"
        else:
            return "long"
    
    def get_tags(self):
        """
        Return all unique tags found in the dataset.
        """
        return self.unique_tags
    
    def get_filtered_posts(self, length, language, tags):
        """
        Filter posts by length category, language, and at least one matching tag.

        Parameters:
        - length (str): The post length category ("short", "medium", "long").
        - language (str): The language to match (case-insensitive).
        - tags (list or str): Tag(s) to filter by; matches if any tag is present.

        Returns:
        - List of filtered post dictionaries.
        """
        if isinstance(tags, str):
            tags = [tags]  # Convert single string tag into list

        # Filter posts based on all criteria
        df_filtered = self.df[
            (self.df["length"] == length) &
            (self.df["language"].str.lower() == language.lower()) &
            (self.df["tags"].apply(lambda post_tags: any(tag in post_tags for tag in tags)))
        ]
        return df_filtered.to_dict(orient="records")

# ---------------------------------------------
# Example usage and output for testing
# ---------------------------------------------
if __name__ == "__main__":
    fs = FewshotPosts()

    # Print all available tags for reference
    print("\nAvailable Tags:", fs.get_tags())

    # Try to find posts that are 'medium' in length, written in English, and tagged with 'Criticism'
    filtered_posts = fs.get_filtered_posts("medium", "English", ["Criticism"])

    # Display each filtered post or a fallback message
    if filtered_posts:
        for i, post in enumerate(filtered_posts, 1):
            print(f"\n--- Post {i} ---")
            print(f"Text: {post['text']}")
            print(f"Tags: {post['tags']}")
            print(f"Length: {post['length']}")
            print(f"Language: {post['language']}")
    else:
        print("\nNo posts matched the given filters.")
