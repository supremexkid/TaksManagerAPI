# Описание проекта
## API Contracts
### Модель Task: 

##### Поля задачи:

- **id** — <span style="color: orange;">int</span> - целое 
  число, первичный ключ, автогенерация.
- **title** — <span style="color: orange;">str</span> - 
  (строка), обязательное.
- **description** — <span style="color: orange;">str</span> - (строка, текст), необязательное (может
  быть <span style="color: orange;">null</span>).
- **status** — <span style="color: orange;">str (enum)</span> - по умолчанию "todo".
- **priority** — <span style="color: orange;">str (enum)</span> - по умолчанию "medium" (или 
  сделать обязательным при создании).
- **due_date** — <span style="color: orange;">date 
  (datetime)</span> (enum)
- **created_at / updated_at** — <span style="color: orange;">datetime</span>, 
  заполняются 
  автоматически.

### TaskCreate (Входящие данные): 

Клиент присылает:
1. <span style="color: green;">title</span> -  не **null**,
   максимум 100 символов
2. <span style="color: green;">description</span> -
   необязательное, <u>может быть</u> **null**.
3. <span style="color: green;">priority</span> - str, 
   необязательное (если не передали — 
  сервер ставит medium).
4. <span style="color: green;">due_date</span> - date, 
   необязательное. Важно: если передана, 
  то она не может быть в прошлом (меньше сегодняшнего дня).

Поля **id**, **status** (по умолчанию todo) и **временные метки** 
клиент присылать <u>не должен</u> — их генерирует сервер.

### TaskResponse (Исходящие данные): 
То, что сервер возвращает клиенту. 

Сервер возвращает: 
1. <span style="color: green;">id</span> - int 
   (генерируется БД)
2. <span style="color: green;">title, description, priority, due_date:</span> то, что передал 
  клиент (или дефолты).
3. <span style="color: green;">status</span> - всегда есть (при создании будет todo).
4. <span style="color:green;">created_at</span> - дата и время в формате ISO 
  (например, 2026-10-20T10:00:00Z), генерируются сервером автоматически.
5. <span style="color: green;">updated_at</span> - дата и время в формате ISO 
  (например, 2026-10-20T10:00:00Z), генерируются сервером автоматически.

   
