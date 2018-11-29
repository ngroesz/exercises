package com.groesz;

import com.codahale.metrics.ConsoleReporter;
import com.codahale.metrics.MetricRegistry;
import io.dropwizard.Application;
import io.dropwizard.setup.Bootstrap;
import io.dropwizard.setup.Environment;
import java.util.concurrent.TimeUnit;

import com.groesz.core.UserRepository;
import com.groesz.resources.UserResource;


public class UsersApplication extends Application<UsersConfiguration>
{
    public static MetricRegistry metrics = new MetricRegistry();
    public static void main(final String[] args) throws Exception
    {
        new UsersApplication().run(args);
    }

    @Override
    public String getName()
    {
        return "Users";
    }

    @Override
    public void initialize(final Bootstrap<UsersConfiguration> bootstrap)
    {
    }

    @Override
    public void run(final UsersConfiguration configuration, final Environment environment)
    {
        final ConsoleReporter reporter = ConsoleReporter.forRegistry(metrics)
                                                .convertRatesTo(TimeUnit.SECONDS)
                                                .convertDurationsTo(TimeUnit.MILLISECONDS)
                                                .build();
        reporter.start(1, TimeUnit.MINUTES);

        UserRepository repository = new UserRepository(metrics);
        UserResource userResource = new UserResource(repository, metrics);
        environment.jersey().register(userResource);
    }
}
