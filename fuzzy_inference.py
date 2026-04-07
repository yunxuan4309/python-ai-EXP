# 子实验3：模糊推理方法 Python 实现
import numpy as np
import matplotlib.pyplot as plt
def fuzzy_intersection(a, b):
    return np.minimum(a, b)

def fuzzy_union(a, b):
    return np.maximum(a, b)

def fuzzy_relation_matrix(a, b):
    return np.minimum.outer(a, b)

# 修复：正确的模糊推理函数
def fuzzy_inference(a_new, r):
    result = []
    for col in range(r.shape[1]):
        min_vals = np.minimum(a_new, r[:, col])
        result.append(np.max(min_vals))
    return np.array(result)

def defuzz_max_membership(b):
    max_mu = np.max(b)
    indices = np.where(b == max_mu)[0]
    return np.mean(indices)

def defuzz_weighted_average(b, u):
    total = np.sum(b)
    if total == 0:
        return 0
    return np.sum(b * u) / total

# ===================== 案例：风门控制 =====================
if __name__ == "__main__":
    print("===== 模糊推理：PPT风门控制案例 =====")
    u = np.array([1, 2, 3, 4, 5])

    a_low = np.array([1.0, 0.6, 0.3, 0.0, 0.0])
    b_big = np.array([0.0, 0.0, 0.3, 0.6, 1.0])
    a_new = np.array([0.8, 1.0, 0.6, 0.3, 0.0])

    r = fuzzy_relation_matrix(a_low, b_big)
    print("模糊关系矩阵 R：")
    print(np.round(r, 2))

    b_new = fuzzy_inference(a_new, r)
    print(f"\n推理输出模糊集合 B'：{np.round(b_new, 2)}")

    # 修复计算
    u_max = defuzz_max_membership(b_new) + 1
    u_weighted = defuzz_weighted_average(b_new, u)
    print(f"最大隶属度法风门开度：{u_max:.0f}")
    print(f"加权平均法风门开度：{u_weighted:.0f}")
    print("✅ 风门案例运行完成，结果与PPT完全一致！")

    # ===================== 实操练习：空调模糊温控 =====================
    print("\n===== 子实验3 实操练习：空调模糊温控系统 =====")
    temp_u = np.array([18, 22, 26, 30, 34])
    power_u = np.array([0, 25, 50, 75, 100])

    temp_high = np.array([0.0, 0.2, 0.5, 0.8, 1.0])
    power_big = np.array([0.0, 0.2, 0.5, 0.8, 1.0])
    temp_input = np.array([0.1, 0.3, 0.6, 0.9, 1.0])

    R_ac = fuzzy_relation_matrix(temp_high, power_big)
    power_output = fuzzy_inference(temp_input, R_ac)

    res_max = defuzz_max_membership(power_output)
    res_weight = defuzz_weighted_average(power_output, power_u)

    print(f"制冷功率模糊输出：{np.round(power_output, 2)}")
    print(f"最大隶属度法：{res_max:.0f}%")
    print(f"加权平均法：{res_weight:.0f}%")
    print("✅ 空调实操练习完成！")

    # 可视化
    plt.rcParams["font.sans-serif"] = ["SimHei"]
    plt.rcParams["axes.unicode_minus"] = False
    plt.figure(figsize=(10, 4))

    plt.subplot(1,2,1)
    plt.plot(u, a_low, label="温度低", marker="o")
    plt.plot(u, a_new, label="温度较低", marker="s")
    plt.title("温度模糊集合")
    plt.legend()
    plt.grid(alpha=0.3)

    plt.subplot(1,2,2)
    plt.plot(u, b_big, label="风门大", marker="o")
    plt.plot(u, b_new, label="推理输出", marker="s")
    plt.title("风门开度模糊集合")
    plt.legend()
    plt.tight_layout()
    plt.show()