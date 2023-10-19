#! Валидация формата xlsx.
#! Валидация original_file_name
Наполнение словарей (Имя Фамилия) при добавлении учеников/учителей с новыми именами/фамилиями

#! Проверка домашнего задания и выставление оценок

#! class HWChecker

 Табель перевода ученика: xlsx-документ со вкладками оценок и личными данными

Вкладка 0 - student имя, фамилия, дата рождения, класс зачисления, предполагаемая литера(необязательно)
Имя и фамилия должны быть в справочниках
При зачислении проверять три условия:
 - численность класса менее 5 человек
 - размещение в классе с минимальным числом учеников
 - если все классы заполнены, отказ(отмена импорта)

В зависимости от того, в какой класс переводится студент, 
количество вкладок должно соответствовать числу предметов.

1-2 класс: русский, алгебра
3 класс: +литература
4 класс: +изо
если число вкладок не соответствует предметам, ошибка формата импорта
(нет необходимых предметов, вернуть список недостающих предметов)

Требования: 
 - на каждой вкладке хотя бы одна оценка
 - при переводе grade_description дополнять пометкой "перевод"
(так как нет д.з.+как ведет себя система при перепроверке) 
 - общая проверка адекватности: средний балл по всем предметам должен превышать 3
(отмена импорта, вернуть причину отказа)


Личное дело студента будем сохранять, будем сохранять файл перевода. Необходимо создать модель
При повторной загрузке файла перевода - выдавать ошибку
