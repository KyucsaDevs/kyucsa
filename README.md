<h1 align="center">KYUCSA</h1>
<h3 align="center">Kyambogo University Computing Students Association</h3>
<img width="850" alt="homepage" src="https://github.com/kyucsa-kyambogo/kyucsa/assets/117981104/cd8afa97-05dc-4a0c-b42a-05d7ac3db757">
<br>
<h3 align="center">Welcome to the kyucsa website repository!</h3>

## Table of Contents
- [Getting Started](#getting-started)
  - [Features](#features)
  - [Installation](#installation)
  - [Configuration](#configuration)
  - [Running the Development Server](#running-the-development-server)
- [Contributing](#contributing)
  - [Cloning the Repository](#cloning-the-repository)
  - [Setting Up a Development Environment](#setting-up-a-development-environment)
  - [Development Workflow](#development-workflow)
  - [Submitting a Pull Request](#submitting-a-pull-request)
- [Contact](#contact)

## Getting Started
### Features
- Robust Security
- Online Event Attendance and History
- Membership Registration
- Auto Membership ID Generation
- Membership Fee Payment
- Upcoming Events
- Past Events Gallery
- Live Event Broadcasting

### Installation

1. Clone the repository to your local machine using the following command:
```
git clone https://github.com/kyucsa-kyambogo/kyucsa.git
```
2. Change into the project directory:
```
cd kyucsa/
```
3. Install Virtual enviroment
```
py -m venv env
```
4. Activate the virtual enviroment
```
kyucsa/env/Scripts/activate.bat
```
5. Change into the project directory
```
cd kyucsa/website
```
6. Install the project dependencies using pip:
```
pip install -r requirements.txt
```

### Running the Development Server

1. Start the development server:
```
python manage.py runserver
```

2. Access the website in your browser at `http://localhost:8000`.

## Contributing

We welcome contributions from anyone who wants to improve the KYUCSA website. Please follow the guidelines below to contribute to the project.

### Cloning the Repository

To clone the repository, run the following command:
```
git clone https://github.com/kyucsa-kyambogo/kyucsa.git
```

### Setting Up a Development Environment

1. Follow the [Installation](#installation) and [Configuration](#configuration) steps mentioned above to set up the project on your local machine.

2. Create a new branch for your changes:
```
git checkout -b feature/your-feature-name
```

3. Make your desired changes to the codebase.

### Development Workflow

1. Before starting to work on a new feature or bug fix, create an issue on the [GitHub repository](https://github.com/kyucsa-kyambogo/kyucsa/issues) to discuss it with the maintainers.

2. Follow the coding style and conventions used in the project.

3. Write tests for new features or modifications to existing features to ensure code quality and stability.

4. Run the tests to make sure everything is working correctly:
```
python manage.py test
```

5. Commit your changes with a descriptive commit message:
```
git commit -m "Add feature/fix: description of the changes"
```

### Submitting a Pull Request

1. Push your changes to your forked repository:
```
git push origin feature/your-feature-name
```

2. Open a new pull request on the [GitHub repository](https://github.com/kyucsa-kyambogo/kyucsa/pulls) and provide a detailed description of your changes.

3. The project maintainers will review your pull request, provide feedback, and merge it once approved.

## Contact

If you have any questions or need further assistance, feel free to reach out at:

- Web Lead Chris: kris.skyfallgraphix@gmail.com
