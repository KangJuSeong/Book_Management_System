package com.example.libraryserver.config

import com.example.libraryserver.domain.book.Book
import com.example.libraryserver.domain.book.BookDto
import com.example.libraryserver.domain.book.BookRepository
import com.example.libraryserver.domain.rental.Rental
import com.example.libraryserver.domain.rental.RentalDto
import com.example.libraryserver.domain.rental.RentalRepository
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
    private val bookRepository: BookRepository,
    private val rentalRepository: RentalRepository
) {
    private val faker = faker {  }
    private val log = KotlinLogging.logger {  }

    @EventListener(ApplicationReadyEvent::class)
    private fun generateDummy() {
        var cnt: Int = 10
        var users = generateUsers(cnt)
        var books = generateBooks(cnt)
        var rentals = generateRentals(cnt, books, users)
        userRepository.saveAll(users)
        bookRepository.saveAll(books)
        rentalRepository.saveAll(rentals)
    }

    fun generateUsers(cnt: Int): MutableList<User> {
        var users = mutableListOf<User>()

        for (i in 1..cnt) {
            val user = generateUser()
            log.info { "Insert User(Dummy) : $user"}
            users.add(user)
        }
        return users
    }

    fun generateBooks(cnt: Int): MutableList<Book> {
        var books = mutableListOf<Book>()

        for (i in 1..cnt) {
            val book: Book = generateBook()
            log.info { "Insert Book(Dummy) : $book"}
            books.add(book)
        }
        return books
    }

    fun generateRentals(cnt: Int, books: MutableList<Book>, users: MutableList<User>): MutableList<Rental> {
        var rentals = mutableListOf<Rental>()

        for (i in 0..cnt / 2) {
            books[i].isRental = true
            val rental: Rental = generateRental(books[i], users[i])
            log.info { "Insert Rental(Dummy): $rental"}
            rentals.add(rental)
        }
        return rentals
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

    fun generateBook(): Book =
        BookDto(
            name = faker.book.title(),
            author = faker.book.author(),
            isbn = faker.barcode.isbn(),
            isRental = false,
            location = faker.code.asin()
        ).toEntity()

    fun generateRental(book: Book, user: User): Rental =
        RentalDto(
            book = book,
            user = user,
            rental = true
        ).toEntity()
}