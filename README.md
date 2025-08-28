# BulgeFX Trading Bot 🚀

A Telegram bot for [BulgeFX](https://bulgefx.com/) trading platform that helps users get started with trading by providing information about deposit bonuses, trading signals, educational content, and automated trading solutions.

## Created By

This bot was created by **Mo Gadaphy**, Founder/CEO of [MOGADONKO AGENCY](https://mogadonko.com/) in partnership with **Sule Yaouba**, Founder/CEO of [Xcel Group](https://xcelgroup.ltd/).

## Features

- **Interactive Welcome Flow**: Guided conversation to onboard new users
- **Deposit Bonus Information**: Details about up to 20% bonus on first deposits
- **Trading Signals**: Information about free daily trading tips from expert traders
- **Educational Content**: Access to tutorials, webinars, and e-books
- **Trading Bot Access**: Information about automated trading for passive income
- **Error Handling**: Robust error handling and logging
- **Conversation Management**: State-based conversation flow with multiple input methods

## Prerequisites

- Python 3.7 or higher
- A Telegram Bot Token (obtained from [@BotFather](https://t.me/botfather))

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/mgadaphy/bulgefx_bot.git
   cd bulgefx_bot
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the project root and add your Telegram bot token:
   ```
   TELEGRAM_BOT_TOKEN=your_bot_token_here
   ```

## Usage

### Local Development

1. Start the bot:
   ```bash
   python bulgefx_bot.py
   ```

2. Open Telegram and start a conversation with your bot

3. Use `/start` to begin the onboarding flow

### Deploy to Cloud Platforms

#### Railway.app

1. Fork this repository or push to your own GitHub repository

2. Visit [Railway.app](https://railway.app/) and sign up/login

3. Click "New Project" → "Deploy from GitHub repo"

4. Select your `bulgefx_bot` repository

5. Add environment variable:
   - Key: `TELEGRAM_BOT_TOKEN`
   - Value: Your bot token from [@BotFather](https://t.me/botfather)

6. Railway will automatically detect the `Procfile` and deploy your bot

7. Your bot will be running 24/7 on Railway's infrastructure

#### Render.com

1. Fork this repository or push to your own GitHub repository

2. Visit [Render.com](https://render.com/) and sign up/login

3. Click "New" → "Background Worker"

4. Connect your GitHub repository and select `bulgefx_bot`

5. Configure the service:
   - **Name**: `bulgefx-bot`
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python bulgefx_bot.py`

6. Add environment variable:
   - Key: `TELEGRAM_BOT_TOKEN`
   - Value: Your bot token from [@BotFather](https://t.me/botfather)

7. Click "Create Background Worker" to deploy

#### PythonAnywhere

1. Sign up for a free account at [PythonAnywhere](https://www.pythonanywhere.com/)

2. Upload your project files to your PythonAnywhere account:
   - Go to "Files" tab
   - Upload `bulgefx_bot.py`, `requirements.txt`, and `.env` files

3. Open a Bash console and install dependencies:
   ```bash
   pip3.10 install --user -r requirements.txt
   ```

4. Create a `.env` file with your bot token:
   ```
   TELEGRAM_BOT_TOKEN=your_bot_token_here
   ```

5. Go to "Tasks" tab and create a new task:
   - **Command**: `python3.10 /home/yourusername/bulgefx_bot.py`
   - **Hour**: `*` (to run continuously)
   - **Minute**: `*`

6. Enable the task to start your bot

**Note**: Free PythonAnywhere accounts have limited always-on tasks. Consider upgrading for 24/7 bot operation.

#### Heroku (Free Alternative)

1. Sign up for a free account at [Heroku](https://heroku.com/)

2. Install the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)

3. Login to Heroku via CLI:
   ```bash
   heroku login
   ```

4. Create a new Heroku app:
   ```bash
   heroku create your-bulgefx-bot-name
   ```

5. Set your bot token as an environment variable:
   ```bash
   heroku config:set TELEGRAM_BOT_TOKEN=your_bot_token_here
   ```

6. Deploy your bot:
   ```bash
   git push heroku master
   ```

7. Scale your worker dyno:
   ```bash
   heroku ps:scale worker=1
   ```

**Note**: Heroku offers 550-1000 free dyno hours per month, perfect for small bots.

### Premium Deployment Options

#### DigitalOcean App Platform (Paid)

**Cost**: Starting at $5/month for basic apps

1. Sign up at [DigitalOcean](https://www.digitalocean.com/)

2. Go to "Apps" in the control panel

3. Click "Create App" and connect your GitHub repository

4. Configure your app:
   - **Name**: `bulgefx-bot`
   - **Source**: Select your GitHub repository
   - **Branch**: `master`
   - **Autodeploy**: Enable for automatic updates

5. Configure the component:
   - **Type**: Worker
   - **Run Command**: `python bulgefx_bot.py`
   - **Instance Count**: 1
   - **Instance Size**: Basic ($5/month)

6. Add environment variables:
   - Key: `TELEGRAM_BOT_TOKEN`
   - Value: Your bot token

7. Review and create the app

**Benefits**: 
- Automatic scaling
- Built-in monitoring
- Easy rollbacks
- 99.99% uptime SLA

#### AWS Elastic Beanstalk (Paid)

**Cost**: Starting at $10-15/month (t3.micro instance)

1. Sign up for [AWS](https://aws.amazon.com/) and access Elastic Beanstalk

2. Create a new application:
   - **Application name**: `bulgefx-bot`
   - **Platform**: Python 3.9
   - **Application code**: Upload your code as ZIP

3. Create a `requirements.txt` file (already exists)

4. Create an `application.py` file:
   ```python
   from bulgefx_bot import main
   
   if __name__ == "__main__":
       main()
   ```

5. Configure environment variables:
   - Go to Configuration → Software
   - Add environment property:
     - Name: `TELEGRAM_BOT_TOKEN`
     - Value: Your bot token

6. Deploy the application

7. Configure auto-scaling and monitoring as needed

**Benefits**:
- Enterprise-grade infrastructure
- Auto-scaling capabilities
- Integrated with AWS ecosystem
- Advanced monitoring and logging
- Load balancing

## Bot Commands

- `/start` - Begin your trading journey with BulgeFX
- `/help` - Show help message with available commands and information

## Bot Flow

1. **Welcome Message**: Users are greeted with options to start immediately or learn more
2. **Information Sharing**: Details about BulgeFX services including:
   - Deposit bonuses up to 20%
   - Free daily trading signals
   - Educational resources
   - Automated trading bot access
3. **Account Creation**: Direct users to the BulgeFX website for account creation

## Project Structure

- `bulgefx_bot.py` - Main bot application
- `application.py` - AWS Elastic Beanstalk entry point
- `requirements.txt` - Python dependencies
- `.env` - Environment variables (not tracked in git)
- `.gitignore` - Git ignore rules
- `Procfile` - Railway.app/Heroku deployment configuration
- `README.md` - Project documentation

## Dependencies

- `python-telegram-bot==20.7` - Telegram Bot API wrapper
- `python-dotenv==1.0.0` - Environment variable management

## Configuration

The bot requires a Telegram Bot Token which should be stored in a `.env` file:

```
TELEGRAM_BOT_TOKEN=your_telegram_bot_token
```

To get a bot token:
1. Message [@BotFather](https://t.me/botfather) on Telegram
2. Use the `/newbot` command
3. Follow the instructions to create your bot
4. Copy the provided token to your `.env` file

## Error Handling

The bot includes comprehensive error handling:
- Telegram API errors are logged and handled gracefully
- Network timeouts are managed
- Users are notified of errors with helpful messages
- All errors are logged for debugging purposes

## Logging

The bot uses Python's built-in logging module to track:
- User interactions
- Command executions
- Errors and exceptions
- Bot state changes

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For questions about the bot or BulgeFX services, visit [BulgeFX](https://bulgefx.com/)

For development inquiries, contact:
- [MOGADONKO AGENCY](https://mogadonko.com/)
- [Xcel Group](https://xcelgroup.ltd/)

## Disclaimer

This bot is designed to provide information about [BulgeFX](https://bulgefx.com/) trading services. Trading involves risk, and users should carefully consider their investment objectives and risk tolerance before trading.