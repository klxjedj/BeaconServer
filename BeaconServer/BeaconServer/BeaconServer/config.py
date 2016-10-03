from BeaconServer.function import *

admin_list = ['add_caregiver',
            'create_carerecipient',
            'create_family_member',
            'create_doctor',
            'create_admin',
            'block_bad_giver',
            'edit_carerecipient_info']

action_map = {
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
         'edit_care_giver_info':editCareGiverInfo,
         'accept_request':acceptRequest,
         'cancel_request':cancelRequest,
         'view_full_info':viewFullInfo,
         'view_all_request':viewAllRequest,
         'show_doctor_contact':showDoctorContact,
         'view_service_to_performe':viewServiceToPerform,
         'view_care_giver':viewCareGiver,
         'view_care_giver_by_id':viewCareGiverById,
         'save_service_summary':saveServiceSummary,
         'get_summarized_profile':getSummarisedProfile, 
         'view_restricted_carerecipient_info':viewRestrictedCareRecipientInfo,
         'api_login':apiLogin
        },
    'r':{'change_password':changePassword,
         'create_care_request':createCareRequest,
         'rate_review_care_service':rateReviewCareService,
          'view_available_care_givers':viewAvailableCareGivers,
          'view_care_giver_by_id':viewCareGiverById,
         'edit_care_recipient_info':editCareRecipientInfo,
         'api_login':apiLogin
         },
    'm':{'change_password':changePassword},
    'd':{'change_password':changePassword}
    }