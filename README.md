
# 📢 LinkedIn Post Generator Tool Using LLaMA 3.2

A complete end-to-end GenAI project leveraging **LLaMA 3.2**, **LangChain**, **Streamlit**, and **Python** to generate personalized LinkedIn posts that mirror an influencer's writing style.

---

## 📌 Project Overview

This tool analyzes previous LinkedIn posts from an influencer to:

- 🔍 Extract key topics they frequently write about  
- ✍️ Identify their unique writing style  
- 🧠 Generate new posts that maintain consistent tone and focus  
- ⚙️ Allow customization by **topic**, **language**, and **post length**


---

UI Preview
Here's what the Streamlit user interface looks like:

![UI Preview](images/system_architecture.png)

---

## System Architecture
Here's a visual representation of how the system works:


![System Architecture](images/system_architecture.png)

---

## 🏗️ Technical Architecture

![Technical Architecture](images/system_architecture.png)
The project is divided into two primary stages:

### 🔹 Stage 1: Pre-Processing

- Collects previous posts from a LinkedIn influencer (manual collection for demo)
- Stores post data in `JSON` format with engagement metrics
- Uses **LLaMA 3.2** to enrich the data with:
  - Topic Tags (limited to 2 per post)
  - Language Detection (English or Hinglish)
  - Line Count Classification

### 🔹 Stage 2: Post Generation

- Creates a **Streamlit UI** with dropdown menus for:
  - Topic selection (from extracted post data)
  - Post length (Short / Medium / Long)
  - Language selection
- Implements a **few-shot learning** approach using examples
- Generates new content matching the influencer’s writing style


---

## 🚀 How to Use

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/linkedin-post-generator.git
   cd linkedin-post-generator
   ```

2. **Install Requirements**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up Environment Variables**
   Create a `.env` file in the project root:
   ```bash
   # .env
   GROQ_API_KEY=your_api_key_here
   ```

4. **Run the Streamlit App**
   ```bash
   streamlit run main.py
   ```

5. **Generate a LinkedIn Post**
   - Select topic, length, and language from dropdowns
   - Click **Generate**
   - 

---

## 🧰 Technologies Used

- **LLaMA 3.2** – 90B parameter model for text generation  
- **LangChain** – LLM application development framework  
- **Streamlit** – For building interactive UIs  
- **Python** – Core programming language  
- **JSON** – For structured data storage  
- **Pandas** – For efficient data handling  

---


## 🙏 Acknowledgements

- Inspired by community tutorials  
- Thanks to the teams behind **LLaMA 3.2**, **LangChain**, and **Streamlit**
