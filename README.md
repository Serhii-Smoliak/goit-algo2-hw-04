# goit-algo2-hw-04

# Задача 1. Розширення функціоналу префіксного дерева

#### Приклад використання
```
python task1.py
```
#### Виведе:
```
1
1
1
1
True
False
True
True
```

### Підсумок:
1. Реалізовано два методи:
    - count_words_with_suffix(pattern): підраховує кількість слів, що закінчуються на заданий суфікс.
    - has_prefix(prefix): перевіряє, чи існують слова з заданим префіксом.
2. Метод count_words_with_suffix перевіряє всі кінці слів у дереві та рахує їх за заданим шаблоном.
3. Метод has_prefix перевіряє наявність слів з префіксом, повертаючи True або False.
4. Методи ефективно працюють з набором даних і обробляють некоректні вхідні дані.

----

# Завдання 2. Порівняння ефективності OOBTree і словника для діапазонних запитів

#### Приклад використання
```
python task2.py
```
#### Виведе:
````
fl
inters
````

### Підсумок:
1. Реалізовано метод find_longest_common_word для знаходження найдовшого спільного префікса для масиву слів.
2. Метод перевіряє спільний префікс для всіх слів в масиві і повертає його.
3. Якщо спільного префікса немає, метод повертає порожній рядок.
4. Виконано перевірку коректних та некоректних даних для входу.