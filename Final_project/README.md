# Exam — Data Science I (Summer Term 2025)

This README summarizes `exam.ipynb` (Exam I, Summer Term 2025). It explains the high-level purpose and objectives in a detailed paragraph, lists required files and dependencies, and provides a concise per-question explanation of what is done and why. Use this as a quick reference while working through the notebook and as a checklist before submission.

## Purpose and Objectives

This exam notebook is designed to assess practical data-science skills across the full analysis pipeline: data ingestion and preprocessing, exploratory visualization and time-series analysis, statistical inference, anomaly detection, and unsupervised user segmentation. The exam emphasises reproducible, well-documented code and critical interpretation: you must justify choices (plots, tests, model parameters) and interpret findings in context. Practically, the tasks simulate working with large, noisy, real-world social-media-derived datasets and require combining domain-aware feature engineering (temporal posting behavior, interaction ratios), robust time-series decomposition to uncover trends and periodicities, non-parametric hypothesis testing when assumptions fail, and both rule-based and model-driven anomaly detection. The objectives are threefold: (1) demonstrate competence in transforming raw, time-indexed social-data into aggregated, analysis-ready tables and meaningful per-user features; (2) use visualization and signal-processing tools to discover and explain temporal patterns (seasonality, weekly effects); and (3) apply statistical tests and unsupervised algorithms (Isolation Forest and clustering) to identify anomalous users and discover coherent user segments, while providing interpretable summaries and evaluation of results. Throughout, the exam tests reproducibility (saving intermediate artifacts), critical thinking (choice and justification of methods), and communication (clear comments and written interpretation of results).

## Required files (provided with the exam)

- `author_interaction_stats.csv.gz` — aggregated per-author incoming interaction counts
- `user_interaction_stats.csv.gz` — aggregated per-user outgoing interaction counts
- `user_post_stats_per_day.csv.gz` — per-user, per-day posting activity with sentiment
- The notebook expects these files and writes intermediate CSVs to resume work if needed.

## Environment / Dependencies

The notebook suggests using the provided Docker image or the GWDG Jupyter Cloud. Required Python packages (minimum):

- numpy
- pandas
- scipy
- scikit-learn
- matplotlib
- seaborn
- statsmodels
- umap-learn (optional, used in notebook)
- plotly (optional for interactive plots)

Install with pip if needed:

pip install numpy pandas scipy scikit-learn matplotlib seaborn statsmodels umap-learn plotly

Note: The exam includes a Dockerfile and docker-compose setup — use those for a reproducible environment when possible.

## Quick run checklist

1. Ensure the three gzipped CSVs are in the working directory or update the file paths in the notebook cells.
2. Run the notebook top-to-bottom. The preprocessing steps create intermediate files so you can re-load them later if the kernel restarts.
3. Save final artifacts (`user_stat.csv`, figures) and include the signed code of conduct PDF in your submission zip.

## Per-task concise explanations

### Task 0 — Setup
- Describes the Docker environment and cloud options. Instruction: use the provided Dockerfile or GWDG Jupyter Cloud for reproducibility. Install additional packages inside the notebook if you deviate from the provided environment.

### Task 1: Data Preprocessing (18 points)

Task 1.1 — Data Loading (2 points)
- Load the three provided datasets into pandas DataFrames and convert `date` in `user_post_stats_per_day` to datetime. This creates the working tables used in later tasks.

Task 1.2 — Aggregation (11 points)
- Aggregate per-day statistics: compute total posts per day, average user sentiment per day, and average sentiment per post (a weighted mean using `post_count` as weights). Index the resulting DataFrame by `date` (as a datetime index). Also construct user-level statistics by grouping `user_post_stats_per_day` by `user_id` to compute features: total posts, average sentiment (weighted), sentiment std, average posts/day, active days, first/last post dates. Compute temporal posting statistics (mean, median, std, CV of days between posts) by computing differences between sorted unique post dates per user.
- Purpose: produce per-day and per-user feature tables for visualization and downstream modeling.

Task 1.3 — Merging (4 points)
- Merge `user_stats` with `user_interaction_stats` (left join) and then `author_interaction_stats` (left join, suffix `_by_others` for incoming interactions). The result consolidates per-user behavior (activity & temporal features) with outgoing and incoming engagement metrics.
- Replace missing counts in interaction columns with 0 (fill NaNs).

Task 1.4 — Save Dataframes (2 points)
- Save the computed `final_merge` / `user_stats` to CSV and include a second cell to reload them. This ensures long computations need not be repeated and supports reproducibility when re-opening the notebook.

### Task 2: Plotting (24 points)

Task 2.1 — Posts per day (2 points)
- Plot total posts per day (time series). This is the starting EDA plot that motivates spectral analysis and STL decomposition.

