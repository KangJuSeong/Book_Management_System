package com.example.libraryserver.domain.user

import com.example.libraryserver.domain.AuditEntity
import jakarta.persistence.*
import org.hibernate.annotations.Fetch


@Entity
@Table(name = "User")
class User(
    name: String,
    address: String,
    phone: String,
    email: String,
    role: Role,
    password: String
): AuditEntity() {
    @Column(name = "name")
    var name: String = name

    @Column(name = "address")
    var address: String = address

    @Column(name = "phone")
    var phone: String = phone

    @Column(name = "email")
    var email: String = email

    @Column(name = "password")
    var password: String = password

    @Column(name = "role")
    @Enumerated(EnumType.STRING)
    var role: Role = role

    override fun toString(): String =
        "${this.name}, ${this.address}, ${this.phone}, ${this.email}, ${this.password}, ${this.role}"

    fun toDto(): UserDto =
        UserDto(
            name = this.name,
            address = this.address,
            phone = this.phone,
            email = this.email,
            password = this.password,
            role = this.role
        )
    fun toResDto(): UserResDto =
        UserResDto(
            id = this.id!!,
            name = this.name,
            address = this.address,
            phone = this.phone,
            email = this.email,
            role = this.role
        )
}

enum class Role {
    USER,
    MANAGER
}
