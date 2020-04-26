```mermaid
gantt
    title Gantt Chart: A Project Plan

    dateFormat  YYYY-MM-DD

    section Milestone-2_Expected
    Milestone-2_due (5d)                : m1, 2020-04-14, 5d
    Setup Flask (1d)                    : setup, 2020-04-14, 1d
    Setup README (1d)                   : 2020-04-14, 1d

    Setup User Schema : 2020-04-14, 1d
    Home Page - Frontend (1d)           : home, after setup, 1d
    Login Page - Frontend (1d)          : log, after setup, 1d
    Logout Page - Frontend (1d)         : log, after setup, 1d
    Register Page - Frontend (1d)       : register, after setup, 1d

    Login Page - Functionality (2d)     : after log, 2d
    Logout Page - Functionality (2d)    : after log, 2d
    Register Page - Functionality (2d)  : after register, 2d

    Sphinx Documentation (2d)           : 2020-04-17, 2d



    section Milestone-2_Actual
    Milestone-2_due (5d)                : done, 2020-04-14, 5d
    Setup Flask (1d)                    : done, setup, 2020-04-14, 1d
    Setup README (1d)                   : done, 2020-04-14, 1d

    Setup User Schema (1d)              : done, 2020-04-14, 1d
    Home Page - Frontend (1d)           : done, home, after setup, 1d
    Login Page - Frontend (1d)          : done, log, after setup, 1d
    Logout Page - Frontend (1d)         : done, log, after setup, 1d
    Register Page - Frontend (1d)       : done, register, after setup, 1d

    Login Page - Functionality (2d)     : done, after log, 2d
    Logout Page - Functionality (2d)    : done, after log, 2d
    Register Page - Functionality (2d)  : done, after register, 2d

    Sphinx Documentation (2d)           : done, 2020-04-17, 2d



    section Milestone-3_Expected
    Milestone-3_due (11d - 4/22 ~ 5/03)                     : 2020-04-22, 11d
    Event Schema (9d)                                       : stage1, 2020-04-24, 1d
    Setting Page - Frontend (1d)                            : 2020-04-27, 6d

    Delete Account - Functionality (1d)                     : after stage1, 1d
    Set Appointment Availability - Functionality (3d)       : stage2, after stage1, 3d
    Email Confirmation - Functionality (3d)                 : after stage1, 3d

    Guess Page Calendar (5d)                                : after stage2, 5d
    Meeting Page (A.K.A. Home Page) (5d)                    : after stage2, 5d

    README Documentation (2d)                               : 2020-05-01, 2d
    Sphinx Documentation (2d)                               : 2020-05-01, 2d
```
