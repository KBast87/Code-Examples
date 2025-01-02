 %{
Version 6: Parallel Coding is AMAZING! For one case, the average and scintillation takes about the same time as running them all at once with the increased RAM! 
 - Kavon
%}

tic

parpool("Processes",4);

%Percent Format:
formatSpec = '%s and %s are %3.2f percent complete!';
formatSpec2 = '%s is %3.2f percent complete!';
formatSpec3 = 'Center Pixel %s (x,y): (%d,%d)';

%Use this to change the image format
frmt = '.jpg';

%Code Starts Here

%Getting Directory
listing = dir('C:\Users\basti\OneDrive\Desktop\Videos and New Code\Videos\');
path = 'C:\Users\basti\OneDrive\Desktop\Videos and New Code\Videos\';
backslash = '\';

%Getting Folder Names and length
name = {listing(:).name};
name = name';
len = length(name);

name_str = string(name);

for i = 3:len
    name_str_fin(i - 2) = name_str(i);
end 

name_str_fin = erase(name_str_fin,'.mp4');

name_str_fin = name_str_fin';

m1_data = single(zeros(1,len - 2));
n1_data = single(zeros(1,len - 2));

avg_min_data = single(zeros(1,len - 2));
avg_max_data = single(zeros(1,len - 2));

scin_min_data = single(zeros(1,len - 2));
scin_max_data = single(zeros(1,len - 2));

twopoint_min_data = single(zeros(1,len - 2));
twopoint_max_data = single(zeros(1,len - 2));

wander = single(zeros(1,len - 2));

%Cutoff [in percent of the maximum values of the array]:
cutoff = 0.2;

parfor a = 3:len

    %Name of the video file%
    multi_vid = name(a);
    multi_vid = string(multi_vid);
    
    %Naming and formatting the files for first video
    name_a = erase(multi_vid,'.mp4');
    name_a_avg = strcat(name_a,'-AVG',frmt);
    name_a_scin = strcat(name_a,'-SCIN',frmt);
    name_a_two = strcat(name_a,'-TWOPOINT');
    
    %Read Video
    vid = VideoReader(multi_vid);
    v = read(vid);
    
    frames = vid.NumFrames;

    blue_frames = single(squeeze(v(:,:,3,:)));
    
    vid = [];
    v = [];
    
    blue_frames = blue_frames(1:1024,129:1152,:)./255;
    
    %Average and Scintillation Index:

    avg = mean(blue_frames,3);
    
    scin = var(blue_frames,1,3)./avg.^2;
    
    avg_min = min(min(avg));
    avg_max = max(max(avg));

    scin_min = min(min(scin));
    scin_max = max(max(scin));

    %Adding a cutoff:
    point_linear = find(scin > (cutoff.*max(max(scin))));
    
    sz = [1024 1024];
    
    [xvals,yvals] = ind2sub(sz,point_linear);
    
    xval_max = max(max(xvals));
    xval_min = min(min(xvals));
    
    yval_max = max(max(yvals));
    yval_min = min(min(yvals));
    
    num_rows = xval_max - xval_min;
    num_cols = yval_max - yval_min;
    
    %{
    You have to take the floor division here otherwise, you won't get an
    integer for your point, depends on if the array has even or odd length.
    %}
    
    %Returning coordinates to original:
    m1 = floor((xval_max + xval_min)./2);
    n1 = floor((yval_max + yval_min)./2);
    
    str_m1 = string(m1);
    str_n1 = string(n1);
    str_m1n1 = strcat("-","(",str_m1,",",str_n1,")");

    name_a_two_fin = strcat(name_a_two,str_m1n1,frmt);  
    
    x_cm_val = [];
    y_cm_val = [];

    %Center of Intensity Calculation:

    p_1 = squeeze(blue_frames(m1,n1,:)); 

    twopoint = single(zeros(1024,1024));

    %Two Point Correlation:
        for x1 = 1:1024
            for y1 = 1:1024
                %Finding I(x,y,t)
                p_n = squeeze(blue_frames(x,y,:));
            
                %Mean p_n;
                mean_p_n = mean(p_n);

                %Finding I(m,n,t);
                mean_p_1 = mean(p_1);

                %Cumulative Sum [Top part of Covariance]:

                cumsum_p_1_p_n = cumsum((p_n - mean_p_n).*(p_1 - mean_p_1));
            
                %Covariance:

                covar = (cumsum_p_1_p_n(frames))./(frames);

                %Two Point:

                twopoint(x1,y1) = covar./((mean_p_n).*(mean_p_1));

            end 
        end 
    
    twopoint_min = min(min(twopoint));
    twopoint_max = max(max(twopoint));

    m1_data(1,a - 2) = m1;
    n1_data(1,a - 2) = n1;

    avg_min_data(1,a - 2) = avg_min;
    avg_max_data(1, a - 2) = avg_max;

    scin_min_data(1, a - 2) = scin_min;
    scin_max_data(1, a - 2) = scin_max;
    
    twopoint_min_data(1, a - 2) = twopoint_min;
    twopoint_max_data(1, a - 2) = twopoint_max;
    
    figure(1)
    colormap(jet);
    pcolor(avg);
    set(gca,'XTick',[], 'YTick', [])
    shading interp;
    saveas(gcf,name_a_avg);
    
    figure(2)
    colormap(jet);
    pcolor(scin);
    set(gca,'XTick',[], 'YTick', [])
    shading interp;
    saveas(gcf,name_a_scin);

    figure(3)
    colormap(jet);
    pcolor(twopoint);
    set(gca,'XTick',[], 'YTick', [])
    shading interp;
    saveas(gcf,name_a_two_fin);

end
%}

