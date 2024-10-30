# Fungsi Reusable untuk menemukan game berdasarkan nama
def find_game(game_name, games):
    return [game for game in games if game_name.lower() in game.get("name", game).lower()]


# Fungsi untuk Library
def display_library(user_profile):
    game_library = user_profile.get("game_library", {})
    return {game: status for game, status in game_library.items()}


def download_game(user_profile, game_name):
    game_library = user_profile.get("game_library", {})
    if game_name in game_library:
        if game_library[game_name] == "Not Installed":
            new_library = game_library.copy()
            new_library[game_name] = "Installed"
            user_profile["game_library"] = new_library
            return user_profile, f"{game_name} sedang diunduh..."
        return user_profile, f"{game_name} sudah terinstal."
    return user_profile, f"{game_name} tidak ada di Library Anda."


def search_library(user_profile, game_name):
    game_library = user_profile.get("game_library", {})
    results = find_game(game_name, game_library.keys())
    return {game: game_library[game] for game in results} if results else "Game tidak ditemukan dalam Library Anda."


# Fungsi untuk Store
def search_store(store_games, game_name):
    results = find_game(game_name, store_games)
    return [{game["name"]: game["price"]} for game in results] if results else "Game tidak ditemukan di Store."


def add_to_wishlist(user_profile, game_name):
    new_profile = user_profile.copy()
    new_profile["wishlist"].append(game_name)
    return new_profile, f"{game_name} berhasil ditambahkan ke wishlist."


def purchase_game(user_profile, store_games, game_name):
    game_library = user_profile.get("game_library", {})
    if any(game["name"].lower() == game_name.lower() for game in store_games):
        new_library = game_library.copy()
        new_library[game_name] = "Not Installed"
        user_profile["game_library"] = new_library
        return user_profile, f"{game_name} berhasil dibeli dan ditambahkan ke Library!"
    return user_profile, "Game tidak tersedia di Store."


# Fungsi untuk Social Hub
def view_friends(friend_list):
    return friend_list


def send_message(friend_list, friend_name, message):
    if friend_name in friend_list:
        return f"Pesan terkirim ke {friend_name}: {message}"
    return f"{friend_name} tidak ditemukan dalam daftar teman."


def invite_friend(friend_list, friend_name):
    if friend_name in friend_list:
        return f"Undangan terkirim ke {friend_name} untuk bermain."
    return f"{friend_name} tidak ditemukan dalam daftar teman."


# Fungsi untuk Account Management
def view_profile(user_profile):
    return {
        "Username": user_profile["username"],
        "Wishlist": user_profile["wishlist"],
        "Privacy": user_profile.get("privacy", "Public"),
        "Game Library": user_profile.get("game_library", {})
    }


def edit_username(user_profile, new_username):
    new_profile = user_profile.copy()
    new_profile["username"] = new_username
    return new_profile, f"Username berhasil diubah menjadi {new_username}."


def change_privacy(user_profile, setting):
    if setting in ["Public", "Private"]:
        new_profile = user_profile.copy()
        new_profile["privacy"] = setting
        return new_profile, f"Pengaturan privasi diubah menjadi {setting}."
    return user_profile, "Pengaturan privasi tidak valid."


# Fungsi untuk Game Recommendations
def recommend_games_by_genre(store_games, genre):
    return [game for game in store_games if game.get("genre", "").lower() == genre.lower()]


def recommend_popular_games(store_games):
    return [game for game in store_games if game["price"] == 0.00]


def recommend_friends_favorite_games(friend_list, user_profile):
    # Misalkan kita punya daftar game favorit teman (simulasi)
    friends_favorites = {
        "Player1": "Fortnite",
        "Player2": "The Witcher 3",
        "Player3": "Cyberpunk 2077"
    }
    recommended_games = []
    for friend in friend_list:
        favorite = friends_favorites.get(friend)
        if favorite:
            recommended_games.append(favorite)
    return list(set(recommended_games))


# Main menu and feature menus
def library_menu(user_profile):
    while True:
        print("\n=== Library Menu ===")
        print("1. Tampilkan Daftar Game")
        print("2. Unduh Game")
        print("3. Cari Game")
        print("4. Kembali ke Menu Utama")

        choice = input("Pilih opsi: ")
        if choice == "1":
            library = display_library(user_profile)
            print("=== Library Anda ===")
            for game, status in library.items():
                print(f"- {game} : {status}")
        elif choice == "2":
            game_name = input("Masukkan nama game yang ingin diunduh: ")
            user_profile, message = download_game(user_profile, game_name)
            print(message)
        elif choice == "3":
            game_name = input("Masukkan nama game yang ingin dicari: ")
            results = search_library(user_profile, game_name)
            if isinstance(results, dict):
                print("Game ditemukan dalam Library:")
                for game, status in results.items():
                    print(f"- {game}: {status}")
            else:
                print(results)
        elif choice == "4":
            print("Kembali ke Menu Utama.")
            break
        else:
            print("Opsi tidak valid.")

    return user_profile


