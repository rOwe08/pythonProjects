import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

directory_grid = 'D:\\School\\Gitlab\AI4Games\\super-mario-astar\\results\\astarGrid'
directory_window = 'D:\\School\\Gitlab\AI4Games\\super-mario-astar\\results\\astarWindow'


def create_data(directory, r):
    all_data = []
    total_files = len([filename for filename in os.listdir(directory) if filename.endswith('.csv')])
    processed_files = 0

    for filename in os.listdir(directory):
        if filename.endswith('.csv'):
            filepath = os.path.join(directory, filename)
            # Check if the file is empty
            if os.path.getsize(filepath) > 0:
                with open(filepath, 'r') as file:
                    metadata = {}
                    for i in range(r):
                        line = file.readline()
                        if ':' in line:
                            key, value = line.strip().split(':')
                            metadata[key.strip()] = float(value.strip())

                    df = pd.read_csv(file)
                    for key, value in metadata.items():
                        df[key] = value
                    all_data.append(df)
            processed_files += 1
            # Print the progress after processing each file
            print(
                f"Processed {processed_files} out of {total_files} files ({(processed_files / total_files) * 100:.2f}%)")

    combined_data_temp = pd.concat(all_data)
    return combined_data_temp


combined_data = create_data(directory_grid, 7)

combined_data['win_rate'] = combined_data['win/fail'].map({'true': 1, 'false': 0})

if 'SEARCH_STEPS' in combined_data.columns:
    average_win_rate = combined_data.pivot_table(index='SEARCH_STEPS', columns='TTFW', values='win/fail')
    average_run_time = combined_data.pivot_table(index='SEARCH_STEPS', columns='TTFW', values='run time',
                                                 aggfunc='mean')
    print(average_win_rate)
    print(average_run_time)
else:
    raise ValueError("Column 'SEARCH_STEPS' doesnt exist")

if not average_win_rate.empty:
    plt.figure(figsize=(12, 9))
    sns.heatmap(average_win_rate, annot=True, fmt=".2f", cmap="viridis")
    plt.title("Average Win Rate Dependence on searchSteps and TTFW")
    plt.xlabel("Time To Finish Weight")
    plt.ylabel("Search Steps")
    plt.show()

else:
    print("No data for creating heatmap avg win")

if not average_run_time.empty:

    plt.figure(figsize=(12, 9))
    sns.heatmap(average_run_time, annot=True, fmt=".2f", cmap="magma")
    plt.title("Average Run Time Dependence on searchSteps and TTFW")
    plt.xlabel("Time To Finish Weight")
    plt.ylabel("Search Steps")
    plt.show()
else:
    print("No data for creating heatmap avg time")

##################################################################################################

combined_data = create_data(directory_window, 6)

combined_data['win_rate'] = combined_data['win/fail'].map({'true': 1, 'false': 0})

if 'RIGHT_WINDOW_BORDER_X' in combined_data.columns:
    average_win_rate = combined_data.pivot_table(index='RIGHT_WINDOW_BORDER_X', columns='TTFW', values='win/fail')
    average_run_time = combined_data.pivot_table(index='RIGHT_WINDOW_BORDER_X', columns='TTFW', values='run time')

    print(average_win_rate)  # Check the contents of the pivot table
    print(average_run_time)
else:
    raise ValueError("Column 'RIGHT_WINDOW_BORDER_X' doesnt exist")

if not average_win_rate.empty:
    plt.figure(figsize=(12, 9))
    sns.heatmap(average_win_rate, annot=True, fmt=".2f", cmap="viridis")
    plt.title("Average Win Rate Dependence on RIGHT_WINDOW_BORDER_X and TTFW")
    plt.xlabel("Time To Finish Weight")
    plt.ylabel("RIGHT_WINDOW_BORDER_X")
    plt.show()

else:
    print("No data for creating heatmap avg win")

if not average_run_time.empty:
    plt.figure(figsize=(12, 9))
    sns.heatmap(average_run_time, annot=True, fmt=".2f", cmap="magma")
    plt.title("Average Run Time Dependence on RIGHT_WINDOW_BORDER_X and TTFW")
    plt.xlabel("Time To Finish Weight")
    plt.ylabel("RIGHT_WINDOW_BORDER_X")
    plt.show()
else:
    print("No data for creating heatmap avg time")
