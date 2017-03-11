function twiddle()

    p = 1;
    dp = 1;
    best_error = (p-4)^2;
    figure;
    x = linspace(0,8,100);
    y = (x-4).^2;
    plot(x,y);
    axis([0 8 -2 16]);
    hold;
    c = 0;
    while (1),
        p = p + dp;
        error = (p-4)^2;
        if(error < best_error)
            best_error = error;
            dp = dp * 1.1;
            c=1;
        else
            p = p - 2 * dp;
            error = (p-4)^2;
            if(error < best_error)
                best_error = error;
                dp = dp * 1.1;
                c=2;
            else
                p = p + dp;
                dp = dp * .9;
                c=3;
            end
        end
        plot(p,(p-4)^2,'r*');
        fprintf(1,'p=%f, dp=%f, case: %d', p, dp, c);
        fprintf(1,'\n');
        pause;
    end
end