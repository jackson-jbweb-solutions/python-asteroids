import pygame

from circleshape import CircleShape
from constants import LINE_WIDTH, PLAYER_SHOOT_SPEED, PLAYER_TURN_SPEED, SHOT_RADIUS


class Shot(CircleShape):
    def __init__(self, x, y, rotation):
        super().__init__(x, y, SHOT_RADIUS)
        self.x = x
        self.y = y
        self.radius = SHOT_RADIUS
        self.rotation = rotation
        self.velocity = pygame.Vector2(0, 1)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        # self.position += self.velocity * dt
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * PLAYER_SHOOT_SPEED * dt
        self.position += rotated_with_speed_vector

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
