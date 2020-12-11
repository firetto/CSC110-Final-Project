"""
firemap.py

Contains functions for drawing the map onto the screen, along with drawing dots onto the map.

CSC110 Final Project by Anatoly Zavyalov, Austin Blackman, Elliot Schrider.
"""
import pygame
import os
from typing import List, Tuple
from window import Window


class FireMap:
    """
    Wrapper class for the core wildfire map, storing the map image and
    providing methods to draw dots on the map.

    """

    # Private Instance Attributes:
    # - _dot_positions: A list of positions to draw dots on the map the next time
    #                   the map is to be drawn onto the screen.
    # - _map_image: PyGame Surface containing background image of the map
    # - _map_surface: PyGame Surface onto which map image and dots will be drawn.
    # - _map_date_text: The string representation of the date that will be drawn.
    # - _MAP_POSITION: The position of the top-left corner of the map image
    # - _MAP_COORDINATE_BOUNDS: Latitude and longitude of the top left and bottom right
    #                           corners of the map image
    # - _MAP_DATE_LABEL_POSITION: The position of where the date label is to be drawn on the map

    # TODO: Think about adding an "intensity" to the dots to change the size of the dots drawn
    _dot_positions: List[Tuple[float, float]]
    _map_image: pygame.Surface
    _map_surface: pygame.Surface
    _map_date_text: str

    # CONSTANTS
    _MAP_POSITION: Tuple[int, int] = (50, 0)

    # (top left, top right) latitude and longitude
    _MAP_COORDINATE_BOUNDS: Tuple[Tuple[int, int], Tuple[int, int]] = ((90, -180), (15, -45))
    _MAP_DATE_LABEL_POSITION: Tuple[int, int] = (0, 0)

    def __init__(self) -> None:
        """
        Initialize map image, list of dot positions.
        """

        # Initialize dot position list
        self._dot_positions = []

        # Load the map image
        self._map_image = pygame.image.load(os.path.join("assets/map.png"))
        self._map_image.convert()

        # Set a placeholder value for the text.
        self._map_date_text = "Click `Play/Pause`"

        # Initialize map surface with size based on image size.
        self._map_surface = pygame.Surface(self._map_image.get_size())

    def draw(self, window: Window) -> None:
        """
        Draw background map image, dots to window.
        """

        # Clear the map surface
        self._map_surface.fill((0, 0, 0))

        # Draw the map image on the map surface
        self._map_surface.blit(self._map_image, (0, 0))

        # Draw each dot on the map surface
        for position in self._dot_positions:
            pygame.draw.circle(self._map_surface, (255, 0, 0), position, 10)

        # Draw the date label onto the map
        self._map_surface.blit(window.render_text(text=self._map_date_text, antialias=True,
                                                  color=pygame.color.Color([255, 255, 255]),
                                                  background=pygame.color.Color(0, 0, 0, 50)),
                               self._MAP_DATE_LABEL_POSITION)

        # Draw the map surface on the screen
        window.draw_to_screen(surface=self._map_surface, position=self._MAP_POSITION)

    def add_dot(self, coordinates: Tuple[float, float]) -> None:
        """
        Add a dot to the map given its latitude and longitude on the map.

        Preconditions:
         - coordinates is in the format (latitude, longitude)
        """

        self._dot_positions.append(self._coords_to_pixel(coordinates))

    def clear_dots(self) -> None:
        """
        Clear dots off the map image. This also redraws the map image.
        """

        self._dot_positions.clear()

    def set_map_date_text(self, text: str) -> None:
        """
        Update the map date text.

        Preconditions:
         - len(text) > 0
        """
        self._map_date_text = text

    def _coords_to_pixel(self, coordinates: Tuple[float, float]) -> Tuple[int, int]:
        """
        Return the pixel position, relative to self._map_image position,
        of coordinates given latitude and longitude.

        NOTE:
        Top left of _map_image represents
        (latitude, longitude) = (90, -180)

        Bottom right of _map_image represents
        (latitude, longitude) = (15, -45)

        Preconditions:
         - coordinates is in the format (latitude, longitude)
        """

        # Size of the map image in pixels
        image_size = self._map_image.get_size()

        # Extract latitude and longitude from coordinates
        latitude, longitude = coordinates

        # Top left and bottom right latitudes and longitudes
        top_left = self._MAP_COORDINATE_BOUNDS[0]
        bot_right = self._MAP_COORDINATE_BOUNDS[1]

        # X and Y ratios of the coordinate's position relative to the image
        # This will be multiplied by the image size later, so it's just a proportion
        # of the image size
        ratio = ((longitude - top_left[1]) / (bot_right[1] - top_left[1]),
                 1 - (latitude - bot_right[0]) / (top_left[0] - bot_right[0]))

        return (int(ratio[0] * image_size[0]), int(ratio[1] * image_size[1]))
