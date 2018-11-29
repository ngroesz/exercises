package com.groesz.resources;

import io.dropwizard.jersey.params.LongParam;
import com.codahale.metrics.Timer;
import com.codahale.metrics.MetricRegistry;
import java.util.Collections;
import java.util.Optional;
import java.util.Date;
import java.util.List;
import javax.ws.rs.*;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response;
import javax.ws.rs.WebApplicationException;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import com.groesz.core.User;
import com.groesz.core.UserRepository;

@Path("users")
@Produces(MediaType.APPLICATION_JSON)
public class UserResource
{
    MetricRegistry metrics;
    final Timer getUserResourceTimer;
    final Timer createUserResourceTimer;
    final Timer deleteUserResourceTimer;
    final Timer listUsersResourceTimer;
    final Timer updateUserResourceTimer;

    private UserRepository repository;
    protected final Logger logger = LoggerFactory.getLogger(getClass());

    public UserResource(UserRepository repository, MetricRegistry metrics)
    {
        this.repository = repository;
        this.metrics = metrics;

        this.getUserResourceTimer = metrics.timer("get-user-resource-timer");
        this.createUserResourceTimer = metrics.timer("create-user-resource-timer");
        this.deleteUserResourceTimer = metrics.timer("delete-user-resource-timer");
        this.listUsersResourceTimer = metrics.timer("list-users-resource-timer");
        this.updateUserResourceTimer = metrics.timer("update-user-resource-timer");
    }

    @GET
    public List<User> allUsers()
    {
        final Timer.Context context = listUsersResourceTimer.time();
        logger.info(String.format("Listing all users"));
        List<User> users = repository.findAll();
        context.stop();
        return users;
    }

    @GET
    @Path("{id}")
    public User user(@PathParam("id") LongParam id)
    {
        final Timer.Context context = getUserResourceTimer.time();
        logger.info(String.format("Returning user with id=%d", id.get()));
        Optional<User> user = repository.findById(id.get());
        context.stop();
        if (user.isPresent()) {
            return user.get();
        } else {
            throw new WebApplicationException(String.format("User id [%d] not found", id), 404);
        }
    }

    @POST
    public User create(User user)
    {
        final Timer.Context context = createUserResourceTimer.time();
        User new_user = new User(repository.idCounter.incrementAndGet(), user.getFirstName(), user.getLastName(), user.getZipcode(), user.getEmail());
        logger.info(
            String.format(
                "Creating user with id=%d, firstName=%s, lastName=%s, zipcode=%s, email=%s",
                new_user.getId(), new_user.getFirstName(), new_user.getLastName(), new_user.getZipcode(), new_user.getEmail()
            )
        );
        new_user = repository.save(new_user);
        context.stop();
        return new_user;
    }

    @PUT
    @Path("{id}")
    public User update(@PathParam("id") LongParam id, User user)
    {
        final Timer.Context context = updateUserResourceTimer.time();
        logger.info(
            String.format(
                "Updating user with id=%d, firstName=%s, lastName=%s, zipcode=%s, email=%s",
                user.getId(), user.getFirstName(), user.getLastName(), user.getZipcode(), user.getEmail()
            )
        );

        Optional<User> existing_user = repository.findById(id.get());
        if (existing_user.isPresent()) {
            User new_user = new User(id.get(), user.getFirstName(), user.getLastName(), user.getZipcode(), user.getEmail());
            new_user = repository.update(id.get(), new_user);
            context.stop();
            return new_user;
        } else {
            context.stop();
            throw new WebApplicationException(String.format("User id [%s] not found", id.get()), 404);
        }
    }

    @DELETE
    @Path("{id}")
    public Response delete(@PathParam("id") LongParam id)
    {
        final Timer.Context context = deleteUserResourceTimer.time();
        logger.info(String.format("Deleting user with id=%d", id.get()));
        repository.delete(id.get());
        context.stop();
        return Response.ok().build();
    }
}
