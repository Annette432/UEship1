import pygame
import random
FPS=60
WHITE = (255, 255, 255)
RED = (255,0,0)
ORANGE=(255,128,0)
BLACK=(0,0,0)
# Khởi tạo kích thước màn hình
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 525
# Khởi tạo kích thước bom, áo, nón, bình, dây đeo
bom_x=70
bom_y=70
ao_x=70
ao_y=70
non_x=70
non_y=70
binh_x=70
binh_y=70
day_x=70
day_y=70
# Khởi tạo tốc độ táo
bom_speed= 1
ao_speed= 1
non_speed= 1
binh_speed= 1
day_speed= 1
# Khởi tạo điểm số
score = 0
# Khởi tạo mạng để chơi
Lives=3
# Khởi tạo pygame
pygame.init()
# Khởi tạo âm thanh
pygame.mixer.init()
# Khởi tạo âm thanh khi hứng được item và khi hứng bom
dung= pygame.mixer.Sound("vacham.wav")
dung_bom= pygame.mixer.Sound("bom.wav")
# Thiết lập kích thước màn hình
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Hứng hàng")
# Nạp ảnh người chơi,items và bom
player_img = pygame.image.load("xe12.png")
ao_img = pygame.image.load("ao.png")
non_img = pygame.image.load("non.png")
binh_img = pygame.image.load("binh.png")
day_img = pygame.image.load("day.png")
bom_img = pygame.image.load("boom.png")
# Lấy kích thước của ảnh người chơi
player_width = player_img.get_width()
player_height = player_img.get_height()
# Vị trí ban đầu của người chơi
player_x = (SCREEN_WIDTH - player_width) // 2
player_y = SCREEN_HEIGHT - player_height
# Vị trí và tốc độ ban đầu của bom
Bom_x = random.randint(0, SCREEN_WIDTH - bom_x)
Bom_y = -bom_y
Bom_speed = bom_speed
# Vị trí và tốc độ ban đầu của áo
Ao_x = random.randint(0, SCREEN_WIDTH - ao_x)
Ao_y = -bom_y
Ao_speed = ao_speed
# Vị trí và tốc độ ban đầu của nón
Non_x = random.randint(0, SCREEN_WIDTH - non_x)
Non_y = -non_y
Non_speed = non_speed
# Vị trí và tốc độ ban đầu của bình
Binh_x = random.randint(0, SCREEN_WIDTH - binh_x)
Binh_y = -binh_y
Binh_speed = binh_speed
# Vị trí và tốc độ ban đầu của dây
Day_x = random.randint(0, SCREEN_WIDTH - day_x)
Day_y = -day_y
Day_speed = day_speed
# Nạp danh sách các background
backgrounds = ["ueh111.png", "ueh2.png", "ueh3.png","ueh4.png"]
# Tạo danh sách các hình ảnh nền
background_images = ["ueh111.png", "ueh2.png", "ueh3.png"]
backgrounds = [pygame.image.load(image).convert() for image in background_images]
# Vị trí ban đầu của nền
background_x = 0
# Chỉ số của hình ảnh nền hiện tại
background_index = 0
# Tạo một đối tượng Clock để giới hạn tốc độ khung hình
clock = pygame.time.Clock()
def game_over():
    global running
    font = pygame.font.Font(None, 72)
    text = font.render("Game Over", True, RED)
    text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, 100))
    screen.blit(text, text_rect)
    score_text = font.render("Score: " + str(score), True, WHITE)
    score_rect = score_text.get_rect(center=(SCREEN_WIDTH // 2, 150))
    screen.blit(score_text, score_rect)
    pygame.display.flip()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    pygame.quit()
                    
# Hàm hiển thị điểm số
def show_score():
    font = pygame.font.Font(None, 36)
    text = font.render("Score: " + str(score), True, WHITE)
    screen.blit(text, (10, 10))
# Hàm hiển thị số mạng chơi
def show_Lives():
    font = pygame.font.Font(None, 36)
    text = font.render("Live: " + str(Lives), True, BLACK)
    screen.blit(text, (500, 30))
# Hàm hiển thị người chơi, items và bom
def show_objects():
    screen.blit(bom_img, (Bom_x, Bom_y))
    screen.blit(player_img, (player_x, player_y))
    screen.blit(ao_img, (Ao_x, Ao_y))
    screen.blit(non_img, (Non_x, Non_y))
    screen.blit(binh_img, (Binh_x, Binh_y))
    screen.blit(day_img, (Day_x, Day_y))
# Hàm kiểm tra va chạm
def check_collision_ao():
    global score
    if Ao_y+ ao_y >= player_y and Ao_y + ao_y <= player_y + player_height:
        if Ao_x >= player_x and Ao_x <= player_x + player_width or \
           Ao_x + ao_x >= player_x and Ao_x + ao_x <= player_x + player_width:
            score += 1
            dung.play()
            reset_ao()
def check_collision_non():
    global score
    if Non_y+ non_y >= player_y and Non_y + non_y <= player_y + player_height:
        if Non_x >= player_x and Non_x <= player_x + player_width or \
           Non_x + non_x >= player_x and Non_x+ non_x <= player_x + player_width:
            score += 2
            dung.play()
            
            reset_non()
def check_collision_binh():
    global score
    if Binh_y + binh_y >= player_y and Binh_y + binh_y <= player_y + player_height:
        if Binh_x >= player_x and Binh_x <= player_x + player_width or \
           Binh_x + binh_x >= player_x and Binh_x + binh_x <= player_x + player_width:
            score += 1
            dung.play()
        
            reset_binh()
def check_collision_day():
    global score
    if Day_y + day_y >= player_y and Day_y + day_y <= player_y + player_height:
        if Day_x >= player_x and Day_x <= player_x + player_width or \
           Day_x + day_x >= player_x and Day_x + day_x <= player_x + player_width:
            score += 1
            dung.play()
            reset_day()
def check_collision_bom():
    global score
    global Lives
    if Bom_y + bom_y >= player_y and Bom_y + bom_y <= player_y + player_height:
        if Bom_x >= player_x and Bom_x <= player_x + player_width or \
           Bom_x + bom_x >= player_x and Bom_x + bom_x <= player_x + player_width:
            Lives-= 1
            dung_bom.play()
            reset_bom()
# Hàm reset áo
def reset_ao():
    global Ao_x,Ao_y,Ao_speed
    Ao_x = random.randint(0, SCREEN_WIDTH - ao_x)
    Ao_y = -ao_y
    Ao_speed += 0.5
    # Hàm reset nón
def reset_non():
    global Non_x,Non_y,Non_speed
    Non_x = random.randint(0, SCREEN_WIDTH - non_x)
    Non_y = -non_y
    Non_speed += 0.5
    # Hàm reset bình
def reset_binh():
    global Binh_x,Binh_y,Binh_speed
    Binh_x = random.randint(0, SCREEN_WIDTH - binh_x)
    Binh_y = -binh_y
    Binh_speed += 0.5
    # Hàm reset dây
def reset_day():
    global Day_x,Day_y,Day_speed
    Day_x = random.randint(0, SCREEN_WIDTH - day_x)
    Day_y = -Day_y
    Day_speed += 0.5
   # Hàm reset bom
def reset_bom():
    global Bom_x,Bom_y,Bom_speed
    Bom_x = random.randint(0, SCREEN_WIDTH - bom_x)
    Bom_y = -Bom_y
    Bom_speed += 0.25
# Hàm chuyển background
def change_background():
    global current_background, background_img
    current_background = (current_background + 1) % len(backgrounds)
    clock.tick(60)
# Vòng lặp chính của game
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    background_x -= 1
    # Kiểm tra xem nền đã di chuyển đủ xa chưa
    if background_x <= -backgrounds[background_index].get_width():
        # Tăng chỉ số của hình ảnh nền
        background_index = (background_index + 1) % len(backgrounds)
        background_x = 0


    # Vẽ nền lên màn hình
    screen.blit(backgrounds[background_index], (background_x, 0))
    screen.blit(backgrounds[background_index], (background_x + backgrounds[background_index].get_width(), 0))

    # Cập nhật màn hình
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= 5
    if keys[pygame.K_RIGHT]:
        player_x += 5
    Ao_y += Ao_speed
    Binh_y += Binh_speed
    Non_y += Non_speed
    Day_y += Day_speed
    Bom_y += Bom_speed
    if Ao_y > SCREEN_HEIGHT:
        reset_ao()
    if Non_y > SCREEN_HEIGHT:
        reset_non()
    if Binh_y > SCREEN_HEIGHT:
        reset_binh()
    if Day_y > SCREEN_HEIGHT:
        reset_day()
    if Bom_y > SCREEN_HEIGHT:
        reset_bom()
    check_collision_ao()
    check_collision_non()
    check_collision_binh()
    check_collision_day()
    check_collision_bom()
    show_objects()
    show_score()
    show_Lives()
    if Lives==0:
      game_over()
    pygame.display.flip()
    clock.tick(60)
pygame.quit()