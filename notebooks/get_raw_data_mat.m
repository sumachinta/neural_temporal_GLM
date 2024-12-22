addpath D:\MATLAB_Analysis\Pre+process\Fncs\Run_tuning\testing_model_helper_fns\utils
addpath 'D:\MATLAB_Analysis\Pre+process\Fncs'

bin_res = .02;

%%% bins
bins = 0:bin_res:Exp.t(end);
%%% Wheel speeds
[WheelSpeed,~] = hist(Exp.t(Exp.Wheel.WheelTics),bins); 
WheelSpeed = (WheelSpeed*(1/bin_res))*55.8575/5000;
%%% Behavior variables
LOI = Whisking.free_whisk_LOI;
Setpoint = get_whisking_vars_in_timebins(Exp,Whisking,bins,LOI,Whisking.Setpoint);
Amplitude = get_whisking_vars_in_timebins(Exp,Whisking,bins,LOI,Whisking.Amplitude);

%%% Spikerate in bins
ListSpkClust = Spiking.SC.ListSpkClust_SC;
k = 1;
for n = 1:length(ListSpkClust)
        [spike(k,:)] = hist(Spiking.SC.SpikeTime_SC{n,1},bins);
        spike(k,:) = spike(k,:)/bin_res;
        k = k+1;
end

%% Filter bins based on stimulus conditions and get behavior & spike values in those bins 

Drum(:,1) = Exp.Drum.Drum(:,1);

% Free Whisking
startT =[]; startT = Exp.Drum.StimTime(Drum==4&Exp.Whisker==1,2);%&Exp.ignorevideos~=1,2); 
endT = []; endT =  Exp.Drum.ReturnTime(Drum==4&Exp.Whisker==1,2);%&Exp.ignorevideos~=1,1); 
[spike_fw_raw,run_fw_raw,stpt_fw_raw,amp_fw_raw, BOOL] = get_spike_beh_between_times_temp(bins,startT,endT,spike,WheelSpeed,Setpoint,Amplitude);
spike_count_fw_raw = spike_fw_raw*bin_res;

select_time_bins = bins(logical(BOOL));

%% Save the variables to a .mat file
save('neural_data.mat', 'spike_fw_raw', 'run_fw_raw', 'stpt_fw_raw', 'amp_fw_raw', 'select_time_bins');

