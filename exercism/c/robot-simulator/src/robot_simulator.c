#include <stdlib.h>

#include "robot_simulator.h"

robot_grid_status_t robot_init_with_position(int bearing, int x, int y) {
  robot_grid_status_t *status = malloc(sizeof(robot_grid_status_t));
  robot_coordinates_t *grid = malloc(sizeof(robot_coordinates_t));
  status->bearing = bearing < HEADING_MAX ? bearing : 0;
  status->grid = *grid;
  status->grid.x_position = x;
  status->grid.y_position = y;
  return *status;
}

robot_grid_status_t robot_init(void) {
  return robot_init_with_position(DEFAULT_BEARING, DEFAULT_X_COORDINATE,
                                  DEFAULT_Y_COORDINATE);
}

void robot_turn_right(robot_grid_status_t *robot) {
  robot->bearing = (robot->bearing + 1) % HEADING_MAX;
}

void robot_turn_left(robot_grid_status_t *robot) {
  robot->bearing = (robot->bearing - 1) % HEADING_MAX;
}

void robot_advance(robot_grid_status_t *robot) {
  switch (robot->bearing) {
  case HEADING_NORTH:
    robot->grid.y_position++;
    break;
  case HEADING_EAST:
    robot->grid.x_position++;
    break;
  case HEADING_SOUTH:
    robot->grid.y_position--;
    break;
  case HEADING_WEST:
    robot->grid.x_position--;
    break;
  default:
    break;
  }
}

void robot_simulator(robot_grid_status_t *robot, const char *commands) {
  char c;
  while ((c = *commands++) != '\0') {
    switch (c) {
    case COMMAND_LEFT:
      robot_turn_left(robot);
      break;
    case COMMAND_RIGHT:
      robot_turn_right(robot);
      break;
    case COMMAND_ADVANCE:
      robot_advance(robot);
      break;
    }
  }
}
