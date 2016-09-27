from BeaconServer.function import *

admin_list=['add_caregiver',
            'create_carerecipient',
            'create_family_member',
            'create_doctor',
            'create_admin',
            'block_bad_giver',
            'edit_carerecipient_info'
    ]

action_map={
    'a':{'change_password':changePassword,
         'create_caregiver':createCareGiver,
         'create_carerecipient':createCareRecipient,
         'create_family_member':createFamilyMember,
         'create_doctor':createDoctor,
         'create_admin':createAdministrator,
         'block_bad_giver':blockBadGiver,
         'edit_carerecipient_info':editCareRecipientInfo,
         'view_care_giver':viewCareGiver
         },
    'g':{'change_password':changePassword,
         'accept_request':acceptRequest,
         'cancel_request':cancelRequest,
         'view_full_info':viewFullInfo,
         'view_request':viewRequest,
         'show_doctor_contact':showDoctorContact,
         'view_service_to_performe':viewServiceToPerform,
         'view_care_giver':viewCareGiver
        },
    'r':{'change_password':changePassword,
         'view_care_giver':viewCareGiver
         },
    'm':{'change_password':changePassword,
        },
    'd':{'change_password':changePassword
        }
    }