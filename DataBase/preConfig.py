pre_config = {'Children':
                  {1: {'Name': 'Battery Capacity', 'Rule': 'Highest Better', 'Value': 'N/A', 'Weight': 5},
                   2: {'Name': 'Year', 'Rule': 'Highest Better', 'Value': 'N/A', 'Weight': 4},
                   3: {'Name': 'Height', 'Rule': 'Optimal Value', 'Value': '145', 'Weight': 3},
                   4: {'Name': 'Width', 'Rule': 'Optimal Value', 'Value': '65', 'Weight': 3},
                   5: {'Name': 'Weight', 'Rule': 'Lowest Better', 'Value': 'N/A', 'Weight': 4},
                   6: {'Name': 'No. of SIM Cards', 'Rule': 'Not Important', 'Value': 1, 'Weight': 1},
                   7: {'Name': 'SIM Card Type', 'Rule': 'Not Important', 'Value': [1, 2, 3, 4], 'Weight': 1},
                   8: {'Name': 'Screen Size', 'Rule': 'Optimal Value', 'Value': '4.75', 'Weight': 5},
                   9: {'Name': 'Screen Resolution', 'Rule': 'Highest Better', 'Value': 'N/A', 'Weight': 5},
                   10: {'Name': 'Operating System', 'Rule': 'Constant Scale', 'Value': [6, 5, 4, 3, 1, 2], 'Weight': 5},
                   11: {'Name': 'No. of CPU Cores', 'Rule': 'Highest Better', 'Value': 'N/A', 'Weight': 4},
                   12: {'Name': 'SD Card Option', 'Rule': 'Not Important', 'Value': 'Good', 'Weight': 2},
                   13: {'Name': 'Max SD Card Size', 'Rule': 'Highest Better', 'Value': 'N/A', 'Weight': 4},
                   14: {'Name': 'RAM', 'Rule': 'Highest Better', 'Value': 'N/A', 'Weight': 4},
                   15: {'Name': 'Main Camera Quality', 'Rule': 'Highest Better', 'Value': 'N/A', 'Weight': 4},
                   16: {'Name': 'Main Camera Video', 'Rule': 'Highest Better', 'Value': 'N/A', 'Weight': 4},
                   17: {'Name': 'Secondary Camera Quality', 'Rule': 'Highest Better', 'Value': 'N/A', 'Weight': 4},
                   18: {'Name': 'Secondary Camera Video', 'Rule': 'Highest Better', 'Value': 'N/A', 'Weight': 4},
                   19: {'Name': 'IR Transmitter', 'Rule': 'Not Important', 'Value': 'Good', 'Weight': 2},
                   20: {'Name': 'Radio', 'Rule': 'Not Important', 'Value': 'Good', 'Weight': 1},
                   21: {'Name': 'Charging Cable Type', 'Rule': 'Constant Scale', 'Value': [3, 1, 2], 'Weight': 1},
                   22: {'Name': 'NFC', 'Rule': 'Boolean', 'Value': 'Good', 'Weight': 1},
                   23: {'Name': 'Finger Print', 'Rule': 'Boolean', 'Value': 'Bad', 'Weight': 2},
                   24: {'Name': 'Price', 'Rule': 'Lowest Better', 'Value': 'N/A', 'Weight': 5},
                   25: {'Name': 'BaseMark Test', 'Rule': 'Highest Better', 'Value': 'N/A', 'Weight': 3},
                   26: {'Name': 'Load Speaker', 'Rule': 'Highest Better', 'Value': 'N/A', 'Weight': 5},
                   27: {'Name': 'Audio Quality', 'Rule': 'Highest Better', 'Value': 'N/A', 'Weight': 5},
                   28: {'Name': 'Battery Endurance', 'Rule': 'Highest Better', 'Value': 'N/A', 'Weight': 5},
                   29: {'Name': 'Water Resistant', 'Rule': 'Boolean', 'Value': 'Good', 'Weight': 4}},
              'Hi-Tech Employee': {
                  1: {'Name': 'Battery Capacity', 'Rule': 'Highest Better', 'Value': 'N/A', 'Weight': 5},
                  2: {'Name': 'Year', 'Rule': 'Highest Better', 'Value': 'N/A', 'Weight': 5},
                  3: {'Name': 'Height', 'Rule': 'Optimal Value', 'Value': '150', 'Weight': 3},
                  4: {'Name': 'Width', 'Rule': 'Optimal Value', 'Value': '70', 'Weight': 3},
                  5: {'Name': 'Weight', 'Rule': 'Lowest Better', 'Value': 'N/A', 'Weight': 4},
                  6: {'Name': 'No. of SIM Cards', 'Rule': 'Highest Better', 'Value': 'N/A', 'Weight': 4},
                  7: {'Name': 'SIM Card Type', 'Rule': 'Constant Scale', 'Value': [4, 3, 2, 1], 'Weight': 3},
                  8: {'Name': 'Screen Size', 'Rule': 'Optimal Value', 'Value': '5.25', 'Weight': 4},
                  9: {'Name': 'Screen Resolution', 'Rule': 'Highest Better', 'Value': 'N/A', 'Weight': 5},
                  10: {'Name': 'Operating System', 'Rule': 'Constant Scale', 'Value': [6, 5, 3, 4, 1, 2], 'Weight': 4},
                  11: {'Name': 'No. of CPU Cores', 'Rule': 'Highest Better', 'Value': 'N/A', 'Weight': 4},
                  12: {'Name': 'SD Card Option', 'Rule': 'Boolean', 'Value': 'Good', 'Weight': 5},
                  13: {'Name': 'Max SD Card Size', 'Rule': 'Highest Better', 'Value': 'N/A', 'Weight': 5},
                  14: {'Name': 'RAM', 'Rule': 'Highest Better', 'Value': 'N/A', 'Weight': 5},
                  15: {'Name': 'Main Camera Quality', 'Rule': 'Highest Better', 'Value': 'N/A', 'Weight': 5},
                  16: {'Name': 'Main Camera Video', 'Rule': 'Highest Better', 'Value': 'N/A', 'Weight': 5},
                  17: {'Name': 'Secondary Camera Quality', 'Rule': 'Highest Better', 'Value': 'N/A', 'Weight': 5},
                  18: {'Name': 'Secondary Camera Video', 'Rule': 'Highest Better', 'Value': 'N/A', 'Weight': 5},
                  19: {'Name': 'IR Transmitter', 'Rule': 'Boolean', 'Value': 'Good', 'Weight': 2},
                  20: {'Name': 'Radio', 'Rule': 'Not Important', 'Value': 'Good', 'Weight': 1},
                  21: {'Name': 'Charging Cable Type', 'Rule': 'Constant Scale', 'Value': [3, 1, 2], 'Weight': 3},
                  22: {'Name': 'NFC', 'Rule': 'Boolean', 'Value': "Good", 'Weight': 3},
                  23: {'Name': 'Finger Print', 'Rule': 'Boolean', 'Value': 'Good', 'Weight': 4},
                  24: {'Name': 'Price', 'Rule': 'Lowest Better', 'Value': 'N/A', 'Weight': 5},
                  25: {'Name': 'BaseMark Test', 'Rule': 'Highest Better', 'Value': 'N/A', 'Weight': 4},
                  26: {'Name': 'Load Speaker', 'Rule': 'Highest Better', 'Value': 'N/A', 'Weight': 1},
                  27: {'Name': 'Audio Quality', 'Rule': 'Highest Better', 'Value': 'N/A', 'Weight': 2},
                  28: {'Name': 'Battery Endurance', 'Rule': 'Highest Better', 'Value': 'N/A', 'Weight': 5},
                  29: {'Name': 'Water Resistant', 'Rule': 'Boolean', 'Value': 'Good', 'Weight': 4}},
              'Pensioners':
                  {1: {'Name': 'Battery Capacity', 'Rule': 'Highest Better', 'Value': 'N/A', 'Weight': 5},
                   2: {'Name': 'Year', 'Rule': 'Highest Better', 'Value': 'N/A', 'Weight': 2},
                   3: {'Name': 'Height', 'Rule': 'Optimal Value', 'Value': '175', 'Weight': 4},
                   4: {'Name': 'Width', 'Rule': 'Optimal Value', 'Value': '85', 'Weight': 4},
                   5: {'Name': 'Weight', 'Rule': 'Lowest Better', 'Value': 'N/A', 'Weight': 4},
                   6: {'Name': 'No. of SIM Cards', 'Rule': 'Not Important', 'Value': 1, 'Weight': 1},
                   7: {'Name': 'SIM Card Type', 'Rule': 'Constant Scale', 'Value': [1, 2, 3, 4], 'Weight': 1},
                   8: {'Name': 'Screen Size', 'Rule': 'Highest Better', 'Value': 'N/A', 'Weight': 5},
                   9: {'Name': 'Screen Resolution', 'Rule': 'Highest Better', 'Value': 'N/A', 'Weight': 3},
                   10: {'Name': 'Operating System', 'Rule': 'Constant Scale', 'Value': [5, 6, 3, 4, 1, 2],
                        'Weight': 1},
                   11: {'Name': 'No. of CPU Cores', 'Rule': 'Highest Better', 'Value': 'N/A', 'Weight': 1},
                   12: {'Name': 'SD Card Option', 'Rule': 'Boolean', 'Value': 'Good', 'Weight': 5},
                   13: {'Name': 'Max SD Card Size', 'Rule': 'Highest Better', 'Value': 'N/A', 'Weight': 5},
                   14: {'Name': 'RAM', 'Rule': 'Highest Better', 'Value': 'N/A', 'Weight': 1},
                   15: {'Name': 'Main Camera Quality', 'Rule': 'Highest Better', 'Value': 'N/A', 'Weight': 4},
                   16: {'Name': 'Main Camera Video', 'Rule': 'Highest Better', 'Value': 'N/A', 'Weight': 4},
                   17: {'Name': 'Secondary Camera Quality', 'Rule': 'Highest Better', 'Value': 'N/A',
                        'Weight': 4},
                   18: {'Name': 'Secondary Camera Video', 'Rule': 'Highest Better', 'Value': 'N/A',
                        'Weight': 4},
                   19: {'Name': 'IR Transmitter', 'Rule': 'Boolean', 'Value': 'Good', 'Weight': 4},
                   20: {'Name': 'Radio', 'Rule': 'Boolean', 'Value': 'Good', 'Weight': 5},
                   21: {'Name': 'Charging Cable Type', 'Rule': 'Constant Scale', 'Value': [3, 1, 2],
                        'Weight': 4}, 22: {'Name': 'NFC', 'Rule': 'Not Important', 'Value': 1, 'Weight': 2},
                   23: {'Name': 'Finger Print', 'Rule': 'Boolean', 'Value': 'Good', 'Weight': 1},
                   24: {'Name': 'Price', 'Rule': 'Lowest Better', 'Value': 'N/A', 'Weight': 5},
                   25: {'Name': 'BaseMark Test', 'Rule': 'Not Important', 'Value': 1, 'Weight': 1},
                   26: {'Name': 'Load Speaker', 'Rule': 'Highest Better', 'Value': 'N/A', 'Weight': 5},
                   27: {'Name': 'Audio Quality', 'Rule': 'Highest Better', 'Value': 'N/A', 'Weight': 5},
                   28: {'Name': 'Battery Endurance', 'Rule': 'Highest Better', 'Value': 'N/A', 'Weight': 5},
                   29: {'Name': 'Water Resistant', 'Rule': 'Boolean', 'Value': 'Good', 'Weight': 3}}}
