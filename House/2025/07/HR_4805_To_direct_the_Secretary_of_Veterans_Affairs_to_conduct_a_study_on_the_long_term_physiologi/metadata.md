# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4805?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4805
- Title: WINGS Act
- Congress: 119
- Bill type: HR
- Bill number: 4805
- Origin chamber: House
- Introduced date: 2025-07-29
- Update date: 2026-04-10T08:05:27Z
- Update date including text: 2026-04-10T08:05:27Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-07-29: Introduced in House
- 2025-07-29 - IntroReferral: Introduced in House
- 2025-07-29 - IntroReferral: Introduced in House
- 2025-07-29 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-10-22 - Committee: Referred to the Subcommittee on Health.
- Latest action: 2025-07-29: Introduced in House

## Actions

- 2025-07-29 - IntroReferral: Introduced in House
- 2025-07-29 - IntroReferral: Introduced in House
- 2025-07-29 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-10-22 - Committee: Referred to the Subcommittee on Health.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-29",
    "latestAction": {
      "actionDate": "2025-07-29",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4805",
    "number": "4805",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "K000399",
        "district": "2",
        "firstName": "Jennifer",
        "fullName": "Rep. Kiggans, Jennifer A. [R-VA-2]",
        "lastName": "Kiggans",
        "party": "R",
        "state": "VA"
      }
    ],
    "title": "WINGS Act",
    "type": "HR",
    "updateDate": "2026-04-10T08:05:27Z",
    "updateDateIncludingText": "2026-04-10T08:05:27Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-10-22",
      "committees": {
        "item": {
          "name": "Health Subcommittee",
          "systemCode": "hsvr03"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Health.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-29",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "hsvr00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Veterans' Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-07-29",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-29",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    }
  ]
}
```

## API Data: committees

```json
{
  "committees": [
    {
      "activities": {
        "item": {
          "date": "2025-07-29T21:01:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-10-22T15:48:00Z",
              "name": "Referred to"
            }
          },
          "name": "Health Subcommittee",
          "systemCode": "hsvr03"
        }
      },
      "systemCode": "hsvr00",
      "type": "Standing"
    }
  ]
}
```

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "G000604",
      "district": "2",
      "firstName": "Maggie",
      "fullName": "Rep. Goodlander, Maggie [D-NH-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Goodlander",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "NH"
    },
    {
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2025-08-05",
      "state": "NE"
    },
    {
      "bioguideId": "M001196",
      "district": "6",
      "firstName": "Seth",
      "fullName": "Rep. Moulton, Seth [D-MA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Moulton",
      "party": "D",
      "sponsorshipDate": "2025-08-05",
      "state": "MA"
    },
    {
      "bioguideId": "T000487",
      "district": "2",
      "firstName": "Jill",
      "fullName": "Rep. Tokuda, Jill N. [D-HI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Tokuda",
      "middleName": "N.",
      "party": "D",
      "sponsorshipDate": "2025-08-05",
      "state": "HI"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-08-15",
      "state": "VA"
    },
    {
      "bioguideId": "H001098",
      "district": "8",
      "firstName": "Abraham",
      "fullName": "Rep. Hamadeh, Abraham J. [R-AZ-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Hamadeh",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-09-03",
      "state": "AZ"
    },
    {
      "bioguideId": "M001216",
      "district": "7",
      "firstName": "Cory",
      "fullName": "Rep. Mills, Cory [R-FL-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Mills",
      "party": "R",
      "sponsorshipDate": "2025-10-24",
      "state": "FL"
    },
    {
      "bioguideId": "L000603",
      "district": "8",
      "firstName": "Morgan",
      "fullName": "Rep. Luttrell, Morgan [R-TX-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Luttrell",
      "party": "R",
      "sponsorshipDate": "2026-02-24",
      "state": "TX"
    },
    {
      "bioguideId": "P000048",
      "district": "11",
      "firstName": "August",
      "fullName": "Rep. Pfluger, August [R-TX-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Pfluger",
      "party": "R",
      "sponsorshipDate": "2026-02-24",
      "state": "TX"
    },
    {
      "bioguideId": "S001225",
      "district": "17",
      "firstName": "Eric",
      "fullName": "Rep. Sorensen, Eric [D-IL-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Sorensen",
      "party": "D",
      "sponsorshipDate": "2026-02-24",
      "state": "IL"
    },
    {
      "bioguideId": "L000598",
      "district": "1",
      "firstName": "Nick",
      "fullName": "Rep. LaLota, Nick [R-NY-1]",
      "isOriginalCosponsor": "False",
      "lastName": "LaLota",
      "party": "R",
      "sponsorshipDate": "2026-04-09",
      "state": "NY"
    }
  ]
}
```

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4805ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4805\nIN THE HOUSE OF REPRESENTATIVES\nJuly 29, 2025 Mrs. Kiggans of Virginia (for herself and Ms. Goodlander ) introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo direct the Secretary of Veterans Affairs to conduct a study on the long-term physiological and psychological effects of military aviation veterans who served as aviators in the Armed Forces, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Warrior Impact from Neurological and G-Force Stress Act or the WINGS Act .\n#### 2. Study on long-term effects of military flight operations on brain health and mental health\n##### (a) Study\nThe Secretary of Veterans Affairs shall conduct a comprehensive, longitudinal study to assess the long-term physiological and psychological effects of military aviation, including with respect to high-performance flight and G-force exposure, on military aviators.\n##### (b) Elements\nThe study under subsection (a) shall examine, at a minimum\u2014\n**(1)**\nthe relationship between cumulative flight hours and exposure to G-forces and incidents of traumatic brain injury, sub-concussive trauma, or cognitive impairment;\n**(2)**\nlong-term mental health outcomes, including with respect to incidence of depression, anxiety disorders, and post-traumatic stress disorder, in military aviators compared to other members of the Armed Forces;\n**(3)**\nthe correlation between aviation-related physiological stress and suicide risk among aviators;\n**(4)**\nthe prevalence of neurodegenerative conditions (including chronic traumatic encephalopathy, amyotrophic lateral sclerosis, and Parkinson\u2019s disease) in current and former military aviators;\n**(5)**\nthe effect of helmet design, oxygen systems, flight suit pressurization, and other cockpit environmental factors on neurocognitive health;\n**(6)**\ncurrent screening and diagnostic procedures used to detect early signs of neurological injury or psychological distress in military aviators; and\n**(7)**\nrecommended improvements in the monitoring, prevention, and treatment of aviation-related brain trauma and mental health challenges.\n##### (c) Consultation\nIn conducting the study under subsection (a), the Secretary shall consult with\u2014\n**(1)**\nthe Secretary of Defense;\n**(2)**\nthe Surgeons General of the military departments;\n**(3)**\nthe Director of the Defense Health Agency; and\n**(4)**\nrelevant academic institutions and federally funded research and development centers with expertise in aviation medicine, neuroscience, and psychiatry.\n##### (d) Pilot health registry\nThe Secretary of Veterans Affairs shall establish and maintain a centralized Military Aviator Neurohealth Registry that includes\u2014\n**(1)**\nanonymized health data of military aviators voluntarily participating in the study under subsection (a);\n**(2)**\nflight exposure metrics, including cumulative hours and G-force profiles;\n**(3)**\nrelevant health outcomes tracked over time; and\n**(4)**\na mechanism for longitudinal follow-up with the military aviators.\n##### (e) Reports\n**(1) Interim report**\nNot later than one year after the date of the enactment of this Act, the Secretary shall submit to Congress an interim report on the study under subsection (a), including any preliminary findings and recommendations.\n**(2) Final report**\nNot later than three years after the date of the enactment of this Act, the Secretary shall submit to Congress report on the study under subsection (a), including findings and recommendations.\n##### (f) Military aviator defined\nIn this section, the term military aviator means a veteran who, as a member of the Armed Forces, including a commissioned officer or a warrant officer\u2014\n**(1)**\nhad been designated as a pilot, naval aviator, or aircrew member by the Secretary of the military department concerned;\n**(2)**\noperated, or was regularly assigned as a flight crew member aboard, high-performance, crewed, fixed-wing or rotary-wing aircraft designed for tactical, training, or reconnaissance missions, including\u2014\n**(A)**\nfighter aircraft (such as the F\u201335, F/A\u201318, F\u201322, and F\u201316 aircraft);\n**(B)**\nattack aircraft (such as the A\u201310 and AH\u201364 aircraft);\n**(C)**\ntrainer jets (such as the T\u20137, T\u201338, and T\u201345 aircraft); and\n**(D)**\ntiltrotor or high-speed rotary aircraft (such as the V\u201322 aircraft);\n**(3)**\nwas subject to sustained or repeated G-forces during the routine execution of flight duties; and\n**(4)**\nserved in a role that may have included aircraft control, weapons employment, navigation, reconnaissance, or mission-specific operations requiring aircrew qualification and exposure to flight-related physiological stressors.",
      "versionDate": "2025-07-29",
      "versionType": "Introduced in House"
    }
  ]
}
```

## API Data: subjects

```json
{
  "subjects": [
    {
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-12-15T21:56:07Z"
      }
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-07-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4805ih.xml"
        }
      ],
      "type": "Introduced in House"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "WINGS Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-11T06:08:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "WINGS Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-11T06:08:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Warrior Impact from Neurological and G-Force Stress Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-11T06:08:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Secretary of Veterans Affairs to conduct a study on the long-term physiological and psychological effects of military aviation veterans who served as aviators in the Armed Forces, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-11T06:03:23Z"
    }
  ]
}
```
