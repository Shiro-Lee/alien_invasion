class GameStats:
    """跟踪游戏的统计信息"""
    level: int
    score: int

    def __init__(self, ai_settings):
        """初始化统计信息"""
        self.ai_settings = ai_settings
        self.ships_left = ai_settings.ship_limit
        # 让游戏一开始处于非活动状态
        self.game_active = False
        self.reset_stats()
        # 在任何情况下都不重置最高分
        self.high_score = 0

    def reset_stats(self):
        """初始化在游戏运行期间可能变化的统计信息"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
