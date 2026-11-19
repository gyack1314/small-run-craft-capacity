# 柔性工坊的共享批次交期与报价方案分析

业务输入与政策见[数据契约](docs/数据契约.md)，原始表见fixtures/manifest.json。

## 本地环境

Python 3.11，依赖固定在requirements.txt。安装与资料检查：

```sh
python -m pip install -r requirements.txt
python -m unittest discover -s tests -v
```

容器可复现资料检查：

```sh
docker build -t culture-analysis-local .
docker run --rm culture-analysis-local
```

业务应用应提供与其实际功能对应的操作说明和运行测试。上述现有检查只验证来源材料，不计算业务结果。
