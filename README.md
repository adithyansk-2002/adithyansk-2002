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

<h3 align="center">🎮 Let's Play a Game!</h3>

<div align="center">
  <p>Try to guess the number between 1 and 100!</p>
  
  <div id="game-container" style="margin: 20px; padding: 20px; border-radius: 10px; background-color: #f0f0f0;">
    <input type="number" id="guess-input" min="1" max="100" placeholder="Enter your guess" style="padding: 8px; border-radius: 5px; border: 1px solid #ccc;">
    <button onclick="checkGuess()" style="padding: 8px 15px; background-color: #0077B5; color: white; border: none; border-radius: 5px; cursor: pointer;">Guess!</button>
    <p id="result" style="margin-top: 10px;"></p>
    <p id="attempts" style="margin-top: 10px;"></p>
  </div>
</div>

<script>
  let targetNumber = Math.floor(Math.random() * 100) + 1;
  let attempts = 0;
  const maxAttempts = 10;

  function checkGuess() {
    const guessInput = document.getElementById('guess-input');
    const result = document.getElementById('result');
    const attemptsDisplay = document.getElementById('attempts');
    const guess = parseInt(guessInput.value);

    if (isNaN(guess) || guess < 1 || guess > 100) {
      result.textContent = 'Please enter a valid number between 1 and 100!';
      return;
    }

    attempts++;
    attemptsDisplay.textContent = `Attempts: ${attempts}/${maxAttempts}`;

    if (guess === targetNumber) {
      result.textContent = `🎉 Congratulations! You guessed the number ${targetNumber} in ${attempts} attempts!`;
      result.style.color = 'green';
      disableGame();
    } else if (attempts >= maxAttempts) {
      result.textContent = `Game Over! The number was ${targetNumber}.`;
      result.style.color = 'red';
      disableGame();
    } else {
      result.textContent = guess > targetNumber ? 'Too high! Try a lower number.' : 'Too low! Try a higher number.';
      result.style.color = 'blue';
    }

    guessInput.value = '';
  }

  function disableGame() {
    document.getElementById('guess-input').disabled = true;
    document.querySelector('button').disabled = true;
  }
</script>

<style>
  #game-container {
    max-width: 400px;
    margin: 0 auto;
    text-align: center;
  }
  
  #guess-input {
    width: 150px;
    margin-right: 10px;
  }
  
  button:hover {
    background-color: #005f8f;
  }
</style>

###
