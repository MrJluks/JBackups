import configparser
import os


class JJcfg:

    def __init__(self,ppath:str): # Инициализация
        # Путь к папке с кэшем, косытль
        self.path = ppath
        
        # Путь к файлу конфигурации
        self.path_to_cfg = os.path.join(ppath, "config.ini") 
        
         # Создание объекта конфига
        self.config = configparser.ConfigParser()
         # Чтение уже существующего
        self.config.read(self.path_to_cfg)

        # Перезапись, нужна для первой инициализации
        with open(self.path_to_cfg, 'w') as config_file: 
            self.config.write(config_file) 

    #Сохранение значения по ключу 
    def save_value(self,value,section:str,key:str): 
        # Создать секцию, если не существует 
        if not self.config.has_section(section): 
            self.config.add_section(section)
        
        # Установить зачение
        self.config.set(section,key,str(value)) 
        # Записать файл
        with open(self.path_to_cfg, 'w') as config_file: 
            self.config.write(config_file)


    def change_value(self,value,section:str,key:str):
        # Создать секцию, если нет 
        if not self.config.has_section(section):
            self.config.add_section(section)
        # Установить зачение
        self.config.set(section,key,str(value))
        

    def get_value(self,section:str,key:str): # Получить значение по ключу
        try:
            return self.config.get(section,key) # Вернуть значение
        except Exception as e:
            print(f"JCFG: can't find section/key: {e}") # Если не получилось вернуть нуль
            return 0


    def save_cfg(self):
        with open(self.path_to_cfg, 'w') as config_file: # Записать файл
            self.config.write(config_file)








