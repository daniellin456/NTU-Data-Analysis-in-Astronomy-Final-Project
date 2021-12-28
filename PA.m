clc; clear all;
% filename = 'PA.xlsx';
% A = xlsread(filename)
load('PA')
Delta_PA=A(:,7);

co_rotate=0; counter_rotate=0; offset_rotation=0;
for i=1:size(Delta_PA)
    if abs(Delta_PA(i))<30
        co_rotate=co_rotate+1;
    elseif abs(Delta_PA(i))>150
        counter_rotate=counter_rotate+1;
    else
        offset_rotation=offset_rotation+1;
    end
end
[co_rotate, counter_rotate, offset_rotation, co_rotate+counter_rotate+offset_rotation]
