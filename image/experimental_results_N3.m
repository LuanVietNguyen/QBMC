
%time_safe8 = [1.6 1.1 8.3 6.9 76.1 40.1 344.8 288.8];
time_safe3 = [4.02  8.3 117.8 ];
time_unsafe3 = [ 3.97 6.9 22.7 94.31];
hycomp_time_safe3 = [0.51 2.2 55.8 539.7];
hycomp_time_unsafe3 = [ 0.51 2.1 6.7 6.5];
dreach_time_safe3 = [1.4 2.7];
dreach_time_unsafe3 = [ 1.3 2.7 959.3 966.8];
%%%%%
mem_safe3 = [48.7 48.7 52.4 ];
mem_unsafe3 = [48.7 48.7 49.7 74.6];
hycomp_mem_safe3 = [120.2 131.8 214.4 713.4];
hycomp_mem_unsafe3 = [121.5 131.8 149.6 167.1];
dreach_mem_safe3 = [2.5 26.4];
dreach_mem_unsafe3 = [ 2.5 26.8 235.3 241.2];
%%%%%

N = [ 4 8 16 32 ];
N_2 = [ 4 8]; 
N_3 = [ 4 8 16];
% plot runtime at k <= 8
figure
%plot(time_safe3, N, 'LineWidth',1.3); 
%plot(N,time_safe3,'-.ro',N,time_unsafe3,'-.b','LineWidth',2);
plot(N_3,time_safe3,'-.o',N,time_unsafe3,'-.s',N,hycomp_time_safe3,'-+',N,hycomp_time_unsafe3,'-d',...
    N_2,dreach_time_safe3,':^',N,dreach_time_unsafe3,':>','LineWidth',2);
%plot(N,time_safe3,'-ro',N,time_unsafe3,'-.b','LineWidth',2);
%hold on;
%plot(N,hycomp_time_safe3,'-+g',N,hycomp_time_unsafe3,'-dy','LineWidth',2);
ax = gca;
set(ax,'XTick',[ 4 8 12 16 20 24 28 32]);
%
xlabel('k');
ylabel('Runtime (s)');
%legend('QBMC-safe','QBMC-unsafe','HyComp-safe','HyComp-unsafe','dReach-safe','dReach-unsafe','Location','northwest');
title('N = 3');
% plot memmory at k <= 8 [ 4 8 12 16 20 24 28 32]
figure
plot(N_3,mem_safe3,'-.o',N,mem_unsafe3,'-.s',N,hycomp_mem_safe3,'-+',N,hycomp_mem_unsafe3,'-d',...
    N_2,dreach_mem_safe3,':^',N,dreach_mem_unsafe3,':>','LineWidth',2);
ax = gca;
set(ax,'XTick',[ 4 8 12 16 20 24 28 32]);
xlabel('k');
ylabel('Memory Usage (MB)');
%legend('QBMC-safe','QBMC-unsafe','HyComp-safe','HyComp-unsafe','dReach-safe','dReach-unsafe','Location','northwest');
title('N = 3');