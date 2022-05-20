% Load data
%data = table2array(readtable('./data_N2_spindles_15sec_200Hz.txt'));

% Define sampling frequency and time vector
%sf = 200;
%times = (1:size(data)) / sf;

% Plot the signal
%plot(times, data);

pyenv('Version','/home/robb/.anaconda3/bin/python');
pyrunfile('yasa_script.py') %  './data_N2_spindles_15sec_200Hz.txt' '200' 



%fig, ax = plt.subplots(1, 1, figsize=(14, 4))
%plt.plot(times, data, lw=1.5, color='k')
%plt.xlabel('Time (seconds)')
%plt.ylabel('Amplitude (uV)')
%plt.xlim([times.min(), times.max()])
%plt.title('N2 sleep EEG data (2 spindles)')
%sns.despine()