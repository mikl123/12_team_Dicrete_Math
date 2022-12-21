# 12_team_Dicrete_Math
Team project
Команда 12: Сивкова Анна, Булешний Михайло, Сидор Наталя, Ткачишин Вероніка, Шараєв Віталій

!!! Модуль запускається викликом програми і функціонує за допомогою input.
Спочатку будуть запропоновані можливості, які може виконати модуль.
Після обрання функції можуть бути запрошені вхідні значення взалежності від неї!!!

Зв'язність графів

Читання графу з файлу функції

read_csv(path:str, orientated:bool)->dict читає граф з файлу (формат файлу - csv, перша колонка містить перші вершини кожного ребра, друга - другі вершини (порядок вершин не грає ролі в випадку неорієнтованого графу, і є важливим коли граф орієнтований), обробляє його і вертає словник із цим графом, де ключами є кожна вершина, значеннями - всі суміжні їй вершини. Функція працює як для орієнтованого і неорієнтованого графу. Для перетворення орієнтованого графу, треба задати параметр orientated = True, за замовчуванням функція перетворює неорієнтований граф (orientated = False).

Якщо користувач ввів не строчку, функція видасть "Write a path(str) to the csv-file" і завершить виконання.

Якщо файлу path не існує, функція напише "No file was found" і завершить виконання.

Якщо файл є папкою, а не файлом, функція напише "You need to input file not directory" і завершить виконання.

Якщо функція закінчується не на '.csv', функція напише "You need .csv file" і завершить виконання.

Функція не робить перевірку, чи є граф орієнтованим, чи ні(чи правильно ви ввели параметр orientated) Воно обробить будь-який граф, але, за умови неправильно заданого параметру orientated, обробить граф некоректно.

Функція обробляє прості графи(без кратних ребер і петель).

Так як граф задано ребрами, ми маємо на увазі, що у графі немає висячіх вершин(тобто кожна вершина має хоча б 1 суміжну)

Неорієнтований граф (порядок розташування неважливий, тобто ребро 1, 2 є те саме, що ребро 2,1 )

1,2 2,4 4,3 1,3 1,4

Функція перетворить у такий словник(тут є усі вершини, із суміжниими їм):

{1: [2, 3, 4], 2: [1, 4], 4: [1, 2, 3], 3: [1, 4]}

Орієнтований граф (тут перша вершина - вершина виходу , друга - вершина входу )

1,2 2,4 4,1 4,3 1,3

Функція перетворить у такий словник(вершини "3" тут немає у ролі ключа, попри те, що у неї є суміжні вершини, адже з неї тільки виходять вершини, але не входять)

{1: [2, 3], 2: [4], 4: [1, 3]}

Запис графу в файл

Функція write_csv(graph:dict, dst:str, orientated:bool)-> None записує перетворює граф з формату dict у строку. Записує цю строку у файл (формат файлу - csv, перша колонка містить перші вершини кожного ребра, друга - другі вершини (порядок вершин не грає ролі в випадку неорієнтованого графу, і є важливим коли граф орієнтований). Функція працює як для орінєнтованого, так і не для орієнтованого графів. Для перетворення орієнтованого графу, треба задати параметр orientated = True, за замовчуванням функція перетворює неорієнтований граф (orientated = False).

Якщо користувач ввів не строчку у dst, функція видасть "Write a path(str) to the csv-file you want to create!" і завершить виконання.

Якщо користувач ввів не словник у graph, функція видасть "Seems like your graph is not dictionary!Write it in dict format(key: vertex, values: neighbour vertixes)" і завершить виконання.

Якщо файлу dst не існує, функція напише "File not found" і завершить виконання.

Функція не робить перевірку, чи є граф орієнтованим, чи ні(чи правильно ви ввели параметр orientated) Воно обробить будь-який граф, але, за умови неправильно заданого параметру orientated, обробить граф некоректно.

Функція обробляє прості графи(без кратних ребер і петель)

Так як граф задано ребрами, ми маємо на увазі, що у графі немає висячіх вершин(тобто кожна вершина має хоча б 1 суміжну)

Неорієнтований граф-словник (порядок розташування неважливий, тобто у ключа 1 є точка 2, так самл у точки 2 є точка 1) {1: [2, 3, 4], 2: [1, 4], 4: [1, 2, 3], 3: [1, 4]}

Функція перетворить і запише у файл таким чином (тут є усі вершини, із суміжниими їм):

1,2 2,4 4,3 1,3 1,4

Неорієнтований граф-словник (вершини "3" тут немає у ролі ключа, попри те, що у неї є суміжні вершини, адже з неї тільки виходять вершини, але не входять) {1: [2, 3], 2: [4], 4: [1, 3]}

Функція перетворить і запише у файл таким чином (тут перша вершина - вершина виходу , друга - вершина входу)

1,2 2,4 4,1 4,3 1,3

Обхід ушир

Допоміжна функція bfs(graph: Dict[int, List[int]], **kwargs) -> List[int]. Приймає граф у форматі словнику і робить його обхід ушир.

Ми не робимо перевірок на тип input, так як запускаємо її в середині інших функцій, які вже роблять перевірку.

Якщо передано тільки граф(graph), то робить обхід з першої точки у словнику.

Якщо передано параметр kwargs, в якому міститься обхід і черга, то робить обхід з першого елементу черги. Це дозволяє робити обхід х будь-якої вершини, а не лише першої.

Тобто при передачі такого графа:

{2:[5], 3:[4, 5], 4:[3, 5], 5:[2, 3, 4]}

Функція поверне такий список:
[2, 5, 3, 4]

Пошук компонентів зв'язності:

Функція find_connectivity_components(graph:dict)->List[int] шукає компоненти зв'язності неорієнтованого графа і повертає список мінімальних вершин кожної компоненти.

Якщо граф зв'язаний, повертає список з одним значеннямм мінімальної вершини.

Якщо передано не словник, функція напише "Seems like your graph is not dictionary! Write it in dict
format(key: vertex, values: neighbour vertixes)" і завершить виконання.

Для такого графа: {0: [1], 1: [0], 2: [3, 4], 3: [2] ,4: [2, 5], 5: [4], 6: [10, 8], 7: [9], 8: [10, 9, 6], 9: [10, 8, 7], 10: [8, 9, 6]})

Функція поверне такий список: [0, 2, 6]

Пошук копонент сильної зв'язності:

Функція strong_connectivity_components(graph : dict, all_scc = None) ->List[int] шукає компоненти сильної зв'язності орієнтованого графа і повертає список мінімальних вершин кожної компоненти.

Якщо передано не словник, функція напише "Seems like your graph is not dictionary! Write it in dict format(key: vertex, values: neighbour vertixes)" і завершить виконання.

Для такого графа: {0: [1], 1: [0], 2: [3, 4], 3: [2] ,4: [2, 5], 5: [4], 6: [10, 8], 7: [9], 8: [10, 9, 6], 9: [10, 8, 7], 10: [8, 9, 6]})