def store_menu(user_profile, store_games):
    while True:
        print("\n=== Store Menu ===")
        print("1. Cari Game")
        print("2. Tambahkan ke Wishlist")
        print("3. Beli Game")
        print("4. Kembali ke Menu Utama")

        choice = input("Pilih opsi: ")
        if choice == "1":
            game_name = input("Masukkan nama game: ")
            results = search_store(store_games, game_name)
            if isinstance(results, list):
                print("Game ditemukan dalam Store:")
                for game in results:
                    for name, price in game.items():
                        print(f"- {name}: ${price}")
            else:
                print(results)
        elif choice == "2":
            game_name = input("Masukkan nama game untuk wishlist: ")
            user_profile, message = add_to_wishlist(user_profile, game_name)
            print(message)
        elif choice == "3":
            game_name = input("Masukkan nama game yang ingin dibeli: ")
            user_profile, message = purchase_game(user_profile, store_games, game_name)
            print(message)
        elif choice == "4":
            print("Kembali ke Menu Utama.")
            break
        else:
            print("Opsi tidak valid.")

    return user_profile


def social_hub_menu(friend_list):
    while True:
        print("\n=== Social Hub Menu ===")
        print("1. Lihat Daftar Teman")
        print("2. Kirim Pesan")
        print("3. Undang Teman")
        print("4. Kembali ke Menu Utama")

        choice = input("Pilih opsi: ")
        if choice == "1":
            friends = view_friends(friend_list)
            print("Daftar Teman:")
            for friend in friends:
                print(f"- {friend}")
        elif choice == "2":
            friend_name = input("Masukkan nama teman: ")
            message = input("Tulis pesan: ")
            response = send_message(friend_list, friend_name, message)
            print(response)
        elif choice == "3":
            friend_name = input("Masukkan nama teman untuk diundang: ")
            response = invite_friend(friend_list, friend_name)
            print(response)
        elif choice == "4":
            print("Kembali ke Menu Utama.")
            break
        else:
            print("Opsi tidak valid.")

    return friend_list


def account_management_menu(user_profile):
    while True:
        print("\n=== Account Management Menu ===")
        print("1. Lihat Profil")
        print("2. Edit Username")
        print("3. Ubah Pengaturan Privasi")
        print("4. Kembali ke Menu Utama")

        choice = input("Pilih opsi: ")
        if choice == "1":
            profile_info = view_profile(user_profile)
            print("=== Profil Anda ===")
            for key, value in profile_info.items():
                print(f"{key}: {value}")
        elif choice == "2":
            new_username = input("Masukkan username baru: ")
            user_profile, message = edit_username(user_profile, new_username)
            print(message)
        elif choice == "3":
            setting = input("Masukkan pengaturan privasi (Public/Private): ")
            user_profile, message = change_privacy(user_profile, setting)
            print(message)
        elif choice == "4":
            print("Kembali ke Menu Utama.")
            break
        else:
            print("Opsi tidak valid.")

    return user_profile


def recommendation_menu(store_games, friend_list, user_profile):
    while True:
        print("\n=== Recommendations Menu ===")
        print("1. Rekomendasi Game berdasarkan Genre")
        print("2. Rekomendasi Game Populer")
        print("3. Rekomendasi Game Favorit Teman")
        print("4. Kembali ke Menu Utama")

        choice = input("Pilih opsi: ")
        if choice == "1":
            genre = input("Masukkan genre game: ")
            recommendations = recommend_games_by_genre(store_games, genre)
            if recommendations:
                print("Rekomendasi Game berdasarkan Genre:")
                for game in recommendations:
                    print(f"- {game['name']} (${game['price']})")
            else:
                print("Tidak ada game yang cocok dengan genre tersebut.")
        elif choice == "2":
            recommendations = recommend_popular_games(store_games)
            if recommendations:
                print("Rekomendasi Game Populer:")
                for game in recommendations:
                    print(f"- {game['name']} (${game['price']})")
            else:
                print("Tidak ada game populer.")
        elif choice == "3":
            recommendations = recommend_friends_favorite_games(friend_list, user_profile)
            if recommendations:
                print("Rekomendasi Game Favorit Teman:")
                for game in recommendations:
                    print(f"- {game}")
            else:
                print("Tidak ada rekomendasi dari teman.")
        elif choice == "4":
            print("Kembali ke Menu Utama.")
            break
        else:
            print("Opsi tidak valid.")


def main():
    user_profile = {
        "username": "Gamer123",
        "wishlist": [],
        "game_library": {
            "Fortnite": "Installed",
            "Cyberpunk 2077": "Not Installed"
        },
        "privacy": "Public"
    }
    store_games = [
        {"name": "Fortnite", "price": 0.00, "genre": "Battle Royale"},
        {"name": "Cyberpunk 2077", "price": 29.99, "genre": "RPG"},
        {"name": "The Witcher 3", "price": 39.99, "genre": "RPG"},
        {"name": "Among Us", "price": 4.99, "genre": "Party"},
    ]
    friend_list = ["Player1", "Player2", "Player3"]

    while True:
        print("\n=== Epic Games Store Menu ===")
        print("1. Library")
        print("2. Store")
        print("3. Social Hub")
        print("4. Account Management")
        print("5. Recommendations")
        print("6. Keluar")

        choice = input("Pilih opsi: ")
        if choice == "1":
            user_profile = library_menu(user_profile)
        elif choice == "2":
            user_profile = store_menu(user_profile, store_games)
        elif choice == "3":
            social_hub_menu(friend_list)
        elif choice == "4":
            user_profile = account_management_menu(user_profile)
        elif choice == "5":
            recommendation_menu(store_games, friend_list, user_profile)
        elif choice == "6":
            print("Keluar dari aplikasi.")
            break
        else:
            print("Opsi tidak valid.")


if __name__ == "__main__":
    main()
