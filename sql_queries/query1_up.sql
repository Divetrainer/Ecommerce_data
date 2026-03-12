INSERT INTO department (department_id, name) VALUES
(1, 'Engineering')
, (2, 'Marketing')
, (3, 'Human Resources')
, (4, 'Finance')
;

INSERT INTO locations (location_id, name, city, state) VALUES
(1, 'HQ', 'Los Angeles', 'CA')
, (2, 'East Coast', 'New York', 'NY')
, (3, 'Central Hub', 'Kokomo', 'IN')
, (4, 'South Office', 'Miami', 'FL')
;

INSERT INTO users (id, username, employee_id, is_admin, department_id, location_id) VALUES
(1, 'jsmith',    1001, TRUE,  1, 1)
, (2, 'mjohnson',  1002, FALSE, 2, 2)
, (3, 'swilliams', 1003, FALSE, 3, 3)
, (4, 'bbrown',    1004, FALSE, 1, 4)
, (5, 'jdavis',    1005, TRUE,  4, 1)
;

