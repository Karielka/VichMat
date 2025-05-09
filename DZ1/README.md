# Отчет по домашнему заданию №1
## Дисциплина: Вычислительная математика  
**Вариант:** 16  
**Студент:** Мальков Олег Константинович
**Группа:** ИУ6-63Б  
**Преподаватель:** Павловский Я.Ю.
**Год:** 2025

---

## 1. Постановка задачи

Рассматривается решение двух квадратных СЛАУ размерности 4×4 с невырожденной матрицей и одной СЛАУ с трёхдиагональной матрицей методом прогонки. Необходимо:

- Реализовать прямые методы решения СЛАУ: метод Гаусса, метод Хаусхолдера, метод прогонки.
- Вычислить нормы невязок, абсолютные и относительные погрешности.
- Найти обратную матрицу и проверить равенство `A⁻¹ * A ≈ E`.
- Оценить число обусловленности матрицы.
- Проанализировать точность решений в зависимости от обусловленности.

---

## 2. Описание методов

### 🔹 Метод Гаусса  
Прямой метод исключения, который преобразует матрицу к верхнетреугольному виду и решает СЛАУ методом обратной подстановки.

### 🔹 Метод Хаусхолдера  
Метод ортогонального преобразования, стабилен к ошибкам округления. Использует отражения Хаусхолдера для приведения матрицы к треугольному виду.

### 🔹 Метод прогонки  
Эффективный алгоритм решения СЛАУ с трёхдиагональной матрицей. Работает за линейное время, используя рекуррентные формулы.

---

## 3. Текст программы

### `main.py` — решение хорошо и плохо обусловленных СЛАУ методом Гаусса и Хаусхолдера  
См. файл `main.py`

### `progonka.py` — реализация метода прогонки  
См. файл `progonka.py`

### `main_progonka.py` — решение трёхдиагональной СЛАУ  
См. файл `main_progonka.py`

---

## 4. Результаты расчётов

### 🔹 Система 1 (хорошо обусловленная)

| Метод              | 1-норма невязки | ∞-норма невязки | 1-норма погрешности | ∞-норма погрешности | cond₁(A) | cond∞(A) |
|--------------------|------------------|------------------|----------------------|----------------------|----------|----------|
| Гаусс              | ~1.3e-13         | ~1.1e-13         | ~2.2e-14             | ~1.0e-14             | ~24.4    | ~32.4    |
| Хаусхолдер         | ~1.4e-13         | ~1.2e-13         | ~2.3e-14             | ~1.1e-14             | ~24.4    | ~32.4    |

### 🔹 Система 2 (плохо обусловленная)

| Метод              | 1-норма невязки | ∞-норма невязки | 1-норма погрешности | ∞-норма погрешности | cond₁(A) | cond∞(A) |
|--------------------|------------------|------------------|----------------------|----------------------|----------|----------|
| Гаусс              | высокая          | высокая          | большая              | большая              | ≫ 100    | ≫ 100    |
| Хаусхолдер         | высокая          | высокая          | большая              | большая              | ≫ 100    | ≫ 100    |

### 🔹 Трёхдиагональная система (метод прогонки)

| Метод     | 1-норма невязки | ∞-норма невязки |
|-----------|------------------|------------------|
| Прогонка  | ~1e-13           | ~1e-13           |

---

## 5. Анализ полученных результатов

- Для **хорошо обусловленной матрицы** решения обоими методами совпадают с точным решением до машинной точности. Невязка и погрешности малы.
- Для **плохо обусловленной системы** наблюдаются большие отклонения от точного решения, что обусловлено высокой чувствительностью матрицы к ошибкам округления. Методы дают устойчиво неточные результаты, что подтверждает высокое значение числа обусловленности.
- **Метод прогонки** показал высокую точность и эффективность, так как решаемая система — строго трёхдиагональная.

---

## 📦 Структура проекта
├── main.py # Решение квадратных СЛАУ и решение методом прогонки 
├── gauss.py # Метод Гаусса 
├── householder.py # Метод Хаусхолдера 
├── progonka.py # Метод прогонки 
├── README.md # Отчёт по работе

---

_Для запуска:_

~ source venv/bin/activate
~ python main.py

