package com.groesz.core;

import com.fasterxml.jackson.annotation.JsonCreator;
import com.fasterxml.jackson.annotation.JsonProperty;
import org.hibernate.validator.constraints.NotEmpty;
import java.util.Date;
import java.util.Objects;
import javax.validation.constraints.NotNull;

public class User {
    @NotNull
    private Long id;
    @NotEmpty
    private String firstName = "";
    @NotEmpty
    private String lastName = "";
    @NotEmpty
    private String zipcode = "";
    @NotEmpty
    private String email = "";

    @JsonCreator
    public User(
        @JsonProperty("id") Long id,
        @JsonProperty("firstName") String firstName,
        @JsonProperty("lastName") String lastName,
        @JsonProperty("zipcode") String zipcode,
        @JsonProperty("email") String email)
    {
        this.id = id;
        this.firstName = firstName;
        this.lastName = lastName;
        this.zipcode = zipcode;
        this.email = email;
    }

    public User(User user)
    {
        this.id = user.id;
        this.firstName = user.firstName;
        this.lastName = user.lastName;
        this.zipcode = user.zipcode;
        this.email = user.email;
    }

    @JsonProperty("getId")
    public Long getId() {
        return id;
    }

    @JsonProperty("getFirstName")
    public String getFirstName() {
        return firstName;
    }

    @JsonProperty("getLastName")
    public String getLastName() {
        return lastName;
    }

    @JsonProperty("getZipcode")
    public String getZipcode() {
        return zipcode;
    }

    @JsonProperty("getEmail")
    public String getEmail() {
        return email;
    }

    public boolean equals(Object o)
    {
        if (o == this) return true;
        if (!(o instanceof User)) {
            return false;
        }
        User user = (User) o;
        return Objects.equals(firstName, user.firstName) &&
               Objects.equals(lastName, user.lastName) &&
               Objects.equals(zipcode, user.zipcode) &&
               Objects.equals(email, user.email);
    }

    @Override
    public int hashCode() {
        return Objects.hash(firstName, lastName, zipcode, email);
    }
}
