import com.codahale.metrics.MetricRegistry;
import java.util.Optional;
import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.Test;
import java.util.concurrent.atomic.AtomicLong;

import org.assertj.core.api.Assertions;
import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertArrayEquals;
import static org.junit.jupiter.api.Assertions.assertTrue;

import com.groesz.core.User;
import com.groesz.core.UserRepository;

public class UserRepositoryTest
{
    private static MetricRegistry metrics;
    private static UserRepository repo;
    public final static AtomicLong idCounter = new AtomicLong();

    @BeforeAll
    static void initAll()
    {
        metrics = new MetricRegistry();
        repo = new UserRepository(metrics);
    }

    @Test
    void save()
    {
        final User user = new User(idCounter.incrementAndGet(), "Joe", "Smith", "97756", "joe.smith@gmail.com");

        final User saved_user = repo.save(user);

        Optional<User> fetched_user = repo.findById(saved_user.getId());

        assertEquals("Joe", saved_user.getFirstName());
        assertEquals("Smith", saved_user.getLastName());
        assertEquals("97756", saved_user.getZipcode());
        assertEquals("joe.smith@gmail.com", saved_user.getEmail());
    }

    @Test
    void findAll()
    {
        final User user_1 = new User(idCounter.incrementAndGet(), "Johnny", "Rotten", "12345", "johnny@sexpistols.com");
        repo.save(user_1);
        final User user_2 = new User(idCounter.incrementAndGet(), "Sid", "Vicious", "00000", "sid@sexpistols.com");
        repo.save(user_2);

        Assertions.assertThat(repo.findAll())
            .containsExactly(
                new User(idCounter.incrementAndGet(), "Johnny", "Rotten", "12345", "johnny@sexpistols.com"),
                new User(idCounter.incrementAndGet(), "Sid", "Vicious", "00000", "sid@sexpistols.com")
            );
    }

    @Test
    void update()
    {
        Long newId = idCounter.incrementAndGet();
        final User user_1 = new User(newId, "Johnny", "Rotten", "12345", "johnny@sexpistols.com");
        final User user_2 = new User(newId, "Sid", "Vicious", "12345", "sid@sexpistols.com");
        repo.update(newId, user_2);
        assertEquals(new User(newId, "Sid", "Vicious", "12345", "sid@sexpistols.com"), repo.findById(newId).get());
    }
}
