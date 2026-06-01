# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3961?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3961
- Title: Stop Post-Disaster Vultures Act
- Congress: 119
- Bill type: S
- Bill number: 3961
- Origin chamber: Senate
- Introduced date: 2026-03-02
- Update date: 2026-03-20T15:11:38Z
- Update date including text: 2026-03-20T15:11:38Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-03-02: Introduced in Senate
- 2026-03-02 - IntroReferral: Introduced in Senate
- 2026-03-02 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.
- Latest action: 2026-03-02: Introduced in Senate

## Actions

- 2026-03-02 - IntroReferral: Introduced in Senate
- 2026-03-02 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-02",
    "latestAction": {
      "actionDate": "2026-03-02",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3961",
    "number": "3961",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Emergency Management"
    },
    "sponsors": [
      {
        "bioguideId": "S001150",
        "district": "",
        "firstName": "Adam",
        "fullName": "Sen. Schiff, Adam B. [D-CA]",
        "lastName": "Schiff",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Stop Post-Disaster Vultures Act",
    "type": "S",
    "updateDate": "2026-03-20T15:11:38Z",
    "updateDateIncludingText": "2026-03-20T15:11:38Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-02",
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
      "actionDate": "2026-03-02",
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
          "date": "2026-03-02T23:34:22Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3961is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 3961\nIN THE SENATE OF THE UNITED STATES\nMarch 2, 2026 Mr. Schiff introduced the following bill; which was read twice and referred to the Committee on Homeland Security and Governmental Affairs\nA BILL\nTo prohibit solicitation by institutional investors after a major disaster, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Stop Post-Disaster Vultures Act .\n#### 2. Prohibition on solicitation by institutional investors after major disasters\n##### (a) In general\nTitle IV of the Robert T. Stafford Disaster Relief and Emergency Assistance Act (42 U.S.C. 5170) is amended by adding at the end the following:\n431. Prohibition on solicitation by institutional investors (a) Institutional investor defined In this section, the term institutional investor means, with respect to any taxable year, any individual or entity that owns, directly or indirectly, not less than 75 single-family homes. (b) Prohibition During the 6-month period following the declaration of a major disaster under section 401, an institutional investor may not make an offer to purchase a property, including any lot, parcel, or home, located within the area affected by the major disaster\u2014 (1) through the mail or any interstate wire; or (2) through any other type of solicitation or method of contact. (c) Severability If any provision of this section or the application of such provision is held to be unconstitutional, the remainder of this section, and the application of the provision to any other person or circumstance, shall not be affected. .",
      "versionDate": "",
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
        "name": "Emergency Management",
        "updateDate": "2026-03-20T15:11:38Z"
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
      "date": "",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3961is.xml"
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
      "title": "Stop Post-Disaster Vultures Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-19T03:23:28Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Stop Post-Disaster Vultures Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-19T03:23:26Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to prohibit solicitation by institutional investors after a major disaster, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-19T03:18:47Z"
    }
  ]
}
```
