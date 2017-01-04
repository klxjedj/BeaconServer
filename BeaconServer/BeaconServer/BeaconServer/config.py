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
         },
    'r':{'change_password':changePassword,
         'create_care_request':createCareRequest,
         'delete_requests':DeleteRequests,
         'view_available_care_givers':viewCareGivers
         },
    'g':{'change_password':changePassword,
         'view_all_request':viewRequests,
         'view_service_to_perform_today':viewRequestToday,
         'get_summarized_profile':viewProfile,
         'get_cancellations_left':getCancelLeft
        },

    'm':{'change_password':changePassword},
    'd':{'change_password':changePassword}
    }