# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4176?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4176
- Title: STOP FRAUD in Medicaid Act
- Congress: 119
- Bill type: S
- Bill number: 4176
- Origin chamber: Senate
- Introduced date: 2026-03-24
- Update date: 2026-04-28T11:03:23Z
- Update date including text: 2026-04-28T11:03:23Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-03-24: Introduced in Senate
- 2026-03-24 - IntroReferral: Introduced in Senate
- 2026-03-24 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2026-03-24: Introduced in Senate

## Actions

- 2026-03-24 - IntroReferral: Introduced in Senate
- 2026-03-24 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-24",
    "latestAction": {
      "actionDate": "2026-03-24",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4176",
    "number": "4176",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "M001244",
        "district": "",
        "firstName": "Ashley",
        "fullName": "Sen. Moody, Ashley [R-FL]",
        "lastName": "Moody",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "STOP FRAUD in Medicaid Act",
    "type": "S",
    "updateDate": "2026-04-28T11:03:23Z",
    "updateDateIncludingText": "2026-04-28T11:03:23Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-24",
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
      "actionDate": "2026-03-24",
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
          "date": "2026-03-24T18:25:39Z",
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
      "bioguideId": "E000295",
      "firstName": "Joni",
      "fullName": "Sen. Ernst, Joni [R-IA]",
      "isOriginalCosponsor": "False",
      "lastName": "Ernst",
      "party": "R",
      "sponsorshipDate": "2026-04-27",
      "state": "IA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4176is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4176\nIN THE SENATE OF THE UNITED STATES\nMarch 24, 2026 Mrs. Moody introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend title XIX of the Social Security Act to direct State medicaid fraud control units to investigate and prosecute instances of beneficiary fraud.\n#### 1. Short title\nThis Act may be cited as the States Taking On Power For Redressing All Unlawful Deceits in Medicaid Act or the STOP FRAUD in Medicaid Act .\n#### 2. Directing State medicaid fraud control units to investigate and prosecute beneficiary fraud\n##### (a) In general\nSection 1903(q)(3) of the Social Security Act ( 42 U.S.C. 1396b(q)(3) ) is amended\u2014\n**(1)**\nby inserting , application for, or receipt of after the provision of each place it appears; and\n**(2)**\nby inserting , and individuals applying for or receiving, after providers of each place it appears.\n##### (b) Conforming change\nSection 1902(a)(61) of the Social Security Act ( 42 U.S.C. 1396a(a)(61) ) is amended by inserting , application for, and receipt of after the provision of each place it appears.\n##### (c) Effective date\nThe amendments made by this section shall apply beginning on the date that is 180 days after the date of the enactment of this Act.",
      "versionDate": "2026-03-24",
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
        "name": "Health",
        "updateDate": "2026-04-09T14:53:13Z"
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
      "date": "2026-03-24",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4176is.xml"
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
      "title": "STOP FRAUD in Medicaid Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-28T11:03:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "STOP FRAUD in Medicaid Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-03T05:38:27Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "States Taking On Power For Redressing All Unlawful Deceits in Medicaid Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-03T05:38:27Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title XIX of the Social Security Act to direct State medicaid fraud control units to investigate and prosecute instances of beneficiary fraud.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-03T05:33:40Z"
    }
  ]
}
```
