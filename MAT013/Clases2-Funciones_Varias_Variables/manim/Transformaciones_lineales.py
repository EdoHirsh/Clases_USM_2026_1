from manim import *

class TransformacionLinealEjemplo1(LinearTransformationScene):
  def __init__(self):
    LinearTransformationScene.__init__(
      self,
      show_coordinates=True,
      leave_ghost_vectors=True,
    )

  def construct(self):
    matrix = [[1, 1], [1, 1]]

    #titulo escena
    title=Title("Transformación lineal $T(x)=Ax$")
    self.add(title)
    title.color=YELLOW_B
    title.background_stroke_opacity=1


    Matriz=Tex("$\displaystyle A=\left[\\begin{matrix}1 & 1\\\\1 & 1\\end{matrix}\\right]$")
    Matriz.next_to(title,DOWN)
    Matriz.align_on_border(LEFT)
    Matriz.color=YELLOW_B
    self.add(Matriz)

    self.apply_matrix(matrix)
    self.wait()

class TransformacionLinealEjemplo2(LinearTransformationScene):
  def __init__(self):
    LinearTransformationScene.__init__(
      self,
      show_coordinates=True,
      leave_ghost_vectors=True,
    )

  def construct(self):
    matrix = [[1, 1], [-1, 1]]

    #titulo escena
    title=Title("Transformación lineal $T(x)=Ax$")
    self.add(title)
    title.color=YELLOW_B
    title.background_stroke_opacity=1


    Matriz=Tex("$\displaystyle A=\left[\\begin{matrix}1 & 1\\\\-1 & 1\\end{matrix}\\right]$")
    Matriz.next_to(title,DOWN)
    Matriz.align_on_border(LEFT)
    Matriz.color=YELLOW_B
    self.add(Matriz)

    self.apply_matrix(matrix)
    self.wait()

class TransformacionLinealEjemplo3(LinearTransformationScene):
  def __init__(self):
    LinearTransformationScene.__init__(
      self,
      show_coordinates=True,
      leave_ghost_vectors=True,
    )

  def construct(self):
    matrix = [[1, 1], [0, 1]]

    #titulo escena
    title=Title("Transformación lineal $T(x)=Ax$")
    self.add(title)
    title.color=YELLOW_B
    title.background_stroke_opacity=1


    Matriz=Tex("$\displaystyle A=\left[\\begin{matrix}1 & 1\\\\0 & 1\\end{matrix}\\right]$")
    Matriz.next_to(title,DOWN)
    Matriz.align_on_border(LEFT)
    Matriz.color=YELLOW_B
    self.add(Matriz)

    self.apply_matrix(matrix)
    self.wait()

class TransformacionLinealEjemplo4(LinearTransformationScene):
  def __init__(self):
    LinearTransformationScene.__init__(
      self,
      show_coordinates=True,
      leave_ghost_vectors=True,
    )

  def construct(self):
    matrix = [[1, 0], [0, -1]]

    #titulo escena
    title=Title("Transformación lineal $T(x)=Ax$")
    self.add(title)
    title.color=YELLOW_B
    title.background_stroke_opacity=1


    Matriz=Tex("$\displaystyle A=\left[\\begin{matrix}1 & 0\\\\0 & -1\\end{matrix}\\right]$")
    Matriz.next_to(title,DOWN)
    Matriz.align_on_border(LEFT)
    Matriz.color=YELLOW_B
    self.add(Matriz)

    self.apply_matrix(matrix)
    self.wait()

class TransformacionLinealEjemplo5(LinearTransformationScene):
  def __init__(self):
    LinearTransformationScene.__init__(
      self,
      show_coordinates=True,
      leave_ghost_vectors=True,
    )

  def construct(self):
    matrix = [[1, -1], [-1, 1]]

    #titulo escena
    title=Title("Transformación lineal $T(x)=Ax$")
    self.add(title)
    title.color=YELLOW_B
    title.background_stroke_opacity=1


    Matriz=Tex("$\displaystyle A=\left[\\begin{matrix}1 & -1\\\\-1 & 1\\end{matrix}\\right]$")
    Matriz.next_to(title,DOWN)
    Matriz.align_on_border(LEFT)
    Matriz.color=YELLOW_B
    self.add(Matriz)

    self.apply_matrix(matrix)
    self.wait()

class TransformacionLinealEjemplo6(LinearTransformationScene):
  def __init__(self):
    LinearTransformationScene.__init__(
      self,
      show_coordinates=True,
      leave_ghost_vectors=True,
    )

  def construct(self):
    matrix = [[1, -1], [1, -1]]

    #titulo escena
    title=Title("Transformación lineal $T(x)=Ax$")
    self.add(title)
    title.color=YELLOW_B
    title.background_stroke_opacity=1


    Matriz=Tex("$\displaystyle A=\left[\\begin{matrix}1 & -1\\\\1 & -1\\end{matrix}\\right]$")
    Matriz.next_to(title,DOWN)
    Matriz.align_on_border(LEFT)
    Matriz.color=YELLOW_B
    self.add(Matriz)

    self.apply_matrix(matrix)
    self.wait()