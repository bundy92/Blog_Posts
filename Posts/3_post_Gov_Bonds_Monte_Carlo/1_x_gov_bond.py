# Import dependencies.
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

class GovernmentBond:
    def __init__(self, face_value: float, coupon_rate: float, maturity_period: int):
        """
        Initialize GovernmentBond object.

        Parameters:
        - face_value: Face value of the bond (float)
        - coupon_rate: Annual coupon rate (float, percentage)
        - maturity_period: Number of periods until maturity (int)
        """
        self.face_value = face_value
        self.coupon_rate = coupon_rate
        self.maturity_period = maturity_period

    def present_value(self, yield_rate: float) -> float:
        """
        Calculate the present value of the bond.

        Parameters:
        - yield_rate: Yield or interest rate (float, percentage)

        Returns:
        - Present value of the bond (float)
        """
        present_value = 0
        for t in range(1, self.maturity_period + 1):
            present_value += self.face_value * self.coupon_rate / 100 / ((1 + yield_rate / 100) ** t)
        present_value += self.face_value / ((1 + yield_rate / 100) ** self.maturity_period)
        return present_value

class MonteCarloBondPricer:
    def __init__(self, bond: GovernmentBond, num_simulations: int):
        """
        Initialize MonteCarloBondPricer object.

        Parameters:
        - bond: GovernmentBond object
        - num_simulations: Number of Monte Carlo simulations (int)
        """
        self.bond = bond
        self.num_simulations = num_simulations

    def simulate_yield_rates(self, mean_yield: float, volatility: float) -> np.ndarray:
        """
        Simulate yield rates using normal distribution.

        Parameters:
        - mean_yield: Mean yield rate (float, percentage)
        - volatility: Volatility of yield rates (float, percentage)

        Returns:
        - Array of simulated yield rates (numpy.ndarray)
        """
        return np.random.normal(mean_yield, volatility, self.num_simulations)

    def price_bond(self, mean_yield: float, volatility: float) -> np.ndarray:
        """
        Price the bond using Monte Carlo simulation.

        Parameters:
        - mean_yield: Mean yield rate (float, percentage)
        - volatility: Volatility of yield rates (float, percentage)

        Returns:
        - Array of bond prices from Monte Carlo simulation (numpy.ndarray)
        """
        simulated_yield_rates = self.simulate_yield_rates(mean_yield, volatility)
        bond_prices = np.zeros(self.num_simulations)
        for i in range(self.num_simulations):
            bond_prices[i] = self.bond.present_value(simulated_yield_rates[i])
        return bond_prices

    def scenario_analysis(self, scenarios: dict) -> dict:
        """
        Perform scenario analysis by varying mean yield and volatility.

        Parameters:
        - scenarios: Dictionary with scenario names as keys and (mean_yield, volatility) tuples as values

        Returns:
        - Dictionary with scenario names as keys and corresponding bond prices as values
        """
        scenario_results = {}
        for scenario_name, (mean_yield, volatility) in scenarios.items():
            bond_prices = self.price_bond(mean_yield, volatility)
            scenario_results[scenario_name] = bond_prices
        return scenario_results

    def sensitivity_analysis(self, parameters: list, values: dict, mean_yield: float, volatility: float) -> dict:
        """
        Perform sensitivity analysis by varying model parameters.

        Parameters:
        - parameters: List of parameter names to vary
        - values: Dictionary mapping parameter names to lists of values to test
        - mean_yield: Mean yield rate (float, percentage)
        - volatility: Volatility of yield rates (float, percentage)

        Returns:
        - Dictionary with parameter names as keys and corresponding bond prices as values
        """
        sensitivity_results = {}
        for param_name in parameters:
            for value in values[param_name]:
                setattr(self.bond, param_name, value)
                bond_prices = self.price_bond(mean_yield, volatility)
                sensitivity_results[param_name] = bond_prices
        return sensitivity_results

# Test.
if __name__ == "__main__":
    face_value = 1000  # Face value of the bond
    coupon_rate = 5  # Annual coupon rate (%)
    maturity_period = 10  # Number of periods until maturity
    num_simulations = 10000  # Number of Monte Carlo simulations
    mean_yield = 5  # Mean yield rate (%)
    volatility = 1  # Volatility of yield rates (%)

    bond = GovernmentBond(face_value, coupon_rate, maturity_period)
    bond_pricer = MonteCarloBondPricer(bond, num_simulations)

    # The Scenario Analysis.
    scenarios = {
        "Base Scenario": (mean_yield, volatility),
        "High Volatility": (mean_yield, volatility + 1),
        "Low Yield": (mean_yield - 1, volatility),
        # Expanable if needed.
    }
    scenario_results = bond_pricer.scenario_analysis(scenarios)

    # The Sensitivity Analysis.
    parameters = ["coupon_rate", "maturity_period"]  # Parameters to vary
    values = {
        "coupon_rate": [4, 5, 6],  # Values to test for coupon rate
        "maturity_period": [5, 10, 15],  # Values to test for maturity period
    }
    sensitivity_results = bond_pricer.sensitivity_analysis(parameters, values, mean_yield, volatility)

    # Plot of the bond price distributions for scenario analysis.
    plt.figure(figsize=(12, 6))
    sns.set_style("whitegrid")
    for scenario_name, prices in scenario_results.items():
        sns.histplot(prices, bins=30, kde=True, label=scenario_name)
    plt.title('Distribution of Bond Prices (Scenario Analysis)')
    plt.xlabel('Bond Price')
    plt.ylabel('Frequency')
    plt.legend()
    plt.show()

    # Plot of the bond price distributions for sensitivity analysis.
    plt.figure(figsize=(12, 6))
    sns.set_style("whitegrid")
    for param_name, prices in sensitivity_results.items():
        sns.histplot(prices, bins=30, kde=True, label=param_name)
    plt.title('Distribution of Bond Prices (Sensitivity Analysis)')
    plt.xlabel('Bond Price')
    plt.ylabel('Frequency')
    plt.legend()
    plt.show()
