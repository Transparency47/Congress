# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6528?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6528
- Title: Tracking and Restricting Adversarial Circumvention of Embargoes Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 6528
- Origin chamber: House
- Introduced date: 2025-12-09
- Update date: 2026-04-10T21:46:11Z
- Update date including text: 2026-04-10T21:46:11Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-12-09: Introduced in House
- 2025-12-09 - IntroReferral: Introduced in House
- 2025-12-09 - IntroReferral: Introduced in House
- 2025-12-09 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committee on Intelligence (Permanent Select), for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-12-09 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committee on Intelligence (Permanent Select), for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-12-09: Introduced in House

## Actions

- 2025-12-09 - IntroReferral: Introduced in House
- 2025-12-09 - IntroReferral: Introduced in House
- 2025-12-09 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committee on Intelligence (Permanent Select), for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-12-09 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committee on Intelligence (Permanent Select), for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-09",
    "latestAction": {
      "actionDate": "2025-12-09",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6528",
    "number": "6528",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "K000391",
        "district": "8",
        "firstName": "Raja",
        "fullName": "Rep. Krishnamoorthi, Raja [D-IL-8]",
        "lastName": "Krishnamoorthi",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "Tracking and Restricting Adversarial Circumvention of Embargoes Act of 2025",
    "type": "HR",
    "updateDate": "2026-04-10T21:46:11Z",
    "updateDateIncludingText": "2026-04-10T21:46:11Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-09",
      "committees": {
        "item": {
          "name": "Intelligence (Permanent Select) Committee",
          "systemCode": "hlig00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Foreign Affairs, and in addition to the Committee on Intelligence (Permanent Select), for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-09",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Foreign Affairs, and in addition to the Committee on Intelligence (Permanent Select), for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-12-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-09",
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
          "date": "2025-12-09T17:02:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Intelligence (Permanent Select) Committee",
      "systemCode": "hlig00",
      "type": "Select"
    },
    {
      "activities": {
        "item": {
          "date": "2025-12-09T17:02:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Foreign Affairs Committee",
      "systemCode": "hsfa00",
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
      "bioguideId": "C001118",
      "district": "6",
      "firstName": "Ben",
      "fullName": "Rep. Cline, Ben [R-VA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Cline",
      "party": "R",
      "sponsorshipDate": "2025-12-09",
      "state": "VA"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2026-01-07",
      "state": "NJ"
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
      "sponsorshipDate": "2026-01-08",
      "state": "PA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6528ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6528\nIN THE HOUSE OF REPRESENTATIVES\nDecember 9, 2025 Mr. Krishnamoorthi (for himself and Mr. Cline ) introduced the following bill; which was referred to the Committee on Foreign Affairs , and in addition to the Permanent Select Committee on Intelligence , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo require a report on the purchases of Iranian oil by the People\u2019s Republic of China, support from entities and individuals in the People\u2019s Republic of China for Iran\u2019s ballistic missile program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Tracking and Restricting Adversarial Circumvention of Embargoes Act of 2025 .\n#### 2. Reporting requirement\n##### (a) In general\nNot later than 180 days after the date of the enactment of this Act, the Director of National Intelligence shall submit to the appropriate congressional committees and Secretary of the Treasury a report analyzing oil and ballistic missile-related transactions between the People\u2019s Republic of China and the Islamic Republic of Iran.\n##### (b) Elements\nThe report required by subsection (a) shall include the following:\n**(1)**\nAn assessment of the purchases of Iranian oil by the People\u2019s Republic of China since 2020, including an assessment of the use of transshipment points and shell companies as methods to insulate the People\u2019s Republic of China from sanctions.\n**(2)**\nAn assessment of significant financial transactions by entities in the People\u2019s Republic of China related to the sale, supply, or transfer to Iran of chemical precursors and other materials that may support the ballistic missile program of Iran.\n##### (c) Appropriate congressional committees defined\nIn this section, the term appropriate congressional committees means\u2014\n**(1)**\nthe Committee on Banking, Housing, and Urban Affairs, the Committee on Commerce, Science, and Transportation, the Committee on Armed Services, the Committee on Foreign Relations, and the Select Committee on Intelligence of the Senate; and\n**(2)**\nthe Committee on Financial Services, the Committee on Energy and Commerce, the Committee on Armed Services, the Committee on Foreign Affairs, and the Permanent Select Committee on Intelligence of the House of Representatives.\n#### 3. Determination\nNot later than 6 months after the submission of the report required by section 2, the Secretary of the Treasury shall determine whether the People\u2019s Republic of China is conducting any sanctionable activities and report such determination to Congress.",
      "versionDate": "2025-12-09",
      "versionType": "Introduced in House"
    }
  ]
}
```

## API Data: relatedbills

```json
{
  "relatedBills": [
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2026-02-04",
        "text": "Referred to the Subcommittee on Health."
      },
      "number": "7007",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Governing for the People Act",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-12-09",
        "text": "Read twice and referred to the Select Committee on Intelligence."
      },
      "number": "3390",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Tracking and Restricting Adversarial Circumvention of Embargoes Act of 2025",
      "type": "S"
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
        "name": "International Affairs",
        "updateDate": "2025-12-10T21:30:46Z"
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
      "date": "2025-12-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6528ih.xml"
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
      "title": "Tracking and Restricting Adversarial Circumvention of Embargoes Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-10T09:53:27Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Tracking and Restricting Adversarial Circumvention of Embargoes Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-10T09:53:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require a report on the purchases of Iranian oil by the People's Republic of China, support from entities and individuals in the People's Republic of China for Iran's ballistic missile program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-10T09:48:20Z"
    }
  ]
}
```
