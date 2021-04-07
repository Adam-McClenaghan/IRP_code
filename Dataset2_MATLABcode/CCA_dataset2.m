% clear 
% clc

%% Setup
clear
clc

stimfreq = [8,9,10,11,12,13,14,15];
roi = [56,57,58,61,62,63]; %first dimension of 4D data array
srate = 250;
% trialsecs = 30;
% srate = 250;
% start = 22; %seconds
% endtest = 24; %seconds

    
load('S1.mat');
load('Freq_Phase.mat')

Input_frequency = 13; %Changes input frequency based on value in freqs file
Row_number = find(freqs == Input_frequency);

for i = 1:length(roi)
    Dataset_red(i,:,:,:) = data(roi(i),:,:,:);
end

for j = 1:length(stimfreq)
    Trial_1 = Dataset_red(:,:,1:j,1);

end   
Input_1 = Trial_1(:,:,Row_number)';
   
%% CanonCorrelation

S = srate;
T = length(data);
t = (1/S:1/S:T/S);
num_harmonics = 4;
num_inputs = length(stimfreq);

compmat = zeros(2*num_harmonics,length(t),num_inputs);

%% Create comparrisson matrix

for i = 1:length(compmat(1,1,:))


input_freq = stimfreq(i);
 
    for k = 1:2:2*num_harmonics
    compmat(k,:,i) = sin((k+1)*pi*input_freq*t);
    end

    for j = 2:2:2*num_harmonics
    compmat(j,:,i) = cos(j*pi*input_freq*t);    
    end

end

%% Compute canonical correlation values
num_inputs = length(stimfreq);
 r = zeros(num_inputs,length(roi));
for d = 1:num_inputs
    [A,B,r(d,:)] = canoncorr(Input_1,compmat(:,:,d)');
end

r_tot = sum(r,2);
[result,position] = max(r_tot);
probable_input = stimfreq(position);

disp(probable_input);

writematrix(probable_input, 'C:\Users\Adam\Documents\MENG_yr3\IRP_papers\pytest.csv')
