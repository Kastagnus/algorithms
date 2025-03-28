This is completed task of 50 algorithms

Project follows the SOLID principles of OOP

You can find interface file where general interface for each algorithm is given
In algo_manager you will find alogirthm manager which will help you to run algorithm test cases, custom inputs,
getting source code and explanation

Step by step guide:
>> git clone https://github.com/Kastagnus/algorithms.git

>> cd algorithms

>> pip install -r requirements.txt

Use:
1. manager.add_algorithm("Algorithm name", Algorithm) it is already done
2. Run custom input: manager.execute_algorithm("Algorithm name", *args)
3. Run ready test cases: manager.run_tests("Algorithm name")
4. Retrieve source code: manager.get_algorithm_source_code("Algorithm name")
5. Get explanation: manager.get_algorithm_documentation("Algorithm Name")
6. Get all the algorithm names added by manager.add_algorithm method

All the algorithms itself are given into tasks1.py
If you will run app.py you will see the small interface where all 50 algorithms are loaded and you
can run test cases from there, see explanations and source code

P.S app.py is still under development and for some algorithms test runs and custom inputs might not work yet


