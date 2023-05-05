package com.example.libraryserver.domain.book

import com.linecorp.kotlinjdsl.query.spec.ExpressionOrderSpec
import com.linecorp.kotlinjdsl.query.spec.predicate.PredicateSpec
import com.linecorp.kotlinjdsl.querydsl.expression.column
import com.linecorp.kotlinjdsl.spring.data.SpringDataQueryFactory
import com.linecorp.kotlinjdsl.spring.data.listQuery
import org.springframework.data.jpa.repository.JpaRepository

interface BookRepository: JpaRepository<Book, Long>, BookJdslRepository {
}

interface BookJdslRepository {
    fun findBooks(keyword: String): List<Book>
}

class BookJdslRepositoryImpl(
    private val queryFactory: SpringDataQueryFactory
): BookJdslRepository {
    override fun findBooks(keyword: String): List<Book> {
        return queryFactory.listQuery<Book> {
            select(entity(Book::class))
            from(entity(Book::class))
            whereOr(
                column(Book::name).like(keyword),
                column(Book::author).like(keyword),
                column(Book::isbn).like(keyword)
            )
        }
    }
}