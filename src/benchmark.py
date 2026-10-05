import pandas as pd
import yaml


def main():
    with open("config.yaml", "r") as file:
        config = yaml.safe_load(file)

    data_path = config["data"]["sample_path"]

    df = pd.read_csv(data_path)

    summary = (
        df.groupby("interface")
        .agg(
            avg_task_time=("task_time_seconds", "mean"),
            task_success_rate=("task_success", "mean"),
            avg_errors=("error_count", "mean"),
            avg_satisfaction=("satisfaction", "mean"),
        )
        .reset_index()
    )

    print("\n=== Mobile UX Benchmark ===")
    print(summary.to_string(index=False))

    print("\nPrimary metric:")
    print("Average task completion time")

    print("\nGuardrail metrics:")
    print("Task success rate >= 90%")
    print("Error rate <= 10%")


if __name__ == "__main__":
    main()