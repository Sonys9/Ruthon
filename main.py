import sys
import compiler
import os
import runner

args = sys.argv

if len(args) != 3:
    print('Используйте <команда> <имя файла>\nКоманды:\n\tкомпилирование - Скомпилировать файл\n\tзапуск - Запуск скомпилированного файла')
else:
    command = args[1]
    file_name = args[2]

    if not os.path.exists(file_name):
        print('Файл не найден.')
    else:
        if command.lower() == 'компилирование':
            comp = compiler.Compiler(file_name)
            comp.convert()
            comp.save()
            print('Успешно скомпилировано.')
        elif command.lower() == 'запуск':
            run = runner.Runner(file_name)
            run.convert()
            run.run()