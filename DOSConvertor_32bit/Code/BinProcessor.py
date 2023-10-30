import os
import numpy as np
import re
import struct

class BinaryKonfigFileProcessor:
    def __init__(self, config_file_path):
        self.config_file_path = config_file_path
        self.binary_data = self.read_binary_data()
        self.lines = self.decode_and_split_lines()
        self.temperature_cal = self.extract_temperature_cal()

    def read_binary_data(self):
        with open(self.config_file_path, 'rb') as binary_file:
            return binary_file.read()

    def decode_and_split_lines(self):
        decoded_data = self.binary_data.decode('latin-1')
        return decoded_data.split('\r\n')

    def extract_numerical_value(self, s):
        matches = re.findall(r'=\s*([-+]?\d*\.?\d+|\d+)', s.replace(',', '.'))
        return float(matches[0]) if matches else None

    def extract_temperature_cal(self):
        return self.extract_numerical_value(self.lines[-4])
    
class BinaryDataProcessor:
    def __init__(self, directory_path):
        self.directory_path = directory_path
        self.filtered_file_list = self.filter_files()
        self.whole_data = []
        self.M = None
        self.n_LW = None
        self.length_data = None
        self.Zeitschift = None
        self.combined_array = None

    def filter_files(self):
        file_list = os.listdir(self.directory_path)
        return [item for item in file_list if re.match(r'REF\.\d{3}', item)]

    def process_files(self):
        for file_name in self.filtered_file_list:
            file_path = os.path.join(self.directory_path, file_name)
            with open(file_path, 'rb') as binary_file:
                binary_data = binary_file.read()
                self.M = struct.unpack(f"{len(binary_data)//2}H", binary_data)

                self.n_LW = self.M[2]
                self.n_mess = self.M[4]
                self.length_data = self.M[5]
                self.Zeitschift = self.M[10]
                self.Spalte_Zeit = 1

                data_v_raw1 = self.M[:(self.n_mess+2)*self.length_data+21]
                data_v_raw2 = data_v_raw1[21:]
                data_v = np.reshape(data_v_raw2, (self.length_data, self.n_mess+2))
                self.whole_data.append(data_v)
                comb_arr = np.concatenate(self.whole_data)
        return comb_arr
    
class DataProcessor:
    def __init__(self, combined_array, temperature_cal, Zeitschift, n_mess):
        self.combined_array = combined_array
        self.temperature_cal = temperature_cal
        self.n_mess = n_mess
        self.Zeitschift = Zeitschift
        self.num_datapoints = None
        

    def process_combined_array(self):
        l = self.combined_array.shape
        self.num_datapoints = 10235 / 5

        floatarray = self.combined_array.astype(np.float64)
        floatarray[:, 2:(self.n_mess + 2)] = (self.num_datapoints * np.ones((l[0], self.n_mess)) - floatarray[:, 2:(self.n_mess + 2)]) * 5 / 1000
        floatarray[:, 2] = floatarray[:, 2] * self.temperature_cal
        floatarray[:, 0] = ((floatarray[:, 0] - floatarray[0, 0]) / self.Zeitschift).astype(int) * 1000
        matrix = np.unique(floatarray, axis=0)
        return matrix
    
class DataExporter:
    def __init__(self, result_matrix, n_LW ,tcyc=None, num_cycle=None):
        self.result_matrix = result_matrix
        self.tcyc = tcyc
        self.n_LW = n_LW
        self.num_cycle = num_cycle
        self.Zeit_arr = []
        self.Temp_arr = []
        self.Strain_arr = []
        self.num_cycle = num_cycle
        self.format_data()

    def format_data(self):
        if self.tcyc is None:
            self.tcyc = self.result_matrix.shape[0] // (self.n_LW - 2)

        if self.num_cycle is None:
            self.num_cycle = self.result_matrix.shape[0] // self.tcyc

        self.num_cycles = self.result_matrix.shape[0] // self.tcyc

        if self.num_cycle < 1 or self.num_cycle > self.num_cycles:
            print("Invalid cycle selected.")
        else:
            start_index = (self.num_cycle - 1) * self.tcyc
            end_index = self.num_cycle * self.tcyc

            self.Zeit_arr = ((self.result_matrix[start_index:end_index, 0] - self.result_matrix[start_index, 0]).astype(int)).tolist()
            self.Temp_arr = np.round(self.result_matrix[start_index:end_index, 2], 3).tolist()
            self.Strain_arr = self.result_matrix[start_index:end_index, 3].tolist()

    def save_data(self, file_path):
        with open(file_path, 'w') as file:
            for z, t, d in zip(self.Zeit_arr, self.Temp_arr, self.Strain_arr):
                file.write(f"{z}\t{t}\t{d}\n")



    """config_file_path = 'C:\Pythonscripts\DATA\C265H\KFG\EPS.KFG'
    config_file_processor = BinaryKonfigFileProcessor(config_file_path)

    directory_path = 'C:\Pythonscripts\DATA\C265H\REF'
    bin_data_processor = BinaryDataProcessor(directory_path)
    combined_array = bin_data_processor.process_files()

    data_processor = DataProcessor(combined_array, config_file_processor.temperature_cal, bin_data_processor.Zeitschift, bin_data_processor.n_mess)
    result_matrix = data_processor.process_combined_array()

    tcyc = 90
    num_cycle = 4

    data_Exporter = DataExporter(result_matrix, tcyc, num_cycle)

    # Specify the file path and save the data
    file_path = 'LW6.txt'
    data_Exporter.save_data(file_path)"""