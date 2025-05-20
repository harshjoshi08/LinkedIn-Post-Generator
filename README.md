# 🔮 LinkedIn Post Generator 

This project demonstrates how to build a **LinkedIn Post Generator Tool** using:

- 🦙 Llama 3.2 (open-source LLM)
- 🔗 LangChain (prompt chaining and LLM orchestration)
- 🖼️ Streamlit (UI framework)
- ⚡ Groq  

The tool analyzes an influencer's existing LinkedIn posts to generate new content matching their style, tone, and topics.

---
## 📸 UI Preview

![UI Screenshot](https://github.com/harshjoshi08/LinkedIn-Post-Generator/blob/main/UI%20Preview.png) 

---

## 🧠 Project Architecture


### Technical Architecture

![Technical Architecture](https://github.com/harshjoshi08/LinkedIn-Post-Generator/blob/main/Techinical%20Architecture.png)

### System Architecture

![System Architecture](https://github.com/harshjoshi08/LinkedIn-Post-Generator/blob/main/System%20Architecture.png)

## ⚙️ Core Components and Workflow

### 🧪 Two-Stage Processing Pipeline

**Stage 1: Pre-processing**
- Collect and analyze existing posts
- Extract metadata: tags, language, line count

**Stage 2: Generation**
- Use processed data to generate new posts matching the original style

---

## 🗃️ Data Handling

- Posts are stored in `.json` format
- Metadata added during processing:  
  `tags`, `language`, `line_count`, and more
- Sample data: ~10-11 posts from influencer **Muskan Honda**

---

## 🤖 LLM Implementation

- Uses **Llama 3.2 90B** parameter model
- API keys handled via environment variables
- Robust error handling with try-catch blocks
  
---

## Installation

### Prerequisites

- Python 3.10 or higher
- `pip` (Python package manager)

### Setup Instructions

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/linkedin-post-generator.git
cd linkedin-post-generator
```
---
2. **Create a virtual environment** (inside your project folder):

```bash
python -m venv env
```
---
3. **After creating the virtual environment, activate it with the following command:**

```bash
env\Scripts\activate
```
---
4. **With your virtual environment activated, run the following command in the terminal to install all required Python packages:**

```bash
pip install -r requirements.txt
```
---
## 🙏 Acknowledgments

✨ Thanks to all the open-source libraries that made this project possible.

💡 Inspired by LinkedIn influencers like Muskan Honda.

---
## 🙌 Contributing

**Contributions are welcome! Please open an issue or submit a pull request for any improvements or features.**
