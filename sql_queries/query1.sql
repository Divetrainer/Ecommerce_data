CREATE TABLE department (
    department_id INT PRIMARY KEY
    , name VARCHAR(50) NOT NULL
);

CREATE TABLE locations (
    location_id INT PRIMARY KEY
    , name VARCHAR(50) NOT NULL
    , city VARCHAR(50) NOT NULL
    , state CHAR(2) NOT NULL
);

CREATE TABLE users (
    id INT PRIMARY KEY
    , username VARCHAR(25) UNIQUE NOT NULL
    , employee_id INT NOT NULL
    , is_admin BOOLEAN DEFAULT FALSE --for security default = false
    , department_id INT
    , location_id INT,
    CONSTRAINT fk_department
    	FOREIGN KEY (department_id)
    	REFERENCES department(department_id)
	CONSTRAINT fk_location
  		FOREIGN KEY (location_id)
  		REFERENCES locations(location_id)
);
