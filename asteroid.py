import random
from circleshape import *
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event

class Asteroid(CircleShape):
	def __init__(self, x: float, y: float, radius: float) -> None:
		super().__init__(x, y, radius)

	def draw(self, screen: pygame.Surface) -> None:
		pygame.draw.circle(screen, "white", self.position, self.radius, width=LINE_WIDTH)

	def update(self, dt: float) -> None:
		self.position += (self.velocity * dt)

	def split(self):
		self.kill()
		if self.radius <=  ASTEROID_MIN_RADIUS:
			return
		log_event("asteroid_split")
		angle = random.uniform(20, 50)
		ast1_vector = self.velocity.rotate(angle)
		ast2_vector = self.velocity.rotate(-angle)
		new_radii = self.radius - ASTEROID_MIN_RADIUS
		new_ast1 = Asteroid(self.position.x, self.position.y, new_radii)
		new_ast2 = Asteroid(self.position.x, self.position.y, new_radii)
		new_ast1.velocity = ast1_vector * 1.2
		new_ast2.velocity = ast2_vector * 1.2
