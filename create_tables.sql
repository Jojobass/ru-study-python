CREATE TABLE IF NOT EXISTS Regions(
    Region_id SERIAL PRIMARY KEY,
    "name" VARCHAR UNIQUE
);
CREATE TABLE IF NOT EXISTS Locations(
    Location_id SERIAL PRIMARY KEY,
    "address" VARCHAR,
    Region_id INTEGER,
    CONSTRAINT valid_region 
    FOREIGN KEY (Region_id)
    REFERENCES Regions(Region_id)
);
CREATE TABLE IF NOT EXISTS Departments(
    Department_id SERIAL PRIMARY KEY,
    "name" VARCHAR,
    Location_id INTEGER,
    Manager_id INTEGER,
    CONSTRAINT valid_location
    FOREIGN KEY (Location_id)
    REFERENCES Locations(Location_id)
);
CREATE TABLE IF NOT EXISTS Employees(
    Employee_id SERIAL PRIMARY KEY,
    "name" VARCHAR,
    Last_name VARCHAR,
    Hire_date DATE,
    Salary INTEGER,
    Email VARCHAR,
    Manager_id INTEGER,
    Department_id INTEGER,
    CONSTRAINT valid_manager
    FOREIGN KEY (Manager_id)
    REFERENCES Employees(Employee_id),
    CONSTRAINT valid_department
    FOREIGN KEY (Department_id)
    REFERENCES Departments(Department_id)
);
ALTER TABLE Departments
ADD CONSTRAINT valid_manager
    FOREIGN KEY (Manager_id)
    REFERENCES Employees(Employee_id);