from app.models.animals_management import Animal_management
from app.service.animal_service import Animal_service
from app.repositories.animal_repo import Animal_repo

def test_get_list_animal_succes(test_app, mocker):
    mock_animal_data = [
        Animal_management(id=1, species='Dog', age=1, gender='Male', spesial_requirements='Needs special care'),
        Animal_management(id=2, species='Dog', age=1, gender='Male', spesial_requirements='Needs special care')
    ]
    mocker.patch.object(Animal_repo, 'list_animal', return_value=mock_animal_data)

    with test_app.test_request_context():
        animal_service = Animal_service().list_animal()

    assert len(animal_service) == 2
    assert animal_service[0]['species'] == 'Dog'
    assert animal_service[1]['gender'] == 'Male'

def test_create_animal_succes(test_app, mocker):
    mock_animal_data = Animal_management(id=2, species='Dog', age=2, gender='Female', spesial_requirements='Needs special care')
    mocker.patch.object(Animal_repo, 'create_animal', return_value=mock_animal_data)

    animal_data = {
        'id': 2,
        'species': 'Dog',
        'age': 2,
        'gender': 'Female',
        'spesial_requirements': 'Needs special care'
    }

    with test_app.test_request_context():
        animal_service_create = Animal_service().create_animal(animal_data)

        assert animal_service_create['id'] == 2
        assert animal_service_create['species'] == 'Dog'
        assert animal_service_create['age'] == 2
        assert animal_service_create['gender'] == 'Female'
        assert animal_service_create['spesial_requirements'] == 'Needs special care'
