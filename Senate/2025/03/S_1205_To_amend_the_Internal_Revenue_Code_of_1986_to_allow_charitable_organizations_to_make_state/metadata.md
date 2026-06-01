# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1205?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1205
- Title: Free Speech Fairness Act
- Congress: 119
- Bill type: S
- Bill number: 1205
- Origin chamber: Senate
- Introduced date: 2025-03-31
- Update date: 2025-12-05T21:43:12Z
- Update date including text: 2025-12-05T21:43:12Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-03-31: Introduced in Senate
- 2025-03-31 - IntroReferral: Introduced in Senate
- 2025-03-31 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-03-31: Introduced in Senate

## Actions

- 2025-03-31 - IntroReferral: Introduced in Senate
- 2025-03-31 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-31",
    "latestAction": {
      "actionDate": "2025-03-31",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1205",
    "number": "1205",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "L000575",
        "district": "",
        "firstName": "James",
        "fullName": "Sen. Lankford, James [R-OK]",
        "lastName": "Lankford",
        "party": "R",
        "state": "OK"
      }
    ],
    "title": "Free Speech Fairness Act",
    "type": "S",
    "updateDate": "2025-12-05T21:43:12Z",
    "updateDateIncludingText": "2025-12-05T21:43:12Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-31",
      "committees": {
        "item": {
          "name": "Finance Committee",
          "systemCode": "ssfi00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Finance.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-03-31",
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
          "date": "2025-03-31T20:52:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Finance Committee",
      "systemCode": "ssfi00",
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
      "bioguideId": "C001098",
      "firstName": "Ted",
      "fullName": "Sen. Cruz, Ted [R-TX]",
      "isOriginalCosponsor": "True",
      "lastName": "Cruz",
      "party": "R",
      "sponsorshipDate": "2025-03-31",
      "state": "TX"
    },
    {
      "bioguideId": "W000437",
      "firstName": "Roger",
      "fullName": "Sen. Wicker, Roger F. [R-MS]",
      "isOriginalCosponsor": "False",
      "lastName": "Wicker",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2025-04-04",
      "state": "MS"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1205is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1205\nIN THE SENATE OF THE UNITED STATES\nMarch 31, 2025 Mr. Lankford (for himself and Mr. Cruz ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Internal Revenue Code of 1986 to allow charitable organizations to make statements relating to political campaigns if such statements are made in the ordinary course of carrying out its tax exempt purpose.\n#### 1. Short title\nThis Act may be cited as the Free Speech Fairness Act .\n#### 2. Allowing 501(c)(3) organization to make statements relating to political campaign in ordinary course of carrying out its tax exempt purpose\n##### (a) In general\nSection 501 of the Internal Revenue Code of 1986 is amended by adding at the end the following new subsection:\n(s) Special rule relating to political campaign statements of organization described in subsection (c)(3) (1) In general For purposes of subsection (c)(3) and sections 170(c)(2), 2055, 2106, 2522, and 4955, an organization shall not fail to be treated as organized and operated exclusively for a purpose described in subsection (c)(3), nor shall it be deemed to have participated in, or intervened in any political campaign on behalf of (or in opposition to) any candidate for public office, solely because of the content of any statement which\u2014 (A) is made in the ordinary course of the organization\u2019s regular and customary activities in carrying out its exempt purpose, and (B) results in the organization incurring not more than de minimis incremental expenses. .\n##### (b) Effective date\nThe amendment made by this section shall apply to taxable years ending after the date of the enactment of this Act.",
      "versionDate": "2025-03-31",
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
        "actionDate": "2025-03-31",
        "text": "Referred to the House Committee on Ways and Means."
      },
      "number": "2501",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Free Speech Fairness Act",
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
        "name": "Taxation",
        "updateDate": "2025-05-09T13:50:40Z"
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
      "date": "2025-03-31",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1205is.xml"
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
      "title": "Free Speech Fairness Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-12T02:53:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Free Speech Fairness Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-12T02:53:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Internal Revenue Code of 1986 to allow charitable organizations to make statements relating to political campaigns if such statements are made in the ordinary course of carrying out its tax exempt purpose.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-12T02:48:20Z"
    }
  ]
}
```
