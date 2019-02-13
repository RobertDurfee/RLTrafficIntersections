import scipy.interpolate
import scipy.integrate
import numpy

class Path:

  def __init__(self, xs, ys):
    # Reconstruct the time-parameterized path
    time_spline, _ = scipy.interpolate.splprep([xs, ys], s=0)
    time_path = lambda t: numpy.array(scipy.interpolate.splev(t, time_spline, der=0))

    # Determine the speed function
    speed = lambda t: numpy.linalg.norm(scipy.interpolate.splev(t, time_spline, der=1), axis=0)

    # Determine the length of the path
    length_total = lambda t: scipy.integrate.quad(speed, 0, 1)[0]

    # Determine the length inverse function
    t = numpy.linspace(0, 1, 100)
    length_star_inverse_spline = scipy.interpolate.splrep(scipy.integrate.cumtrapz(speed(t) / length_total, t, initial=0), t, s=0)
    length_star_inverse = lambda s: scipy.interpolate.splev(s, length_star_inverse_spline)

    # Determine the arc-length-parameterized path
    arc_length_path = lambda s: time_path(length_star_inverse(s))

    # Fit a spline one more time to get more accurate gradient
    s = numpy.linspace(0, 1, 100)
    self.arc_length_spline = scipy.interpolate.splprep(arc_length_path(s), s=0)
    self.arc_length_path = lambda s: numpy.array(scipy.interpolate.splev(s, self.arc_length_spline, der=0))
    self.arc_length_path_gradient = lambda s: numpy.array(scipy.interpolate.splev(s, self.arc_length_spline, der=1))

  def position(self, s):
    return tuple(self.arc_length_path(s))

  def direction(self, s):
    return tuple(self.arc_length_path_gradient(s) / numpy.linalg.norm(self.arc_length_path_gradient(s)))