from app.service.employees_service import Employees_service
from app import db

def test_get_employees(test_app, mocker):
    #Arrange
    mock_employees_data = [
        {
            "email": "wid@gmail.com",
            "id": 25,
            "name": "Sari",
            "phonenumber": 857194817,
            "role": "Staff",
            "schedule": "Night"
        },
    ]
    mocker.patch.object(Employees_service, 'list_employees', return_value=mock_employees_data)
    
    #Act
    with test_app.test_client() as client:
        response = client.get("/employees/")

    #Assert
    assert response.status_code == 200
    assert len(response.json['data']) == len(mock_employees_data)
    assert response.json['data'] == (mock_employees_data)

def test_post_employees(test_app, mocker):
    #Arrange
    data = {
        "email": "wid@gmail.com",
        "id": 25,
        "name": "Sari",
        "phonenumber": 857194817,
        "role": "Staff",
        "schedule": "Night"
    }
    mocker.patch.object(Employees_service, 'create_employees', return_value=data)

    #Act
    with test_app.test_client() as client:
        response = client.post("/employees/", json=data)
    
    #Assert
    expected_response = {
        "email": "wid@gmail.com",
        "name": "Sari",
        "phonenumber": 857194817,
        "role": "Staff",
        "schedule": "Night"
    }

    assert response.json['data']["name"] == "Sari"
    assert response.status_code == 200

def test_put_edit_employees(test_app, mocker):
    #Arrange
    data = {
        "email": "wid@gmail.com",
        "name": "Sari",
        "phonenumber": 857194817,
        "role": "Staff",
        "schedule": "Night"
    }

    mocker.patch.object(Employees_service, 'edit_employees', return_value=data)

    #Act
    with test_app.test_client() as client:
        response = client.put("/employees/99", json=data)
    
    #Assert
    assert response.status_code == 200

def test_delete_employees(test_app, mocker):
    #Arrange
    expected_response ={
        "email": "wid@gmail.com",
        "name": "Sari",
        "phonenumber": 857194817,
        "role": "Staff",
        "schedule": "Night"
    }

    mocker.patch.object(Employees_service, 'delete_employees', return_value=expected_response)

    #Act
    with test_app.test_client() as client:
        response = client.delete("/employees/99")
    
    #Assert
    assert response.status_code == 200

def test_delete_employees_not_found(test_app, mocker):
   # Arrange
   expected_response = "Employees not found"

   mocker.patch.object(Employees_service, 'delete_employees', return_value=expected_response)
   
   with test_app.test_client() as client:
      # Act
      response = client.delete("/employees/1000")

   # Assert
   assert response.status_code == 404