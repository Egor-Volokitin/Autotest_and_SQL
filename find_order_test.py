# Волокитин Егор, 7-я кагорта. Финальный проект. Инженер по тестированию плюс

import sender_stand_request


def test_something_wrong_here():
    order_response = sender_stand_request.find_order()

    assert order_response.status_code == 200
