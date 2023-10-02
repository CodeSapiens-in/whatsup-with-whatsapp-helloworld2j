import re
from datetime import datetime
from collections import defaultdict
import matplotlib.pyplot as plt

# Read data from the file
data = []
with open("_chat.txt", 'r', encoding='utf-8') as fp:
    data = fp.readlines()

message_count_by_hour = defaultdict(int)

# Extract timestamps and count messages by hour
for line in data:
    match = re.search(r'\[(.*?)\]', line)
    if match:
        timestamp_str = match.group(1)
        try:
            timestamp = datetime.strptime(timestamp_str, "%d/%m/%y, %I:%M:%S %p")
            hour = timestamp.hour
            if "joined" not in line:  # Exclude join messages
                message_count_by_hour[hour] += 1
        except ValueError:
            # Handle lines with invalid timestamps (skip them)
            continue

# Sort the data by hour
sorted_message_counts = sorted(message_count_by_hour.items())

# Extract hours and message counts for plotting
hours, message_counts = zip(*sorted_message_counts)

# Create a bar chart to show message counts by hour
plt.figure(figsize=(12, 6))
plt.bar(hours, message_counts, color='b', alpha=0.7)
plt.xlabel('Hour of the Day')
plt.ylabel('Number of Messages Sent')
plt.title('Message Activity by Hour')
plt.grid(axis='y')
plt.xticks(range(24))
plt.tight_layout()

# Show the plot
plt.show()