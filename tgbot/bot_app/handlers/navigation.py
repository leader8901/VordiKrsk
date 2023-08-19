class Handler:
    def __init__(self):
        self.menu_stack = []  # Stack to store the menu history

    def handle_message(self, message):
        # Check if the message is a "back" command
        if message.text == "назад":
            if len(self.menu_stack) > 1:  # Убедитесь, что есть хотя бы одно предыдущее меню
                self.menu_stack.pop()  # Удалить текущее меню из стека
                previous_menu = self.menu_stack[-1]  # Получить предыдущее меню
                self.display_menu(previous_menu)
            else:
                self.display_menu(self.menu_stack[0])  # Показать начальное меню

        # Обработка других действий меню здесь

    def display_menu(self, menu):
        # Показать меню пользователю
        # Реализовать логику для отображения кнопок, опций или команд на основе меню.

        # Поместить текущее меню в стек
        self.menu_stack.append(menu)

