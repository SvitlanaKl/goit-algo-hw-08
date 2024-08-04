# Є декілька мережевих кабелів різної довжини, їх потрібно об'єднати по два за раз в один кабель,
# використовуючи з'єднувачі, у порядку, який призведе до найменших витрат. 
# Витрати на з'єднання двох кабелів дорівнюють їхній сумі довжин, а загальні витрати дорівнюють сумі з'єднання всіх кабелів.
# Завдання полягає в тому, щоб знайти порядок об'єднання, який мінімізує загальні витрати.


import heapq

def min_cost_to_connect_cables(cable_lengths):
    # Ініціалізуємо купу з довжин кабелів
    heapq.heapify(cable_lengths)
    
    total_cost = 0
    
    # Поки в купі більше одного елементу, продовжуємо злиття
    while len(cable_lengths) > 1:
        # Витягуємо два найменші елементи
        first = heapq.heappop(cable_lengths)
        second = heapq.heappop(cable_lengths)
        
        # Сума цих двох кабелів - це вартість їх з'єднання
        local_cost = first + second
        total_cost += local_cost
        
        # Додаємо новоутворений кабель назад у купу
        heapq.heappush(cable_lengths, local_cost)
    
    return total_cost

# Приклад використання
cable_lengths = [5, 4, 2, 8, 6]
print("Мінімальна вартість з'єднання кабелів:", min_cost_to_connect_cables(cable_lengths))
