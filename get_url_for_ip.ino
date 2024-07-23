#include <Keyboard.h>

void setup() {
  // Ожидание подключения клавиатуры
  delay(1000);

  // Нажатие и отпускание клавиш для запуска окна "Выполнить"
  Keyboard.press(KEY_LEFT_GUI);
  Keyboard.press('r');
  Keyboard.releaseAll();
  delay(200);

  // Ввод команды в выплывающем окне "Выполнить"
  Keyboard.println("cmd");
  delay(900);

  // Ввод команды для GET запроса (нужно вставить url после curl)
  Keyboard.println("curl ");
  delay(400);

  // Keyboard.println("exit");
}

void loop() {
  // Пустой цикл
}