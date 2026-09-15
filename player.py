from circleshape import *
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN_SECONDS
from shot import Shot

class Player(CircleShape):

	def __init__(self, x: float, y: float):
		super().__init__(x, y, PLAYER_RADIUS)
		self.rotation = 0
		self.cooldown = 0

		# in the Player class
	def triangle(self) -> list[pygame.Vector2]:
		forward = pygame.Vector2(0, 1).rotate(self.rotation)
		right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
		a = self.position + forward * self.radius
		b = self.position - forward * self.radius - right
		c = self.position - forward * self.radius + right
		return [a, b, c]

	def rotate(self, dt: float) -> None:
		self.rotation += (PLAYER_TURN_SPEED * dt)

	def update(self, dt: float) -> None:
		keys = pygame.key.get_pressed()

		if keys[pygame.K_a]:
			dt *= -1
			self.rotate(dt)
		if keys[pygame.K_d]:
			self.rotate(dt)
		if keys[pygame.K_w]:
			self.move(dt)
		if keys[pygame.K_s]:
			dt *= -1
			self.move(dt)
		if keys[pygame.K_SPACE]:
			if self.cooldown > 0:
				None
			else:
				self.cooldown = PLAYER_SHOOT_COOLDOWN_SECONDS
				self.shoot()

		self.cooldown -= dt

	def move(self, dt: float) -> None:
		unit_vector = pygame.Vector2(0, 1)
		rotated_vector = unit_vector.rotate(self.rotation)
		rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt
		self.position += rotated_with_speed_vector

	def shoot(self) -> None:
		new_shot = Shot(self.position.x, self.position.y)
		new_shot.velocity = pygame.Vector2(0, 1)
		rotated_vector = new_shot.velocity.rotate(self.rotation)
		rotated_with_speed_vector = rotated_vector * PLAYER_SHOOT_SPEED
		new_shot.velocity += rotated_with_speed_vector
