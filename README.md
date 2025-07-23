
# 📈 Portfolio Visualiser

A fullstack website that retrieves a range of client's asset data
using broker's APIs or manually through spreadsheet files.
Condensing it into a single portfolio that can be easily visualised,
analysed and backtested against other portfolios or strategies.


## ✨ Features

- OAuth2 User Authorisation with JWT Session Tokens
- No-Knowledge Server-Side Encryption
- ...and many more to come!


## 🛠️ Tech Stack

**Backend**:
- Python
- FastAPI
- Pytest
- SQLAlchemy
- See `requirements.txt` for a much more comprehensive list.

**Server**:
- PostgreSQL
- Alembic

**Frontend**
- Svelte
- Chart.js
- npm


## 🎥 Demo

There is a demo of the website on the login page, a button titled "See a Demo?", this will show the full website with a mock portfolio and user.

Soon, I intend to replace this section with a fully recorded demo video!


## 🛫 Run Locally

Using Uvicorn for Backend and Vite for Frontend.

```bash
# Clone the project
git clone https://github.com/Dakkabi/Portfolio-Visualiser.git

# Change directory to Backend
cd /Portfolio-Visualiser/backend/src

# Run FastAPI Entry-point
python main.py &

# Change directory to Frontend
cd ../../frontend

# Install npm dependencies
npm install

# Run local host
npm run dev --open
```


## 👤 Authors

This is (currently) a personal project; there are no other authors apart from myself. Please see __Contributing__ if you would like to help contribute! :)


## 👨‍💻 Contributing

Contributions will be very helpful in adding new features that may of been overlooked,
even simple additions drastically increase the usability of the site.

I recommend using PyCharm as this will help with FastAPI integration and Pytest case testing!

- Backend merge requests should include successful pytest coverage for your additions.
- Comments docstring are necessary and should use the reST format (default in PyCharm).


## ☁️ Environment Variables

The full `.env` file requirements are found in `.env.local` with some default values.

`backend/src/core/config.py` will import the `.env` file, which can then be retrieved by importing `settings()` and add some type hinting via pydantic
- Adding new `.env` variables, you should specify the type in the config file.


## 💬 Feedback

Feedback, whether requesting a new feature or changing existing features, should be made as an Issue with a __Deliverable__ heading detailing what the project needs, and a __Requirement__ optional header detailing what should be delivered to the project in terms of additions.

See: [Example Issue.](https://github.com/users/Dakkabi/projects/1/views/1?pane=issue&itemId=115883069&issue=Dakkabi%7CPortfolio-Visualiser%7C5)

You are free to see what issues I am currently working on at: https://github.com/users/Dakkabi/projects/1/views/1

