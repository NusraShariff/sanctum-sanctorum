def test_members_can_be_paginated(client, make_member):
    first = make_member(name="First")
    second = make_member(name="Second")
    third = make_member(name="Third")

    response = client.get("/members", params={"limit": 2, "offset": 1})

    assert response.status_code == 200
    assert response.json() == {
        "items": [second, third],
        "total": 3,
        "limit": 2,
        "offset": 1,
    }
    assert first["id"] < second["id"] < third["id"]


def test_failed_multi_item_order_does_not_reserve_earlier_stock(client, make_member, make_book):
    member = make_member()
    first = make_book(stock=2)
    second = make_book(stock=1)

    response = client.post(
        "/orders",
        json={
            "member_id": member["id"],
            "items": [
                {"book_id": first["id"], "quantity": 1},
                {"book_id": second["id"], "quantity": 2},
            ],
        },
    )

    assert response.status_code == 409
    assert client.get(f"/books/{first['id']}").json()["stock"] == 2
    assert client.get(f"/books/{second['id']}").json()["stock"] == 1