package com.example.libraryserver.service

import com.example.libraryserver.domain.user.User
import com.example.libraryserver.domain.user.UserDto
import com.example.libraryserver.domain.user.UserRepository
import org.springframework.stereotype.Service
import java.util.NoSuchElementException


@Service
class UserService(
    private val userRepository: UserRepository
) {
    fun findAll(): MutableList<User> = userRepository.findAll()
    fun login(email: String, password: String): UserDto? {
        return userRepository.findByEmailAndPassword(email, password)?.toDto()
    }
}