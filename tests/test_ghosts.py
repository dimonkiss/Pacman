import pytest
import pygame
from ghosts import Blinky
from vector import Vector2
from constants import *
from nodes import Node

@pytest.fixture
def node():
    return Node(0, 0)

@pytest.fixture
def ghost(node):
    pygame.init()
    pygame.display.set_mode((1, 1))
    return Blinky(node)

def test_ghost_initialization(ghost):
    assert ghost.name == BLINKY
    assert isinstance(ghost.position, Vector2)
    assert ghost.direction == STOP
    assert ghost.speed == 100
    assert ghost.color == RED
    assert ghost.mode.current == SCATTER

def test_ghost_movement(ghost, node):
    # Додаємо сусіда ліворуч
    left_node = Node(-1, 0)
    node.neighbors[LEFT] = left_node
    ghost.target = left_node
    initial_pos = ghost.position.copy()
    ghost.direction = LEFT
    ghost.update(1.0)  # Update for 1 second
    assert ghost.position.x < initial_pos.x
    assert ghost.position.y == initial_pos.y

def test_ghost_mode_change(ghost):
    assert ghost.mode.current == SCATTER
    ghost.mode.current = CHASE
    assert ghost.mode.current == CHASE
    ghost.mode.current = SCATTER
    assert ghost.mode.current == SCATTER 