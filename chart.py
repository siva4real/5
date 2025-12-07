import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Generate realistic synthetic data for customer support response times
# Simulating different support channels with varying response time distributions

# Email Support: Moderate response times with high variability
email_times = np.random.gamma(shape=3, scale=4, size=200)

# Live Chat: Faster response times with moderate variability
chat_times = np.random.gamma(shape=1.5, scale=2, size=250)

# Phone Support: Fast response times with lower variability
phone_times = np.random.gamma(shape=2, scale=1.5, size=180)

# Social Media: Variable response times with high peaks
social_times = np.random.gamma(shape=2.5, scale=3.5, size=150)

# Create DataFrame
data = pd.DataFrame({
    'Response Time (hours)': np.concatenate([email_times, chat_times, phone_times, social_times]),
    'Support Channel': (['Email'] * len(email_times) + 
                        ['Live Chat'] * len(chat_times) + 
                        ['Phone'] * len(phone_times) + 
                        ['Social Media'] * len(social_times))
})

# Set Seaborn style and context for professional appearance
sns.set_style("whitegrid")
sns.set_context("talk", font_scale=0.9)

# Create figure with specified dimensions for 512x512 output
plt.figure(figsize=(8, 8))

# Create violinplot with professional styling
ax = sns.violinplot(
    data=data,
    x='Support Channel',
    y='Response Time (hours)',
    palette='Set2',
    inner='quartile',
    linewidth=1.5,
    saturation=0.8
)

# Customize the plot
plt.title('Customer Support Response Time Distribution\nAcross Communication Channels', 
          fontsize=14, fontweight='bold', pad=20)
plt.xlabel('Support Channel', fontsize=12, fontweight='bold')
plt.ylabel('Response Time (hours)', fontsize=12, fontweight='bold')

# Rotate x-axis labels for better readability
plt.xticks(rotation=45, ha='right')

# Add grid for better readability
ax.grid(axis='y', alpha=0.3, linestyle='--')
ax.set_axisbelow(True)

# Add subtle background color
ax.set_facecolor('#f8f9fa')

# Adjust layout to prevent label cutoff
plt.tight_layout()

# Save the chart with exact specifications
plt.savefig('chart.png', dpi=64, bbox_inches='tight')
print("Chart successfully generated and saved as 'chart.png'")
print(f"Total samples analyzed: {len(data)}")
print("\nResponse Time Statistics by Channel:")
print(data.groupby('Support Channel')['Response Time (hours)'].describe().round(2))

