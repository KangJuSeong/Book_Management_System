package com.example.libraryserver.domain.rental

import com.example.libraryserver.domain.book.Book
import com.example.libraryserver.domain.user.User
import com.linecorp.kotlinjdsl.querydsl.expression.column
import com.linecorp.kotlinjdsl.querydsl.from.fetch
import com.linecorp.kotlinjdsl.spring.data.SpringDataQueryFactory
import com.linecorp.kotlinjdsl.spring.data.listQuery
import com.linecorp.kotlinjdsl.spring.data.subquery
import org.springframework.data.jpa.repository.JpaRepository

interface RentalRepository: JpaRepository<Rental, Long>, RentalJdslRepository {

}

interface RentalJdslRepository {
    fun findJoinAll(): List<Rental>
    fun findJoinAll(id: Int): List<Rental>
}

class RentalJdslRepositoryImpl(
    private val queryFactory: SpringDataQueryFactory
): RentalJdslRepository {
    override fun findJoinAll(): List<Rental> {
        return queryFactory.listQuery<Rental> {
            select(entity(Rental::class))
            from(entity(Rental::class))
            fetch(Rental::book)
            fetch(Rental::user)
        }
    }

    override fun findJoinAll(id: Int): List<Rental> {
        return queryFactory.listQuery<Rental> {
            select(entity(Rental::class))
            from(entity(Rental::class))
            fetch(Rental::book)
            fetch(Rental::user)
            where(column(Book::id).equal(id.toLong()))
        }
    }
}