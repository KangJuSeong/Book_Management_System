package com.example.libraryserver.config

import com.example.libraryserver.domain.book.Book
import com.example.libraryserver.domain.book.BookDto
import com.example.libraryserver.domain.book.BookRepository
import com.example.libraryserver.domain.user.Role
import com.example.libraryserver.domain.user.User
import com.example.libraryserver.domain.user.UserDto
import com.example.libraryserver.domain.user.UserRepository
import io.github.serpro69.kfaker.faker
import mu.KotlinLogging
import org.springframework.boot.context.event.ApplicationReadyEvent
import org.springframework.context.annotation.Configuration
import org.springframework.context.event.EventListener


@Configuration
class Generator(
    private val userRepository: UserRepository,
    private val bookRepository: BookRepository
) {
    private val faker = faker {  }
    private val log = KotlinLogging.logger {  }

    @EventListener(ApplicationReadyEvent::class)
    private fun generateDummy() {
        var users = mutableListOf<User>()
        var books = mutableListOf<Book>()
        for (i in 1..10) {
            val user: User = generateUser()
            val book: Book = genrateBook()
            log.info { "Insert User(Dummy) : $user"}
            log.info { "Insert Book(Dummy) : $book"}
            users.add(user)
            books.add(book)
        }
        userRepository.saveAll(users)
        bookRepository.saveAll(books)
    }

    fun generateUser(): User =
        UserDto(
            name = faker.name.name(),
            address = faker.address.city(),
            phone = faker.phoneNumber.phoneNumber(),
            email = faker.internet.email(),
            password = "1234",
            role = Role.USER
        ).toEntity()

    fun genrateBook(): Book =
        BookDto(
            name = faker.book.title(),
            author = faker.book.author(),
            isbn = faker.barcode.isbn(),
            location = faker.code.asin()
        ).toEntity()
}