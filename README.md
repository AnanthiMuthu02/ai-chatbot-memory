# 🤖 AI Chatbot with Memory

A conversational AI chatbot that remembers everything you say during a conversation — built using the **Claude API by Anthropic** and Python.

---

## 💡 What It Does

Unlike basic AI scripts that forget everything after each response, this chatbot maintains **full conversation memory**. You can tell it your name, share context, and ask follow-up questions — just like talking to a real person.

This is the core concept behind every AI assistant ever built.

---

## 🧠 Key Concept — How Memory Works

Every message (yours + Claude's) is stored in a `conversation_history` list and sent to Claude with every new message. Claude reads the full history each time, which is how it remembers context.

```python
conversation_history = [
    {"role": "user",      "content": "My name is Ananthi"},
    {"role": "assistant", "content": "Hi Ananthi! Nice to meet you!"},
    {"role": "user",      "content": "What is my name?"},
    # Claude reads all of this and knows the answer 
]
```

---

## 🛠️ Tech Stack

- **Python 3.10+**
- **Claude API** (Anthropic) — `claude-sonnet-4-6`
- **python-dotenv** — for secure API key management

---

## 🚀 How to Run It

### 1. Clone the repo
```bash
git clone https://github.com/AnanthiMuthu02/ai-chatbot-memory.git
cd ai-chatbot-memory
```

### 2. Create and activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install anthropic python-dotenv
```

### 4. Set up your API key
Create a `.env` file in the root folder:
```
ANTHROPIC_API_KEY=your-api-key-here
```
Get your key at [platform.claude.com](https://platform.claude.com)

### 5. Run the chatbot
```bash
python chatbot.py
```

---

## 💬 Example Conversation

```
🤖 Claude Chatbot - type 'quit' to exit
----------------------------------------
You: My name is Ananthi
Claude: Hi Ananthi! Nice to meet you! How can I help you today?

You: I am a software engineer in Dublin
Claude: That's great! Dublin has a fantastic tech scene.
        What kind of software engineering do you do?

You: What do you know about me so far?
Claude: You've told me that your name is Ananthi and that
        you're a software engineer based in Dublin, Ireland!

You: quit
Claude: Goodbye! 👋
```

---

## 🔒 Security Note

Never commit your `.env` file. This repo includes a `.gitignore` that automatically excludes it.

---

## 👩‍💻 Author

**Ananthi Muthu**
Backend & Full Stack Software Engineer | Dublin, Ireland
[LinkedIn](https://www.linkedin.com/in/ananthi-muthu-76b3101a8/) | [GitHub](https://github.com/AnanthiMuthu02)

---