Функція поверне такий список: [0, 2, 6]

Для такого : {2: [5], 3: [4], 4: [], 5: [3, 4]} Функція поверне : [2, 3, 4, 5]

Якщо введено порожній словник {} Функція поверне None

Пошук точок сполучення

Функція connecting_points(graph:dict)->List[int] отримує на вхід граф у форматі словника і вертає список із всіма точками зв'язності. Якщо у графі немає точок сполучення, вертає пустий список [].

Якщо graph - не словник, функція друкує "Seems it is not graph in dictionary type!".

Функція по черзі видаляє кожну вершину із графу(як з ключа, так і зі значень) , завдяки циклу for і пускає функцію find_connectivity_components для кожного графу без однієї вершини. Після чого порівнює кількість компонент графа без однієї вершини із кількістю компонент початкового словника. Якщо вони не рівні,то початковий граф, після видалення цієї точки, кількість компонент зростає. Отже, поточна точка - точка зв'язності. Ми додаємо її в список, який потім вертаємо. Зауважимо, що 1) на початку кожної ітерації отримуємо копію даного умовою графа; 2) під час кожної ітерації видаляється тільки одна вершина і до того ж та, яка раніше видалена не була.

Завдяки використанню модуля copy стандартної бібліотеки python даний умовою граф залишається незмінним.

Функція працює як для зв'язаних, так і для незв'язаних графів.

У графі, заданому таким словником(ключ - кожна вершина, значення - усі суміжні їй вершини)

{1:[2, 3, 4], 2:[1, 3, 5], 3:[1, 2], 4:[1], 5:[2, 6, 8], 6:[5, 7], 7:[6, 8], 8:[5, 7]}

Функція верне список: [1, 2, 5] - вершини 1, 2, 5 є точками сполучення даного графу.

Пошук мостів неорієнтованого графа

Функція find_bridges(graph: dict) -> list приймає словник, ключами якого є вершини неорієнтованого графа, а значеннями - суміжні вершини, що відповідають конкретним вершинам і шукає мости у цьому графі. Повертає список з кортежів, які репрезентують ребра, що є мостами.

У випадку передачі функції аргумента невідповідного типу (тобто не словникового), у консоль буде виведено "Seems it is not graph in dictionary type!", а функція завершить роботу нічого не повертаючи.

Результатом роботи функції за передачі їй коректного аргумента буде список кортежів, кожен з яких містить дві точки, що є кінцями ребра, яке визначене функцією як міст.

Концепція пошуку мостів: Створимо граф, що не містить певного ребра. Для нового графа порахуємо кількість компонент за допомогою функції find_connectivity_components. Якщо кількість компонент нового графа не співпадатиме з кількістю компонент початкового графа, то вважатимемо, що це ребро - міст. Це ітеративний процес, який повторюватиметься стільки разів, скільки унікальних ребер є у графа. Зауважимо, що 1) на початку кожної ітерації отримуємо копію даного умовою графа; 2) під час кожної ітерації видаляється тільки одне ребро і до того ж таке, яке раніше видаленим не було.

Завдяки використанню модуля copy стандартної бібліотеки python даний умовою граф залишається незмінним.

Усі ребра, які вважаються мостами, зберігаються у списку. Як результат роботи функція повертає відфільтрований список.

Граф подано у вигляді такого словника:

{1:[2, 4], 2:[1, 3], 3:[2, 4], 4:[1, 3, 5], 5:[4, 6, 8], 6:[5, 7], 7:[6, 8], 8:[5, 7]}

Результат: [(5, 4)] - тобто таке ребро є мостом

Граф подано у вигляді такого словника:

{1: [2], 2:[1, 3, 6], 3:[2, 4, 18], 4:[3, 5], 5:[4], 6:[2, 7, 8], 7:[6, 9], 8:[9, 6], 9:[7, 8, 10], 10:[9, 11, 14, 15], 11:[10, 12], 12:[11, 13], 13:[12, 14], 14:[10, 13], 15:[10, 16, 18], 16:[15, 17], 17:[18, 16], 18:[3, 15, 17]} Результат:

[(2, 1), (4, 3), (5, 4)] - тобто такі ребра є мостами

Граф подано у вигляді такого словника: {{1:[2, 3], 2:[1, 3], 3:[1, 2]} Результат: [] - тобто даний граф мостів не має
