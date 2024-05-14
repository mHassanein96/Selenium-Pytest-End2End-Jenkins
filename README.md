# Selenium Pytest End2End Jenkins CI/CD

This project is a comprehensive demonstration of testing automation skills using pytest and Selenium, coupled with CI/CD integration through Jenkins. It's structured into three main parts, each focusing on different aspects of testing and automation:

## 1. DemoPytest Package:

In this part, various features of pytest are showcased, providing insights into how pytest can enhance testing processes. It covers:
- **Hard and Soft Assertions**: Demonstrates the use of both types of assertions for different testing scenarios.
- **Marks**: Utilized for categorizing tests and running specific subsets like Somke, Regression and Sainty tests during test execution.
- **Fixtures**: Shows how fixtures can be used to set up preconditions for tests and perform cleanup afterward.
- **Data Parameters**: Illustrates parameterization of tests to run with different input data.
- **Xfails and Skips**: Highlights handling of expected failures and skipping tests under certain conditions.

![Screenshot 2024-05-13 214300](https://github.com/mHassanein96/Selenium-Pytest-End2End-Jenkins/assets/133708970/eda4b813-922e-4d8a-a5f8-21fbedbf4691)

## 2. Testing Login and Change Password Features with Page Object Model (POM):

This section focuses on applying the Page Object Model (POM) design pattern to test the login and password change functionalities. It includes:
- **Pages Package**: Organizes Page Object Model classes:
  - **Base Page**: Serves as a parent class with essential methods and constructors shared across all pages.
  - **Login Page**: Contains methods for interacting with the login page elements and performing login actions.
  - **Password Page**: Implements actions related to changing passwords.
- **Utilities Package**: Includes:
  - **Test Data**: Centralized data storage for login credentials, page URLs, etc.
  - **Locators**: Defines locators for web elements to maintain a clean separation of concerns.
- **Tests Package**: Contains test logic for login and password change features, utilizing the Page Object Model for better test readability and maintenance.
- **Conftest File**: Defines fixtures to set up different browsers (Chrome, Firefox, Edge) for testing and handles teardown operations after each test.

![SeleniumPytest-ezgif com-speed](https://github.com/mHassanein96/Selenium-Pytest-End2End-Jenkins/assets/133708970/b48a978f-a759-42c0-be2d-37ee177da4cb)

## 3. Jenkins Integration:

This part demonstrates the integration of the testing suite with Jenkins for continuous integration and delivery. It covers:
- **Jenkins Setup**: Instructions on setting up Jenkins for CI/CD purposes.
- **Repository Integration**: Explains how to extract tests from the GitHub repository.
- **Environment Setup**: Details on configuring the testing environment within Jenkins.

![SeleniumPytestJenkinsConfig-ezgif com-speed](https://github.com/mHassanein96/Selenium-Pytest-End2End-Jenkins/assets/133708970/1bc8500d-e36a-435e-b393-dd94235e8219)

- **Test Execution**: Steps to run the tests automatically triggered by Jenkins.
- **Reporting**: Exporting test reports in Allure and HTML formats for comprehensive result analysis.

![SeleniumPytestJenkinsReport-ezgif com-speed](https://github.com/mHassanein96/Selenium-Pytest-End2End-Jenkins/assets/133708970/14c77acb-d82a-4701-a69d-637ce0ff43af)

## Demonstration:

This project serves as a comprehensive demonstration of testing automation skills, encompassing test case organization, Page Object Model implementation, and seamless integration with Jenkins for automated testing and reporting.

## Disclaimer:

Specific test data and detailed Jenkins setup instructions are not included in this public repository for security and privacy reasons.
We would like to extend our gratitude to the team at [LambdaTest](https://lambdatest.com/) for their support and services in facilitating cross-browser testing for this project.
