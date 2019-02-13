class Car:

  # path_len: (1, ['mi'], [])
  # max_throt_val: (3.5, ['m'], ['s', 's'])
  # max_brk_val: (7.5, ['m'], ['s', 's'])
  # drag_area: (0.79, ['m', 'm'], [])
  # air_density: (1.225, ['kg'], ['m', 'm', 'm'])
  # s: (0, ['mi'], ['hr'])
  # v: (25, ['mi'], ['hr'])

  def __init__(self, path, path_len, path_len_units, max_throt_val, max_throt_val_units, max_brk_val, max_brk_val_units, drag_area, drag_area_units, s, s_units, v, v_units, throt_pct, brk_pct, prndl):
    # Constants
    self.path = path
    self.max_throt_val = max_throt_val
    self.max_brk_val = max_brk_val
    self.drag_area = drag_area
    # Variables
    self.s = s
    self.v = v
    self.throt_pct = throt_pct
    self.brk_pct = brk_pct
    self.prndl = prndl
    # Computed
    self.on_path = (0 <= self.s <= 1)
    self.x, self.y = self.path.position(self.s)
    self.dx, self.dy = self.path.direction(self.s)

  def change_prndl(self, prndl):

    # If off-path, behavior is undefined.
    if not self.on_path:
      return

    # Ensure the car is not moving before changing gear.
    if self.v == 0:
      self.prndl = prndl

  def move(self, dt):

    # If off-path, behavior is undefined.
    if not self.on_path:
      return

    # Acceleration is given by positive throttle, negative break, and negative drag.
    a = (self.throt_pct * self.max_throt_val) - (self.brk_pct * self.max_brk_val) - self.drag

    # Assume speed and acceleration are constant over small time interval dt.
    ds = self.v * dt + (1 / 2) * a * dt ** 2

    if ds > 0:

      if self.prndl == 'drive':
        self.s += ds
      elif self.prndl == 'reverse':
        self.s -= ds

      self.v += a * dt

    # If the car changes direction, it must stop.
    else:
      self.v = 0

    if 0 <= self.s <= 1:

      self.x, self.y = self.path.position(self.s)
      self.dx, self.dy = self.path.direction(self.s)
    
    # If car goes off-path, behavior is undefined.
    else:

      self.s = None
      self.v = None
      self.throt_pct = None
      self.brk_pct = None
      self.prndl = None
      self.on_path = False
      self.x, self.y = None, None
      self.dx, self.dy = None, None
