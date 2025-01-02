%The image format:
ST = '.jpg';

%Frame Number:
frames = 1;

%Code:
s=dir('*.mp4');
files={s.name};

%dir = 'E:\BGC Videos Raw\';
%Allows you to make a seperate directory for each set of frames:
%mkdir('Frames');

for k=1:numel(files)
v = VideoReader(files{k});

name = v.Name;
time = v.Duration;
framerate = v.Framerate;

full_frame = time.*framerate;

%Erasing the extension from the string name.

name_final = erase(name,'.mp4');

disp(name_final);

%Allows you to make a seperate directory for each set of frames:
cd('Frames');
for x = 1:frames
    Sx = num2str(x);
    under = '_frame_';
    Sx_final = strcat(under,Sx);
    vid = read(v,x);
    Strc = strcat(name_final,Sx_final,ST);
    imwrite(vid,Strc);
    disp(x);
end

cd(char(dir));
end 
