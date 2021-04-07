%% Setting up test - CCA recognition test script
clear

stimfreq = [5,6,7,8];
roi = [1,4,5,10,15,16];
length_trial_s = 2;
num_trials = 25;
trials_completed = 0;
correct_trials = 0;
srate = 256;
elapsed_time = zeros(1,num_trials);

%%
for i = 1:num_trials
    n = randi([5 8]);
    %n = 6;
    input_val = n;
    %start = randi([3,28]);
    start = randi([1 30-length_trial_s]);
    endtest = start + length_trial_s;
    
    if input_val == 5
        load('session_5Hz.mat');
    elseif input_val == 6
        load('session_6Hz.mat');
    elseif input_val == 7
        load('session_7Hz.mat');
    else 
        load('session_8Hz.mat');
        
    end
    
    CCA_data1
   
     if input_val == probable_input
        correct_trials = correct_trials+1;
    end
    trials_completed = trials_completed+1;
 end

    accuracy = (correct_trials/trials_completed)*100
    
%% Calculating ITR
Num_inputs = 4;
 P_c = accuracy/100;
 P_I = 1-P_c;
 
 trials_pm = 60/length_trial_s;
 ITR_test =trials_pm * (log2(Num_inputs) + ((1-P_I)*log2(1-P_I)))
 
 if P_c == 1
     ITR100 =trials_pm * (log2(Num_inputs) + ((1-P_I)*log2(1-P_I)))
 else
     ITR =trials_pm * (log2(Num_inputs) + ((1-P_I)*log2(1-P_I))+ P_I*(log2(P_I/(Num_inputs-1))))

     
 end