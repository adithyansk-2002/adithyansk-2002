###

<div align="center">
  <a href="https://www.linkedin.com/in/adithyan-suresh-kumar-319723287/" target="_blank">
    <img src="https://img.shields.io/static/v1?message=LinkedIn&logo=linkedin&label=&color=0077B5&logoColor=white&labelColor=&style=for-the-badge" height="25" alt="linkedin logo"  />
  </a>
  <a href="https://www.instagram.com/_.adithyan.sk._/" target="_blank">
    <img src="https://img.shields.io/static/v1?message=Instagram&logo=instagram&label=&color=E4405F&logoColor=white&labelColor=&style=for-the-badge" height="25" alt="instagram logo"  />
  </a>
</div>

###

<div align="center">
  <img src="https://visitor-badge.laobi.icu/badge?page_id=adithyansk-2002.adithyansk-2002&"  />
</div>

###

<h1 align="center">Hey there 👋</h1>

###

<h3 align="left">👩‍💻  About Me</h3>

###

<p align="left">I'm Adithyan Suresh Kumar <br><br>- 👀 I'm interested in coding and photography<br>- 🌱 I'm currently learning Python, C/C++ nd Java<br>- ⚡ Fun fact: I have created Minecraft mods in the past</p>

###

<h3 align="left">🛠 Language and tools</h3>

###

<div align="left">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" height="40" alt="python logo"  />
  <img width="12" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/jupyter/jupyter-original.svg" height="40" alt="jupyter logo"  />
  <img width="12" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/anaconda/anaconda-original.svg" height="40" alt="anaconda logo"  />
  <img width="12" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/cplusplus/cplusplus-original.svg" height="40" alt="cplusplus logo"  />
  <img width="12" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/java/java-original.svg" height="40" alt="java logo"  />
</div>

###

<h3 align="center">🚀 Interactive Code Showcase</h3>

<div align="center">
  <h4>🎨 ASCII Art Generator</h4>
  <pre><code># Python ASCII Art Generator
import pyfiglet
from termcolor import colored

def create_ascii_art(text, font='slant', color='cyan'):
    ascii_art = pyfiglet.figlet_format(text, font=font)
    return colored(ascii_art, color)

print(create_ascii_art('Hello!'))
</code></pre>
  <details>
    <summary>Try it yourself!</summary>
    <p>Install dependencies: <code>pip install pyfiglet termcolor</code></p>
    <p>Run the code to generate colorful ASCII art! 🎨</p>
  </details>

  <h4>🎮 Simple Game Engine</h4>
  <pre><code>// C++ Game Engine Snippet
#include <SFML/Graphics.hpp>

class Game {
    sf::RenderWindow window;
    sf::CircleShape player;
    
public:
    Game() : window(sf::VideoMode(800, 600), "My Game") {
        player.setRadius(50.f);
        player.setFillColor(sf::Color::Green);
    }
    
    void run() {
        while (window.isOpen()) {
            handleEvents();
            update();
            render();
        }
    }
};
</code></pre>
  <details>
    <summary>Build Instructions</summary>
    <p>Install SFML: <code>sudo apt-get install libsfml-dev</code></p>
    <p>Compile with: <code>g++ -std=c++17 game.cpp -lsfml-graphics -lsfml-window -lsfml-system</code></p>
  </details>

  <h4>🤖 Machine Learning Demo</h4>
  <pre><code># Python ML Example
import numpy as np
import tensorflow as tf
from sklearn.datasets import make_moons

# Generate data
X, y = make_moons(n_samples=1000, noise=0.1)

# Create model
model = tf.keras.Sequential([
    tf.keras.layers.Dense(10, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

# Train model
model.compile(optimizer='adam', loss='binary_crossentropy')
model.fit(X, y, epochs=100)
</code></pre>
  <details>
    <summary>Run this ML example</summary>
    <p>Install: <code>pip install tensorflow numpy scikit-learn</code></p>
    <p>This creates a neural network to classify moon-shaped data! 🌙</p>
  </details>

  <h4>🌐 Web Scraping Tool</h4>
  <pre><code># Python Web Scraper
import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_website(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    data = []
    
    for item in soup.find_all('div', class_='content'):
        data.append({
            'title': item.find('h2').text,
            'description': item.find('p').text
        })
    
    return pd.DataFrame(data)
</code></pre>
  <details>
    <summary>Try it out!</summary>
    <p>Install: <code>pip install requests beautifulsoup4 pandas</code></p>
    <p>This tool scrapes websites and stores data in a pandas DataFrame! 📊</p>
  </details>

  <h4>🎵 Audio Visualizer</h4>
  <pre><code>// Java Audio Processing
import javax.sound.sampled.*;
import java.io.*;

public class AudioVisualizer {
    public static void main(String[] args) {
        try {
            AudioInputStream audioStream = AudioSystem.getAudioInputStream(
                new File("music.wav"));
            byte[] audioData = new byte[1024];
            while (audioStream.read(audioData) != -1) {
                visualizeAudio(audioData);
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
</code></pre>
  <details>
    <summary>How to use</summary>
    <p>Compile with: <code>javac AudioVisualizer.java</code></p>
    <p>Run with: <code>java AudioVisualizer</code></p>
    <p>This creates a basic audio visualizer! 🎶</p>
  </details>
</div>

<div align="center">
  <h4>📊 GitHub Stats</h4>
  <img src="https://github-readme-stats.vercel.app/api?username=adithyansk-2002&show_icons=true&theme=radical" alt="GitHub Stats"/>
  <img src="https://github-readme-streak-stats.herokuapp.com/?user=adithyansk-2002&theme=radical" alt="GitHub Streak"/>
</div>
