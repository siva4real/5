# Customer Support Response Time Analysis

## Project Overview

This project was developed for **Hickle Wolf and Hilpert**, a data-driven customer experience company, to visualize customer support response time distribution across different communication channels for a major retail client.

## Business Context

The visualization provides actionable insights into support efficiency across four key channels:
- **Email Support**: Traditional channel with moderate response times
- **Live Chat**: Real-time digital support with faster response
- **Phone Support**: Direct communication with quick resolution
- **Social Media**: Public-facing support with variable response patterns

## Visualization Details

- **Chart Type**: Violin Plot (Seaborn)
- **Purpose**: Display distribution and density of response times
- **Output**: 512x512 pixel PNG image
- **Statistical Features**: Quartile markers showing median and IQR

## Key Insights

The violinplot effectively communicates:
1. **Distribution Shape**: Visual representation of response time density
2. **Central Tendency**: Median response times per channel
3. **Variability**: Width indicates frequency of specific response times
4. **Outliers**: Identification of unusual response patterns

## Files

- `chart.py` - Python script generating the Seaborn visualization
- `chart.png` - Generated 512x512 pixel chart image
- `README.md` - Project documentation

## Technical Requirements

### Dependencies
```
seaborn
matplotlib
pandas
numpy
```

### Installation
```bash
pip install seaborn matplotlib pandas numpy
```

### Usage
```bash
python chart.py
```

## Contact

**Email**: 24f3004072@ds.study.iitm.ac.in

## Methodology

The analysis uses synthetic data generated with gamma distributions to simulate realistic response time patterns across different support channels. The violin plot combines box plot and kernel density estimation to provide comprehensive distribution visualization suitable for executive presentations and strategic decision-making.

## Professional Standards

This visualization adheres to best practices for business intelligence reporting:
- Clear, publication-ready formatting
- Professional color palette
- Statistical rigor with quartile markers
- Appropriate labeling and titles
- High-quality output resolution

---

*Developed for Hickle Wolf and Hilpert - Data-Driven Customer Experience Analytics*

