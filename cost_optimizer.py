import math

# --- AWS EC2 Cost Optimization Simulation ---
# This script simulates monthly costs for a backend service running on EC2
# and demonstrates potential savings through simple optimization strategies.

# Hypothetical hourly costs for different EC2 instance types (e.g., us-east-1, On-Demand)
# These values are illustrative and should be replaced with actual costs for real scenarios.
INSTANCE_HOURLY_COSTS = {
    "t3.medium": 0.0416,  # Example: 2 vCPU, 4 GiB RAM
    "t3.small": 0.0208,   # Example: 2 vCPU, 2 GiB RAM
    "t3.micro": 0.0104,   # Example: 2 vCPU, 1 GiB RAM
}

HOURS_IN_MONTH = 24 * 30.44  # Average hours in a month

def calculate_monthly_cost(instance_type: str, hours_per_day: float) -> float:
    """
    Calculates the estimated monthly cost for a given instance type
    and average daily operational hours.
    """
    if instance_type not in INSTANCE_HOURLY_COSTS:
        raise ValueError(f"Unknown instance type: {instance_type}")

    hourly_rate = INSTANCE_HOURLY_COSTS[instance_type]
    # Calculate total hours used based on daily usage over the month
    total_hours_used = hours_per_day * (HOURS_IN_MONTH / 24)
    
    # Ensure total_hours_used does not exceed max hours in a month
    total_hours_used = min(total_hours_used, HOURS_IN_MONTH)

    return hourly_rate * total_hours_used

def main():
    print("--- AWS EC2 Backend Service Cost Optimization Simulation ---")
    print(f"Average hours in a month: {HOURS_IN_MONTH:.2f}\n")

    # Scenario 1: Default (Potentially Over-provisioned) Setup
    # A common scenario where a service runs 24/7 on a moderately sized instance.
    default_instance_type = "t3.medium"
    default_hours_per_day = 24.0 # Runs continuously
    default_cost = calculate_monthly_cost(default_instance_type, default_hours_per_day)
    print(f"Scenario 1: Default Setup ({default_instance_type}, {default_hours_per_day} hrs/day)")
    print(f"  Estimated Monthly Cost: ${default_cost:.2f}\n")

    # Scenario 2: Optimized Setup - Right-sizing
    # If analysis shows the service doesn't need t3.medium constantly,
    # it could be downsized to a smaller instance (e.g., t3.small).
    optimized_instance_type_1 = "t3.small"
    optimized_hours_per_day_1 = 24.0 # Still runs continuously
    optimized_cost_1 = calculate_monthly_cost(optimized_instance_type_1, optimized_hours_per_day_1)
    savings_1 = default_cost - optimized_cost_1
    print(f"Scenario 2: Optimized - Right-sizing ({optimized_instance_type_1}, {optimized_hours_per_day_1} hrs/day)")
    print(f"  Estimated Monthly Cost: ${optimized_cost_1:.2f}")
    # This demonstrates savings by selecting a smaller instance type that still meets performance needs.
    print(f"  Potential Savings vs. Default (Right-sizing): ${savings_1:.2f}\n")

    # Scenario 3: Optimized Setup - Scheduling/Shutdown
    # If the service is only critical during business hours (e.g., 12 hours/day)
    # and can be shut down or scaled down significantly off-hours.
    optimized_instance_type_2 = "t3.small" # Using the smaller instance from Scenario 2
    optimized_hours_per_day_2 = 12.0 # Runs only 12 hours a day
    optimized_cost_2 = calculate_monthly_cost(optimized_instance_type_2, optimized_hours_per_day_2)
    savings_2 = default_cost - optimized_cost_2
    print(f"Scenario 3: Optimized - Scheduling/Shutdown ({optimized_instance_type_2}, {optimized_hours_per_day_2} hrs/day)")
    print(f"  Estimated Monthly Cost: ${optimized_cost_2:.2f}")
    # This demonstrates savings by stopping or scaling down resources when not actively needed.
    print(f"  Potential Savings vs. Default (Right-sizing + Scheduling): ${savings_2:.2f}\n")

    # Scenario 4: More aggressive optimization - using micro instance for limited hours
    # Combining both right-sizing to the smallest viable instance and aggressive scheduling.
    optimized_instance_type_3 = "t3.micro"
    optimized_hours_per_day_3 = 8.0 # Runs only 8 hours a day
    optimized_cost_3 = calculate_monthly_cost(optimized_instance_type_3, optimized_hours_per_day_3)
    savings_3 = default_cost - optimized_cost_3
    print(f"Scenario 4: Optimized - Aggressive Scheduling ({optimized_instance_type_3}, {optimized_hours_per_day_3} hrs/day)")
    print(f"  Estimated Monthly Cost: ${optimized_cost_3:.2f}")
    print(f"  Potential Savings vs. Default (Aggressive Optimization): ${savings_3:.2f}\n")


    print("--- Key Takeaways for Cost Optimization ---")
    print("1. Right-sizing: Choose the smallest instance type that meets your performance needs.")
    print("2. Scheduling: Shut down or scale down instances when not in use (e.g., off-peak hours, weekends).")
    print("3. Monitor usage: Regularly review resource utilization to identify over-provisioned resources.")

if __name__ == "__main__":
    main()
