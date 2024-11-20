import csv

def process_csv(input_file, output_file, gdp_threshold):
    try:
        # Відкриваємо вхідний CSV файл для читання
        with open(input_file, mode='r', newline='', encoding='utf-8') as infile:
            csv_reader = csv.reader(infile)
            # Пропускаємо заголовки
            headers = next(csv_reader)
            # Створюємо список для збереження результатів пошуку
            filtered_data = []
            # Читаємо кожний рядок і перевіряємо умови
            for row in csv_reader:
                #GDP і чи немає ".." в кінці
                if len(row) < 5 or ".." in row[4] or row[0] != "GDP (current US$)":
                    continue 
                try:
                    gdp = float(row[4])
                    country = row[2]
                    if gdp > gdp_threshold:
                        filtered_data.append(row)
                except ValueError:
                    continue
        print("Вміст файлу:")
        with open(input_file, mode='r', newline='', encoding='utf-8') as infile:
            print(infile.read())

        # Записуємо результат пошуку у новий CSV файл
        with open(output_file, mode='w', newline='', encoding='utf-8') as outfile:
            csv_writer = csv.writer(outfile)
            # Записуємо заголовки
            csv_writer.writerow(headers)
            # Записуємо знайдені дані
            csv_writer.writerows(filtered_data)

        print(f"Результати записано у файл {output_file}")

    except FileNotFoundError:
        print(f"Помилка: Файл {input_file} не знайдено.")
    except Exception as e:
        print(f"Сталася помилка: {e}")
gdp_threshold = float(input("Введіть мінімальне значення GDP per capita для пошуку: "))
process_csv('gbp.csv', 'filtered_gdp_data.csv', gdp_threshold)
