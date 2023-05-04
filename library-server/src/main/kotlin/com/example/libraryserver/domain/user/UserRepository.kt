package com.example.libraryserver.domain.user

import org.springframework.data.jpa.repository.JpaRepository

interface UserRepository: JpaRepository<User, Long> {
    fun findByEmailAndPassword(email: String, password: String): User?
}