# 🏗️ AITools: The Blueprint of Brilliance! 🌟

Welcome, intrepid explorer, to the architectural wonderland of AITools! 🏰✨

## 🎯 Our Mission

We're on a quest to create a codebase so clean, so modular, and so extensible that it brings tears of joy to developers' eyes. 😢 (Happy tears, we promise!)

## 🧱 The Building Blocks of Greatness

AITools is built on these rock-solid principles:

1. **📦 Modularity**: Like LEGO bricks, but for code! Each file has its special purpose, making our codebase a joy to explore and extend.

2. **🏃‍♂️ Asynchronous Input**: We use Python's `asyncio` and `prompt_toolkit` to handle input. It's so smooth, you'll think your computer can read minds!

3. **🧵 Threaded Output**: Responses from our AI friends are processed and displayed in their own thread. It's like having a separate stage for each performer in a concert!

4. **🎭 API Abstraction**: Our `OllamaClient` class is like a universal translator for AI APIs. Want to switch models? It's as easy as changing hats!

5. **🚀 Extensibility**: We've left plenty of room for growth. Adding new features is like planting seeds in fertile soil - they'll grow in no time!

6. **🧠 Context Management**: Our conversation history management is like giving the AI a really good memory. It's not just smart; it's wise!

## 🎭 The Cast of Characters

- `main.py`: The ringmaster of our AI circus 🎪
- `modules/utils/input_util.py`: The attentive listener 👂
- `modules/utils/response.py`: The smooth-talking responder 🗣️
- `modules/utils/mprint.py`: Our retired printer, enjoying its golden years 👴
- `modules/utils/context.py`: The elephant that never forgets 🐘

## 🔍 Spotlight on: Context Management

Our context management system is like a time machine for conversations:

1. **💾 Storage**: We keep the last 15 interactions in a FIFO queue. It's like a highlight reel of your chat!

2. **➕ Adding Context**: Every new chat gets VIP treatment in our context queue.

3. **🧠 Smart Prompts**: We serve each prompt to the AI with a side of context. It's like giving them a little history lesson before each response!

4. **🧹 Fresh Start**: Need a clean slate? Just say "clear history"! It's like a reset button for your conversation.

5. **🔄 The Circle of Chat**:
   a. You speak 🗣️
   b. We add some context 🧠
   c. AI ponders 🤔
   d. AI responds 💬
   e. We remember this moment 📸
   f. Repeat! 🔁

## 🌟 Special Features Showcase

### 🔍 Memory Search: Your AI's Time Machine
Imagine giving your AI the power to remember everything perfectly. That's our memory search! It doesn't just find information; it uncovers insights from past conversations, making each interaction richer and more meaningful. It's like having a librarian, historian, and fortune teller all rolled into one! 📚🔮

### 📝 Logging: The All-Seeing Eye
Our logging system is like a super-detailed diary of your AI's thoughts. Every decision, every computation, all laid out for you to see. It's not just for squashing bugs; it's for understanding the very soul of your AI interactions! Perfect for curious minds and debugging detectives alike. 🕵️‍♂️🔍

## 🚀 The Future is Bright!

We've paved the way for some exciting additions:

1. **🤖 More AI Friends**: Adding new AI models will be a piece of cake!
2. **🎛️ Input Processing 2.0**: We're gearing up for even smarter input handling.
3. **✨ Output Makeover**: Get ready for responses so pretty, they belong in a museum.
4. **🧠 AI Agents and Models**: We're preparing for a future filled with brilliant AI agents.
5. **💽 Data Wizardry**: Future data handling so smooth, it's practically magic.
6. **🔌 Plugin Paradise**: We're dreaming of a plugin system that'll make extensions a breeze.

## 💖 Join the AITools Family!

We're on an exciting journey, and we want you with us! Whether you're a code wizard or just AI-curious, there's a place for you here. Got ideas? Suggestions? Or just want to chat about the future of AI? Drop us a line!

Remember, AITools is in beta, which means you're not just a user - you're a pioneer! Every question, every bug report, every "what if" helps shape the future of AITools. So don't be shy - dive in, explore, and let's make AI magic together! 🌟🚀

Happy coding, and may your AI conversations be ever insightful! 🧠💬✨
# AITools

## Note:  It's my hope that this architecture will allow me to keep track of all the code as well as possible.  It's important that ony core functionality exist in each module.

