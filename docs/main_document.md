2023-11-18

## Цель

Необходимо реализовать минимальный работающий сайт, на котором можно войти как родителем, так и воспитателем. Со стороны родителя должен быть реализован функционал: видеть, чем по расписанию занимается ребенок, видеть, в садике ли ребенок, напоминания о следующем мероприятии / домашке / че принести. Со стороны воспитателя должен быть реализован функционал: возможность отметить каждого пришедшего ребенка, возможность добавить какое-то напоминание родителям. Этот функционал должен размещаться на внешнем сервере, со своим, желательно коротким, доменным именем. Визуал сайта должен быть минимально красивым и привликательным. Сайт должен работать, а не выдавать ошибку. Сайт должен выдержать обращений от нескольких устройств, сайт не должен ломаться от нескольких десятков пользователей, вошедших одновременно. Сайт не должен ломаться на телефоне. Все эти требования должны быть выполнены к 3 декабря 23:59. 

## Яндекс.Трекер

Задачи будут прописаны в Яндекс трекере. Каждый участник команды будет иметь к нему доступ. При поступлении задачи участник должен будет ее рассмотреть, вникнуть в суть, уточнить у автора все детали и только когда будет кристально понятно, чем исполнитель должен заниматься, приступать к работе. Также трекер отлично подходит для самостоятельного планирования работ. Если вам нужно сделать какое-то дело, которое занимает больше чем один день, логичнее всего разбить эту задачу на более мелкие и понятные, чтобы а) не забыть, что вам нужно делать б) не отходить от плана, в) создать видимость работы.

### Как работать с Трекером задач?

В работе над Сайтом у нас будут 3 Проекта: [Маркетинг](https://tracker.yandex.ru/pages/projects/3), [Дизайн](https://tracker.yandex.ru/pages/projects/1), [Разработка](https://tracker.yandex.ru/pages/projects/2). 

Проекты нужны для того, чтобы разделять задачи. Каждая задача может быть определена к одному проекту по основному профилю и указана тегами по побочному. При создании задачи очень важно указывать, к какому проекту относится задача. Сделать это можно в поле “Проект”

![Pasted image 20231120222102.png](files/Pasted%20image%2020231120222102.png)

Еще раз напоминаю, что задача создается, если нужно что-то распланировать, передать файлы, отслеживать результат. Если у вас есть какая-то пятиминутная просьба к коллеге, ее можно просто озвучить в личку. Желательно в личку, потому что в групповом чате почти никто не чувствует ответственности за какие-то задачи, потому что неясно, кому они адресованы. Но в беседе также можно передавать задачи, предварительно тегнув исполнтеля.

Также очень важно, если вы на кого-то создали задачу, отправьте ее, пожалуйста в личку. Так будет проще.

### Как работать с самими задачами?

Когда вы садитесь за работу, рекомендую ее начинать с [этой страницы](https://tracker.yandex.ru/agile/board/1) . Этот метод называется Kanban доска, когда у вас есть доска с 3мя позициями задачи: Открыто, В работе, Закрыто.

Исходя из этого, когда вы не знаете чем можете заняться, рекомендуется открыть страницу доску задач, перетянуть задачи, которыми вы хотите сегодня заниматься в колонку в работу и начать понемногу ими заниматься. Как только закончите работать не забывайте переводить задачу в колонку закрыто. Лично мне очень нравится наблюдать именно за тем, как задачи уменьшаются из колонки открыто или в работе. 

Возможно в какой-то момент задачи начнут просто сыпаться тоннами, чтобы в них не запутаться, важно запомнить кнопку группировки, вот она на картинке:

![Pasted image 20231120223005.png](files/Pasted%20image%2020231120223005.png)

## Разработка

Мы будем работать по парадигме [GitFlow ](https://habr.com/ru/articles/767424/) и вот еще немного на [почитать](https://habr.com/ru/articles/541258/) про гит для его осознания.

Ход работы:
1. Создать задачу. Для этого достаточно указать исполнителя, измеряемый результат, дедлайн и проект.

![Pasted image 20231120224642.png](files/Pasted%20image%2020231120224642.png)
2. Взять задачу в работу.

![Pasted image 20231120224717.png](files/Pasted%20image%2020231120224717.png)

3. Из ветки dev cоздать ветку с кодом как у задачи.

![Pasted image 20231120224906.png](files/Pasted%20image%2020231120224906.png)
4. Реализовать изменения

![files/Pasted image 20231120225042.png](files/Pasted%20image%2020231120225042.png)
5. Перейти во вкладку коммит, выбрать файлы, которые ты менял и хочешь залить в код, пишешь комментарий и пушишь новую ветку:

![Pasted image 20231120225241.png](files/Pasted%20image%2020231120225241.png)
6. Смотришь что добавляешь, какие файлы меняешь, какую ветку создаешь, после того, как запушишь изменения не забудь вернуться на ветку dev, если больше ничего не собираешь делать по задаче, это важно, потому что если менять ветки из ветки, то изменения будут накладываться от задачи к задаче и мы получим франкенштейна, который делает кучу изменений. Шанс получить конфликт в таком случае высок.

![Pasted image 20231120225337.png](files/Pasted%20image%2020231120225337.png)
7. Заходишь в гит, нажимаешь кнопку Compare & pull request

![Pasted image 20231120225447.png](files/Pasted%20image%2020231120225447.png)
8. Смотришь, чтобы база была dev, пишешь комментарий (по желанию) и нажимаешь кнопку create pull request

![Pasted image 20231120225604.png](files/Pasted%20image%2020231120225604.png)
9. Копируешь ссылку на этот МР(мердж реквест) мне в личку или в группу и можешь сегдня идти спать.

#### Лучше коммитить свои изменения, когда ты достиг какой-то финальной точки, например дописал функционал или закончил рабочий день. 