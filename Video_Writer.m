outputfilename = "Scran 0-6 500Hz.mp4";
newVid = VideoWriter(outputfilename, 'MPEG-4'); % New
newVid.FrameRate = 60;
newVid.Quality = 100;
open(newVid);

%Generating datastore
imgds = imageDatastore('C:\Users\basti\OneDrive\Desktop\MATLAB Codes\Sorted Images v2\Scram 0-6 500Hz\*.tif');
imgs = readall(imgds);
len_imgs = length(imgs);

%Reading each frame from datastore
for i = 1:len_imgs
    %Reading the ith image:
    img = readimage(imgds,i);
    writeVideo(newVid,img);
end
close(newVid)