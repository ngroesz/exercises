package com.groesz.core;
import com.codahale.metrics.Counter;
import com.codahale.metrics.MetricRegistry;
import java.util.ArrayList;
import java.util.Collection;
import java.util.concurrent.atomic.AtomicLong;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Optional;
import java.util.Set;

import com.groesz.core.User;

public class UserRepository
{
    MetricRegistry metrics;
    Counter userCounter;

    private Map<Long, User> users = new HashMap<Long, User>();
    public final AtomicLong idCounter = new AtomicLong();

    public UserRepository(MetricRegistry metrics)
    {
        this.metrics = metrics;
        userCounter = metrics.counter("user-counter");
    }

    public List<User> findAll()
    {
        return new ArrayList<User>(users.values());
    }

    public Optional<User> findById(Long id)
    {
        Optional<User> user = Optional.of(users.get(id));
        return user;
    }

    public User save(User user)
    {
        userCounter.inc();
        users.put(user.getId(), user);
        return user;
    }

    public User update(Long id, User user)
    {
        users.put(id, user);
        return user;
    }

    public void delete(Long id)
    {
        userCounter.dec();
        users.remove(id);
    }
}
