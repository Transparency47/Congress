# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5203?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5203
- Title: To direct the Secretary of Veterans Affairs to update directives of the Department of Veterans Affairs regarding the management of acute sexual assault, and for other purposes.
- Congress: 119
- Bill type: HR
- Bill number: 5203
- Origin chamber: House
- Introduced date: 2025-09-08
- Update date: 2026-05-21T08:07:51Z
- Update date including text: 2026-05-21T08:07:51Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-09-08: Introduced in House
- 2025-09-08 - IntroReferral: Introduced in House
- 2025-09-08 - IntroReferral: Introduced in House
- 2025-09-08 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-12-19 - Committee: Referred to the Subcommittee on Health.
- 2026-03-18 - Committee: Committee Hearings Held
- 2026-03-18 - Committee: Subcommittee on Health Discharged
- 2026-05-20 - Committee: Committee Hearings Held
- Latest action: 2025-09-08: Introduced in House

## Actions

- 2025-09-08 - IntroReferral: Introduced in House
- 2025-09-08 - IntroReferral: Introduced in House
- 2025-09-08 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-12-19 - Committee: Referred to the Subcommittee on Health.
- 2026-03-18 - Committee: Committee Hearings Held
- 2026-03-18 - Committee: Subcommittee on Health Discharged
- 2026-05-20 - Committee: Committee Hearings Held

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-08",
    "latestAction": {
      "actionDate": "2025-09-08",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5203",
    "number": "5203",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "M001234",
        "district": "3",
        "firstName": "Kelly",
        "fullName": "Rep. Morrison, Kelly [D-MN-3]",
        "lastName": "Morrison",
        "party": "D",
        "state": "MN"
      }
    ],
    "title": "To direct the Secretary of Veterans Affairs to update directives of the Department of Veterans Affairs regarding the management of acute sexual assault, and for other purposes.",
    "type": "HR",
    "updateDate": "2026-05-21T08:07:51Z",
    "updateDateIncludingText": "2026-05-21T08:07:51Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-05-20",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "hsvr00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Committee Hearings Held",
      "type": "Committee"
    },
    {
      "actionDate": "2026-03-18",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "hsvr00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Committee Hearings Held",
      "type": "Committee"
    },
    {
      "actionDate": "2026-03-18",
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
      "text": "Subcommittee on Health Discharged",
      "type": "Committee"
    },
    {
      "actionDate": "2025-12-19",
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
      "actionDate": "2025-09-08",
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
      "actionDate": "2025-09-08",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-08",
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
        "item": [
          {
            "date": "2026-05-20T13:27:25Z",
            "name": "Hearings By (full committee)"
          },
          {
            "date": "2026-03-18T16:54:38Z",
            "name": "Hearings By (full committee)"
          },
          {
            "date": "2025-09-08T16:05:10Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": [
              {
                "date": "2026-03-18T16:54:32Z",
                "name": "Discharged from"
              },
              {
                "date": "2025-12-19T19:11:05Z",
                "name": "Referred to"
              }
            ]
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5203ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5203\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 8, 2025 Ms. Morrison introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo direct the Secretary of Veterans Affairs to update directives of the Department of Veterans Affairs regarding the management of acute sexual assault, and for other purposes.\n#### 1. Directives regarding the management of acute sexual assault in the Department of Veterans Affairs\n##### (a) Update\nNot later than 18 months after the date of the enactment of this Act, the Secretary of Veterans Affairs shall update directives of the Department of Veterans Affairs regarding emergency management of an acute sexual assault of a covered veteran, and ensure that the policies, of each medical facility, and of police, of the Department conform to such directive. Elements of such directives and policies shall include the following:\n**(1)**\nUpdated policies and guidance for all employees of the Department of Veterans Affairs who respond to covered veterans.\n**(2)**\nA requirement that the director of a medical facility of the Department\u2014\n**(A)**\nemploys a certified SAFE clinical provider or a SANE certified through curricula such as those developed by the International Association of Forensic Nurses;\n**(B)**\nrefers, pursuant to section 1703 of title 38, United States Code, covered veterans to a local non-Department health care provider that employs a certified SAFE clinical provider or a SANE; or\n**(C)**\ncoordinates with the Under Secretary for Health and the Director of the Veteran Integrated Service Network concerned regarding alternate plans of care for covered veterans at such facility.\n**(3)**\nRequirements in the emergency medicine and urgent care directives of the Veterans Health Administration that a medical facility of the Department that employs a certified SAFE clinical provider or a SANE maintains a supply of unexpired rape kits.\n**(4)**\nIf clinically indicated, a covered veteran shall be offered prophylaxes for sexually transmitted disease and for pregnancy. If so indicated, the personnel of the facility shall provide, to the health care providers of the facility who treat the covered veteran, clinical practice guidelines or clinical order sets.\n**(5)**\nEach covered veteran shall be offered local mental health care counseling or a referral to a mental health care provider. If such referral is to a non-Department provider, an appropriate employee of the Department facility shall coordinate care with the non-Department provider.\n**(6)**\nClear guidance regarding when and how a police officer of the Department shall document the notification of a local law enforcement agency of an acute sexual assault of a covered veteran. Such guidance shall balance the confidentiality of a covered veteran with Federal, State, and local reporting requirements.\n##### (b) Training\n**(1) For employees of the VHA**\nNot less than once each year after the Secretary updates directives under subsection (a), the Secretary shall provide, to appropriate employees of the Veterans Health Administration, training regarding the directives and policies updated in accordance with paragraphs (1) through (5) of subsection (a).\n**(2) For police officers of the Department**\nNot less than once each year after the Secretary updates directives under subsection (a), the Secretary shall provide, to each police officer of the Department, a training regarding the guidance under paragraph (6) of subsection (a) and developed\u2014\n**(A)**\nby the Director of the Office of Security and Law Enforcement of the Department; and\n**(B)**\nin accordance with trauma-informed sexual assault investigation curricula, such as ones provided by the International Association of Chiefs of Police; and\n**(3) Format**\nTraining under this subsection\u2014\n**(A)**\nmay be provided in-person or electronically;\n**(B)**\nshall be provided in-person at least once every five years to an employee of the Department described in paragraph (1) or (2);\n**(C)**\nshall include guided instruction;\n**(D)**\nshall include information specific to the facility of the Department where the employee works, including on-site resources and State and local requirements; and\n**(E)**\nmay not consist solely of printed materials.\n##### (c) Oversight\nThe director of each Veteran Integrated Service Networks shall monitor compliance with the requirements of this Act and oversee cases with lack of compliance to determine reasons for lack of compliance and additional resources and support as determined necessary by the Secretary to ensure compliance.\n##### (d) Definitions\nIn this section:\n**(1)**\nThe term acute sexual assault means unwanted sexual contact with an alleged perpetrator.\n**(2)**\nThe term covered veteran means a veteran who exhibits symptoms of acute sexual assault\u2014\n**(A)**\nat a medical facility of the Department of Veterans Affairs; and\n**(B)**\nnot later than 72 hours after such acute sexual assault.\n**(3)**\nThe term SAFE means sexual assault forensic examination.\n**(4)**\nThe term SANE means a sexual assault nurse examiner.",
      "versionDate": "2025-09-08",
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
            "name": "Assault and harassment offenses",
            "updateDate": "2026-04-16T19:10:39Z"
          },
          {
            "name": "Employment and training programs",
            "updateDate": "2026-04-16T19:10:57Z"
          },
          {
            "name": "Government employee pay, benefits, personnel management",
            "updateDate": "2026-04-16T19:10:48Z"
          },
          {
            "name": "Health personnel",
            "updateDate": "2026-04-16T19:10:52Z"
          },
          {
            "name": "Law enforcement officers",
            "updateDate": "2026-04-16T19:11:03Z"
          },
          {
            "name": "Sex offenses",
            "updateDate": "2026-04-16T19:10:35Z"
          },
          {
            "name": "Veterans' medical care",
            "updateDate": "2026-04-16T19:10:43Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-09-12T16:21:57Z"
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
      "date": "2025-09-08",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5203ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Secretary of Veterans Affairs to update directives of the Department of Veterans Affairs regarding the management of acute sexual assault, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-11T04:48:19Z"
    },
    {
      "title": "To direct the Secretary of Veterans Affairs to update directives of the Department of Veterans Affairs regarding the management of acute sexual assault, and for other purposes.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-09T08:05:42Z"
    }
  ]
}
```
