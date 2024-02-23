from app.service.animal_service import Animal_service
from app import db

def test_get_animal(test_app, mocker):
    #Arrange
    mock_animal_data = [
        {
            "age": 5,
            "gender": "Male",
            "id": 13,
            "species": "Monkey",
            "spesial_requirements": "Needs special care"
        },
    ]
    mocker.patch.object(Animal_service, 'list_animal', return_value=mock_animal_data)
    
    #Act
    with test_app.test_client() as client:
        response = client.get("/animals/")

    #Assert
    assert response.status_code == 200
    assert len(response.json['data']) == len(mock_animal_data)
    assert response.json['data'] == (mock_animal_data)

def test_post_customer(test_app, mocker):
    #Arrange
    data = {
        "age": 1,
        "gender": "Male",
        "id": 99,
        "species": "Dog",
        "spesial_requirements": "No Needs special care"
    }
    mocker.patch.object(Animal_service, 'create_animal', return_value=data)

    #Act
    with test_app.test_client() as client:
        response = client.post("/animals/", json=data)
    
    #Assert
    expected_response = {
        "age": 1,
        "gender": "Male",
        "species": "Dog",
        "spesial_requirements": "No Needs special care"
    }

    assert response.json['data']["species"] == "Dog"
    assert response.status_code == 200

def test_put_edit_animal(test_app, mocker):
    #Arrange
    data = {
        "age": 1,
        "gender": "Male",
        "species": "Dog",
        "spesial_requirements": "No Needs special care"
    }


    mocker.patch.object(Animal_service, 'edit_animals', return_value=data)

    #Act
    with test_app.test_client() as client:
        response = client.put("/animals/99", json=data)
    
    #Assert
    assert response.status_code == 200

def test_delete_animal(test_app, mocker):
    #Arrange
    expected_response ={
        "age": 1,
        "gender": "Male",
        "species": "Dog",
        "spesial_requirements": "No Needs special care"
    }

    mocker.patch.object(Animal_service, 'delete_animal', return_value=expected_response)

    #Act
    with test_app.test_client() as client:
        response = client.delete("/animals/99")
    
    #Assert
    assert response.status_code == 200

def test_delete_animal_not_found(test_app, mocker):
   # Arrange
   expected_response = "Animal not found"

   mocker.patch.object(Animal_service, 'delete_animal', return_value=expected_response)
   
   with test_app.test_client() as client:
      # Act
      response = client.delete("/animals/1000")

   # Assert
   assert response.status_code == 404