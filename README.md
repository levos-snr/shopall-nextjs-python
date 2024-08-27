# NextJS + Tailwind CSS + TypeScript + Python +SQLAlchemy + PostgreSQL + Vercel

#  🚀 Getting Started

## What is Full Stack Web Development? 
- Full Stack Web Development represents a holistic approach
  to web application development, where an individual or a 
  team is responsible for both the front-end (client-side) and
  back-end (server-side) development.
  This involves creating the visual components that users 
  interact with (the front-end), and also managing data, 
  server logic, and more behind the scenes (the back-end).


## Exploring the Layers in Full Stack Web Development
- Full Stack Web Development essentially comprises three 
  distinct layers:
1. The presentation layer: This is the front-end of the 
  application, which is built using tools such as HTML, 
  CSS, JavaScript and various JavaScript libraries or frameworks 
  like ReactJS. One recent and innovative framework is NextJS, 
  which is a React-based framework known for features such as 
  server-side rendering and generating static websites.
2. The business logic layer: This is the back-end portion 
  of the application. It’s here that all the logical 
  operations, data manipulation, and server-side tasks 
  are carried out. This is where the use of Python 
  becomes important. A powerful and versatile language,
  Python is used extensively in back-end development for
  its simplicity and vast capabilities.
3. The database layer: This is the very core of any web 
  application. It’s the layer where data is stored, 
  retrieved, and manipulated. Python is again a common
  tool used to interact with databases, thanks to the 
  diverse range of libraries it offers for database operations. 

## Combining NextJS and Python in Full Stack Web Development
- Many developers are finding a potent combination in using 
  NextJS with a Python backend for their full stack web 
  development needs. This is often referred to as a “NextJS 
  Python backend”. This approach allows you to harness the 
  dynamic capabilities of the NextJS front-end framework, 
  while benefiting from Python’s easy-to-read syntax and
  powerful back-end processing abilities.
  
## Benefits of Full Stack Web Development
- One-stop Solution
- Efficiency and Coordination
- Wide Array of Tools and Libraries
- Cost-Effective

# Setting up the development environment

## 📝 Prerequisites

-   [Git](https://git-scm.com/)
-   [Node.js](https://nodejs.org/en/download/)
-   [Yarn](https://yarnpkg.com/)
-   [Python](https://www.python.org/downloads/)
-   [PostgreSQL](https://www.postgresql.org/download/)
-   [Bun](https://bun.sh/)

## 🔧 Installation

1. Clone the repository
   ```sh
   git clone https://github.com/levos-snr/shopall-nextjs-python.git
   ```
2. Install dependencies
   ```sh
   yarn install
   npm install
   bun install
   ```
3. Create `.env.local` file
   ```sh
   cp .env.local.example .env.local
   ```
4. Create a `.env` file
   ```sh
   cp .env.example .env
   ```
5. Installing Python and virtual environment
  ```sh
  python -m venv venv
  source venv/bin/activate
  pip install -r requirements.txt
  ```
  
## Creating a new NextJS project

  ```sh
  npx create-next-app your-project-name
  cd your-project-name
  bun run dev or npm run dev or yarn dev
  ```
