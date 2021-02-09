# import math
import numpy as np
from scipy import stats

# footballers_list = [70, 50, 65, 60, 75]
# hockey_players_list = [80, 75, 90, 70, 75, 65, 85, 100]
# weightlifters_list = [130, 100, 140, 150, 160, 170, 200]


footballers_list = [173, 175, 180, 178, 177, 185, 183, 182]
hockey_players_list = [177, 179, 180, 188, 177, 172, 171, 184, 180]
weightlifters_list = [172, 173, 169, 177, 166, 180, 178, 177, 172, 166, 170]


def task_1():
    """
    Задача 1:
        Провести дисперсионный анализ для определения того, есть ли различия среднего роста среди взрослых футболистов,
        хоккеистов и штангистов. Даны значения роста в трех группах случайно выбранных спортсменов:
        Футболисты: 173, 175, 180, 178, 177, 185, 183, 182.
        Хоккеисты: 177, 179, 180, 188, 177, 172, 171, 184, 180.
        Штангисты: 172, 173, 169, 177, 166, 180, 178, 177, 172, 166, 170.
    Решение:
        среднее значение выборки:
            футболистов = 179.1250
            хоккеистов = 178.6667
            штангистов = 172.7273
            общее = 176.4643
        критерий Фишера расчетный = 5.5001
        Критическое значение распределения Фишера для v1=2, v2=25:
        при alpha=0.05: Fкрит=3.3852
            Различие между группами статистически значимое для уровня значимости alpha = 0.05.
        при alpha=0.01: Fкрит=5.57
            Различие между группами статистически не значимое для уровня значимости alpha = 0.01.
        Значение параметра eta2 = s2f/s2 = 0.3056 близко к значению 0.3.
        Принято считать, что при значениях eta2 ниже 0.2-0.3 групповые значения средних
        не имеют статистически достоверного отличия.
    Вывод:
        Для данных выборок различия находятся на уровне поорогового значения eta2 = 0.3
        Для уровня значимости alpha = 0.05 различие статистически значимо
        Для уровня значимости alpha = 0.01 и ниже различие статистически не значимо
        Соответственно для уточнения гипотезы необходимы дополнительные измерения роста в группах спортсменов.
    """
    print("Задача 1")
    k = 3
    footballers_n = len(footballers_list)
    hockey_players_n = len(hockey_players_list)
    weightlifters_n = len(weightlifters_list)
    total_n = footballers_n + hockey_players_n + weightlifters_n

    footballers_sum = sum(footballers_list)
    hockey_players_sum = sum(hockey_players_list)
    weightlifters_sum = sum(weightlifters_list)
    total_sum = footballers_sum + hockey_players_sum + weightlifters_sum

    footballers_y_mean = footballers_sum / footballers_n
    hockey_players_y_mean = hockey_players_sum / hockey_players_n
    weightlifters_y_mean = weightlifters_sum / weightlifters_n
    total_y_mean = total_sum / total_n
    print(f"    среднее значение выборок:")
    print(f"        футболистов = {footballers_y_mean:.4f}")
    print(f"        хоккеистов = {hockey_players_y_mean:.4f}")
    print(f"        штангистов = {weightlifters_y_mean:.4f}")
    print(f"        общее = {total_y_mean:.4f}")
    footballers_s2 = sum(map(lambda x: (x - total_y_mean) ** 2, footballers_list))
    hockey_players_s2 = sum(map(lambda x: (x - total_y_mean) ** 2, hockey_players_list))
    weightlifters_s2 = sum(map(lambda x: (x - total_y_mean) ** 2, weightlifters_list))
    total_s2 = footballers_s2 + hockey_players_s2 + weightlifters_s2
    print(f"    сумма квадратов отклонений наблюдений s2 = {total_s2:.4f}")
    footballers_s2f = ((footballers_y_mean - total_y_mean) ** 2) * footballers_n
    hockey_players_s2f = ((hockey_players_y_mean - total_y_mean) ** 2) * hockey_players_n
    weightlifters_s2f = ((weightlifters_y_mean - total_y_mean) ** 2) * weightlifters_n
    total_s2f = footballers_s2f + hockey_players_s2f + weightlifters_s2f
    print(f"    сумма квадратов отклонений средних групповых s2f = {total_s2f:.4f}")
    footballers_s2res = sum(map(lambda x: (x - footballers_y_mean) ** 2, footballers_list))
    hockey_players_s2res = sum(map(lambda x: (x - hockey_players_y_mean) ** 2, hockey_players_list))
    weightlifters_s2res = sum(map(lambda x: (x - weightlifters_y_mean) ** 2, weightlifters_list))
    total_s2res = footballers_s2res + hockey_players_s2res + weightlifters_s2res
    print(f"    остаточная сумма квадратов отклонений s2res = {total_s2res:.4f}")
    total_s2 = total_s2f + total_s2res
    print(f"    проверка - сумма квадратов отклонений наблюдений s2 = {total_s2:.4f}")
    eta2 = total_s2f / total_s2
    print(f"    s2f / s2 = {eta2:.4f}")
    sigma2f = total_s2f / (k - 1)
    print(f"    факторная дисперсия sigma2f = {sigma2f:.4f}")
    sigma2res = total_s2res / (total_n - k)
    print(f"    остаточная дисперсия sigma2res = {sigma2res:.4f}")
    f_n = sigma2f / sigma2res
    print(f"    наблюдаемое значение критерия Фишера f_н = {f_n:.4f}")
    print(f"    df_межд (v1) = {k - 1}")
    print(f"    df_внутр (v2) = {total_n - k}")
    f_crit_a_0_05 = 3.3852
    print(f"    Критическое значение распределения Фишера")
    print(f"    для v1={k - 1}, v2={total_n - k}, alpha=0.05: Fкрит={f_crit_a_0_05}")
    if f_n > f_crit_a_0_05:
        print(f"Вывод 1:")
        print(f"    {f_n:.4f} > {f_crit_a_0_05:.4f}")
        print(f"    Различие между группами статистически значимое для уровня значимости alpha = 0.05.")
    else:
        print(f"Вывод 1:")
        print(f"    {f_n:.4f} < {f_crit_a_0_05:.4f}")
        print(f"    Различие между группами статистически не значимое для уровня значимости alpha = 0.05.")
    print()
    f_crit_a_0_01 = 5.57
    print(f"    для v1={k - 1}, v2={total_n - k}, alpha=0.01: Fкрит={f_crit_a_0_01}")
    if f_n > f_crit_a_0_01:
        print(f"Вывод 2:")
        print(f"    {f_n:.4f} > {f_crit_a_0_01:.4f}")
        print(f"    Различие между группами статистически значимое для уровня значимости alpha = 0.01.")
    else:
        print(f"Вывод 2:")
        print(f"    {f_n:.4f} < {f_crit_a_0_01:.4f}")
        print(f"    Различие между группами статистически не значимое для уровня значимости alpha = 0.01.")
    print()
    print(f"Вывод 3:")
    print(f"    Значение параметра eta2 = s2f/s2 = {eta2:.4f} близко к пороговому значению 0.3.")
    print(f"    Принято считать, что при значениях eta2 ниже 0.2-0.3 групповые значения средних")
    print(f"    не имеют статистически достоверного отличия.")
    print()
    print(f"    Для уточнения гипотезы необходимы дополнительные измерения роста в группах спортсменов.")
    print()
    print()


def task_1_stats():
    """
        Проверка при помощи scipy.stats
    """
    print(f"Задача 1. Проверка при помощи scipy.stats.")
    footballers = np.array(footballers_list)
    hockey_players = np.array(hockey_players_list)
    weightlifters = np.array(weightlifters_list)
    f_n, p_value = stats.f_oneway(footballers, hockey_players, weightlifters)
    # print(result)
    print(f"    f_n = {f_n:.4f}")
    print(f"    p_value = {p_value:.4f}")
    print(f"Вывод:")
    print(f"    Уровень значимости p-value = {p_value:.4f}.")
    print()


task_1()
task_1_stats()
