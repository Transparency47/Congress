# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3258?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3258
- Title: Aviation Medication Transparency Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 3258
- Origin chamber: Senate
- Introduced date: 2025-11-20
- Update date: 2026-02-11T12:03:25Z
- Update date including text: 2026-02-11T12:03:25Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-11-20: Introduced in Senate
- 2025-11-20 - IntroReferral: Introduced in Senate
- 2025-11-20 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- Latest action: 2025-11-20: Introduced in Senate

## Actions

- 2025-11-20 - IntroReferral: Introduced in Senate
- 2025-11-20 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-20",
    "latestAction": {
      "actionDate": "2025-11-20",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3258",
    "number": "3258",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "D000622",
        "district": "",
        "firstName": "Tammy",
        "fullName": "Sen. Duckworth, Tammy [D-IL]",
        "lastName": "Duckworth",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "Aviation Medication Transparency Act of 2025",
    "type": "S",
    "updateDate": "2026-02-11T12:03:25Z",
    "updateDateIncludingText": "2026-02-11T12:03:25Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-11-20",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Commerce, Science, and Transportation.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-11-20",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in Senate",
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
            "date": "2025-11-20T18:57:26Z",
            "name": "Referred To"
          },
          {
            "date": "2025-11-20T18:57:26Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Commerce, Science, and Transportation Committee",
      "systemCode": "sscm00",
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
      "bioguideId": "H001061",
      "firstName": "John",
      "fullName": "Sen. Hoeven, John [R-ND]",
      "isOriginalCosponsor": "True",
      "lastName": "Hoeven",
      "party": "R",
      "sponsorshipDate": "2025-11-20",
      "state": "ND"
    },
    {
      "bioguideId": "D000563",
      "firstName": "Richard",
      "fullName": "Sen. Durbin, Richard J. [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Durbin",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "IL"
    },
    {
      "bioguideId": "B001319",
      "firstName": "Katie",
      "fullName": "Sen. Britt, Katie Boyd [R-AL]",
      "isOriginalCosponsor": "True",
      "lastName": "Britt",
      "party": "R",
      "sponsorshipDate": "2025-11-20",
      "state": "AL"
    },
    {
      "bioguideId": "H000273",
      "firstName": "John",
      "fullName": "Sen. Hickenlooper, John W. [D-CO]",
      "isOriginalCosponsor": "False",
      "lastName": "Hickenlooper",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2026-02-10",
      "state": "CO"
    },
    {
      "bioguideId": "R000584",
      "firstName": "James",
      "fullName": "Sen. Risch, James E. [R-ID]",
      "isOriginalCosponsor": "False",
      "lastName": "Risch",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2026-02-10",
      "state": "ID"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3258is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3258\nIN THE SENATE OF THE UNITED STATES\nNovember 20, 2025 Ms. Duckworth (for herself, Mr. Hoeven , Mr. Durbin , and Mrs. Britt ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo require the Administrator of the Federal Aviation Administration to publish the list of medications that the Administrator has compiled for purposes of the medical certification of airmen and air traffic control specialists, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Aviation Medication Transparency Act of 2025 .\n#### 2. Aviation medication transparency; list of approved medications\n##### (a) Purpose\nThe purpose of this Act is to ensure that aviation stakeholders, including airmen, air traffic control specialists, and individuals training to become airmen or air traffic control specialists, who are applicants for medical certification are informed, in a user-friendly and accessible manner, of the medications they may be safely prescribed.\n##### (b) In general\nNot later than 1 year after the date of enactment of this Act, the Administrator of the Federal Aviation Administration (in this section referred to as the Administrator ) shall publish and maintain on a publicly available website of the Federal Aviation Administration (in this section referred to as the FAA ) a list of medications that the Administrator, as of the date of publication, has\u2014\n**(1)**\ndetermined may be safely prescribed to an applicant for medical certification to treat certain medical conditions; and\n**(2)**\napproved for purposes of the issuance of a medical certification to an airman or air traffic control specialist.\n##### (c) Requirements\nTo ensure medical appropriateness, user-friendliness, and appropriate dissemination, the list required under subsection (b) shall\u2014\n**(1)**\nbe drafted in consultation with\u2014\n**(A)**\nthe Aeromedical Innovation and Modernization Working Group (established under section 411(a) of the FAA Reauthorization Act of 2024 ( 49 U.S.C. 44703 note)) (in this section referred to as the Working Group );\n**(B)**\ninstitutions of higher education that are accredited by the Aviation Accreditation Board International;\n**(C)**\nthe certified exclusive bargaining representatives of air traffic controllers of the FAA certified under section 7111 of title 5, United States Code;\n**(D)**\norganizations representing certified collective bargaining representative of airline pilots; and\n**(E)**\nany other stakeholder determined relevant by the Working Group;\n**(2)**\ncover all medications approved by the Administrator, including prescription medications and over-the-counter medications;\n**(3)**\nbe drafted in a user-friendly and accessible manner and provided to airmen, air traffic control specialists, and individuals training to become airmen or air traffic control specialists at the time when any such individual first seeks a medical certification;\n**(4)**\nif applicable, indicate the minimum and average period of time an airman or air traffic control specialist is required to have limited or no duties to stabilize on an approved medication;\n**(5)**\ninclude the list of medications that the Administrator has designated as Do Not Issue ;\n**(6)**\ninclude information for doctors or medical providers to contact the FAA regarding questions related to such list, including through a new or existing mechanism that is accessible to such doctors and medical providers;\n**(7)**\ninclude any additional information that the Administrator determines is appropriate to provide with respect to what conditions a certain medication may or may not be used to treat, as well as any information to explain why a medication is allowed or prohibited by the FAA; and\n**(8)**\ninclude any other information or clarification that the Administrator determines appropriate.\n##### (d) Annual update\nNot later than 1 year after the date of publication of the list required under subsection (b), and annually thereafter, the Administrator shall update such list, as appropriate.",
      "versionDate": "2025-11-20",
      "versionType": "Introduced in Senate"
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
        "name": "Transportation and Public Works",
        "updateDate": "2026-01-05T15:06:00Z"
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
      "date": "2025-11-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3258is.xml"
        }
      ],
      "type": "Introduced in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Aviation Medication Transparency Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-11T12:03:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Aviation Medication Transparency Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-19T05:38:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require the Administrator of the Federal Aviation Administration to publish the list of medications that the Administrator has compiled for purposes of the medical certification of airmen and air traffic control specialists, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-19T05:28:15Z"
    }
  ]
}
```
