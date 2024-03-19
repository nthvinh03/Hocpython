import turtle

t = turtle.Turtle()

t.pencolor('red')


def draw(n, width=100):
    """Hàm vẽ hình đa giác đều
    n - số cạnh của đa giác đều,
    width - chiều dài của các cạnh
    """
    # Giá trị mỗi góc của đa giác
    angle = (n - 2) * 180 / n
    for i in range(n):
        t.forward(width)
        t.right(180 - angle)

    turtle.done()

draw(10)