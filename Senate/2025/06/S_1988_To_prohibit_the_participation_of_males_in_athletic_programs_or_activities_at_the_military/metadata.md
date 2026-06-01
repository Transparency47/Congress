# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1988?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1988
- Title: A bill to prohibit the participation of males in athletic programs or activities at the military service academies that are designated for women or girls.
- Congress: 119
- Bill type: S
- Bill number: 1988
- Origin chamber: Senate
- Introduced date: 2025-06-09
- Update date: 2025-12-05T21:48:03Z
- Update date including text: 2025-12-05T21:48:03Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-06-09: Introduced in Senate
- 2025-06-09 - IntroReferral: Introduced in Senate
- 2025-06-09 - IntroReferral: Read twice and referred to the Committee on Armed Services.
- Latest action: 2025-06-09: Introduced in Senate

## Actions

- 2025-06-09 - IntroReferral: Introduced in Senate
- 2025-06-09 - IntroReferral: Read twice and referred to the Committee on Armed Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-09",
    "latestAction": {
      "actionDate": "2025-06-09",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1988",
    "number": "1988",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Sports and Recreation"
    },
    "sponsors": [
      {
        "bioguideId": "T000278",
        "district": "",
        "firstName": "Tommy",
        "fullName": "Sen. Tuberville, Tommy [R-AL]",
        "lastName": "Tuberville",
        "party": "R",
        "state": "AL"
      }
    ],
    "title": "A bill to prohibit the participation of males in athletic programs or activities at the military service academies that are designated for women or girls.",
    "type": "S",
    "updateDate": "2025-12-05T21:48:03Z",
    "updateDateIncludingText": "2025-12-05T21:48:03Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-09",
      "committees": {
        "item": {
          "name": "Armed Services Committee",
          "systemCode": "ssas00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Armed Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-06-09",
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
          "date": "2025-06-09T20:14:19Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Armed Services Committee",
      "systemCode": "ssas00",
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
      "bioguideId": "S001232",
      "firstName": "Tim",
      "fullName": "Sen. Sheehy, Tim [R-MT]",
      "isOriginalCosponsor": "False",
      "lastName": "Sheehy",
      "party": "R",
      "sponsorshipDate": "2025-06-24",
      "state": "MT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1988is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1988\nIN THE SENATE OF THE UNITED STATES\nJune 9, 2025 Mr. Tuberville introduced the following bill; which was read twice and referred to the Committee on Armed Services\nA BILL\nTo prohibit the participation of males in athletic programs or activities at the military service academies that are designated for women or girls.\n#### 1. Prohibition on participation of males in athletic programs or activities at the military service academies that are designated for women or girls\n##### (a) In general\nThe Secretary of Defense shall ensure that the United States Military Academy, the United States Naval Academy, and the United States Air Force Academy do not permit a person whose sex is male to participate in an athletic program or activity that is designated for women or girls.\n##### (b) Rule of construction\nNothing in this section shall be construed to prohibit a recipient from permitting males to train or practice with an athletic program or activity that is designated for women or girls so long as no female is deprived of a roster spot on a team or sport, opportunity to participate in a practice or competition, scholarship, admission to an educational institution, or any other benefit that accompanies participating in the athletic program or activity.\n##### (c) Definitions\nIn this section\u2014\n**(1)**\nthe term athletic programs and activities includes all programs or activities that are provided conditional upon participation with any athletic team; and\n**(2)**\nthe term sex means a person\u2019s reproductive biology and genetics at birth.",
      "versionDate": "2025-06-09",
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
        "actionDate": "2025-11-12",
        "actionTime": "12:10:52",
        "text": "Held at the desk."
      },
      "number": "2296",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "National Defense Authorization Act for Fiscal Year 2026",
      "type": "S"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-06-11",
        "text": "Referred to the House Committee on Armed Services."
      },
      "number": "3917",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "To prohibit the participation of males in athletic programs or activities at the military service academies that are designated for women or girls.",
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
        "name": "Sports and Recreation",
        "updateDate": "2025-07-09T15:07:57Z"
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
      "date": "2025-06-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1988is.xml"
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
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to prohibit the participation of males in athletic programs or activities at the military service academies that are designated for women or girls.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-13T03:33:14Z"
    },
    {
      "title": "A bill to prohibit the participation of males in athletic programs or activities at the military service academies that are designated for women or girls.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-10T10:56:20Z"
    }
  ]
}
```
