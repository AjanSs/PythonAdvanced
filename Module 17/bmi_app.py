from abc import ABC, abstractmethod
import streamlit as st

class Person(ABC):
    def __init__(self,name,age,weight,height):
        self.name = name
        self.age = age
        self._weight = weight
        self._height = height

    @property
    def weight(self):
            return self._weight

    @weight.setter
    def weight(self,value):
      if value <0:
            raise ValueError("Weight can not be negative")
      self._weight = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value < 0:
            raise ValueError("Height can not be negative")
        self._height = value


    @abstractmethod
    def calculate_bmi(self):
        pass
    @abstractmethod
    def get_bmi_category(self):
        pass

    def print_info(self):
        print(f"{self.name}, Age:{self.age}, Weight: {self._weight} kg, Height: {self._height} m,"
              f"BMI: {self.calculate_bmi():.2f}, Category: {self.get_bmi_category()}")


class Adult(Person):

    def calculate_bmi(self):
        return self.weight / (self.height ** 2)

    def get_bmi_category(self):

        bmi = self.calculate_bmi()
        if bmi < 18.5:
            return 'Underweight'
        elif 18.5 <= bmi < 24.9:
            return 'Normal Weight'
        elif 24.9 <= bmi < 29.9:
            return 'Overweight'
        else:
            return 'Obese'

class Child(Person):

    def calculate_bmi(self):
        return self.weight / (self.height ** 2) * 1.3

    def get_bmi_category(self):

        bmi = self.calculate_bmi()
        if bmi < 14:
            return 'Underweight'
        elif 14 <= bmi < 18:
            return 'Normal Weight'
        elif 18 <= bmi < 24:
            return 'Overweight'
        else:
            return 'Obese'


class BMIapp:
    def __init__(self):

        self.people=[]

    def add_people(self,person):
        self.people.append(person)

    def collect_user_data(self):

        st.title("BMI Calculator")

        name = st.text_input("Enter name:")
        age = st.number_input("Enter age:", min_value=0,max_value=120, value=25)
        weight = st.number_input("Enter weight in kilograms:",min_value=0.0, value=70.0)
        height = st.number_input("Enter height in meters:",min_value=0.0,value=1.75)

        if st.button("Add person"):
            if age >=18:
                person = Adult(name,age,weight,height)
            else:
                person = Child(name,age,weight,height)

            self.add_people(person)
            st.success(f"{name} has been added.")


    def print_results(self):

        for person in self.people:
            person.print_info()


    def run(self):

        while True:
            self.collect_user_data()
            cont = input("Do you want to add another person? (yes/no): ").strip().lower()

            if cont != 'yes':
                break

            self.print_results()

#Create an instance of BMIApp and run the application
if __name__ == "__main__":
    app = BMIapp()
    app.run()