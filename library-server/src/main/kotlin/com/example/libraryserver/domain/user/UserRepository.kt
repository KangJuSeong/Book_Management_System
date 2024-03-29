package com.example.libraryserver.domain.user

import com.linecorp.kotlinjdsl.query.spec.ExpressionOrderSpec
import com.linecorp.kotlinjdsl.querydsl.expression.column
import com.linecorp.kotlinjdsl.spring.data.SpringDataQueryFactory
import com.linecorp.kotlinjdsl.spring.data.listQuery
import org.springframework.data.jpa.repository.JpaRepository

interface UserRepository: JpaRepository<User, Long>, UserJdslRepository {

    fun findByEmail(email: String): User?
    fun findByEmailAndPassword(email: String, password: String): User?
    fun findById(id: Int): User
}

interface UserJdslRepository {
    fun findUsers(keyword: String): List<User>
}

class UserJdslRepositoryImpl(
    private val queryFactory: SpringDataQueryFactory
): UserJdslRepository {
    override fun findUsers(keyword: String): List<User> {
        return queryFactory.listQuery<User> {
            select(entity(User::class))
            from(entity(User::class))
            whereOr(
                column(User::name).like(keyword),
                column(User::email).like(keyword),
                column(User::address).like(keyword),
                column(User::phone).like(keyword)
            )
        }
    }
}