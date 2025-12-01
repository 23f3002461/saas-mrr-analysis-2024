import matplotlib.pyplot as plt

# Quarterly data
quarters = ["Q1", "Q2", "Q3", "Q4"]
mrr_values = [8.11, 3.15, 6.31, 9.42]

# Calculate average
average_mrr = sum(mrr_values) / len(mrr_values)
print("Average MRR Growth (2024):", round(average_mrr, 2))

# Industry target
industry_target = 15

# --- Chart 1: Quarterly Trend ---
plt.figure(figsize=(8,5))
plt.plot(quarters, mrr_values, marker='o', linewidth=2)
plt.title("2024 Quarterly MRR Growth Trend")
plt.xlabel("Quarter")
plt.ylabel("MRR Growth (%)")
plt.grid(True)
plt.savefig("chart_trend.png")
plt.close()

# --- Chart 2: Benchmark Comparison ---
plt.figure(figsize=(6,5))
plt.bar(["Company Avg", "Industry Target"], [average_mrr, industry_target])
plt.title("Average MRR vs Industry Benchmark")
plt.ylabel("MRR Growth (%)")
plt.savefig("chart_benchmark.png")
plt.close()

print("Charts generated: chart_trend.png, chart_benchmark.png")
