import numpy as np

def resolve_circle_collision(b1, b2):
    normal = b2.position - b1.position
    dist = np.linalg.norm(normal)

    if dist == 0:
        return

    if dist < b1.radius + b2.radius:
        normal /= dist

        relative_velocity = b2.velocity - b1.velocity
        vel_along_normal = np.dot(relative_velocity, normal)

        if vel_along_normal > 0:
            return

        restitution = min(b1.restitution, b2.restitution)

        impulse_mag = -(1 + restitution) * vel_along_normal
        impulse_mag /= b1.inv_mass + b2.inv_mass

        impulse = impulse_mag * normal

        b1.velocity -= impulse * b1.inv_mass
        b2.velocity += impulse * b2.inv_mass

        # Positional correction
        penetration = b1.radius + b2.radius - dist
        correction = normal * penetration * 0.5

        if b1.mass != 0:
            b1.position -= correction
        if b2.mass != 0:
            b2.position += correction


def resolve_wall_collision(body, width, height):
    if body.mass == 0:
        return

    # Left / Right
    if body.position[0] - body.radius < 0:
        body.position[0] = body.radius
        body.velocity[0] *= -body.restitution

    if body.position[0] + body.radius > width:
        body.position[0] = width - body.radius
        body.velocity[0] *= -body.restitution

    # Top / Bottom
    if body.position[1] - body.radius < 0:
        body.position[1] = body.radius
        body.velocity[1] *= -body.restitution

    if body.position[1] + body.radius > height:
        body.position[1] = height - body.radius
        body.velocity[1] *= -body.restitution