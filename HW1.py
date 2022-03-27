#
# Решение задач 1,2
#
documents = [
  {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
      ]

directories = {
        '1': ['2207 876234', '11-2'],
        '2': ['10006'],
        '3': []
      }

def get_name(number):
  for record in documents:
    if record.get("number") == number:
      return record.get("name")
  return "Документ не найден"

def get_shelf(number):
  for k,v in directories.items():
    if number in v:
      return k
  return "Документ не найден"

def get_list():
  l = list();
  for record in documents:
    l.append(f'{record.get("type")} "{record.get("number")}" "{record.get("name")}"')
  for s in l:
    print(s)
  return l

def get_full_list():
  print("\nСписок документов:")
  for record in documents:
    print(f'{record.get("type")} {record.get("number")} {record.get("name")}')

  print("\nСодержимое полок:")
  for k,v in directories.items():
    print(f'{k}: {v}')
  return


def add_record(doc_type, number, name, shelf):
  documents.append({"type":doc_type, "number": number, "name": name})
  directories.get(shelf).append(number)
  return

def delete_document(number):
  for k,v in directories.items():
    if number in v:
      v.remove(number)
      for record in documents:
        if record.get("number") == number:
          documents.remove(record)  
          return True
  return False

def enter_shelf():
  shelf = '-1'
  while shelf not in directories.keys():
    if shelf!='-1':
      print("несуществующий номер полки !")
    shelf = str(input("Введите номер целевой полки: "))
  return shelf

def move_document(number, shelf):
  is_found = False
  for k,v in directories.items():
    if number in v:
      v.remove(number)
      is_found = True
      break
  if is_found:
    directories.get(shelf).append(number)
    return True
  return False

def add_shelf(shelf):
  if shelf not in directories.keys():
    directories[shelf]=list()
    return True
  else:
    return False


def main_circle():
  command = ''
  while command != 'q':
    command = input("Введите команду (help - для справки): ")

    if command == 'p':
      print(get_name(str(input("Введите номер документа: "))))

    elif command == 'help':
      print("Список команд:")
      print("help - выводит этот текст")
      print("q - выход из программы")
      print("p - команда, которая спросит номер документа и выведет имя человека, которому он принадлежит")
      print("s - команда, которая спросит номер документа и выведет номер полки, на которой он находится")
      print("l -  команда, которая выведет список всех документов")
      print("la -  команда, которая выведет список всех документов и полок")
      print("a - команда добавления документа")
      print("d - команда удаления документа")
      print("m - команда перемещения документа")
      print("as - команда добавления полки")

    elif command == 's':
      print(get_shelf(str(input("Введите номер документа: "))))

    elif command == 'l':
      get_list()

    elif command == 'la':
      get_full_list()

    elif command =='a':
      doc_type = input("Введите тип документа: ")
      number = input("Введите номер документа: ")
      name = input("Введите имя владельца: ")
      add_record(doc_type, number, name, enter_shelf())
      print("Документ добавлен")

    elif command == 'd':
      if delete_document(str(input("Введите номер документа: "))) == False:
        print("Документ не найден")
      else:
        print("Документ удален")

    elif command == 'm':
      number = input("Введите номер документа: ")
      if move_document(number, enter_shelf()) == False:
        print("Номер документа не найден")
      else:
        print("Документ перемещен")

    elif command == 'as':
      if add_shelf(str(input("Введите номер добавляемой полки: "))):
        print("Новая полка добавлена")
      else:
        print("Такая полка уже существует")

#main_circle()