fft_corr_min_data = single([]);
fft_corr_max_data = single([]);
fft_corr_range_data = single([]);
name_a_fft_corr_data = strings(0);

for a = 3:len
    
    %Name of the video file%
    multi_vid = name(a);
    multi_vid = string(multi_vid);

    %Naming and formatting the files for first video
    name_a = erase(multi_vid,'.mp4');

    %Read Video
    vid = VideoReader(multi_vid);
    v = read(vid);
    
    blue_frames = single(squeeze(v(:,:,3,:)));

    v = [];
    
    blue_frames = blue_frames(1:1024,129:1152,:)./255;
    
    parfor b = 3:len
        
        fftcorr_mat = single(zeros(1024,1024,1000));

        name_ab = string(strcat(name(a),'-',name(b)));
        name_ab = erase(name_ab,'.mp4');

        frames = vid.NumFrames;

        multi_vid2 = name(b);
        multi_vid2 = string(multi_vid2);
        
        vid2 = VideoReader(multi_vid2);
        v2 = read(vid2);
    
        frames2 = vid2.NumFrames;

        blue_frames2 = single(squeeze(v2(:,:,3,:)));
   
        vid2 = [];
        v2 = [];

        blue_frames2 = blue_frames2(1:1024,129:1152,:)./255;
        
        name_a_fftcorr_nofrmt = strcat(name_ab,'-FFTCORR');
        name_a_fftcorr = strcat(name_ab,'-FFTCORR',frmt);

        if frames2 < frames
            frames = frames2;
            name_a_fftcorr = strcat(name_ab,'-FFTCORR-',string(frames),'-frames',frmt);

        elseif frames < frames2
            frames2 = frames;
            name_a_fftcorr = strcat(name_ab,'-FFTCORR-',string(frames),'-frames',frmt);
        end 
     
        for z = 1:frames
            frames_fft = fftshift(fft2(blue_frames(:,:,z)));
            frames2_fft = fftshift(fft2(blue_frames2(:,:,z)));
            
            fftcorr_mat(:,:,z) = abs(ifftshift(ifft2(frames_fft.*conj(frames2_fft))));  
        end 

        fft_corr = mean(fftcorr_mat,3);

        fft_corr_max = max(max(fft_corr));
        fft_corr_min = min(min(fft_corr));

        fft_corr_min_data(1, b - 2) = fft_corr_min;
        fft_corr_max_data(1, b - 2) = fft_corr_max;;
        name_a_fft_corr_data(1, b - 2) = name_a_fftcorr_nofrmt;

        figure(4)
        colormap(jet);
        pcolor(fft_corr);
        set(gca,'XTick',[], 'YTick', [])
        shading interp;
        saveas(gcf,name_a_fftcorr);

    end
    
    filename_fft = strcat(name_a,"-FFTCORR",".csv");
    
    name_a_fft_corr_data = name_a_fft_corr_data';
    fft_corr_min_data = fft_corr_min_data';
    fft_corr_max_data = fft_corr_max_data';

    fft_corr_range_data = fft_corr_max_data - fft_corr_min_data;
    
    %Feature scaling the mins and maxes.

    data_fft = table(name_a_fft_corr_data,fft_corr_min_data,fft_corr_max_data,fft_corr_range_data);
    
    writetable(data_fft,filename_fft);
    
    clear fftcorr_mat
end

parfor a = 3:len
    
    %Name of the video file%
    multi_vid = name(a);
    multi_vid = string(multi_vid);

    %Naming and formatting the files for first video
    name_a = erase(multi_vid,'.mp4');

    %Read Video
    vid = VideoReader(multi_vid);
    v = read(vid);
    
    frames = vid.NumFrames;
    blue_frames = single(squeeze(v(:,:,3,:)));
    
    blue_frames = blue_frames(1:1024,129:1152,:)./255;

    vid = [];
    v = [];

    %Center of Intensity Calculation:
    
    x_cm = single(zeros(1,frames));
    y_cm = single([zeros(1,frames)]);

    for i=1:frames

        frame = blue_frames(:,:,i);
    
        tot_I = sum(frame(:));
        [x,y] = ndgrid(1:size(frame,1),1:size(frame,2));
    
        x_cm_val = sum(x(:).*frame(:))./tot_I;
        y_cm_val = sum(y(:).*frame(:))./tot_I;

        x_cm(1,i) = floor(x_cm_val);
        y_cm(1,i) = floor(y_cm_val);
    end 

   r_data = sqrt((x_cm - m1_data(1, a-2)).^2 + (y_cm - n1_data(1, a-2)).^2);
   
   wander(1, a - 2) = std(r_data);

end 

avg_min_data = avg_min_data';
avg_max_data= avg_max_data';
scin_min_data = scin_min_data';
scin_max_data = scin_max_data';
twopoint_min_data = twopoint_min_data';
twopoint_max_data = twopoint_max_data';
m1_data = m1_data';
n1_data = n1_data';
wander = wander';

data = table(name_str_fin,avg_min_data,avg_max_data,scin_min_data,scin_max_data,twopoint_min_data,twopoint_max_data,m1_data,n1_data);
data_wander = table(name_str_fin,wander);

%Writing data to a table
writetable(data,"data_video.csv")
writetable(data_wander,"data_wander.csv")
%}

toc
