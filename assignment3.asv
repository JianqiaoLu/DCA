clear all;
global m n c R;
load net_util_data.mat;
[m,n] = size(R);
%  plot_homework('rdual')
%  plot_homework('eta')
plot_homework('uandl')

function []  = plot_homework(what_pic)
  if strcmp(what_pic,'eta')
      epsilon = 0.1;
      lambda = [0.5 ; .5];
      Prime_Dual_IPM(lambda,epsilon,what_pic)
  elseif strcmp(what_pic,'rdual')
      epsilon = 0.1;
      lambda = [.5 ; .5];
      Prime_Dual_IPM(lambda,epsilon,what_pic)
  elseif strcmp(what_pic,'uandl')
      get_U_vs_L();
  end
end

function [] = get_U_vs_L()
epsilon = 0.1;
lambda = [.5 ; .5];
figure = 'none';
U_plot = [];
L_plot = [];
for i = 1  : 4
    lambda(1) = i;
    lambda(2) = 5 - i;
    [U, L]  =  Prime_Dual_IPM(lambda,epsilon,figure);
    U_plot = [U_plot, U];
    L_plot = [L_plot, L];
end
plot( L_plot ,U_plot)
end

function [U, L] = Prime_Dual_IPM(lambda,epsilon,what_pic)
    global m n c R;
    f = ones( n,1)*0.01 ;
    L  = max( R'* ((c-R*f).^(-1)))+5;
    dual_variable =  -1./ inequality_constraint(f,L);
    beta = 0.5;
    alpha = 0.1;
    s_max = 1;
    mu = 10;
    eta_plot = [];
    r_dual_plot = [];
    while true
    eta = -inequality_constraint(f,L)' * dual_variable;
    eta_plot = [eta_plot;eta];
    t = mu* n /eta;
    direction  = get_search_direction(f,L,dual_variable,t,lambda);
    f_direction = direction(1:n);
    L_direction = direction(n+1);
    dual_variable_direction = direction( n+2:end);
    for j = 1 : n                                                    %lambda>=0
        if (dual_variable_direction(j) < 0) && (-dual_variable(j) / dual_variable_direction(j) < s_max)
            s_max = -dual_variable(j) /dual_variable_direction(j);
        end
    end
    s = s_max*0.99;
    while max(inequality_constraint(f + s *  f_direction , L + s *  L_direction )) > 0
            s = s * beta;
    end
    [old_r_d,  old_r_c] = get_residual(f,L,dual_variable,t,lambda);
    while true
        new_f = f + s*f_direction;
        new_L = L + s*L_direction;
        new_dual_variable = dual_variable + s * dual_variable_direction;
        [new_r_d,new_r_c] = get_residual(new_f,new_L,new_dual_variable,t,lambda);
        if norm([new_r_d; new_r_c])<= (1 - alpha * s)*norm([old_r_d;old_r_c] )
            f = new_f;
            L = new_L;
            dual_variable = new_dual_variable;
            break
        else
            s = s*beta;
        end
    end
    r_dual_plot =  [r_dual_plot;norm(new_r_d)];
    function_1 =inequality_constraint(f, L);
    eta = - function_1'* dual_variable;
    if norm(new_r_d)<= epsilon  && eta <= epsilon
        break
    end
    end 
    U = sum(log(f));
    if strcmp(what_pic,'eta')
        plot([1:1:length(eta_plot)],eta_plot);
    elseif strcmp(what_pic,'rdual')
        plot([1:1:length( r_dual_plot )], r_dual_plot );
    end

end

function [r_dual, r_cent] = get_residual(f,L ,dual_variable,t,lambda)
    global m n c R;
    gradient_0_part1 =  (f.^(-1)) ;
    gradient_0_part2 = 1;
    gradient_0  =  [-gradient_0_part1*lambda(1) ;gradient_0_part2*lambda(2) ] ;
    gradient_1 = total_gradient_fix(f);
    f_ix  =  inequality_constraint(f, L);
    r_dual = gradient_0 + gradient_1'*dual_variable;
    r_cent =   -diag(dual_variable)* f_ix  - (1/t)*ones(m+n+n,1);
end

function search_direction = get_search_direction(f,L,dual_variable,t,lambda)
    global m n c R;
    hessain_0  = diag([ lambda(1)*f.^(-2); 0]);
    gradient_1 = total_gradient_fix(f);
    hessain_1= zeros(n+1,n+1);
    for i = 1 : n 
      hessain_1 =  hessain_1 + dual_variable(i) * single_hessain_fix(f, i);
    end
    f_ix  =  inequality_constraint(f, L);
    linearize_matrix = [hessain_0 + hessain_1 , gradient_1'; -dual_variable.* gradient_1,  -diag(f_ix)];
    [r_dual, r_cent] = get_residual(f,L,dual_variable,t,lambda);
    search_direction =  linearize_matrix\ -[r_dual; r_cent];
end


function single_hessain_fix =single_hessain_fix(f, i)
global m n c R;
single_hessain_fix = zeros(n , n );
for edge = 1 : m
        edge_latency = c(edge) - R(edge, :) * f;
        single_hessain_fix  = single_hessain_fix  +R(edge, :)' * R(edge, :) * (2 * R(edge, i ) /edge_latency ^3 );
end
single_hessain_fix(n+1,n+1) =0 ;

end

function inequality_function_value = inequality_constraint(f, L)
global m n c R;
inequality_function_value  =  [R'* ((c-R*f).^(-1)) - L; -f; R*f-c ];
end


function gradient_1 = total_gradient_fix(f)
    global m n c R;
    gradient_1_part2 =zeros(n);
    for i = 1 : m
        edge_latency = c(i) -  R(i, :) * f;
        for j = 1 : n
            gradient_1_part2(j, : ) = gradient_1_part2(j, : ) + R(i, :) * (R(i, j) / edge_latency^2);
        end
    end
    aaa = 
    gradient_1 = [ gradient_1_part2;
                  -eye(n); 
                  R ] ;
    gradient_1(1:n,n+1) =  -ones(n, 1);
end

