# 🍱 Fuji Grill AI Assistant

> Your friendly neighborhood restaurant chatbot for seamless ordering and reservations! 

![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4-orange.svg)

## 🌟 Features

Experience the future of restaurant service with our AI assistant that can:

🎯 **Take Orders**
- Process takeaway orders naturally
- Handle special dietary requirements
- Calculate totals automatically
- Provide order confirmations

🪑 **Make Reservations**
- Book tables effortlessly
- Handle special requests
- Manage party sizes
- Send confirmation details

🧠 **Smart Interactions**
- Natural conversation flow
- Menu recommendations
- Real-time availability checks
- Dietary restriction handling

## 🚀 Quick Start

### Prerequisites

Before diving in, make sure you have:
```bash
- Python 3.8+
- OpenAI API key
- Pinecone API key
```

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/restaurant-chatbot.git
cd restaurant-chatbot
```

2. **Set up your environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

3. **Configure your environment variables**
```bash
cp .env.example .env
# Edit .env with your API keys
```

4. **Run the bot**
```bash
python main.py
```

## 💬 Sample Conversation

```
You: Hi, I'd like to make a reservation
Bot: Welcome to Fuji Grill! I'd be happy to help you with a reservation. 
     May I have your name, please?

You: John Smith
Bot: Thank you, John! What date would you like to reserve?

You: This Friday at 7 PM
Bot: Perfect! How many people will be in your party?
...
```

## 🏗️ Project Structure

```
restaurant-chatbot/
├── src/                  # Source code
│   ├── bot.py           # Main chatbot logic
│   ├── storage.py       # Database operations
│   └── utils.py         # Helper functions
├── data/                # Data files
│   └── menu.txt         # Restaurant menu
├── tests/               # Test suite
└── main.py             # Entry point
```

## 🧪 Testing

Run the test suite to ensure everything's working:
```bash
python -m unittest discover tests
```

## 🔧 Configuration

The bot can be configured through environment variables:

| Variable | Description | Default |
|----------|-------------|---------|
| OPENAI_API_KEY | Your OpenAI API key | - |
| PINECONE_API_KEY | Your Pinecone API key | - |
| GPT_MODEL | GPT model to use | gpt-4 |

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch
3. Write your changes
4. Submit a pull request

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details.

## 📜 License

This project is licensed under the MIT License - see [LICENSE](LICENSE) for details.

## 🙏 Acknowledgments

- OpenAI for the GPT-4 API
- Pinecone for vector search capabilities
- LangChain for the conversation framework

## 🛠️ Troubleshooting

**Q: The bot isn't responding**  
A: Check your API keys in `.env`

**Q: Getting import errors**  
A: Ensure you've installed all dependencies: `pip install -r requirements.txt`

## 📞 Contact

Got questions? Found a bug? Reach out:
- Create an issue
- Email: your.email@example.com
- Twitter: @yourusername

## 🚀 Future Plans

- Voice interaction support
- Multi-language support
- Integration with payment systems
- Mobile app integration

---
Made with ❤️ by [Your Name]
