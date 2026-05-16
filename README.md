# Python AI 实验项目

## 项目简介

本项目包含三个人工智能不确定性推理算法的Python实现，涵盖了可信度方法、D-S证据理论和模糊推理方法。每个实验都包含了理论复现和实际应用案例，适合学习AI中的不确定性处理技术。

## 项目结构

```
python-ai-EXP/
├── cf_model_experiment.py    # 子实验1：可信度方法（C-F模型）
├── ds_theory.py              # 子实验2：D-S证据理论
├── fuzzy_inference.py        # 子实验3：模糊推理方法
└── README.md                 # 项目说明文档
```

## 子实验详情

### 1. 可信度方法（C-F模型）

**文件**: `cf_model_experiment.py`

**功能特性**:
- 实现了可信度的组合证据计算（合取/析取）
- 不确定性传递计算
- 结论合成算法（修复了除零bug和范围限制问题）
- 包含PPT例4.1的完整复现
- 学生课程挂科风险评估实操练习

**核心函数**:
- `clamp_cf(value)`: 可信度范围限制 [-1,1]
- `calc_combination_evidence(cf_list, operator)`: 组合证据计算
- `calc_cf_transfer(cf_he, cf_e)`: 不确定性传递
- `calc_cf_combine(cf1, cf2)`: 结论合成

### 2. D-S证据理论

**文件**: `ds_theory.py`

**功能特性**:
- 信任函数Bel(A)计算
- 似然函数Pl(A)计算
- Dempster正交和融合算法（修复完全冲突问题）
- PPT医疗诊断案例复现
- 红黄蓝证据融合实操练习

**核心函数**:
- `calc_belief(m, a)`: 计算信任函数
- `calc_plausibility(m, a, d)`: 计算似然函数
- `dempster_combine(m1, m2, d)`: Dempster正交和融合

### 3. 模糊推理方法

**文件**: `fuzzy_inference.py`

**功能特性**:
- 模糊交集、并集运算
- 模糊关系矩阵构建
- 模糊推理计算
- 去模糊化方法（最大隶属度法、加权平均法）
- 风门控制案例复现
- 空调模糊温控系统实操练习
- 可视化结果展示

**核心函数**:
- `fuzzy_intersection(a, b)`: 模糊交集
- `fuzzy_union(a, b)`: 模糊并集
- `fuzzy_relation_matrix(a, b)`: 模糊关系矩阵
- `fuzzy_inference(a_new, r)`: 模糊推理
- `defuzz_max_membership(b)`: 最大隶属度去模糊化
- `defuzz_weighted_average(b, u)`: 加权平均去模糊化

## 运行环境

- Python 3.7+
- NumPy
- Matplotlib (仅用于模糊推理可视化)

## 安装依赖

```bash
pip install numpy matplotlib
```

## 使用方法

分别运行各个实验文件：

```bash
# 运行可信度方法实验
python cf_model_experiment.py

# 运行D-S证据理论实验
python ds_theory.py

# 运行模糊推理实验
python fuzzy_inference.py
```

## 代码改进说明

### C-F模型改进:
- ✅ 修复结论合成结果无范围限制问题
- ✅ 修复异号结论合成除零崩溃风险
- ✅ 增加输入合法性校验
- ✅ 统一使用numpy函数保证计算一致性

### D-S证据理论改进:
- ✅ 增加完全冲突异常处理
- ✅ 浮点数精度修正
- ✅ 规范数据类型和鲁棒性优化

### 模糊推理改进:
- ✅ 修复模糊推理函数逻辑
- ✅ 完善去模糊化计算方法
- ✅ 添加可视化功能

## 应用场景

- **C-F模型**: 专家系统、医疗诊断、风险评估等需要处理不确定性的场景
- **D-S证据理论**: 多传感器信息融合、模式识别、决策支持系统
- **模糊推理**: 控制系统、智能家电、工业自动化等领域

## 学习价值

通过本项目的学习，可以掌握：
1. 不确定性推理的基本原理和算法实现
2. 不同不确定性处理方法的优缺点比较
3. 实际问题的建模和求解能力
4. Python科学计算库的使用技巧

## 许可证

本项目仅供学习交流使用。