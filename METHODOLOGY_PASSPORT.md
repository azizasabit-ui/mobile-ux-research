# Methodology Passport Card

## 1. Project Information

### Project Title

**The Effect of Mobile Application Interface Design on User Experience**

### Authors

- Aziza Sabit
- Les Akerke

### Research Question

**How does mobile application interface design affect task completion performance and user experience?**

### GitHub Repository

https://github.com/azizasabit-ui/mobile-ux-research

---

## 2. Research Type

### Research Approach

**Quantitative Research**

### Justification

This study uses a quantitative research approach because it evaluates user experience through measurable numerical indicators.

The study compares a baseline mobile application interface with an improved interface using task completion time, task success rate, error rate, and user satisfaction score.

The quantitative approach allows the researchers to compare the two interface versions using numerical data and statistical analysis.

---

## 3. Hypotheses

### Null Hypothesis (H0)

There is no statistically significant difference in task completion time between the baseline and improved mobile application interfaces.

### Alternative Hypothesis (H1)

The improved mobile application interface significantly reduces task completion time compared with the baseline interface.

---

## 4. Variables Matrix

| Variable Type | Variable | Description |
|---|---|---|
| Independent | Interface Design Version | Baseline or improved interface |
| Dependent | Task Completion Time | Time required to complete the predefined task, measured in seconds |
| Dependent | Task Success Rate | Percentage of successfully completed tasks |
| Dependent | Error Rate | Percentage of user errors during task completion |
| Dependent | Satisfaction Score | User satisfaction measured on a 1–5 scale |
| Controlled | Device | Same device type for all participants |
| Controlled | Operating System | Same operating system version |
| Controlled | Task | Same predefined task and instructions |
| Controlled | Dataset | Same input data |
| Controlled | Network | Same network conditions |

---

## 5. Metrics and Baseline

### Primary Metric

**Task Completion Time (seconds)**

The primary metric measures the amount of time required by a participant to complete the predefined task.

Lower task completion time indicates better task efficiency.

### Guardrail Metrics

| Guardrail Metric | Target |
|---|---|
| Task Success Rate | ≥ 90% |
| Error Rate | ≤ 10% |
| Critical UI Errors | 0 |
| Satisfaction Score | Should not decrease |

### Baseline / Control Condition

The baseline condition is the original mobile application interface without the proposed UX improvements.

The improved interface will be compared against this baseline under the same task and controlled conditions.

---

## 6. Experimental Comparison

| Condition | Description |
|---|---|
| Baseline | Original mobile application interface |
| Improved | Interface with proposed UX improvements |

Participants will perform the same predefined task using both interface conditions.

The collected measurements will be used to compare task performance and user experience.

---

## 7. Benchmark Plan

| Metric | Baseline | Improved | Direction |
|---|---:|---:|---|
| Task Completion Time | TBD | TBD | Lower is better |
| Task Success Rate | TBD | TBD | Higher is better |
| Error Rate | TBD | TBD | Lower is better |
| Satisfaction Score | TBD | TBD | Higher is better |

The current repository contains only a small sample dataset for testing the benchmark pipeline. It does not represent final research results.

---

## 8. Reproducibility

The research repository provides a Docker-based execution environment.

The benchmark can be reproduced using:

```bash
docker build -t mobile-ux-benchmark .
docker run --rm mobile-ux-benchmark