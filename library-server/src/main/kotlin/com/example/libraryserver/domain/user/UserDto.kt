package com.example.libraryserver.domain.user

data class UserDto(
    val name: String,
    val address: String,
    val phone: String,
    val email: String,
    val role: Role,
    val password: String
) {
    fun toEntity(): User =
        User(
            name = this.name,
            address = this.address,
            phone = this.phone,
            email = this.email,
            role = this.role,
            password = this.password
        )
}

data class LoginDto(
    val email: String,
    val password: String
)
data class UserResDto(
    val id: Long,
    val name: String,
    val address: String,
    val phone: String,
    val email: String,
    val role: Role,
)