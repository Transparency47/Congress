# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3390?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3390
- Title: Tracking and Restricting Adversarial Circumvention of Embargoes Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 3390
- Origin chamber: Senate
- Introduced date: 2025-12-09
- Update date: 2026-04-10T21:44:58Z
- Update date including text: 2026-04-10T21:44:58Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-12-09: Introduced in Senate
- 2025-12-09 - IntroReferral: Introduced in Senate
- 2025-12-09 - IntroReferral: Read twice and referred to the Select Committee on Intelligence.
- Latest action: 2025-12-09: Introduced in Senate

## Actions

- 2025-12-09 - IntroReferral: Introduced in Senate
- 2025-12-09 - IntroReferral: Read twice and referred to the Select Committee on Intelligence.

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
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3390",
    "number": "3390",
    "originChamber": "Senate",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "B001277",
        "district": "",
        "firstName": "Richard",
        "fullName": "Sen. Blumenthal, Richard [D-CT]",
        "lastName": "Blumenthal",
        "party": "D",
        "state": "CT"
      }
    ],
    "title": "Tracking and Restricting Adversarial Circumvention of Embargoes Act of 2025",
    "type": "S",
    "updateDate": "2026-04-10T21:44:58Z",
    "updateDateIncludingText": "2026-04-10T21:44:58Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-09",
      "committees": {
        "item": {
          "name": "Intelligence (Select) Committee",
          "systemCode": "slin00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Select Committee on Intelligence.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-12-09",
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
        "item": {
          "date": "2025-12-09T15:43:21Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Intelligence (Select) Committee",
      "systemCode": "slin00",
      "type": "Select"
    }
  ]
}
```

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "G000359",
      "firstName": "Lindsey",
      "fullName": "Sen. Graham, Lindsey [R-SC]",
      "isOriginalCosponsor": "True",
      "lastName": "Graham",
      "party": "R",
      "sponsorshipDate": "2025-12-09",
      "state": "SC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3390is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3390\nIN THE SENATE OF THE UNITED STATES\nDecember 9, 2025 Mr. Blumenthal (for himself and Mr. Graham ) introduced the following bill; which was read twice and referred to the Select Committee on Intelligence\nA BILL\nTo require a report on the purchases of Iranian oil by the People\u2019s Republic of China, support from entities and individuals in the People\u2019s Republic of China for Iran\u2019s ballistic missile program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Tracking and Restricting Adversarial Circumvention of Embargoes Act of 2025 .\n#### 2. Reporting requirement\n##### (a) In general\nNot later than 180 days after the date of the enactment of this Act, the Director of National Intelligence shall submit to the appropriate congressional committees and Secretary of the Treasury a report analyzing oil and ballistic missile-related transactions between the People\u2019s Republic of China and the Islamic Republic of Iran.\n##### (b) Elements\nThe report required by subsection (a) shall include the following:\n**(1)**\nAn assessment of the purchases of Iranian oil by the People\u2019s Republic of China since 2020, including an assessment of the use of transshipment points and shell companies as methods to insulate the People\u2019s Republic of China from sanctions.\n**(2)**\nAn assessment of significant financial transactions by entities in the People\u2019s Republic of China related to the sale, supply, or transfer to Iran of chemical precursors and other materials that may support the ballistic missile program of Iran.\n##### (c) Appropriate congressional committees defined\nIn this section, the term appropriate congressional committees means\u2014\n**(1)**\nthe Committee on Banking, Housing, and Urban Affairs, the Committee on Commerce, Science, and Transportation, the Select Committee on Intelligence, the Committee on Appropriations, the Committee on Armed Services, and the Committee on Foreign Relations of the Senate; and\n**(2)**\nthe Committee on Financial Services, the Committee on Energy and Commerce, the Permanent Select Committee on Intelligence, the Committee on Appropriations, the Committee on Armed Services, and the Committee on Foreign Affairs of the House of Representatives.\n#### 3. Determination\nNot later than 180 days after the submission of the report required by section 2, the Secretary of the Treasury shall determine whether the People\u2019s Republic of China is conducting any sanctionable activities and report such determination to Congress.",
      "versionDate": "2025-12-09",
      "versionType": "Introduced in Senate"
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
        "text": "Referred to the Committee on Foreign Affairs, and in addition to the Committee on Intelligence (Permanent Select), for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "6528",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Tracking and Restricting Adversarial Circumvention of Embargoes Act of 2025",
      "type": "HR"
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
        "updateDate": "2026-01-06T21:44:51Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3390is.xml"
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
      "title": "Tracking and Restricting Adversarial Circumvention of Embargoes Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-31T03:53:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Tracking and Restricting Adversarial Circumvention of Embargoes Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-31T03:53:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require a report on the purchases of Iranian oil by the People's Republic of China, support from entities and individuals in the People's Republic of China for Iran's ballistic missile program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-31T03:48:14Z"
    }
  ]
}
```
