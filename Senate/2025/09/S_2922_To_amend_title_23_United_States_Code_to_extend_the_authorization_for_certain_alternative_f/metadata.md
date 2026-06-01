# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2922?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2922
- Title: HOV Lane Exemption Reauthorization Act
- Congress: 119
- Bill type: S
- Bill number: 2922
- Origin chamber: Senate
- Introduced date: 2025-09-19
- Update date: 2025-12-16T16:44:02Z
- Update date including text: 2025-12-16T16:44:02Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-09-19: Introduced in Senate
- 2025-09-19 - IntroReferral: Introduced in Senate
- 2025-09-19 - IntroReferral: Read twice and referred to the Committee on Environment and Public Works. (Sponsor introductory remarks on measure: CR S6794)
- Latest action: 2025-09-19: Introduced in Senate

## Actions

- 2025-09-19 - IntroReferral: Introduced in Senate
- 2025-09-19 - IntroReferral: Read twice and referred to the Committee on Environment and Public Works. (Sponsor introductory remarks on measure: CR S6794)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-19",
    "latestAction": {
      "actionDate": "2025-09-19",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2922",
    "number": "2922",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "P000145",
        "district": "",
        "firstName": "Alex",
        "fullName": "Sen. Padilla, Alex [D-CA]",
        "lastName": "Padilla",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "HOV Lane Exemption Reauthorization Act",
    "type": "S",
    "updateDate": "2025-12-16T16:44:02Z",
    "updateDateIncludingText": "2025-12-16T16:44:02Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-09-19",
      "committees": {
        "item": {
          "name": "Environment and Public Works Committee",
          "systemCode": "ssev00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Environment and Public Works. (Sponsor introductory remarks on measure: CR S6794)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-09-19",
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
          "date": "2025-09-19T17:40:17Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Environment and Public Works Committee",
      "systemCode": "ssev00",
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
      "bioguideId": "C001114",
      "firstName": "John",
      "fullName": "Sen. Curtis, John R. [R-UT]",
      "isOriginalCosponsor": "True",
      "lastName": "Curtis",
      "party": "R",
      "sponsorshipDate": "2025-09-19",
      "state": "UT"
    },
    {
      "bioguideId": "G000555",
      "firstName": "Kirsten",
      "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
      "isOriginalCosponsor": "True",
      "lastName": "Gillibrand",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-09-19",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2922is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2922\nIN THE SENATE OF THE UNITED STATES\nSeptember 19 (legislative day, September 16), 2025 Mr. Padilla (for himself, Mr. Curtis , and Mrs. Gillibrand ) introduced the following bill; which was read twice and referred to the Committee on Environment and Public Works\nA BILL\nTo amend title 23, United States Code, to extend the authorization for certain alternative fuel and clean vehicles to use HOV facilities, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the High Occupancy Vehicle Lane Exemption Reauthorization Act or the HOV Lane Exemption Reauthorization Act .\n#### 2. HOV facilities\nSection 166(b)(5)(A) of title 23, United States Code, is amended, in the matter preceding clause (i), by striking September 30, 2025 and inserting September 30, 2026 .",
      "versionDate": "2025-09-19",
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
        "actionDate": "2025-08-13",
        "text": "Referred to the Subcommittee on Highways and Transit."
      },
      "number": "4948",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "HOV Lane Exemption Reauthorization Act",
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
        "name": "Transportation and Public Works",
        "updateDate": "2025-12-16T16:44:02Z"
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
      "date": "2025-09-19",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2922is.xml"
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
      "title": "HOV Lane Exemption Reauthorization Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-10T05:53:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "HOV Lane Exemption Reauthorization Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-10T05:53:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "High Occupancy Vehicle Lane Exemption Reauthorization Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-10T05:53:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title 23, United States Code, to extend the authorization for certain alternative fuel and clean vehicles to use HOV facilities, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-10T05:48:17Z"
    }
  ]
}
```
