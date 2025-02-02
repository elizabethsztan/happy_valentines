# Happy Valentines 💝

A delightful Python package that generates personalised love poems using OpenAI's GPT-4o. Perfect for adding a touch of romance to your day!

(I made this for my boyfriend for Valentine's Day! You can install this package onto your s/o's computer and they can generate love poems everyday directly from the terminal.)

## Features

- 🎨 Generates unique, personalised love poems
- 💌 Beautiful console display with rich formatting
- 🔄 Caches daily poems to avoid duplicates
- 🌐 Cross-platform support (Windows, macOS, Linux)
- ⚙️ Easy configuration management
- 🎯 Different prompts for variety

## Installation

```bash
pip install happy_valentines
```

## Quick Start (all of this is in your terminal/CLI)

1. Set up your OpenAI API key:
```bash
happy_valentines --setup
```

2. Generate a love poem:
```bash
happy_valentines
```


## Usage Examples

### Basic Usage
```bash
happy_valentines
```

### Personalised Poem
```bash
$ happy_valentines
Enter your love's name (or press Enter to use 'my love'): Ewan
```


## Features in Detail

### Daily Caching
Poems are cached daily to ensure you receive the same poem throughout the day. New poems are generated at midnight local time.

### Rich Formatting
Poems are displayed in a beautiful console format with:
- Colored borders
- Styled text
- Date stamps
- Unicode hearts

### Multiple Prompt Templates
The generator uses various prompt templates to ensure diverse and unique poems while maintaining a romantic theme.

## Dependencies

- openai
- rich


## License

MIT License - See LICENSE file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Troubleshooting

### Common Issues

1. **API Key Error**
   - Ensure your OpenAI API key is correctly set up
   - Run `happy_valentines --setup` to reconfigure

2. **Cache Issues**
   - Clear the cache directory:
     - macOS/Linux: `rm -rf ~/.config/happy_valentines/cache/*`

3. **Model Errors**
   - Verify your OpenAI account has access to GPT models
   - Check your API key permissions

### Getting Help

If you encounter any issues, please:
1. Check the troubleshooting section above
2. Look for existing issues in the GitHub repository
3. Create a new issue if needed

## Credits

Created with ❤️ using OpenAI's GPT-4o API