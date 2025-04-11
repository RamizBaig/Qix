Requirements:
    Python 3.7+
    Pygame 2.x
    
Introduction:
    Welcome to mQIX, our modern implementation of the classic Qix arcade game. 
    In this 2D single-player experience, you navigate the perimeter of a square board, 
    incise into unclaimed territory, and dodge two types of enemies—Sparx 
    and the unpredictable Qix—to claim as much of the board as possible.

Controls:
    Inside menu:
        Use Arrow keys or WASD to navigate
        Spacebar or enter to Select
    
    Inside Game:
        Use Arrow keys or WASD to move
        Press Spacebar and a direction to initiate incursion
        Hold Spacebar during an incursion to trigger slow incursion for bonus points
        Esc / P to Pause the game or open the pause menu.

    Pause menu:
        Press Enter to view help menu
        press Spacebar to return to game

Difficulties:
    Easy: Must claim 65%
    Medium: Must claim 75%
    Hard: Must claim 85%

Levels: 
    Qix gradually becomes faster as levels increases.
    At about level 50, where the qix is almost impossible to avoid.
    This incentives large claims for attempting very high scores.

Enemies:
    Sparx:
        Move randomly along the board edges.
        Contact with the player on the edge costs one life.
        A pixel buffer allows near‑miss moments for extra thrill.
        On death, the player respawns at the last start point.
        New Sparx spawn away from the player and can path‑find out of any trapped claimed areas.

    Qix:
        Roams the interior of unclaimed territory with random size, rotation, and velocity.
        If Qix touches your in-progress line, you lose a life and the board resets.
        The player is invulnerable to Qix when moving along claimed edges.

Extra Features:
    Dynamic Difficulty: Qix speed and Sparx spawn rate increase with each level.
    Pause & Help: Press Esc or P to pause; H to view help at any time.
    Persistent High Scores: Tracks top scores per difficulty; stored locally and never cleared unless manually deleted.
    Seamless Replay: After game over or victory, you can restart within the same session without crashes.


If you wish to report any bugs, I can be reached at:
ramiz.baig@torontomu.ca