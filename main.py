import random
import sys

def main():
    name = "Лао Чжан"
    satiety = 50
    happiness = 50
    energy = 70
    health = 100
    quality = 0
    money = 100
    day = 1
    day_phase = "день"
    dirty_tray = False

    phases = {
        "утро": "день",
        "день": "вечер",
        "вечер": "ночь",
        "ночь": "утро"
    }

    print("МЯУХРУСТ: ФЕРМА ЗОЛОТИСТЫХ ХРУСТЯШЕК")
    print("Добро пожаловать на ферму, Лао Чжан!")
    input("Нажмите Enter, чтобы начать...")

    while day <= 90:
        if satiety <= 0 or happiness <= 0 or health <= 0:
            print("\nВаши коты Мяухрусты погибли или сбежали. Игра окончена.")
            sys.exit()

        satiety = max(0, min(satiety, 100))
        happiness = max(0, min(happiness, 100))
        energy = max(0, min(energy, 100))
        health = max(0, min(health, 100))
        quality = max(0, min(quality, 100))
        money = max(0, money)

        print("\n" + "=" * 50)
        print(f"День: {day} ({day_phase})")
        print(f"Монеты: {money}")
        print(f"Сытость: {satiety} | Счастье: {happiness}")
        print(f"Энергия: {energy} | Здоровье: {health}")
        print(f"Качество хрустяшек: {quality}")
        if dirty_tray:
            print("Внимание: Лоток грязный!")
        print("=" * 50)

        if random.random() < 0.15:
            event = random.randint(1, 5)
            print("\n--- СЛУЧАЙНОЕ СОБЫТИЕ ---")
            if event == 1:
                print("Кот мяукнул от умиления.")
            elif event == 2 and not dirty_tray:
                dirty_tray = True
                print("Кот сходил в лоток. Стало грязно.")
            elif event == 3:
                found = random.randint(1, 5)
                money += found
                print(f"Кот нашел монеты: +{found} шт.")
            elif event == 4:
                print("Испуг! Громкий звук испугал котов, хрустяшки опадают.")
                quality -= 15
            elif event == 5:
                print("Пришел хитрец Фандахуй и украл часть припасов!")
                money -= random.randint(5, 15)
            print("-------------------------\n")

        if dirty_tray:
            happiness -= 2
            health -= 1

        print("0. Выйти из игры")
        print("1. Покормить котов (-5 монет, +10 сытости)")
        print("2. Погладить котов (+5 счастья)")
        print("3. Играть с котами (-5 энергии, +10 счастья)")
        print("4. Убрать лоток (+5 здоровья, +5 счастья)")
        print("5. Тренировать котов на колесе (-10 энергии, +10 качества)")
        print("6. Купить Тяньшаньскую мяту (-20 монет, +15 качества, -5 здоровья)")
        print("7. Выгулять котов (-15 сытости, +25 счастья)")
        print("8. Отправить котов работать на ферме (-10 энергии, +15 монет, -5 счастья)")
        print("9. Сходить к ветеринару (-30 монет, +30 здоровья)")
        print("10. Уложить спать (Смена фазы дня, +25 энергии)")

        choice = input("Выберите действие: ").strip()

        if choice == "0":
            print("Выход из игры. Прогресс не сохранен.")
            break
        elif choice == "1":
            if money >= 5:
                if satiety >= 100:
                    print("Коты уже сыты.")
                else:
                    money -= 5
                    satiety += 10
                    print("Вы покормили котов.")
            else:
                print("Недостаточно монет.")
        elif choice == "2":
            happiness += 5
            print("Вы погладили котов.")
        elif choice == "3":
            if energy >= 5:
                energy -= 5
                happiness += 10
                print("Вы поиграли с котами.")
            else:
                print("У котов мало энергии.")
        elif choice == "4":
            if dirty_tray:
                dirty_tray = False
                health += 5
                happiness += 5
                print("Лоток очищен.")
            else:
                print("Лоток и так чистый.")
        elif choice == "5":
            if energy >= 10:
                energy -= 10
                quality += 10
                print("Коты потренировались. Кровообращение улучшилось.")
            else:
                print("Недостаточно энергии для тренировок.")
        elif choice == "6":
            if money >= 20:
                money -= 20
                quality += 15
                health -= 5
                print("Вы купили Тяньшаньскую мяту. Качество растет, но здоровье падает.")
            else:
                print("Недостаточно монет.")
        elif choice == "7":
            if satiety > 15:
                satiety -= 15
                happiness += 25
                print("Коты погуляли на улице.")
            else:
                print("Коты слишком голодны для прогулки.")
        elif choice == "8":
            if energy >= 10:
                energy -= 10
                money += 15
                happiness -= 5
                print("Коты поработали на ферме и принесли монеты.")
            else:
                print("Коты слишком устали для работы.")
        elif choice == "9":
            if money >= 30:
                money -= 30
                health += 30
                print("Ветеринар осмотрел котов и поправил им здоровье.")
            else:
                print("Недостаточно монет для ветеринара.")
        elif choice == "10":
            print("Коты ложатся спать...")
            energy += 25
            old_phase = day_phase
            day_phase = phases[old_phase]
            if day_phase == "утро":
                day += 1
                quality += int((satiety + happiness + health) / 30)
            print("Наступила следующая фаза дня.")
        else:
            print("Неверный ввод.")

        input("Нажмите Enter, чтобы продолжить...")

    if day > 90:
        print("\n" + "=" * 50)
        print("90 ДНЕЙ ПРОШЛО! СБОР УРОЖАЯ")
        print("=" * 50)
        print(f"Итоговое качество хрустяшек: {quality}")
        
        if quality >= 80:
            final_money = money + 500
            print(f"Превосходный результат! Вы собрали идеальные золотистые хрустяшки.")
            print(f"Вы получили бонусные монеты и признание. Всего монет: {final_money}")
        else:
            print(f"Качество хрустяшек среднее или низкое. Урожай отправлен на конвейер по обычной цене.")
            print(f"Всего монет: {money}")
        print("Спасибо за игру!")

if __name__ == "__main__":
    main()
