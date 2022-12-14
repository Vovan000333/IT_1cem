"""
Необходимо реализовать записную книжку с интерфейсом в виде приложения
командной строки (CLI), где пользователь может выбрать следующие операции:
1. Посмотреть список существующих блокнотов
2. Создать новый блокнот
3. Изменить существующий блокнот
4. Удалить существующий блокнот

В блокноте содержатся информация в виде строки следующего вида:
1,Пробудиться,10.00,29.09.2022,(Важно),Выполнено
2,Поехать в универ,11.00,29.09.2022,(Не важно),Выполнено
3,Поесть,11.30,29.09.2022,(Важно),Не выполнено
4,Погладить кота,14.00,29.09.2022,(Очень важно),В процессе

Всего 4 столбца:
*номер записи
*Задача
*Время
*Дата
*Приоритет
*Статус выполнения

Записи разделяются запятыми, имя блокнота задаётся пользователем и сохраняется в виде
name.csv

При выводе информации пользователю необходимо реализовать сортировку записей
по различным критериям (Дата, время, Приоритет, Номер, Статус)
"""
notes =[]
with open("note.csv", "r", encoding="utf-8") as f:
    for line in f:
        l = line.split(',')
        note = {
            "id":l[0],
            "task":l[1],
            "time":l[2],
            "date":l[3],
            "prioryti":l[4],
            "status":l[5][:-1]
        }
        notes.append(note)


print(*notes, sep='\n')

note_values=[str(note["id"]),note["task"],note["time"],note["date"],note["priority"],note["status"]]
        f.write(",".join(note_values)+"\n")
    f.close()
def tableprint(notes):
    print("{:<3} {:<18} {:<6} {:<12} {:<11} {:<17}".format("Id","Task","Time","Date","Priority","Status"))


with open("note.csv","w",encoding="UTF-8") as myfile:
    for runner in runnersMarked:
        myfile.write("id":l[0],
            "task":l[1],
            "time":l[2],
            "date":l[3],
            "prioryti":l[4],
            "status":l[5][:-1])
        notes.append(note)



global notes
notes=[]
global myFile
myFile=[]
global notebookFileName
def fileSaving():
    global notes
    f=open("./gop/"+notebookFileName,"w+",encoding="Utf-8")
    for note in notes:
        note_values=[str(note["id"]),note["task"],note["time"],note["date"],note["priority"],note["status"]]
        f.write(",".join(note_values)+"\n")
    f.close()
def tableprint(notes):
    print("{:<3} {:<18} {:<6} {:<12} {:<11} {:<17}".format("Id","Task","Time","Date","Priority","Status"))
    for note in notes:
        id,task,time,date,priority,status=note.values()
        print("{:<3} {:<18} {:<6} {:<12} {:<11} {:<17}".format(id,task,time,date,priority,status))
def byStatus(note):
    return note["status"]
def byTime(note):
    return note["time"]
def byDate(note):
    return note["date"]
def byId(note):
    return note["id"]
def byTask(note):
    return note["task"]
def byPriority(note):
    if (note["priority"])=="Высокий":
        return 0
    if (note["priority"])=="Средний":
        return 1
    if (note["priority"])=="Низкий":
        return 2
    else:return 3
def uiFileInteraction():
    for i in listdir("./gop"):
        if isfile("./gop/"+i) and i[-4:]==".txt":
            myFile.append(i)
    print("Список доступных блокнотов \n")
    print(myFile)
    print("Ведите имя блокнота, с которым хотите работать \n")
    global notebookFileName
    global notes
    notebookFileName=input()
    if not notebookFileName in myFile:
        print("Файл не найден \n")
        with open ("./gop/"+notebookFileName,"a",encoding="Utf-8") as f:
            notes=[]
    else:
        with open("./gop/"+notebookFileName,"r",encoding="Utf-8") as f:
            for line in f:
                l=line.split(",")
                note={
                "id":int(l[0]),
                "task":l[1],
                "time":l[2],
                "date":l[3],
                "priority":l[4],
                "status":l[5][:-1]
                }
                notes.append(note)
def uiNoteInteractionSort():
    print("Введите по какому критерию отсортировать блокнот,введите поле,для выхода введить exit \n")
    j=input()
    if j=="exit":
        return
    if j=="id":
        notes.sort(key=byId)
        return
    if j=="task":
        notes.sort(key=byTask)
        return
    if j=="time":
        notes.sort(key=byTime)
        return
    if j=="date":
        notes.sort(key=byDate)
        return
    if j=="priority":
        notes.sort(key=byPriority)
    if j=="status":
        notes.sort(key=byStatus)
def uiNoteInteraction():
    global notes
    while True:
        print("Что вы хотите сделать? [1-Добавить,2-Изменить,3-Удалить,0-Выйти] \n")
        a=int(input())
        if a==1:
            print("Введите новую строчку, разделённую запятыми \n")
            stroka=input().split(",")
            note={
            "id":len(notes)+1,
            "task":stroka[0],
            "time":stroka[1],
            "date":stroka[2],
            "priority":stroka[3],
            "status":stroka[4]
            }
            notes.append(note)
        elif a==2:
            print("Введите номер строки \n")
            nom=int(input())
            print("Введите поле,которое хотите изменить и новое поле,через запятую \n")
            pole,skor=input().split(",")
            notes[nom-1][pole]=skor
        elif a==3:
            print("Введите номер строки,которую хотите удалить \n")
            m=int(input())
            del notes[m-1]
            for note in notes:
                if note["id"]>m:
                    note["id"]-=1
        elif a==0:
            break
        else:
            print("Неизвестная команда\n")
uiFileInteraction()
tableprint(notes)
uiNoteInteraction()
fileSaving()
tableprint(notes)