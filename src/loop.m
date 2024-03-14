
long = xlsread('1.xlsx','Sheet1','A2:A1646');
lat = xlsread('1.xlsx','Sheet1','B2:B1646');
AADT = xlsread('1.xlsx','Sheet1','D2:D1646');
AADTT = xlsread('1.xlsx','Sheet1','E2:E1646');

t1 = xlsread('1.xlsx','t1','B2:CR1646');
h_total = xlsread('1.xlsx','htotal','B2:CR1646');
t2 = xlsread('1.xlsx','t2','B2:CR1646');


results = zeros(1645,95);
M_app = zeros(1645,95);
h_app = zeros(1645,95);
salt_to_water_ratio = zeros(1645,95);
SD_totalCl = zeros(1645,95);
C_s_air_day = zeros(1645,95);
C_s_air = zeros(1645,95);

% Loop through each column
%for i = 1:95
    % M_app, the quantity of deicing salts applied on a roadway per day during the winter season
    % W_lane is the lane width in meter, take as 3.75
    % Salt_application_rate is taken as 0.07
    salt_application_rate = 0.07;
    W_lane = 3.75;
    M_app = salt_application_rate .* h_total ./ (W_lane*t1);

    % h_app, thickness of melted water per day with snow melting
    % h_total is in meter
    h_app = h_total /12 ./ t2;
    h_app = h_app / 100;

    % V_speed is taken as 100km/h
    % b is the tire width, taken as 0.56 m
    % K is the ratio of the tire width that is not a groove to the tire
    % width, taken as 0.75
    % h_film is the depth of the water film picked up in each rotation, 0.0001 m
    % water_density is 997 kg/M^3
    % MR stands for mass flow rate
    V_speed = 100/3.6;
    b = 0.56;
    K = 0.75;
    h_film = 0.0001;
    water_density = 997;
    MR_CA = V_speed.*b.*K.* h_film .* water_density;
    MR_TP = V_speed.*b.*(1-K).* h_app.* water_density;
    MR_BW = 0.5 .* V_speed.* b.*(h_app-(K.*h_film)-((1-K) .* h_app)).*water_density;
    MR_SW = 0.5 .* V_speed.* b.*(h_app-(K.*h_film)-((1-K) .* h_app)).*water_density;

    % SD stands for spray density
    % V is the speed limit in miles/hour, taken as 62?
    V = 62.1371;
    SD_CA = (-2.69.*10^(-5).*V + 2.43.*10^(-3)).*MR_CA;
    SD_TP = (1.16.*10^(-5).*V - 5.25.*10^(-5)).*MR_TP;
    SD_BW = (2.67.*10^(-5).*V - 4.71.*10^(-4)).*MR_BW;
    SD_SW = (1.65.*10^(-5).*V - 3.99.*10^(-4)).*MR_SW;

    SD_total = SD_CA + SD_TP + SD_BW + SD_SW;

    % mass of chloride ions by one truck
    % ratio of the mass of salt applied per unit area of road to the mass 
    % of water per unit area of road
    % chloride ratio = 0.61
    chloride_ratio = 0.61;
    salt_to_water_ratio = M_app./ (h_app .* water_density);
    SD_totalCl = SD_total .* salt_to_water_ratio .* chloride_ratio;


    % C_s_air: mass of chloride ions per unit air volume
    % light-duty vehicles ratio can be taken as 6
    % AADTT per lane
    ldv_ratio = 6;
    C_s_air_day = SD_totalCl ./ ldv_ratio .* (AADT-AADTT) + SD_totalCl .* AADTT;
    C_s_air = C_s_air_day .* t2;

    % chloride on bridge surface
    % d is the distance between road edge and bridge substructure, taken as
    % 3.5m
    d = 3.5;
    C_spray = C_s_air .* 0.015;
    C_splash = C_s_air .* 0.985;

    results = C_spray .* exp(-0.05*d) + C_splash .* exp(-0.5*d);

%end