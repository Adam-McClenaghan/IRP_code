% clear 
% clc

%% Setup
stimfreq = [5,6,7,8];
roi = [1,4,5,10,15,16];
trialsecs = 30;
srate = 256;
start = 22; %seconds
endtest = 24; %seconds

    
load('session_7Hz.mat');

if start == 1
    row1 = X(start:endtest*srate,:);
    data = zeros(endtest*srate,length(roi));
elseif start ~= 1
    row1 = X(start*srate:endtest*srate,:);
    rowsdata = ((endtest-start)*srate)+1;
    data = zeros(rowsdata,length(roi));
end

%freqdisplay = 

for i = 1:length(roi)
    data(:,i) = row1(:,roi(i));
end

time = length(data(:,1))/srate;
 

Triallength = trialsecs*srate;

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

 r = zeros(num_inputs,length(roi));
for d = 1:num_inputs
    [A,B,r(d,:)] = canoncorr(data,compmat(:,:,d)');
end

r_tot = sum(r,2);
[result,position] = max(r_tot);
probable_input = stimfreq(position);

disp(probable_input);

writematrix(probable_input, 'C:\Users\Adam\Documents\MENG_yr3\IRP_papers\pytest.csv')
