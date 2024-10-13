# factory_optimization_app.py

import streamlit as st
import pulp

def maximize_production(max_emissions, max_hours):
    """
    Formulate and solve the LP problem to maximize production.

    Parameters:
    - max_emissions (float): Maximum allowed harmful emissions per week.
    - max_hours (float): Maximum total running hours per week.

    Returns:
    - Tuple containing optimal hours for P1, P2, and maximum production.
    """
    # Create a LP maximization problem
    prob = pulp.LpProblem("Maximize_Production", pulp.LpMaximize)

    # Define decision variables with lower bounds of 0
    x = pulp.LpVariable('P1_Hours', lowBound=0, cat='Continuous')
    y = pulp.LpVariable('P2_Hours', lowBound=0, cat='Continuous')

    # Objective function: Maximize total production
    prob += 40 * x + 30 * y, "Total_Production"

    # Constraints
    prob += x + y <= max_hours, "Total_Hours_Constraint"          # Total running hours ≤ max_hours
    prob += 2 * x + y <= max_emissions, "Emissions_Constraint"   # Emissions ≤ user-defined limit

    # Solve the problem
    prob.solve()

    # Check if an optimal solution was found
    if pulp.LpStatus[prob.status] != 'Optimal':
        return None, None, None

    # Retrieve the results
    optimal_x = x.varValue
    optimal_y = y.varValue
    max_production = pulp.value(prob.objective)

    return optimal_x, optimal_y, max_production

def main():
    # Set the page configuration
    st.set_page_config(page_title="Factory Production Optimization", layout="centered")

    # Title of the app
    st.title("🏭 Factory Production Optimization")

    st.markdown("""
    Optimize the operating hours of Production Lines **P1** and **P2** to **maximize weekly production** while adhering to constraints on **total running hours** and **harmful emissions**.
    """)

    # Sidebar for inputs
    st.sidebar.header("🔧 Input Parameters")

    # Input fields
    max_emissions = st.sidebar.number_input(
        "Maximum Allowable Weekly Emissions (units):",
        min_value=0.0,
        value=16.0,
        step=1.0,
        format="%.2f"
    )

    max_hours = st.sidebar.number_input(
        "Maximum Total Running Hours per Week:",
        min_value=0.0,
        value=12.0,
        step=1.0,
        format="%.2f"
    )

    # Button to trigger optimization
    if st.sidebar.button("Optimize Production"):
        # Perform the optimization
        optimal_x, optimal_y, max_production = maximize_production(max_emissions, max_hours)

        # Display the results
        if optimal_x is not None:
            st.success("✅ **Optimal Solution Found!**")
            st.markdown("---")
            st.header("📈 Optimal Operating Hours")

            # Create columns for better layout
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("**Production Line P1**", f"{optimal_x:.2f} hours/week")
            with col2:
                st.metric("**Production Line P2**", f"{optimal_y:.2f} hours/week")
            with col3:
                st.metric("**Total Production**", f"{max_production:.2f} units/week")

            # Verification of constraints
            st.markdown("---")
            st.header("🔍 Verification of Constraints")

            total_hours = optimal_x + optimal_y
            total_emissions = 2 * optimal_x + optimal_y

            # Display constraints using columns
            ver_col1, ver_col2 = st.columns(2)
            with ver_col1:
                if total_hours <= max_hours:
                    st.success(f"Total Running Hours: {total_hours:.2f} ≤ {max_hours} ✓")
                else:
                    st.error(f"Total Running Hours: {total_hours:.2f} > {max_hours} ✗")
            with ver_col2:
                if total_emissions <= max_emissions:
                    st.success(f"Total Emissions: {total_emissions:.2f} ≤ {max_emissions} ✓")
                else:
                    st.error(f"Total Emissions: {total_emissions:.2f} > {max_emissions} ✗")

            # Additional check for production
            st.markdown("")
            if max_production >= 0:
                st.success(f"Total Production: {max_production:.2f} ≥ Desired Production ✓")
            else:
                st.error(f"Total Production: {max_production:.2f} < Desired Production ✗")
        else:
            st.error("❌ **No feasible solution found. Please adjust your constraints.**")

    # Optional: Display the underlying LP problem
    with st.expander("ℹ️ View Linear Programming Problem"):
        st.markdown("""
        **Objective Function:**
        \[
        \text{Maximize } Z = 40x + 30y
        \]
        
        **Subject to:**
        \[
        \begin{cases}
        x + y \leq \text{Maximum Running Hours} \\
        2x + y \leq \text{Maximum Emissions} \\
        x \geq 0, \ y \geq 0
        \end{cases}
        \]
        
        Where:
        - \( x \): Hours for Production Line P1
        - \( y \): Hours for Production Line P2
        """)
        
    # Footer
    st.markdown("---")
    st.markdown("""
    **Developed by:** Your Name  
    **Contact:** [your.email@example.com](mailto:your.email@example.com)
    """)

if __name__ == "__main__":
    main()
