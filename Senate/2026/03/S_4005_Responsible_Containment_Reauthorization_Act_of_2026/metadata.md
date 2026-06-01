# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4005?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4005
- Title: Responsible Containment Reauthorization Act of 2026
- Congress: 119
- Bill type: S
- Bill number: 4005
- Origin chamber: Senate
- Introduced date: 2026-03-05
- Update date: 2026-04-11T02:41:16Z
- Update date including text: 2026-04-11T02:41:16Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-03-05: Introduced in Senate
- 2026-03-05 - IntroReferral: Introduced in Senate
- 2026-03-05 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- Latest action: 2026-03-05: Introduced in Senate

## Actions

- 2026-03-05 - IntroReferral: Introduced in Senate
- 2026-03-05 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-05",
    "latestAction": {
      "actionDate": "2026-03-05",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4005",
    "number": "4005",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Energy"
    },
    "sponsors": [
      {
        "bioguideId": "H000273",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Hickenlooper, John W. [D-CO]",
        "lastName": "Hickenlooper",
        "party": "D",
        "state": "CO"
      }
    ],
    "title": "Responsible Containment Reauthorization Act of 2026",
    "type": "S",
    "updateDate": "2026-04-11T02:41:16Z",
    "updateDateIncludingText": "2026-04-11T02:41:16Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-05",
      "committees": {
        "item": {
          "name": "Energy and Natural Resources Committee",
          "systemCode": "sseg00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Energy and Natural Resources.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-03-05",
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
          "date": "2026-03-05T17:18:52Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Energy and Natural Resources Committee",
      "systemCode": "sseg00",
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
      "sponsorshipDate": "2026-03-05",
      "state": "UT"
    },
    {
      "bioguideId": "B001267",
      "firstName": "Michael",
      "fullName": "Sen. Bennet, Michael F. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Bennet",
      "party": "D",
      "sponsorshipDate": "2026-03-05",
      "state": "CO"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4005is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4005\nIN THE SENATE OF THE UNITED STATES\nMarch 5, 2026 Mr. Hickenlooper (for himself, Mr. Curtis , and Mr. Bennet ) introduced the following bill; which was read twice and referred to the Committee on Energy and Natural Resources\nA BILL\nTo amend the Uranium Mill Tailings Radiation Control Act of 1978 to extend the authorization of a disposal site in Mesa County, Colorado, until the site is filled to designed capacity.\n#### 1. Short title\nThis Act may be cited as the Responsible Containment Reauthorization Act of 2026 .\n#### 2. Extension of authorization\nSection 112(a)(1)(B) of the Uranium Mill Tailings Radiation Control Act of 1978 ( 42 U.S.C. 7922(a)(1)(B) ) is amended by striking , or September 30, 2031, whichever comes first .",
      "versionDate": "2026-03-05",
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
        "actionDate": "2026-03-05",
        "text": "Referred to the House Committee on Energy and Commerce."
      },
      "number": "7811",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Responsible Containment Reauthorization Act",
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
        "name": "Energy",
        "updateDate": "2026-03-24T19:37:17Z"
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
      "date": "2026-03-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4005is.xml"
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
      "title": "Responsible Containment Reauthorization Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-20T02:08:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Responsible Containment Reauthorization Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-20T02:08:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Uranium Mill Tailings Radiation Control Act of 1978 to extend the authorization of a disposal site in Mesa County, Colorado, until the site is filled to designed capacity.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-20T02:03:27Z"
    }
  ]
}
```
