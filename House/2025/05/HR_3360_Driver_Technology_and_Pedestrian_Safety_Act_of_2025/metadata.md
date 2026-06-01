# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3360?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3360
- Title: Driver Technology and Pedestrian Safety Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 3360
- Origin chamber: House
- Introduced date: 2025-05-13
- Update date: 2026-03-18T14:51:36Z
- Update date including text: 2026-03-18T14:51:36Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-05-13: Introduced in House
- 2025-05-13 - IntroReferral: Introduced in House
- 2025-05-13 - IntroReferral: Introduced in House
- 2025-05-13 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2025-05-13 - Committee: Referred to the Subcommittee on Commerce, Manufacturing, and Trade.
- 2026-02-10 - Committee: Forwarded by Subcommittee to Full Committee (Amended) by Voice Vote.
- 2026-02-10 - Committee: Subcommittee Consideration and Mark-up Session Held
- Latest action: 2025-05-13: Introduced in House

## Actions

- 2025-05-13 - IntroReferral: Introduced in House
- 2025-05-13 - IntroReferral: Introduced in House
- 2025-05-13 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2025-05-13 - Committee: Referred to the Subcommittee on Commerce, Manufacturing, and Trade.
- 2026-02-10 - Committee: Forwarded by Subcommittee to Full Committee (Amended) by Voice Vote.
- 2026-02-10 - Committee: Subcommittee Consideration and Mark-up Session Held

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-13",
    "latestAction": {
      "actionDate": "2025-05-13",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3360",
    "number": "3360",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "M001225",
        "district": "15",
        "firstName": "Kevin",
        "fullName": "Rep. Mullin, Kevin [D-CA-15]",
        "lastName": "Mullin",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Driver Technology and Pedestrian Safety Act of 2025",
    "type": "HR",
    "updateDate": "2026-03-18T14:51:36Z",
    "updateDateIncludingText": "2026-03-18T14:51:36Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-02-10",
      "committees": {
        "item": {
          "name": "Commerce, Manufacturing, and Trade Subcommittee",
          "systemCode": "hsif17"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Forwarded by Subcommittee to Full Committee (Amended) by Voice Vote.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-02-10",
      "committees": {
        "item": {
          "name": "Commerce, Manufacturing, and Trade Subcommittee",
          "systemCode": "hsif17"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Subcommittee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionDate": "2025-05-13",
      "committees": {
        "item": {
          "name": "Commerce, Manufacturing, and Trade Subcommittee",
          "systemCode": "hsif17"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Commerce, Manufacturing, and Trade.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-13",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-05-13",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-13",
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
          "date": "2025-05-13T16:06:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": [
              {
                "date": "2026-02-10T20:56:31Z",
                "name": "Reported by"
              },
              {
                "date": "2026-02-10T20:55:48Z",
                "name": "Markup by"
              },
              {
                "date": "2025-05-13T19:55:29Z",
                "name": "Referred to"
              }
            ]
          },
          "name": "Commerce, Manufacturing, and Trade Subcommittee",
          "systemCode": "hsif17"
        }
      },
      "systemCode": "hsif00",
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
      "bioguideId": "S001200",
      "district": "9",
      "firstName": "Darren",
      "fullName": "Rep. Soto, Darren [D-FL-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Soto",
      "party": "D",
      "sponsorshipDate": "2026-02-12",
      "state": "FL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3360ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3360\nIN THE HOUSE OF REPRESENTATIVES\nMay 13, 2025 Mr. Mullin introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo direct the Secretary of Transportation to conduct a study on the effect of driver-controlled technology in motor vehicles with respect to severe traffic injuries and traffic fatalities, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Driver Technology and Pedestrian Safety Act of 2025 .\n#### 2. Driver-controlled technology safety study\n##### (a) Driver-Controlled technology safety study agreement\nSubject to the availability of appropriations, not later than 3 months after the date of the enactment of this Act, the Secretary of Transportation shall seek to enter into an agreement with the National Academies of Sciences, Engineering, and Medicine\u2014\n**(1)**\nto conduct a study on the effect of driver-controlled technology with respect to severe traffic injuries and traffic fatalities, including severe injuries and fatalities of pedestrians, bicyclists, and other vulnerable road users; and\n**(2)**\nto prepare the recommendations described in section 3.\n##### (b) Period of time To be studied\nThe Secretary of Transportation shall determine the period of time to be studied under subsection (a), which shall be a period of time that began not later than 10 years before the date on which the Secretary enters into the agreement under subsection (a).\n##### (c) Information\nThe study described in subsection (a) shall address the following information:\n**(1)**\nThe prevalence and characteristics of touch screen-based systems.\n**(2)**\nThe impact on driver distraction, property damage, severe traffic injuries, and traffic fatalities as a result of the following:\n**(A)**\nReplacing tactile motor vehicle controls with touch screen-based systems.\n**(B)**\nThe characteristics of such systems, including brightness and size.\n**(C)**\nDriver-controlled technology that is not a touch screen-based system.\n**(3)**\nThe user interface designs of touch screen-based systems and other driver-controlled technology, and the effect of those designs on driver behavior.\n**(4)**\nA comparison of\u2014\n**(A)**\nthe extent to which viewing or manipulating a touch screen-based system while driving a motor vehicle results in a severe traffic injury or a traffic fatality; and\n**(B)**\nthe extent to which viewing or manipulating a smartphone, other than a smartphone that is projecting a user interface to a touch screen-based system, while driving a motor vehicle results in a severe traffic injury or a traffic fatality.\n**(5)**\nWhether the time of day and other road conditions, including traffic, weather, and the number of commercial motor vehicles on a road, have a significant effect on the incidence of severe traffic injuries and traffic fatalities, the extent of any effect, the likely reasons for any effect, whether any effect varies between the United States and other countries, and any changes to touch screen-based systems and other driver-controlled technology that may help mitigate any effect.\n**(6)**\nAny other information that is relevant to the study, which may include a previous study.\n#### 3. Report and recommendations\n##### (a) Report\nNot later than 24 months after the date on which the Secretary of Transportation enters into an agreement under section 2, the Secretary shall\u2014\n**(1)**\nsubmit to Congress a report that includes the findings of the study under section 2; and\n**(2)**\npublish the report on the public website of the Department of Transportation.\n##### (b) Recommendations\nNot later than 2 months after the date on which the Secretary of Transportation satisfies the requirements of subsection (a), the Secretary shall submit to Congress recommendations that are based on the findings of the study under section 2, including recommendations\u2014\n**(1)**\nto reduce severe traffic injuries and traffic fatalities; and\n**(2)**\nto change the Fatality Analysis Reporting System, the National Occupant Protection Use Surveys, and the Model Minimum Uniform Crash Criteria of the National Highway Traffic Safety Administration, or another set of Federal surveys, to collect as much data as practicable with respect to the use of a touch screen-based system while driving a motor vehicle and the use of a smartphone while driving a motor vehicle, given the variation in the methods of data collection by States and units of local government.\n##### (c) Categories\nIn submitting the recommendations described in subsection (b), the Secretary of Transportation\u2014\n**(1)**\nmay not include a recommendation that only restates an existing requirement for a department or agency of the Federal Government; and\n**(2)**\nshall divide the recommendations into the following categories:\n**(A)**\nAny recommendations that a department or agency of the Federal Government, including the National Highway Traffic Safety Administration, may implement under the existing authority of the department or agency, including any authority of the department or agency to develop or update guidance or standards on motor vehicle technology.\n**(B)**\nAny recommendations that would require the enactment of Federal law for a department or agency of the Federal Government, including the National Highway Traffic Safety Administration, to implement.\n#### 4. Definitions\nIn this Act:\n**(1) Commercial motor vehicle**\nThe term commercial motor vehicle means any of the following:\n**(A)**\nA commercial motor vehicle, as that term is defined under section 31132 of title 49, United States Code.\n**(B)**\nA vehicle owned or operated by a transportation network company, as that term is defined under section 346 of the National Defense Authorization Act for Fiscal Year 2017 ( Public Law 114\u2013328 ; 10 U.S.C. 113 note).\n**(2) Driver-controlled technology**\nThe term driver-controlled technology \u2014\n**(A)**\nmeans the controls and functions of a motor vehicle that are engaged at the option of a driver of the motor vehicle;\n**(B)**\nincludes the functions that are related to driving, are not related to the safe operation of the motor vehicle, and do not involve the use of a system that is required by law;\n**(C)**\nincludes a touch screen-based system; and\n**(D)**\ndoes not include any functions that are engaged by default as the motor vehicle is driven, such as automatic braking, cameras, and dynamic lighting.\n**(3) Motor vehicle**\nThe term motor vehicle means a passenger motor vehicle, as that term is defined under section 32101 of title 49, United States Code.\n**(4) Tactile motor vehicle control**\nThe term tactile motor vehicle control means a knob, a switch, a trackpad, or another physical control, that is in a motor vehicle and is not a touch screen.\n**(5) Touch screen-based system**\nThe term touch screen-based system means a computer that\u2014\n**(A)**\nis in a motor vehicle;\n**(B)**\ncontrols the functions of the motor vehicle, including the infotainment functions of the motor vehicle;\n**(C)**\nhas a primary user interface that consists of a touch screen and on-screen software controls;\n**(D)**\nmay be able to be manipulated by tactile motor vehicle controls; and\n**(E)**\nmay be able to display a user interface that is projected from a smartphone.\n#### 5. Rules of construction\n##### (a) Regulations\nThis Act shall not be construed to preclude or delay the promulgation of any regulation required or authorized by law.\n##### (b) Deference\nIf a court finds that a term used in this Act is ambiguous, the court shall defer to a reasonable interpretation of the term by the Secretary of Transportation.",
      "versionDate": "2025-05-13",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Computers and information technology",
            "updateDate": "2026-03-18T14:50:45Z"
          },
          {
            "name": "Consumer affairs",
            "updateDate": "2026-03-18T14:51:09Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2026-03-18T14:51:28Z"
          },
          {
            "name": "Government studies and investigations",
            "updateDate": "2026-03-18T14:51:18Z"
          },
          {
            "name": "Hybrid, electric, and advanced technology vehicles",
            "updateDate": "2026-03-18T14:50:25Z"
          },
          {
            "name": "Internet, web applications, social media",
            "updateDate": "2026-03-18T14:51:35Z"
          },
          {
            "name": "Motor vehicles",
            "updateDate": "2026-03-18T14:50:32Z"
          },
          {
            "name": "Product safety and quality",
            "updateDate": "2026-03-18T14:51:03Z"
          },
          {
            "name": "Roads and highways",
            "updateDate": "2026-03-18T14:50:58Z"
          },
          {
            "name": "Technology assessment",
            "updateDate": "2026-03-18T14:50:17Z"
          }
        ]
      },
      "policyArea": {
        "name": "Transportation and Public Works",
        "updateDate": "2025-05-27T15:28:09Z"
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
      "date": "2025-05-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3360ih.xml"
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
      "title": "Driver Technology and Pedestrian Safety Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-20T05:53:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Driver Technology and Pedestrian Safety Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-20T05:53:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Secretary of Transportation to conduct a study on the effect of driver-controlled technology in motor vehicles with respect to severe traffic injuries and traffic fatalities, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-20T05:48:40Z"
    }
  ]
}
```
