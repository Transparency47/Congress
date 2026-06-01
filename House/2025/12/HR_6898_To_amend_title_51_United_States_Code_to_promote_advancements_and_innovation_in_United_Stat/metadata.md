# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6898?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6898
- Title: AIRSHIP Act
- Congress: 119
- Bill type: HR
- Bill number: 6898
- Origin chamber: House
- Introduced date: 2025-12-18
- Update date: 2026-01-22T15:33:14Z
- Update date including text: 2026-01-22T15:33:14Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-18: Introduced in House
- 2025-12-18 - IntroReferral: Introduced in House
- 2025-12-18 - IntroReferral: Introduced in House
- 2025-12-18 - IntroReferral: Referred to the House Committee on Science, Space, and Technology.
- Latest action: 2025-12-18: Introduced in House

## Actions

- 2025-12-18 - IntroReferral: Introduced in House
- 2025-12-18 - IntroReferral: Introduced in House
- 2025-12-18 - IntroReferral: Referred to the House Committee on Science, Space, and Technology.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-18",
    "latestAction": {
      "actionDate": "2025-12-18",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6898",
    "number": "6898",
    "originChamber": "House",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "S001223",
        "district": "13",
        "firstName": "Emilia",
        "fullName": "Rep. Sykes, Emilia Strong [D-OH-13]",
        "lastName": "Sykes",
        "party": "D",
        "state": "OH"
      }
    ],
    "title": "AIRSHIP Act",
    "type": "HR",
    "updateDate": "2026-01-22T15:33:14Z",
    "updateDateIncludingText": "2026-01-22T15:33:14Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-18",
      "committees": {
        "item": {
          "name": "Science, Space, and Technology Committee",
          "systemCode": "hssy00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Science, Space, and Technology.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-12-18",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-18",
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
          "date": "2025-12-18T14:05:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Science, Space, and Technology Committee",
      "systemCode": "hssy00",
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
      "bioguideId": "J000295",
      "district": "14",
      "firstName": "David",
      "fullName": "Rep. Joyce, David P. [R-OH-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Joyce",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2025-12-18",
      "state": "OH"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6898ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6898\nIN THE HOUSE OF REPRESENTATIVES\nDecember 18, 2025 Mrs. Sykes (for herself and Mr. Joyce of Ohio ) introduced the following bill; which was referred to the Committee on Science, Space, and Technology\nA BILL\nTo amend title 51, United States Code, to promote advancements and innovation in United States aeronautical research and technology for enhanced safety, noise, resiliency, and improved environmental impacts in United States aviation systems.\n#### 1. Short title\nThis Act may be cited as the Airship Improvement Research for Safety and Humanitarian Innovation Projects Act or the AIRSHIP Act .\n#### 2. Aeronautical research and development\n##### (a) Sense of Congress\nIt is the sense of Congress that\u2014\n**(1)**\nairships could contribute to sustainable and clean air cargo transportation;\n**(2)**\nairships may one day find much needed applications in supporting disaster response efforts or delivering humanitarian aid to those in need and to areas that may be inaccessible; and\n**(3)**\nadvances in airship design and technology could enable and reintroduce the world to practical, economical, and environmentally friendly airship transportation.\n##### (b) Research and development\nSection 40112 of title 51, United States Code, is amended\u2014\n**(1)**\nin subsection (c)\u2014\n**(A)**\nby striking The Administrator and inserting the following:\n(1) Objective The Administrator ;\n**(B)**\nin paragraph (1), as so designated, by inserting , airship, after rotorcraft ; and\n**(C)**\nby adding at the end the following new paragraph:\n(2) Approach The Administrator may establish a program of competitively awarded grants available to teams of researchers that may include the participation of individuals from universities, industry, and government for the conduct of this research. ; and\n**(2)**\nin subsection (e)\u2014\n**(A)**\nby striking The Administrator and inserting the following:\n(1) Objective The Administrator ;\n**(B)**\nin paragraph (1), as so designated, in the first sentence, by inserting , airship, after fixed wing vehicles ; and\n**(C)**\nby adding at the end the following new paragraph:\n(2) Approach The Administrator may establish a program of competitively awarded grants available to teams of researchers that may include the participation of individuals from universities, industry, and government for the conduct of this research. .",
      "versionDate": "2025-12-18",
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
        "name": "Science, Technology, Communications",
        "updateDate": "2026-01-22T15:33:14Z"
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
      "date": "2025-12-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6898ih.xml"
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
      "title": "AIRSHIP Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-21T11:23:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "AIRSHIP Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-21T11:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Airship Improvement Research for Safety and Humanitarian Innovation Projects Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-21T11:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 51, United States Code, to promote advancements and innovation in United States aeronautical research and technology for enhanced safety, noise, resiliency, and improved environmental impacts in United States aviation systems.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-21T11:18:28Z"
    }
  ]
}
```
