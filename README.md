
# 📈 Portfolio Visualiser

A monolithic full-stack application, allowing users to visualise, analyse and compare their investment portfolios to other models, asset allocations and strategies.

Taking advantage of Investment Brokers' and Crypto Exchanges' REST API endpoints to automatically fetch, sort and combine assets into a single collection.

---

## 🎥 Demo

Currently there are no demos available for the website.

There are plans for a demo user view of the website, as well as adding demo videos to replace this section.

## 🛣️ Roadmap

---

### Broker / Exchange Support

- [ ]  Trading212
- [ ]  Kraken Crypto Exchange
- [ ]  Robinhood

### Development roadmap

- [ ]  Add the ability to store API Keys into the database from Brokers / Exchanges
- [ ]  Dashboard page with charts and basic information

See https://github.com/users/Dakkabi/projects/1 for a full view of what issues I am currently working on, or what will work on in the future.

---

## 🛠️ Tech Stack

**Client**
- React
- TypeScript
- Axios
- DaisyUI
- TailwindCSS

**Server**
- Python3
- FastAPI
- Pydantic
- JWT
- Bcrypt
- And many more, see `requirements.txt` for a full list!

**Database**
- SQLAlchemy
- Postgres
- Alembic

---

## 🚀 Run Locally

Clone the project

```bash
  git clone https://github.com/Dakkabi/Portfolio-Visualiser.git
```

Go to the project directory

```bash
  cd Portfolio-Visualiser
```

Install backend dependencies

```bash
  pip install -r requirements.txt
```

Update alembic database migrations
```bash
  alembic upgrade head
```

Install frontend dependencies

```bash
  # Inside ./frontend/ directory
  npm install
```

Run Entrypoints
```bash
  # Root repository directory
  python3 ./backend/src/main.py

  # In ./frontend/ directory
  npm run dev
```

---
 
## 🤫 Environment Variables

There is a template `.env.local` stored at repository root to show all environment variables available.

Some environmental variables are optional such as for brokers and crypto exchanges.

Pydantic has been used to add types to the `.env` variables

---

## 🧑‍💻 Contributing

Contributions, no matter how small, increases the usability of the site drastically.

PyCharm is recommended for Pytest integration and useful utilities with FastAPI.

There are only two general requirements for pull requests:
- Ensure 100% line coverage with Pytest, using Pytest-cov
- Use ReST docstring format for functions (default in PyCharm).

