from openai import OpenAI
import os
import random
from datetime import datetime
from pathlib import Path
from rich.console import Console
from rich.panel import Panel
from rich.text import Text

class LovePoetry:
    def __init__(self, api_key=None):
        """Initialise the love poetry generator."""
        # Try to get API key from multiple sources
        self.api_key = api_key or os.getenv('OPENAI_API_KEY')

        # If no API key found, check for a config file
        if not self.api_key:
            config_file = self.get_config_path() / 'config.txt'
            if config_file.exists():
                self.api_key = config_file.read_text().strip()

        if not self.api_key:
            raise ValueError(
                "Please set your OpenAI API key using one of these methods:\n"
                "1. Set OPENAI_API_KEY environment variable\n"
                "2. Create a config file using 'happy_valentines --setup'"
            )

        # Only print the first 5 characters of the API key for security
        print(f"Using API key: {self.api_key[:5]}...")

        # Configure the openai library directly

        self.console = Console()

        # Create cache directory
        self.cache_dir = self.get_config_path() / 'cache'
        self.cache_dir.mkdir(exist_ok=True)

    @staticmethod
    def get_config_path():
        """Get the appropriate config directory for the current OS."""
        if os.name == 'nt':  # Windows
            base_dir = Path(os.getenv('APPDATA'))
        else:  # macOS / Linux
            base_dir = Path.home() / '.config'

        config_dir = base_dir / 'happy_valentines'
        config_dir.mkdir(parents=True, exist_ok=True)
        return config_dir

    def generate_poem(self, name="my love"):
        """Generate a unique love poem using gpt-4o"""

        prompts = [
            f"Write a short, romantic poem for {name}. Make it sweet and heartfelt, focusing on the small moments that make love special. Make sure to include their name.",
            f"Create a love poem for {name} that captures the joy and warmth of everyday love. Keep it genuine and avoid clichés. Make it short. Make sure to include their name.",
            f"Compose a tender love poem for {name} that celebrates the simple beauty of being together. Make it personal and touching. Make it short. Make sure to include their name."
        ]

        try:
            client = OpenAI(api_key = self.api_key)
            response = client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {
                        "role": "system",
                        "content": "You are a romantic poet who writes genuine, heartfelt love poems."
                                   "Your style is sweet and intimate but not overly sentimental."
                                   "Your poems are genereally very short. Do not make them too long."
                    },
                    {
                        "role": "user",
                        "content": random.choice(prompts)
                    }
                ],
                max_tokens=150,
                temperature=0.7
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            return f"Error generating poem: {str(e)}"

    def display_poem(self, poem, name):
        """Display the poem in a beautiful format."""
        styled_poem = Text(poem, style="bright_magenta")
        panel = Panel(
            styled_poem,
            border_style="red",
            title=f"♥ A Poem For {name} ♥",
            subtitle=datetime.now().strftime("%B %d, %Y")
        )
        self.console.print(panel)

    def save_poem(self, poem):
        """Save the poem to avoid repeats."""
        date = datetime.now().strftime("%Y-%m-%d")
        poem_file = self.cache_dir / f"{date}.txt"
        poem_file.write_text(poem)

    def get_todays_poem(self, name="my love"):
        """Get or generate today's poem."""
        date = datetime.now().strftime("%Y-%m-%d")
        poem_file = self.cache_dir / f"{date}.txt"

        if poem_file.exists():
            poem = poem_file.read_text()
        else:
            poem = self.generate_poem(name)
            self.save_poem(poem)

        return poem

def setup_config():
    """Set up the configuration with the API key."""
    config_file = LovePoetry.get_config_path() / 'config.txt'

    print("Setting up Happy Valentines configuration...")
    api_key = input("Please enter your OpenAI API key: ").strip()

    config_file.write_text(api_key)
    print(f"\nConfiguration saved to: {config_file}")
    print("You can now run 'happy_valentines' to generate poems!")

def main():
    """Main function to run the poetry generator."""
    import argparse

    parser = argparse.ArgumentParser(description="Generate daily love poems using GPT")
    parser.add_argument('--setup', action='store_true', help='Set up the configuration')
    args = parser.parse_args()

    if args.setup:
        setup_config()
        return

    try:
        name = input("Enter your name (or press Enter to use 'my love'): ").strip() or "my love"
        poetry = LovePoetry()
        poem = poetry.get_todays_poem(name)
        poetry.display_poem(poem, name)
    except Exception as e:
        print(f"\nError: {str(e)}")
        print("\nTo set up your API key, run: happy_valentines --setup")