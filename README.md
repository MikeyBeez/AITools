# 🧠 AITools: Your Friendly AI Companion! 🤖

Welcome to AITools, your gateway to the exciting world of AI interactions! 🌟

🚀 **Beta Release Alert!** We're thrilled to have you on board as an early explorer. Your feedback is pure gold to us! 💎

## 🌈 What's AITools?

AITools is a magical Python project that lets you chat with AI models using the Ollama API. It's like having a super-smart friend in your computer! 💻✨

### 🎭 Features That'll Make You Smile

- 🔮 Crystal-clear conversations with AI models
- ⚡ Lightning-fast responses that flow like a river
- 🎨 Pretty console output that's easy on the eyes
- 🧩 Easy-to-extend framework for endless possibilities
- 🗣️ Smart conversation history that remembers your chat
- 📝 Super-smart logging system (it's like a diary for your AI!)
- 🔍 Memory search that finds needles in AI haystacks
- 🤔 "Thinking" indicator to show when Otto is processing
- 🔄 Real-time streaming of AI responses
- 🔀 Easy model switching with the `/cm` command

## 🏗️ The Building Blocks

```
AITools/
├── 📘 README.md (You are here!)
├── 📂 data/
├── 🚀 main.py
├── 📂 modules/
│   ├── 📂 agents/
│   ├── 📂 data/
│   ├── 📂 models/
│   └── 📂 utils/
│       ├── 🎤 input_util.py
│       ├── 💬 response.py
│       ├── 🖨️ mprint.py
│       ├── 🧠 context.py
│       └── 🔪 slash.py
└── 🧪 tests/
```

## 🌟 Special Features Spotlight

### 🔍 Memory Search: Your AI's Superhero Power!
Our memory search feature is like giving your AI a superpower! It can recall past conversations with incredible accuracy, making each interaction more meaningful and context-aware. It's not just search; it's time travel for knowledge! ⏳💡

#### 🔮 How to Use Memory Search
Activate the memory search by using the `?ms` command followed by parameters:
```
?ms <n> <m> <query>
```
- `n`: Number of top memories to retrieve
- `m`: Similarity threshold (0.0 to 1.0)
- `query`: Your question or prompt

Example:
```
?ms 5 0.8 What did we discuss about Python classes?
```
This will search for the top 5 memories with a similarity threshold of 0.8 related to Python classes.

### 📝 Logging: The AI Whisperer
Our logging system is the secret sauce that makes debugging a breeze. It's like having a play-by-play commentator for your AI interactions. Every detail, every decision, all captured for your curious eyes! 👀📊

### 🔄 Model Switching: Change Your AI's Brain
Want to try a different AI model? Just use the `/cm` command to see available models and switch on the fly. It's like giving your AI a wardrobe of different personalities!

## 🚀 Ready for Takeoff?

1. Clone this treasure chest:
   ```
   git clone https://github.com/MikeyBeez/AITools.git
   cd AITools
   ```

2. Set up your magical environment:
   ```
   conda create --name aitools python=3.12
   conda activate aitools
   ```

3. Summon the required powers:
   ```
   conda install --file requirements.txt
   ```
   (Psst! If conda struggles, try `pip install -r requirements.txt`)

## 🎮 Let's Play!

Fire up the AI playground:
```
python main.py
```

Now you're chatting with an AI! Here are some cool things to try:
- Feel like a fresh start? Just say "/clear" or "/c"!
- Want to use memory search? Try the `?ms` command as explained above!
- Switch models with "/cm"
- Get help anytime with "/help" or "/h"

## 🧪 For the Curious Minds

Run all the tests:
```
python -m unittest discover tests
```

Or try a specific spell:
```
python -m unittest tests.input_util_test
```

## 🤝 Join the AI Revolution!

1. 🍴 Fork this repo
2. 🌿 Create your feature branch (`git checkout -b feature/AmazingIdea`)
3. 💾 Commit your changes (`git commit -m 'Add some AmazingIdea'`)
4. 📤 Push to the branch (`git push origin feature/AmazingIdea`)
5. 🎉 Open a Pull Request and let's celebrate together!

## ⚖️ License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details. It's our way of saying "Go wild, but responsibly!" 😉

## 📞 Let's Chat!

Got questions? Ideas? Just want to say hi? We're all ears! 👂

MikeyBeez

Project Link: [https://github.com/MikeyBeez/AITools](https://github.com/MikeyBeez/AITools)

Remember, AITools is in beta, so if you hit any bumps or have any "Aha!" moments, let us know! Your experience helps make AITools even more amazing for everyone. Let's explore the AI frontier together! 🚀🌠