Task 2.2 — "Weekend whispers": frequency analysis and STL decomposition (14 points)
- Task 2.2.1 Frequency spectrum (6 points): Compute the periodogram of the posts-per-day series to find dominant periodicities (convert frequency to period in days, show periods ≤ 10 days). Highlight the main peak (e.g., weekly pattern). This identifies likely seasonality for STL.
- Task 2.2.2 STL decomposition (5 points): Use `statsmodels.tsa.seasonal.STL` with the chosen period (e.g., 7 days) and `robust=True` to extract trend, seasonal, and residual components. Plot each component to interpret trends and detect anomalies or bursts (e.g., increased activity in February 2024).
- Task 2.2.3 Weekday effect (3 points): Aggregate the seasonal component by weekday and plot the average seasonal effect per weekday as a bar plot to identify which weekdays are more or less active.

Task 2.3 — Sentiment Data (2 points)
- Plot average user sentiment vs average post sentiment over time and compute the Pearson correlation between the two series. This checks whether user-level and post-level sentiment track each other.

Task 2.4 — "Monday Blues?" (4 points)
- Task 2.4.1 Seasonal decomposition for sentiment: Apply STL (period=7) to both user sentiment and post sentiment, plot trend/seasonal/residual components for each.
- Task 2.4.2 Weekday effect: Compute average user sentiment per weekday and plot as a bar chart to identify weekday patterns in sentiment.

Task 2.5 — Highly active users (2 points)
- Plot the distribution of average posts per day across users. Provide both raw and log-transformed histograms to reveal skew and heavy tail behavior (super-active users / possible bots).

### Task 3: Statistics (17 points)

Task 3.1 — Weekday effects on posting behaviour (6 points)
- Fit a linear model regressing the seasonal component on weekday dummy variables (no intercept to avoid dummy trap) to quantify weekday effects on posting activity. Report model statistics and coefficients. Perform multiple-comparison correction (Bonferroni / other) on p-values and interpret which weekdays are significantly different at α=0.05.

Task 3.2 — Weekday effects on sentiment (4 points)
- Repeat the regression procedure for sentiment seasonal components. Test and correct p-values for multiple comparisons and compare whether weekday effects are stronger on posting counts or sentiment.

Task 3.3 — Bot-like behavior & group tests (7 points)
- Define a rule-based `is_bot` label using two conditions: `total_post > 1000` and `cv_days_between_posts < 0.5`. Remove rows with missing temporal features. Compare distributions of `avg_sentiment` and `sentiment_std` between bots and non-bots using appropriate visualizations (boxplots, KDEs). Since distributions are skewed and variances unequal, the notebook uses the non-parametric Mann–Whitney U test; report U-statistics and p-values and state significance.

### Task 4: Machine Learning (40 points)

Task 4.1 — Unsupervised anomaly detection with Isolation Forest (15 points)
- Task 4.1.1 Feature inspection (1 point): select numerical features describing user behavior and engagement to feed the model.
- Task 4.1.3 IsolationForest (4 points): Fit an Isolation Forest using `contamination` matched to the rule-based `is_bot` prevalence and a fixed `random_state`. Generate anomaly labels (`is_bot_forest`).
- Task 4.1.4 Feature importance (5 points): Train a small DecisionTree surrogate on the IsolationForest labels to approximate which features influence anomaly detection. Evaluate surrogate accuracy/confusion matrix and inspect tree rules for interpretability.
- Task 4.1.5 Anomaly vs rule-based classification (3 points): Cross-tabulate rule-based vs IsolationForest labels and discuss agreement and discrepancies.
- Task 4.1.6 Statistical test (2 points): Test whether anomalies differ from normals in `sentiment_mean` and `sentiment_std` using Mann–Whitney U tests and visualize distributions.

Task 4.2 — User Segmentation Analysis (25 points)
- Task 4.2.1 Data preparation (3 points): Re-run IsolationForest with `contamination='auto'`, report counts, and restrict clustering to non-anomalous users.
- Task 4.2.2 Feature engineering (5 points): Create `total_interactions`, interaction ratios (`reply_ratio`, `repost_ratio`, `quote_ratio`), and log-transform counts; these features reduce skew and capture relative behavior.
- Task 4.2.3 Optimal cluster selection (8 points): Sample up to 100k users, standardize features, run KMeans for k=2..8, compute silhouette and inertia scores, and select optimal k based on the trade-off between cohesion and separation.
- Task 4.2.4 Clustering and visualization (5 points): Fit KMeans with chosen k and visualize clusters via PCA projection and t-SNE (or UMAP) to inspect separation.
- Task 4.2.5 Cluster interpretation (4 points): Summarize cluster means, proportions, and assign interpretable labels (e.g., "Reply-oriented", "Superactive", "Silent"). Provide actionable insights for product teams.

---
