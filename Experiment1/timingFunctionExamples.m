%Time function

%% Get time on current clock, since computer startup
t0 = GetSecs; 

%% Wait a particular duration 
t1 = GetSecs;
WaitSecs(3);
t2 = GetSecs;
disp(t2-t1)

%% Wait until a particular time
t3 = GetSecs;
WaitSecs('untiltime', t3+2)
t4 = GetSecs;
<<<<<<< HEAD
disp(t4-t3)
=======
disp(t4-t)


>>>>>>> fb45f784147950a166e4c7aafa6bf9f26f43bdbc
