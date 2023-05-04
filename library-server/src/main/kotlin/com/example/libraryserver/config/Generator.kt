package com.example.libraryserver.config

import com.example.libraryserver.domain.user.Role
import com.example.libraryserver.domain.user.User
import com.example.libraryserver.domain.user.UserRepository
import io.github.serpro69.kfaker.faker
import org.springframework.boot.context.event.ApplicationReadyEvent
import org.springframework.context.annotation.Configuration
import org.springframework.context.event.EventListener


@Configuration
class Generator(
    private val userRepository: UserRepository
) {
    private val faker = faker {  }

    @EventListener(ApplicationReadyEvent::class)
    private fun generateDummy() {
        User(
            name = faker.name.name(),
            address = faker.address.city(),
            phone = faker.phoneNumber.phoneNumber(),
            email = faker.internet.email(),
            role = Role.MANAGER,
            password = faker.internet.slug(),
        ).apply {
            userRepository.save(this)
        }
    }
}