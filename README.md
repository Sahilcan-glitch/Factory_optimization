# Factory Production Optimization

![Factory Optimization](https://img.shields.io/badge/Streamlit-App-FF4B4B?logo=streamlit&logoColor=white)

## 📚 University Project: Reasoning and Decision Making Under Uncertainty

This project is a comprehensive study undertaken as part of the **Reasoning and Decision Making Under Uncertainty** course at [Your University Name]. The primary objective is to optimize factory machinery operations to **maximize production** while **minimizing harmful emissions**. Leveraging the power of **Linear Programming** through the **PuLP** library, this project addresses real-world constraints faced by manufacturing units aiming for both efficiency and sustainability.

---

## 🛠️ Project Overview

In the competitive manufacturing landscape, balancing production efficiency with environmental responsibility is crucial. This project focuses on:

- **Optimizing Operating Hours:** Determining the optimal running hours for different production lines to achieve desired production targets.
- **Emissions Management:** Ensuring that the factory operations stay within the specified emission limits to promote environmental sustainability.
- **Decision Making Under Uncertainty:** Utilizing linear programming to make informed decisions despite uncertain variables and constraints.

---

## 🔧 Technologies Used

- **Python:** The core programming language used for implementing the optimization model.
- **PuLP:** An open-source linear programming library in Python used to formulate and solve the optimization problem.
- **Streamlit:** A powerful library for creating interactive web applications, enabling users to input parameters and visualize optimization results in real-time.

---

## 🚀 Live Demo

Experience the Factory Production Optimization tool live! Input your factory's emission limits and running hours to determine the optimal operating schedule for maximum production efficiency.

🔗 **Access the App Here:** [https://factoryoptimization.streamlit.app/](https://factoryoptimization.streamlit.app/)

---

## 📈 Features

- **Interactive Input:** Users can easily input their factory's maximum allowable emissions and running hours per week.
- **Optimal Scheduling:** The app calculates the optimal operating hours for different production lines to maximize production while adhering to emission constraints.
- **Constraint Verification:** Ensures that the computed schedules do not exceed the specified running hours and emissions limits.
- **User-Friendly Interface:** Designed with Streamlit for a seamless and intuitive user experience.
- **Real-Time Results:** Immediate feedback and results upon adjusting input parameters.

---

## 📝 How It Works

1. **Input Parameters:**
   - **Maximum Allowable Weekly Emissions (units):** Enter the upper limit for emissions your factory can produce weekly.
   - **Maximum Total Running Hours per Week:** Specify the total hours your production lines can operate each week.

2. **Optimization Process:**
   - The app utilizes the PuLP library to solve the linear programming problem, determining the optimal running hours for each production line to maximize output without exceeding emission and running hour constraints.

3. **View Results:**
   - Upon clicking the "Optimize Production" button, the app displays the optimal operating hours for each production line, the total production achieved, and verifies that all constraints are satisfied.

---

## 📂 Project Structure

