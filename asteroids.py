import pyglet

batch = pyglet.graphics.Batch()
sprite1 = pyglet.sprite.Sprite(obrazek, batch=batch)
sprite2 = pyglet.sprite.Sprite(obrazek, batch=batch)

# a potom můžeš vykreslit všechny najednou:
batch.draw()

image = pyglet.image.load(...)
image.anchor_x = image.width // 2
image.anchor_y = image.height // 2
self.sprite = pyglet.sprite.Sprite(image, batch=batch)

self.x = self.x + dt * self.x_speed
self.y = self.y + dt * self.y_speed
self.rotation = self.rotation + dt * rotation_speed

ROTATION_SPEED = 4  # radians per second

self.x_speed += dt * ACCELERATION * math.cos(self.rotation)
self.y_speed += dt * ACCELERATION * math.sin(self.rotation)

self.sprite.rotation = 90 - math.degrees(self.rotation)
self.sprite.x = self.x
self.sprite.y = self.y

from pyglet import gl

def draw():
    window.clear()

    for x_offset in (-window.width, 0, window.width):
        for y_offset in (-window.height, 0, window.height):
            # Remember the current state
            gl.glPushMatrix()
            # Move everything drawn from now on by (x_offset, y_offset, 0)
            gl.glTranslatef(x_offset, y_offset, 0)

            # Draw
            batch.draw()

            # Restore remembered state (this cancels the glTranslatef)
            gl.glPopMatrix()

def draw_circle(x, y, radius):
    iterations = 20
    s = math.sin(2*math.pi / iterations)
    c = math.cos(2*math.pi / iterations)

    dx, dy = radius, 0

    gl.glBegin(gl.GL_LINE_STRIP)
    for i in range(iterations+1):
        gl.glVertex2f(x+dx, y+dy)
        dx, dy = (dx*c - dy*s), (dy*c + dx*s)
    gl.glEnd()

def distance(a, b, wrap_size):
    """Distance in one direction (x or y)"""
    result = abs(a - b)
    if result > wrap_size / 2:
        result = wrap_size - result
    return result

def overlaps(a, b):
    """Returns true iff two space objects overlap"""
    distance_squared = (distance(a.x, b.x, window.width) ** 2 +
                        distance(a.y, b.y, window.height) ** 2)
    max_distance_squared = (a.radius + b.radius) ** 2
    return distance_squared < max_distance_squared