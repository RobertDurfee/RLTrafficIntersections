import numpy
import scipy.interpolate


def get_path(l_a, l_b):

  t = numpy.linspace(0, 1, 100)

  x = numpy.hstack([l_a(t)[0].flatten(), l_b(t)[0].flatten()])
  y = numpy.hstack([l_a(t)[1].flatten(), l_b(t)[1].flatten()])
  points = [x, y]

  spline, _ = scipy.interpolate.splprep(points, s=0)

  return lambda t: scipy.interpolate.splev(t, spline)


def get_turn_matrix(enter, exit):
    
    turn_matrix = [[None for j in range(len(exit))] for i in range(len(enter))]
    
    for i in range(len(enter)):
        for j in range(len(exit)):
            turn_matrix[i][j] = get_path(enter[i], exit[j])
    
    return turn_matrix


if __name__ == '__main__':
  intersection = {
    'entering': [
      (lambda t: numpy.array([[3 + 0 * t], [0 + 1 * t]]))(numpy.linspace(0, 1, 100)).reshape(2, 100).tolist(), # Lower
      (lambda t: numpy.array([[2 + 0 * t], [5 - 1 * t]]))(numpy.linspace(0, 1, 100)).reshape(2, 100).tolist()  # Upper
    ],
    'exiting': [
      (lambda t: numpy.array([[2 + 0 * t], [1 - 1 * t]]))(numpy.linspace(0, 1, 100)).reshape(2, 100).tolist(), # Lower
      (lambda t: numpy.array([[1 - 1 * t], [3 + 0 * t]]))(numpy.linspace(0, 1, 100)).reshape(2, 100).tolist()  # Left
    ]
  }
