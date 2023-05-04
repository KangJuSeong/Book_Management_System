package com.example.libraryserver.domain.rental

import com.example.libraryserver.domain.AuditEntity
import com.example.libraryserver.domain.book.Book
import com.example.libraryserver.domain.user.User
import jakarta.persistence.Column
import jakarta.persistence.FetchType
import jakarta.persistence.JoinColumn
import jakarta.persistence.OneToOne
import org.hibernate.annotations.OnDelete
import org.hibernate.annotations.OnDeleteAction
import java.time.LocalDateTime

class Rental(
    book: Book,
    user: User,
    rental: Boolean
): AuditEntity() {
    @OneToOne(targetEntity = Book::class, fetch = FetchType.EAGER)
    @JoinColumn(name = "book")
    @OnDelete(action = OnDeleteAction.CASCADE)
    var book: Book = book

    @OneToOne(targetEntity = User::class, fetch = FetchType.EAGER)
    @JoinColumn(name = "user")
    @OnDelete(action = OnDeleteAction.CASCADE)
    var user: User = user

    @Column(name = "rental")
    var rental: Boolean = rental

    override fun toString(): String =
        "Book : ${this.book.id}, User: ${this.user.id}, ${this.rental}"
}