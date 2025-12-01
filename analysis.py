import matplotlib.pyplot as plt
import numpy as np

# Store quarterly MRR growth data
quarters = ['Q1', 'Q2', 'Q3', 'Q4']
mrr_growth = [8.11, 3.15, 6.31, 9.42]

# Calculate average
avg_mrr = sum(mrr_growth) / len(mrr_growth)

# Print key insights
print("=" * 50)
print("QUARTERLY MRR GROWTH ANALYSIS")
print("=" * 50)
print(f"\nQuarterly MRR Growth Rates:")
for q, rate in zip(quarters, mrr_growth):
    print(f"  {q}: {rate}%")

print(f"\nAverage MRR Growth: {avg_mrr}%")
print(f"Industry Target: 15%")
print(f"Gap to Target: {15 - avg_mrr:.2f}%")

print("\nKey Insights:")
print(f"  • Best performing quarter: {quarters[mrr_growth.index(max(mrr_growth))]} ({max(mrr_growth)}%)")
print(f"  • Weakest quarter: {quarters[mrr_growth.index(min(mrr_growth))]} ({min(mrr_growth)}%)")
print(f"  • Performance vs target: {(avg_mrr/15)*100:.1f}% of industry benchmark")
print(f"  • Volatility: {max(mrr_growth) - min(mrr_growth):.2f}% range")

# Plot 1: Line chart of quarterly MRR
plt.figure(figsize=(10, 6))
plt.plot(quarters, mrr_growth, marker='o', linewidth=2, markersize=10, color='#2E86AB')
plt.axhline(y=avg_mrr, color='#A23B72', linestyle='--', linewidth=2, label=f'Average: {avg_mrr}%')
plt.axhline(y=15, color='#F18F01', linestyle='--', linewidth=2, label='Industry Target: 15%')
plt.title('Quarterly MRR Growth Rate', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Quarter', fontsize=12, fontweight='bold')
plt.ylabel('MRR Growth (%)', fontsize=12, fontweight='bold')
plt.grid(True, alpha=0.3, linestyle='--')
plt.legend(fontsize=10)
plt.ylim(0, max(mrr_growth) + 3)

# Add value labels on points
for i, (q, v) in enumerate(zip(quarters, mrr_growth)):
    plt.text(i, v + 0.5, f'{v}%', ha='center', va='bottom', fontweight='bold')

plt.tight_layout()
plt.savefig('mrr_quarterly_line_chart.png', dpi=300, bbox_inches='tight')
print("\n✓ Saved: mrr_quarterly_line_chart.png")
plt.close()

# Plot 2: Bar chart comparing average MRR vs industry target
plt.figure(figsize=(8, 6))
categories = ['Average MRR\nGrowth', 'Industry\nTarget']
values = [avg_mrr, 15]
colors = ['#2E86AB', '#F18F01']

bars = plt.bar(categories, values, color=colors, alpha=0.8, edgecolor='black', linewidth=1.5)

plt.title('MRR Growth: Actual vs. Industry Target', fontsize=16, fontweight='bold', pad=20)
plt.ylabel('Growth Rate (%)', fontsize=12, fontweight='bold')
plt.ylim(0, max(values) + 3)
plt.grid(axis='y', alpha=0.3, linestyle='--')

# Add value labels on bars
for bar, val in zip(bars, values):
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height + 0.3,
             f'{val}%', ha='center', va='bottom', fontweight='bold', fontsize=12)

# Add gap annotation
plt.annotate('', xy=(0.5, avg_mrr), xytext=(0.5, 15),
             arrowprops=dict(arrowstyle='<->', color='red', lw=2))
plt.text(0.5, (avg_mrr + 15)/2, f'Gap: {15-avg_mrr:.2f}%',
         ha='center', va='center', fontsize=10, fontweight='bold',
         bbox=dict(boxstyle='round', facecolor='white', edgecolor='red', linewidth=2))

plt.tight_layout()
plt.savefig('mrr_comparison_bar_chart.png', dpi=300, bbox_inches='tight')
print("✓ Saved: mrr_comparison_bar_chart.png")
plt.close()

print("\n" + "=" * 50)
print("Analysis complete! Charts saved successfully.")
print("=" * 50)
