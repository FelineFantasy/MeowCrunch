import random
import sys

def main():
    satiety = 50
    happiness = 50
    energy = 70
    health = 100
    quality = 0
    money = 100
    day = 1
    day_phase = "день"
    dirty_tray = False
    season = "весна"
    harvest_collected = False
    toys = 0
    dreamis = 0
    catnip = 0
    tianshan_mint = 0

    phases = {
        "утро": "день",
        "день": "вечер",
        "вечер": "ночь",
        "ночь": "утро"
    }

    print("МЯУХРУСТ: ФЕРМА ЗОЛОТИСТЫХ ХРУСТЯШЕК")
    print("Добро пожаловать на ферму!")
    player_name = input("Введите ваше имя (Enter — Лао Чжан): ").strip()
    name = player_name if player_name else "Лао Чжан"
    print(f"Добро пожаловать на ферму, {name}!")
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

        if day <= 30:
            season = "весна"
        elif day <= 60:
            season = "лето"
        elif day <= 90:
            season = "осень"
        else:
            season = "зима"

        print("\n" + "=" * 50)
        print(f"День: {day} ({day_phase}) | Сезон: {season}")
        print(f"Монеты: {money}")
        print(f"Сытость: {satiety} | Счастье: {happiness}")
        print(f"Энергия: {energy} | Здоровье: {health}")
        print(f"Качество хрустяшек: {quality}")
        print(f"Игрушки: {toys} | Дримис: {dreamis} | Кошачья мята: {catnip} | Тяньшаньская мята: {tianshan_mint}")
        if dirty_tray:
            print("Внимание: Лоток грязный!")
        print("=" * 50)

        if random.random() < 0.15:
            event = random.randint(1, 9)
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
            elif event == 6:
                gift = random.randint(5, 15)
                money += gift
                print(f"Кот принес подарок: +{gift} монет.")
            elif event == 7:
                print("Кот разбил вазу. Счастье и любовь снижаются.")
                happiness -= 10
            elif event == 8:
                print("Кот застрял в трубе. Энергия и здоровье падают.")
                energy -= 10
                health -= 10
            elif event == 9:
                print("Кот объелся мяты. Здоровье падает, но счастье растет.")
                health -= 10
                happiness += 15
            print("-------------------------\n")

        if dirty_tray:
            happiness -= 2
            health -= 1

        if season == "весна":
            if random.random() < 0.1:
                happiness += 5
                print("Весна: коты радуются и размножаются. Счастье растет.")
        elif season == "лето":
            if random.random() < 0.1:
                quality += 5
                print("Лето: хрустяшки растут быстрее. Качество улучшается.")
        elif season == "осень":
            if random.random() < 0.1:
                money += 10
                print("Осень: урожай созревает. Вы получаете немного монет.")
        elif season == "зима":
            if random.random() < 0.1:
                energy -= 5
                print("Зима: коты мерзнут и тратят энергию.")

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
        print("11. Купить игрушку (-15 монет, +10 счастья)")
        print("12. Купить Дримис (-25 монет, +15 сытости, +10 счастья)")
        print("13. Купить кошачью мяту (-10 монет, +20 счастья, -10 здоровья)")
        print("14. Собрать урожай (если качество >= 80)")

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
                tianshan_mint += 1
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
                if day == 31:
                    season = "лето"
                    print("Наступило лето.")
                elif day == 61:
                    season = "осень"
                    print("Наступила осень.")
                elif day == 91:
                    season = "зима"
                    print("Наступила зима.")
            print("Наступила следующая фаза дня.")
        elif choice == "11":
            if money >= 15:
                money -= 15
                happiness += 10
                toys += 1
                print("Вы купили игрушку. Коты довольны.")
            else:
                print("Недостаточно монет.")
        elif choice == "12":
            if money >= 25:
                money -= 25
                satiety += 15
                happiness += 10
                dreamis += 1
                print("Вы купили Дримис. Коты сыты и счастливы.")
            else:
                print("Недостаточно монет.")
        elif choice == "13":
            if money >= 10:
                money -= 10
                happiness += 20
                health -= 10
                catnip += 1
                print("Вы купили кошачью мяту. Счастье растет, здоровье падает.")
            else:
                print("Недостаточно монет.")
        elif choice == "14":
            if quality >= 80 and not harvest_collected:
                harvest_collected = True
                bonus = quality * 5
                money += bonus
                print(f"Вы собрали урожай! Качество: {quality}. Бонус: +{bonus} монет.")
            elif harvest_collected:
                print("Урожай уже собран.")
            else:
                print("Качество хрустяшек слишком низкое для сбора урожая.")
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
