
----------

RunTrainer (Python web project)
---------

Цел на проекта: Целта на проекта не е само да се напише проект за курса по Python 2014 към FMI, но да се сблъскат различни Python технологии , да се види като цяло как човек може да се оправи с dependency-та в Linux среда. Целта е да се създаде едно красиво, динамично, работещо и функционално уеб приложение.


> * Мотивацията зад проекта се крепи на 3 принципа:

> **KISS** (Keep it simple silly);

> **Stay small** - изграждане на малки части, една по една и oбединението им в едно цяло;

> **User Experience** - Най-важното освен качествения код е и проекта не само да е красив на външен вид, но и полезен, на хората, които го ползват.


#### <i class="icon-file"></i>Описание: 
Приложението ще има за цел да служи като логър на разстоянията, времето и средната скорост на трнировките на бягане на потребителя, както и да му помогне да планира тренировъчния си процес. Приложението ще може да вади статистически данни за напредъка на бегача, ще предоставя възможност за задаване на тренировъчен план и да визуализира неговото спазване.


#### <i class="icon-file"></i>Какво ще вклюва проекта:
#### <i class="icon-file"></i>1. Описание на екраните:

1.1 Екрани за въвеждане на разстоянието и времето на всяко бягане;

1.1.1 На по-късен етап може да се ползва GPS навигация, която сама да го изчислява;

1.2 Филтър за преглед на историята на бяганията;

1.3 Екран за задаване на тренировка;

1.4 Екран за сравнение на тренировъчния план и постигнатите резултати;

1.5 Екрани за статистически данни.

#### <i class="icon-file"></i>2. Използвани технологии:
2.1 Flask, Django като web framework;

2.2 Данните ще се пазят в база данни (най-вероятно sqlite, PostgreSQL);

2.3 Използване на ORM sqlalchemy(http://www.sqlalchemy.org/);

2.4 Използване на pyplot (http://matplotlib.org/1.3.1/users/pyplot_tutorial.html) за представяне на статистическите данни;

2.5 Интерфейс: Twitter Bootstrap.

Списъка на използваните технологии е примерен и може да се промени/ разшири в процеса на разработка. Целта му е само да даде информация към какво ще се стремим.

#### <i class="icon-file"></i>3. Възможни допълнителни функционалности:
 3.1 Използване на Facebook Connect  както за аутентикация, така и за споделяне в социалната мрежа. (вероятно с 3rd part library)
 
3.2 Замяна на PostgreSQL с MongoDB (just to have some fun)

----------

Milestone 1
---------
1. Setting up virtualenv
2. Setting uo Django simple project
3. Running the application on server
4. Testing the database connection

Maybe:

5. Adding a simple module

6. Createing a few test pages (possible use of templates, you know it is fun to template)

7. Creating autentication
