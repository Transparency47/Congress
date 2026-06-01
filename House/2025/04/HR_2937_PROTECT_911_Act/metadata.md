# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2937?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2937
- Title: PROTECT 911 Act
- Congress: 119
- Bill type: HR
- Bill number: 2937
- Origin chamber: House
- Introduced date: 2025-04-17
- Update date: 2026-01-10T09:06:09Z
- Update date including text: 2026-01-10T09:06:09Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-04-17: Introduced in House
- 2025-04-17 - IntroReferral: Introduced in House
- 2025-04-17 - IntroReferral: Introduced in House
- 2025-04-17 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-04-17: Introduced in House

## Actions

- 2025-04-17 - IntroReferral: Introduced in House
- 2025-04-17 - IntroReferral: Introduced in House
- 2025-04-17 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-17",
    "latestAction": {
      "actionDate": "2025-04-17",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2937",
    "number": "2937",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "K000385",
        "district": "2",
        "firstName": "Robin",
        "fullName": "Rep. Kelly, Robin L. [D-IL-2]",
        "lastName": "Kelly",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "PROTECT 911 Act",
    "type": "HR",
    "updateDate": "2026-01-10T09:06:09Z",
    "updateDateIncludingText": "2026-01-10T09:06:09Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-17",
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
      "actionDate": "2025-04-17",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-17",
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
          "date": "2025-04-17T13:30:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
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
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-04-17",
      "state": "PA"
    },
    {
      "bioguideId": "T000474",
      "district": "35",
      "firstName": "Norma",
      "fullName": "Rep. Torres, Norma J. [D-CA-35]",
      "isOriginalCosponsor": "True",
      "lastName": "Torres",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-04-17",
      "state": "CA"
    },
    {
      "bioguideId": "N000191",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Neguse, Joe [D-CO-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Neguse",
      "party": "D",
      "sponsorshipDate": "2025-04-17",
      "state": "CO"
    },
    {
      "bioguideId": "S001221",
      "district": "3",
      "firstName": "Hillary",
      "fullName": "Rep. Scholten, Hillary J. [D-MI-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Scholten",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-04-17",
      "state": "MI"
    },
    {
      "bioguideId": "V000131",
      "district": "33",
      "firstName": "Marc",
      "fullName": "Rep. Veasey, Marc A. [D-TX-33]",
      "isOriginalCosponsor": "False",
      "lastName": "Veasey",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-04-28",
      "state": "TX"
    },
    {
      "bioguideId": "B001315",
      "district": "13",
      "firstName": "Nikki",
      "fullName": "Rep. Budzinski, Nikki [D-IL-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Budzinski",
      "party": "D",
      "sponsorshipDate": "2025-06-17",
      "state": "IL"
    },
    {
      "bioguideId": "N000193",
      "district": "3",
      "firstName": "Zachary",
      "fullName": "Rep. Nunn, Zachary [R-IA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Nunn",
      "party": "R",
      "sponsorshipDate": "2025-09-30",
      "state": "IA"
    },
    {
      "bioguideId": "R000305",
      "district": "2",
      "firstName": "Deborah",
      "fullName": "Rep. Ross, Deborah K. [D-NC-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Ross",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "NC"
    },
    {
      "bioguideId": "M001237",
      "district": "8",
      "firstName": "Kristen",
      "fullName": "Rep. McDonald Rivet, Kristen [D-MI-8]",
      "isOriginalCosponsor": "False",
      "lastName": "McDonald Rivet",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "MI"
    },
    {
      "bioguideId": "D000230",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Davis, Donald G. [D-NC-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Davis",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2026-01-09",
      "state": "NC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2937ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2937\nIN THE HOUSE OF REPRESENTATIVES\nApril 17, 2025 Ms. Kelly of Illinois (for herself, Mr. Fitzpatrick , Mrs. Torres of California , Mr. Neguse , and Ms. Scholten ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo require the Secretary of Health and Human Services to improve the detection, prevention, and treatment of mental health issues among public safety telecommunicators.\n#### 1. Short title\nThis Act may be cited as the Providing Resources and Occupational Training for Emotional Crisis and Trauma in 911 Act or the PROTECT 911 Act .\n#### 2. Best practices and other resources for addressing mental health in public safety telecommunicators\n##### (a) Best practices\nThe Secretary shall\u2014\n**(1)**\ndevelop and make publicly available evidence-based best practices to identify, prevent, and treat posttraumatic stress disorder and co-occurring disorders in public safety telecommunicators; and\n**(2)**\nperiodically reassess and update, as the Secretary determines necessary, such best practices.\n##### (b) Development of resources for educating mental health professionals about treating public safety telecommunicators\nThe Secretary shall develop and make publicly available resources that may be used by the Federal Government and other entities to educate mental health professionals about\u2014\n**(1)**\nthe culture of emergency communications centers;\n**(2)**\nthe different stressors experienced by public safety telecommunicators;\n**(3)**\nchallenges encountered by retired public safety telecommunicators; and\n**(4)**\nevidence-based therapies for mental health issues common to public safety telecommunicators.\n##### (c) Consultation\nIn developing best practices under subsection (a) and resources under subsection (b), the Secretary shall consult with\u2014\n**(1)**\npublic health experts;\n**(2)**\nmental health experts with experience studying suicide, posttraumatic stress disorder, and other illnesses associated with job-related stress;\n**(3)**\nclinicians with experience in diagnosing and treating mental health issues; and\n**(4)**\nrelevant national nonprofit associations of public safety telecommunicators.\n##### (d) Definitions\n**(1) Emergency communications center**\nThe term emergency communications center means a facility that is designated to receive a 9\u20131\u20131 request for emergency assistance and perform one or more of the following functions:\n**(A)**\nProcess and analyze 9\u20131\u20131 requests for emergency assistance and other gathered information.\n**(B)**\nDispatch appropriate emergency response providers.\n**(C)**\nTransfer or exchange 9\u20131\u20131 requests for emergency assistance and other gathered information with other emergency communications centers and emergency response providers.\n**(D)**\nAnalyze any communications received from emergency response providers.\n**(E)**\nSupport incident command functions.\n**(2) Public safety telecommunicator**\nThe term public safety telecommunicator means a public safety telecommunicator as designated in detailed occupation 43\u20135031 in the Standard Occupational Classification Manual of the Office of Management and Budget (2018), or any successor designation.\n#### 3. Grants for behavioral health and wellness programs within emergency communications centers\nPart B of title III of the Public Health Service Act ( 42 U.S.C. 243 et seq. ) is amended by adding at the end the following:\n320C. Grants for behavioral health and wellness programs within emergency communications centers (a) In general The Secretary shall award grants to State, local, and regional emergency communications centers and other eligible entities for the purpose of establishing or enhancing behavioral health and wellness programs. (b) Use of funds An eligible entity receiving a grant under this section shall use funds received through the grant\u2014 (1) to establish evidence-based behavioral health and wellness programs for emergency communications centers to support public safety telecommunicators, including programs dedicated to raising awareness of, preventing, and mitigating job-related mental health issues; (2) to establish or enhance peer-support behavioral health and wellness programs; (3) to acquire materials or instructors to provide such training; and (4) to disseminate such information and materials as are necessary to carry out a evidence-based behavioral health and wellness program. (c) Definitions (1) Emergency communications center The term emergency communications center means a facility that is designated to receive a 9\u20131\u20131 request for emergency assistance and perform one or more of the following functions: (A) Process and analyze 9\u20131\u20131 requests for emergency assistance and other gathered information. (B) Dispatch appropriate emergency response providers. (C) Transfer or exchange 9\u20131\u20131 requests for emergency assistance and other gathered information with other emergency communications centers and emergency response providers. (D) Analyze any communications received from emergency response providers. (E) Support incident command functions. (2) Other eligible entity The term other eligible entity means a nonprofit organization with expertise and experience with respect to the health and wellness of public safety telecommunicators, including State, local, and regional 9\u20131\u20131 authorities and State, regional, and national public safety communications associations. (3) Peer-support behavioral health and wellness program The term peer-support behavioral health and wellness program means programs that use public safety telecommunicators to serve as peer counselors or provide training to public safety telecommunicators to serve as such peer counselors. (4) Public safety telecommunicator The term public safety telecommunicator means a public safety telecommunicator as designated in detailed occupation 43\u20135031 in the Standard Occupational Classification Manual of the Office of Management and Budget (2018), or any successor designation. .",
      "versionDate": "2025-04-17",
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
        "name": "Health",
        "updateDate": "2025-05-20T13:34:06Z"
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
      "date": "2025-04-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2937ih.xml"
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
      "title": "PROTECT 911 Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-02T03:08:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "PROTECT 911 Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-02T03:08:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Providing Resources and Occupational Training for Emotional Crisis and Trauma in 911 Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-02T03:08:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Secretary of Health and Human Services to improve the detection, prevention, and treatment of mental health issues among public safety telecommunicators.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-02T03:03:30Z"
    }
  ]
}
```
