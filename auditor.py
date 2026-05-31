"""个人品牌资产盘点工具"""


class BrandAsset:
    """品牌资产记录，表示个人品牌的一项资产。"""

    def __init__(self, name: str, category: str, value: str = "待评估"):
        """初始化品牌资产。

        Args:
            name: 资产名称，如"公众号文章50篇"
            category: 资产类别，如"内容资产"、"粉丝资产"
            value: 资产估值描述，如"约15w字"
        """
        self.name = name
        self.category = category
        self.value = value

    def __repr__(self):
        """返回资产的字符串表示。

        Returns:
            格式化的资产描述字符串
        """
        return f"[{self.category}] {self.name} — {self.value}"


class BrandAuditor:
    """品牌资产盘点工具，汇总个人品牌各类资产并生成报告。"""

    CATEGORIES = [
        "内容资产", "粉丝资产", "知识产权",
        "人脉资产", "技能资产", "声誉资产",
    ]

    def __init__(self, owner: str):
        """初始化品牌盘点器。

        Args:
            owner: 品牌所有者姓名
        """
        self.owner = owner
        self.assets = {c: [] for c in self.CATEGORIES}

    def add_asset(self, asset: BrandAsset):
        """添加一项资产到对应类别。

        Args:
            asset: BrandAsset 实例

        Returns:
            返回自身以支持链式调用
        """
        if asset.category in self.assets:
            self.assets[asset.category].append(asset)
        return self

    def total_count(self) -> int:
        """计算所有类别资产的总数量。

        Returns:
            资产总数
        """
        return sum(len(v) for v in self.assets.values())

    def summary(self) -> str:
        """生成品牌资产盘点报告。

        Returns:
            Markdown 格式的完整盘点报告
        """
        lines = [f"# {self.owner} 个人品牌资产盘点\n"]
        total = self.total_count()
        lines.append(f"**资产总数**: {total} 项\n")
        lines.append("| 类别 | 数量 | 核心资产 |")
        lines.append("|------|:----:|----------|")
        for cat in self.CATEGORIES:
            items = self.assets[cat]
            core = items[0].name if items else "暂无"
            lines.append(f"| {cat} | {len(items)} | {core} |")
        lines.append(f"\n## 详细清单\n")
        for cat in self.CATEGORIES:
            items = self.assets[cat]
            if items:
                lines.append(f"### {cat}（{len(items)}项）\n")
                for item in items:
                    lines.append(f"- {item.name} — {item.value}")
                lines.append("")
        return "\n".join(lines)


if __name__ == "__main__":
    auditor = BrandAuditor("张三")
    auditor \
        .add_asset(BrandAsset("公众号文章50篇", "内容资产", "约15w字")) \
        .add_asset(BrandAsset("知乎高赞回答20条", "内容资产", "总计10w赞同")) \
        .add_asset(BrandAsset("粉丝5000", "粉丝资产", "公众号+知乎")) \
        .add_asset(BrandAsset("专栏作者认证", "声誉资产", "平台认证"))
    print(auditor.summary())
