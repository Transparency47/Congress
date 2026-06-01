# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2717?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2717
- Title: Servicewomen and Veterans Menopause Research Act
- Congress: 119
- Bill type: HR
- Bill number: 2717
- Origin chamber: House
- Introduced date: 2025-04-08
- Update date: 2026-05-21T08:08:06Z
- Update date including text: 2026-05-21T08:08:06Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-04-08: Introduced in House
- 2025-04-08 - IntroReferral: Introduced in House
- 2025-04-08 - IntroReferral: Introduced in House
- 2025-04-08 - IntroReferral: Referred to the Committee on Armed Services, and in addition to the Committee on Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-04-08 - IntroReferral: Referred to the Committee on Armed Services, and in addition to the Committee on Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-04-08: Introduced in House

## Actions

- 2025-04-08 - IntroReferral: Introduced in House
- 2025-04-08 - IntroReferral: Introduced in House
- 2025-04-08 - IntroReferral: Referred to the Committee on Armed Services, and in addition to the Committee on Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-04-08 - IntroReferral: Referred to the Committee on Armed Services, and in addition to the Committee on Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-08",
    "latestAction": {
      "actionDate": "2025-04-08",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2717",
    "number": "2717",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "H001085",
        "district": "6",
        "firstName": "Chrissy",
        "fullName": "Rep. Houlahan, Chrissy [D-PA-6]",
        "lastName": "Houlahan",
        "party": "D",
        "state": "PA"
      }
    ],
    "title": "Servicewomen and Veterans Menopause Research Act",
    "type": "HR",
    "updateDate": "2026-05-21T08:08:06Z",
    "updateDateIncludingText": "2026-05-21T08:08:06Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-08",
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
      "text": "Referred to the Committee on Armed Services, and in addition to the Committee on Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-08",
      "committees": {
        "item": {
          "name": "Armed Services Committee",
          "systemCode": "hsas00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Armed Services, and in addition to the Committee on Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-04-08",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-08",
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
          "date": "2025-04-08T14:00:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "systemCode": "hsvr00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-04-08T14:00:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Armed Services Committee",
      "systemCode": "hsas00",
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
      "bioguideId": "B000740",
      "district": "5",
      "firstName": "Stephanie",
      "fullName": "Rep. Bice, Stephanie I. [R-OK-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Bice",
      "middleName": "I.",
      "party": "R",
      "sponsorshipDate": "2025-04-08",
      "state": "OK"
    },
    {
      "bioguideId": "S001226",
      "district": "6",
      "firstName": "Andrea",
      "fullName": "Rep. Salinas, Andrea [D-OR-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Salinas",
      "party": "D",
      "sponsorshipDate": "2025-04-21",
      "state": "OR"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-07-02",
      "state": "PA"
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
      "sponsorshipDate": "2025-09-17",
      "state": "HI"
    },
    {
      "bioguideId": "F000110",
      "district": "6",
      "firstName": "Cleo",
      "fullName": "Rep. Fields, Cleo [D-LA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Fields",
      "party": "D",
      "sponsorshipDate": "2025-09-26",
      "state": "LA"
    },
    {
      "bioguideId": "G000591",
      "district": "3",
      "firstName": "Michael",
      "fullName": "Rep. Guest, Michael [R-MS-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Guest",
      "party": "R",
      "sponsorshipDate": "2025-10-06",
      "state": "MS"
    },
    {
      "bioguideId": "B001324",
      "district": "1",
      "firstName": "Wesley",
      "fullName": "Rep. Bell, Wesley [D-MO-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Bell",
      "party": "D",
      "sponsorshipDate": "2025-10-08",
      "state": "MO"
    },
    {
      "bioguideId": "L000582",
      "district": "36",
      "firstName": "Ted",
      "fullName": "Rep. Lieu, Ted [D-CA-36]",
      "isOriginalCosponsor": "False",
      "lastName": "Lieu",
      "party": "D",
      "sponsorshipDate": "2026-04-14",
      "state": "CA"
    },
    {
      "bioguideId": "M001196",
      "district": "6",
      "firstName": "Seth",
      "fullName": "Rep. Moulton, Seth [D-MA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Moulton",
      "party": "D",
      "sponsorshipDate": "2026-04-14",
      "state": "MA"
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
      "sponsorshipDate": "2026-04-16",
      "state": "NC"
    },
    {
      "bioguideId": "J000295",
      "district": "14",
      "firstName": "David",
      "fullName": "Rep. Joyce, David P. [R-OH-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Joyce",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2026-04-20",
      "state": "OH"
    },
    {
      "bioguideId": "G000604",
      "district": "2",
      "firstName": "Maggie",
      "fullName": "Rep. Goodlander, Maggie [D-NH-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Goodlander",
      "party": "D",
      "sponsorshipDate": "2026-04-22",
      "state": "NH"
    },
    {
      "bioguideId": "D000617",
      "district": "1",
      "firstName": "Suzan",
      "fullName": "Rep. DelBene, Suzan K. [D-WA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "DelBene",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2026-05-12",
      "state": "WA"
    },
    {
      "bioguideId": "M001238",
      "district": "0",
      "firstName": "Sarah",
      "fullName": "Rep. McBride, Sarah [D-DE-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "McBride",
      "party": "D",
      "sponsorshipDate": "2026-05-20",
      "state": "DE"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2717ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2717\nIN THE HOUSE OF REPRESENTATIVES\nApril 8, 2025 Ms. Houlahan (for herself and Mrs. Bice ) introduced the following bill; which was referred to the Committee on Armed Services , and in addition to the Committee on Veterans' Affairs , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo direct the Secretary of Defense and the Secretary of Veterans Affairs to take certain steps regarding research related to menopause, perimenopause, or mid-life women\u2019s health, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Servicewomen and Veterans Menopause Research Act .\n#### 2. Evaluation of certain research related to menopause, perimenopause, or mid-life women\u2019s health\n##### (a) In general\nThe Secretary of Defense, in coordination with Secretary of Veterans Affairs, shall evaluate\u2014\n**(1)**\nthe results of completed research related to menopause, perimenopause, or mid-life women\u2019s health among women who are members of the Armed Forces or veterans;\n**(2)**\nthe status of such research that is ongoing;\n**(3)**\nany gaps in knowledge and research on\u2014\n**(A)**\ntreatments, including hormone and non-hormone treatments, for menopause-related symptoms;\n**(B)**\nthe safety and effectiveness of treatments for menopause-related symptoms;\n**(C)**\nthe relation of service in the Armed Forces to perimenopause and menopause and the impact of such service on perimenopause and menopause;\n**(D)**\nthe effect of combat roles on symptoms relating to perimenopause and menopause, including exposure to burn pits, toxic chemicals, and PFAS; and\n**(E)**\nthe impact of perimenopause and menopause on the mental health of women who are members of the Armed Forces or veterans;\n**(4)**\nthe availability of and uptake of professional training resources for covered providers relating to mid-life women\u2019s health with respect to the care, treatment, and management of perimenopause and menopausal symptoms, and related support services; and\n**(5)**\nthe availability of and uptake of treatments for women who are members of the Armed Forces or veterans who are experiencing perimenopause or menopause.\n##### (b) Report; strategic plan\nNot later than 180 days after the date of the enactment of this Act, the Secretary of Defense and the Secretary of Veterans Affairs shall each submit to Congress a report containing\u2014\n**(1)**\nthe findings of the evaluation conducted under subsection (a);\n**(2)**\nrecommendations for improving professional training resources described in subsection (a)(4) for covered providers; and\n**(3)**\na strategic plan that\u2014\n**(A)**\nresolves the gaps in knowledge and research identified in the report; and\n**(B)**\nidentifies topics in need of further research relating to potential treatments for menopause-related symptoms of women who are members of the Armed Forces or veterans.\n##### (c) Nonduplication and supplementation of efforts\nIn carrying out activities under this section, the Secretary of Defense and the Secretary of Veterans Affairs shall ensure that such activities supplement, and minimize the duplication of, existing efforts of the Secretary of Health and Human Services to share information regarding matters described in subsection (a).\n##### (d) Definitions\nIn this section:\n**(1)**\nThe term covered provider means a health care provider who is an employee of the Department of Defense or the Department of Veterans Affairs.\n**(2)**\nThe term menopause \u2014\n**(A)**\nmeans the stage of a woman\u2019s life when menstruation stops permanently and she can no longer get pregnant; and\n**(B)**\nis not a disease state, but a normal part of aging for women.\n**(3)**\nThe term mid-life means a life stage for a woman that\u2014\n**(A)**\ncoincides with perimenopause, which may be physical or emotional;\n**(B)**\nencompasses the late reproductive age, which can begin at approximately 35 years of age, to late postmenopausal stages, which can extend to approximately 65 years of age, of reproductive aging; and\n**(C)**\noften marks the onset of many chronic diseases.\n**(4)**\nThe term perimenopause \u2014\n**(A)**\nmean the time when levels of the hormone estrogen fall unevenly in a woman\u2019s body; and\n**(B)**\nis also called the menopausal transition.\n**(5)**\nThe term PFAS means perfluoroalkyl and polyfluoroalkyl substances.\n**(6)**\nThe term postmenopausal means a period\u2014\n**(A)**\nthat begins after a woman has not menstruated for 12 months and lasts thereafter for the rest of the woman\u2019s life; and\n**(B)**\nduring which a woman is at increased risk for osteoporosis and heart disease.\n#### 3. Sense of Congress on additional research related to menopause, perimenopause, or mid-life women\u2019s health\nIt is the sense of Congress that the Secretary of Defense and the Secretary of Veterans Affairs should each conduct research related to menopause, perimenopause, or mid-life health regarding women who are members of the Armed Forces or veterans.",
      "versionDate": "2025-04-08",
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
        "updateDate": "2025-05-12T18:44:21Z"
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
      "date": "2025-04-08",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2717ih.xml"
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
      "title": "Servicewomen and Veterans Menopause Research Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-17T10:08:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Servicewomen and Veterans Menopause Research Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-17T10:08:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Secretary of Defense and the Secretary of Veterans Affairs to take certain steps regarding research related to menopause, perimenopause, or mid-life women's health, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-17T10:03:24Z"
    }
  ]
}
```
