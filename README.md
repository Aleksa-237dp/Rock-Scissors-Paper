## Rock-Paper-Scissors game in Python using the PyGame library 🐍

[![](https://img.shields.io/badge/github(pygame)-blueviolet?style=for-the-badge)](https://github.com/pygame/pygame)
[![](https://img.shields.io/badge/book(pygame)-green?style=for-the-badge)](https://pygame-docs.website.yandexcloud.net/tut/PygameIntro.html)


$\normalsize{\textsf{\color{violet}I took the Future Code course on "Practical applications of Python in engineering and science}}$
$\normalsize{\textsf{\color{violet}activities" 2023-2024.}}$


> [!NOTE]
> Pygame is a powerful game development library that offers a wide range of features to simplify your programming journey. With Pygame, you can easily create 2D games, manage graphics, sound, and user input. The library provides handy tools for handling images, animations, event handling, and more, making it a great choice for beginners and experienced developers alike. With an active community and many available resources, you'll be able to quickly learn Pygame and start creating your own games.

🎮 The Rock-Paper-Scissors game is a classic game in which the player and computer simultaneously choose one of three options: rock, scissors, or paper. 

📝 The rules are simple:
Rock beats scissors, scissors beats paper, and paper beats rock.

<img src="https://i.ibb.co/r3g8FdJ/2024-11-05-002239.png" width="650" height="500">

## Instructions on how to connect to the "Rock-Paper-Scissors" game

| Download the repository |

* In the repository you selected, click the green ‘Code’ button and copy the URL.
* Then, in Visual Studio Code (or other code editor), open a terminal and type the command:
  
```python
  git clone [repository address]
```

| Create a virtual environment |

* Open a terminal (or command line) and navigate to the project directory.
* Create a virtual environment using the command:
  
```python
  python -m venv env (replace ‘env’ with the desired environment name)
```

* Activate the virtual environment in Windows: `env\Scripts\activate`
* Or activate the virtual environment in macOS/Linux: `source env/bin/activate`
  
| Install dependencies |

* After activating the virtual environment, install the required libraries from the `requirements.txt` file
 
```python
  pip install -r requirements.txt
```
| Start the game |

* Navigate to the directory containing the file (usually the root directory of the project) `main.py`
* Start the game using the command:
  
```python
  python main.py
```
| Additional Notes |
  
* Make sure you have the appropriate version of Python installed, as specified in `requirements.txt`
* And have all the necessary libraries `pip install pygame` installed
  
  (If you are using a different IDE or editor, you may need to configure the environment so that it can find the virtual environment and installed libraries)
