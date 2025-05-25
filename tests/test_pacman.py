import pytest
import pygame
from pacman import Pacman
from vector import Vector2
from constants import *
from nodes import Node

@pytest.fixture
def node():
    return Node(0, 0)

@pytest.fixture
def pacman(node):
    pygame.init()
    pygame.display.set_mode((1, 1))
    return Pacman(node)

def test_pacman_initialization(pacman):
    assert isinstance(pacman, Pacman)
    assert isinstance(pacman.position, Vector2)
    assert pacman.direction == LEFT  # Initial direction is LEFT
    assert pacman.speed == 100 * TILEWIDTH/16
    assert pacman.color == YELLOW
    assert pacman.alive == True

def test_pacman_movement(pacman, node):
    # Додаємо сусіда праворуч
    right_node = Node(1, 0)
    node.neighbors[RIGHT] = right_node
    pacman.target = right_node
    initial_pos = pacman.position.copy()
    pacman.direction = RIGHT
    pacman.update(1.0)  # Update for 1 second
    assert pacman.position.x > initial_pos.x
    assert pacman.position.y == initial_pos.y

def test_pacman_die(pacman):
    assert pacman.alive == True
    pacman.die()
    assert pacman.alive == False
    assert pacman.direction == STOP

def test_pacman_reset(pacman):
    pacman.die()
    pacman.reset()
    assert pacman.alive == True
    assert pacman.direction == LEFT

def test_pacman_collision(pacman):
    pacman.position = Vector2(100, 100)
    pacman.direction = RIGHT
    pacman.update(1.0)
    # Add more specific collision tests based on your game's collision logic 