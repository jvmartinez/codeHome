[logo]: config/img/CodeHome_120.png
# CodeHome
**CodeHome** It allows to create object oriented structure for php where it facilitates the creation of classes with their respective access indicators (get and set), functions with parameters and without parameters.

[![Donate](https://img.shields.io/badge/Donate-PayPal-green.svg)](https://www.paypal.me/jvmartinez)

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
```php
<?php
class Person{
	private $_dni;
	private $_name;
	private $_lastName;
	private $_address;
	#Method Get
	public function getDni(){
		 return $this->_dni;
	}
    #Method Get
	public function getName(){
		 return $this->_name;
	}
    #Method Get
	public function getLastname(){
		 return $this->_lastName;
	}
    #Method Get
	public function getAddress(){
		 return $this->_address;
	}
    #Method Set
	public function setDni($dni){
		 $this->_dni = $dni;
	}
    #Method Set
	public function setName($name){
		 $this->_name = $name;
	}
    #Method Set
	public function setLastname($lastName){
		 $this->_lastName = $lastName;
	}
    #Method Set
	public function setAddress($address){
		 $this->_address = $address;
	}
    #Method with parameter
	public function CalculateAge ($date){
		/* Structure of the method */
	}
}
?>
```

 ## Contribution
 
 *Your contribution will help us to improve this project.*
 
[![paypal](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://www.paypal.me/jvmartinez)

