def test_get_all__lanetswith_no_records(client):
    # Act
    response = client.get("/planets")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []


def test_get_one_planet(client, two_saved_planets):
    # Act
    response = client.get("/planets/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == {
        "name": "Arrakis",
        "description": "Got the spice",
        "has_moons": True
    }


# def test_create_a_book(client):
#     # act
#     response = client.post("/books", json = {
#         "title" : "The Never Ending Story",
#         "description" : "The horse dies"
#     })
#     response_body = response.get_json()
    
#     # assert
#     assert response.status_code == 201
#     assert response_body == {
#         "id" : 1,
#         "title" : "The Never Ending Story",
#         "description": "The horse dies"
#     }