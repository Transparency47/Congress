# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3093?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3093
- Title: DETECT Nitazenes Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 3093
- Origin chamber: Senate
- Introduced date: 2025-11-03
- Update date: 2026-04-06T13:19:38Z
- Update date including text: 2026-04-06T13:19:38Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-11-03: Introduced in Senate
- 2025-11-03 - IntroReferral: Introduced in Senate
- 2025-11-03 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.
- Latest action: 2025-11-03: Introduced in Senate

## Actions

- 2025-11-03 - IntroReferral: Introduced in Senate
- 2025-11-03 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-03",
    "latestAction": {
      "actionDate": "2025-11-03",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3093",
    "number": "3093",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "S001227",
        "district": "",
        "firstName": "Eric",
        "fullName": "Sen. Schmitt, Eric [R-MO]",
        "lastName": "Schmitt",
        "party": "R",
        "state": "MO"
      }
    ],
    "title": "DETECT Nitazenes Act of 2025",
    "type": "S",
    "updateDate": "2026-04-06T13:19:38Z",
    "updateDateIncludingText": "2026-04-06T13:19:38Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-11-03",
      "committees": {
        "item": {
          "name": "Homeland Security and Governmental Affairs Committee",
          "systemCode": "ssga00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Homeland Security and Governmental Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-11-03",
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
          "date": "2025-11-03T22:38:02Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Homeland Security and Governmental Affairs Committee",
      "systemCode": "ssga00",
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
      "bioguideId": "M001243",
      "firstName": "David",
      "fullName": "Sen. McCormick, David [R-PA]",
      "isOriginalCosponsor": "True",
      "lastName": "McCormick",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-11-03",
      "state": "PA"
    },
    {
      "bioguideId": "R000618",
      "firstName": "Pete",
      "fullName": "Sen. Ricketts, Pete [R-NE]",
      "isOriginalCosponsor": "True",
      "lastName": "Ricketts",
      "party": "R",
      "sponsorshipDate": "2025-11-03",
      "state": "NE"
    },
    {
      "bioguideId": "G000574",
      "firstName": "Ruben",
      "fullName": "Sen. Gallego, Ruben [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Gallego",
      "party": "D",
      "sponsorshipDate": "2025-11-03",
      "state": "AZ"
    },
    {
      "bioguideId": "S001208",
      "firstName": "Elissa",
      "fullName": "Sen. Slotkin, Elissa [D-MI]",
      "isOriginalCosponsor": "True",
      "lastName": "Slotkin",
      "party": "D",
      "sponsorshipDate": "2025-11-03",
      "state": "MI"
    },
    {
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "False",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2025-12-02",
      "state": "NH"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3093is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3093\nIN THE SENATE OF THE UNITED STATES\nNovember 3, 2025 Mr. Schmitt (for himself, Mr. McCormick , Mr. Ricketts , Mr. Gallego , and Ms. Slotkin ) introduced the following bill; which was read twice and referred to the Committee on Homeland Security and Governmental Affairs\nA BILL\nTo require the Science and Technology Directorate in the Department of Homeland Security to work with the Drug Enforcement Agency to develop greater capacity to detect, identify, and disrupt illicit substances, such as nitazenes, in very low concentrations.\n#### 1. Short title\nThis Act may be cited as the Detection Equipment and Technology Evaluation to Counter the Threat of Nitazenes Act of 2025 or the DETECT Nitazenes Act of 2025 .\n#### 2. Enhancing the capacity to detect and identify drugs such as nitazenes\nSection 302(15) of the Homeland Security Act of 2002 ( 6 U.S.C. 182(15) ) is amended, in the matter preceding subparagraph (A), by striking fentanyl and xylazine and inserting fentanyl, xylazine, and nitazenes .",
      "versionDate": "2025-11-03",
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
        "actionDate": "2026-03-19",
        "text": "Referred to the House Committee on Homeland Security."
      },
      "number": "8022",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "DETECT Nitazenes Act of 2026",
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
        "name": "Science, Technology, Communications",
        "updateDate": "2025-11-19T15:31:16Z"
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
      "date": "2025-11-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3093is.xml"
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
      "title": "DETECT Nitazenes Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-03T12:03:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "DETECT Nitazenes Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-08T05:23:14Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Detection Equipment and Technology Evaluation to Counter the Threat of Nitazenes Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-08T05:23:14Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require the Science and Technology Directorate in the Department of Homeland Security to work with the Drug Enforcement Agency to develop greater capacity to detect, identify, and disrupt illicit substances, such as nitazenes, in very low concentrations.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-08T05:18:17Z"
    }
  ]
}
```
