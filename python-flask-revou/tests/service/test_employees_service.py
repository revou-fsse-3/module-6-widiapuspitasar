from app.models.employees import Employees
from app.service.employees_service import Employees_service
from app.repositories.employees_repo import Employees_repo

def test_get_list_employees_succes(test_app, mocker):
    mock_employees_data = [
        Employees(id=1, name='wid', phonenumber=85719, role='Staff', schedule='Morning', email='wid@gmail.com'),
        Employees(id=1, name='wid', phonenumber=85719, role='Staff', schedule='Morning', email='wid@gmail.com')
    ]
    mocker.patch.object(Employees_repo, 'list_employees', return_value=mock_employees_data)

    with test_app.test_request_context():
        employees_service = Employees_service().list_employees()

    assert len(employees_service) == 2
    assert employees_service[0]['name'] == 'wid'
    assert employees_service[1]['role'] == 'Staff'

def test_create_employees_succes(test_app, mocker):
    mock_employees_data = Employees(id=2, name='wid', phonenumber=85719, role='Staff', schedule='Morning', email='wid@gmail.com')
    mocker.patch.object(Employees_repo, 'create_employees', return_value=mock_employees_data)

    employees_data = {
        'id': 2,
        'name': 'wid',
        'phonenumber': 85719,
        'role': 'Staff',
        'schedule': 'Morning',
        'email': 'wid@gmail.com'
    }

    with test_app.test_request_context():
        employees_service_create = Employees_service().create_employees(employees_data)

        assert employees_service_create['id'] == 2
        assert employees_service_create['name'] == 'wid'
        assert employees_service_create['phonenumber'] == 85719
        assert employees_service_create['role'] == 'Staff'
        assert employees_service_create['schedule'] == 'Morning'
        assert employees_service_create['email'] == 'wid@gmail.com'
