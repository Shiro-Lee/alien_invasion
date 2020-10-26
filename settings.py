class Settings:
    """存储《外星人入侵》的所有设置的类"""
    def __init__(self):
        """初始化游戏的静态设置"""
        # 屏幕设置
        self.screen_width = 1000
        self.screen_height = 650
        self.bg_color = (0, 0, 0)

        # 飞船设置
        self.ship_speed_factor = None
        self.ship_limit = 3

        # 子弹设置
        self.bullet_speed_factor = None
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 255, 0)
        self.bullets_allowed = 3

        # 外星人设置
        self.fleet_drop_speed = 8
        # fleet_direction为1表示右移，为-1表示左移
        self.fleet_direction = None
        self.alien_speed_factor = None
        self.alien_points = None

        # 加快游戏节奏的速度
        self.speedup_scale = 1.2
        # 外星人点数的提高速度
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """初始化随游戏进行而变化的设置"""
        self.ship_speed_factor = 0.6
        self.bullet_speed_factor = 2
        self.alien_speed_factor = 0.3
        self.fleet_direction = 1
        self.alien_points = 50

    def increase_speed(self):
        """提高速度设置和外星人点数"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
