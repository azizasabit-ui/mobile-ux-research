# The Effect of Mobile Application Interface Design on User Experience

## Authors

- Aziza Sabit
- Les Akerke

## Research Question

How does mobile application interface design affect task completion performance and user experience?

## Research Type

This study uses a quantitative research approach.

The study measures numerical indicators of user experience, including task completion time, task success rate, error rate, and user satisfaction. The quantitative approach allows us to compare the baseline interface with an improved interface using measurable performance indicators.

## Hypotheses

### Null Hypothesis (H0)

There is no statistically significant difference in task completion time between the baseline and improved mobile application interfaces.

### Alternative Hypothesis (H1)

The improved mobile application interface significantly reduces task completion time compared with the baseline interface.

## Variables

| Variable Type | Variable | Description |
|---|---|---|
| Independent | Interface Design Version | Baseline or improved interface |
| Dependent | Task Completion Time | Time required to complete the predefined task |
| Dependent | Task Success Rate | Percentage of successfully completed tasks |
| Dependent | Error Rate | Number of user errors during task completion |
| Dependent | Satisfaction Score | User satisfaction measured on a 1–5 scale |
| Controlled | Device | Same device type for all participants |
| Controlled | Operating System | Same OS version |
| Controlled | Task | Same predefined task and instructions |
| Controlled | Dataset | Same input data |
| Controlled | Network | Same network conditions |

## Metrics

### Primary Metric

**Task Completion Time (seconds)**

The primary metric measures how long users need to complete the predefined task.

### Guardrail Metrics

- Task Success Rate ≥ 90%
- Error Rate ≤ 10%
- Critical UI Errors = 0
- Satisfaction Score should not decrease

## Baseline

The baseline is the original mobile application interface without the proposed UX improvements.

The improved interface is compared against this baseline.

## Planned Benchmark

| Interface | Task Completion Time | Task Success Rate | Error Rate | Satisfaction |
|---|---:|---:|---:|---:|
| Baseline | TBD | TBD | TBD | TBD |
| Improved | TBD | TBD | TBD | TBD |

The values will be collected during the user study. The current sample dataset is provided only to verify the benchmark pipeline.

## Repository Structure

```text
mobile-ux-research/
├── README.md
├── .gitignore
├── Dockerfile
├── requirements.txt
├── config.yaml
├── LICENSE
├── data/
│   └── sample/
│       └── sample_data.csv
├── src/
│   └── benchmark.py
├── notebooks/
├── configs/
└── results/

## Quickstart

### 1. Build the Docker image

docker build -t mobile-ux-benchmark .

### 2. Run the benchmark

docker run --rm mobile-ux-benchmark