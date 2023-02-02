from pay.order import LineItem

def test_line_item_default() -> None:
    li = LineItem('Test', 100)
    assert li.total == 100

def test_line_item() -> None:
    li = LineItem('Test', 200, 5)
    assert li.total == 1000