[logo]: config/img/CodeHome_120.png
# CodeHome
**CodeHome** It allows to create object oriented structure for php where it facilitates the creation of classes with their respective access indicators (get and set), functions with parameters and without parameters.

## Requirements
 + Python 2.7 (recommended)

## Actions
 ** CodeHome directory **
 + *python codeHome.py*
 +  create class

| Type | References |
| -------- | -------- |
| Variable   | _  |
| Method   | :  |
| Parameter   | *  |

## Examples
> create class Person _dni _name _lastName _address :CalculateAge *date

## Result
> Class generated in the file folder
> file/Person.php
> ```php
<?php
class Person{
	private $_dni;
	private $_name;
	private $_lastName;
	private $_address;
	public function getDni(){
		 return $this->_dni;
	}

	public function getName(){
		 return $this->_name;
	}

	public function getLastname(){
		 return $this->_lastName;
	}

	public function getAddress(){
		 return $this->_address;
	}

	public function setDni($dni){
		 $this->_dni = $dni;
	}

	public function setName($name){
		 $this->_name = $name;
	}

	public function setLastname($lastName){
		 $this->_lastName = $lastName;
	}

	public function setAddress($address){
		 $this->_address = $address;
	}

	public function CalculateAge ($date){
		/* Structure of the method */
	}
}
?>
```



