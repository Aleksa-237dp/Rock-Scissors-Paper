## Игра "Камень-Ножницы-Бумага" на Python с использованием библиотеки PyGame 🐍

[![](https://img.shields.io/badge/github-blueviolet?style=for-the-badge)](https://github.com/pygame/pygame)
[![](https://img.shields.io/badge/book-green?style=for-the-badge)](https://pygame-docs.website.yandexcloud.net/tut/PygameIntro.html)


$\normalsize{\textsf{\color{violet}Я прошла курс "Код Будущего" по направлению "Практическое применение Python в инженерной и научной}}$
$\normalsize{\textsf{\color{violet}деятельности" 2023-2024 гг.}}$


> [!NOTE]
> Pygame - это мощная библиотека для разработки игр, предлагающая широкий ряд функций, которые упростят ваше путешествие по программированию. С помощью Pygame вы можете легко создавать 2D-игры, управлять графикой, звуком и вводом от пользователя. Библиотека предоставляет удобные инструменты для работы с изображениями, анимацией, обработкой событий и многим другим, что делает её отличным выбором как для начинающих, так и для опытных разработчиков. Благодаря активному сообществу и множеству доступных ресурсов, вы сможете быстро освоить Pygame и начать создавать свои собственные игры.

🎮 Игра "Камень-ножницы-бумага" — это классическая игра, в которой игрок и компьютер одновременно выбирают один из трёх вариантов: камень, ножницы или бумагу. 

📝 Правила просты:
Камень побеждает ножницы, ножницы побеждают бумагу, а бумага побеждает камень.

<img src="https://i.ibb.co/zWMBVSS/game.png" width="700" height="500">

## Инструкции по подключению к игре «Камень-ножницы-бумага»

| Загрузите репозиторий |

* В репозитории, который вы выбрали, нажмите зеленую кнопку "Code" и скопируйте URL-адрес.
* Затем в Visual Studio Code (или другом редакторе кода) откройте терминал и введите команду:
  
```python
  git clone [адрес репозитория]
```

| Создайте виртуальную среду |

* Откройте терминал (или командную строку) и перейдите в каталог проекта.
* Создайте виртуальную среду с помощью команды:
  
```python
  python -m venv env (замените 'env' на желаемое имя среды)
```

* Активируйте виртуальную среду в Windows:  `env\Scripts\activate`
* Или активируйте виртуальную среду в macOS/Linux:  `source env/bin/activate`
  
| Установите зависимости |

* После активации виртуальной среды установите необходимые библиотеки из файла `requirements.txt`
 
```python
  pip install -r requirements.txt
```
| Запустите игру |

* Перейдите в каталог, содержащий файл (обычно это корневой каталог проекта) `main.py`
* Запустите игру с помощью команды:
  
```python
  python main.py
```
| Дополнительные примечания |
  
* Убедитесь, что у вас установлена ​​соответствующая версия Python, как указано в `requirements.txt`
* И установлены все необходимые библиотеки. Если вы используете другую IDE или редактор, вам может потребоваться настроить среду так, чтобы она могла найти виртуальную среду и установленные библиотеки.
