# demo-api

GitHub PR -> CNB build -> TCR push 演示项目。

## 仓库职责划分

| 平台 | 职责 | 内容 |
|------|------|------|
| GitHub（本仓库） | 源码托管、PR 协作评审 | app.py / Dockerfile |
| CNB (cnb.cool) | CI 流水线、镜像构建 | 额外含 `.cnb.yml`（不进本仓库） |
| 腾讯云 TCR | 镜像制品仓库 | 构建产出的容器镜像 |

`.cnb.yml` 刻意不纳入本仓库（见 .gitignore）：CI 与镜像构建均在 CNB 侧执行，
且该文件涉及镜像仓库凭证配置，凭证本身应存放于 CNB 密钥仓库并通过 imports 引用。
