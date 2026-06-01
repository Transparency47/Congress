# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7940?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7940
- Title: SAFE Pathways Act
- Congress: 119
- Bill type: HR
- Bill number: 7940
- Origin chamber: House
- Introduced date: 2026-03-16
- Update date: 2026-04-02T22:22:24Z
- Update date including text: 2026-04-02T22:22:24Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-03-16: Introduced in House
- 2026-03-16 - IntroReferral: Introduced in House
- 2026-03-16 - IntroReferral: Introduced in House
- 2026-03-16 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2026-03-16: Introduced in House

## Actions

- 2026-03-16 - IntroReferral: Introduced in House
- 2026-03-16 - IntroReferral: Introduced in House
- 2026-03-16 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-16",
    "latestAction": {
      "actionDate": "2026-03-16",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7940",
    "number": "7940",
    "originChamber": "House",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "G000576",
        "district": "6",
        "firstName": "Glenn",
        "fullName": "Rep. Grothman, Glenn [R-WI-6]",
        "lastName": "Grothman",
        "party": "R",
        "state": "WI"
      }
    ],
    "title": "SAFE Pathways Act",
    "type": "HR",
    "updateDate": "2026-04-02T22:22:24Z",
    "updateDateIncludingText": "2026-04-02T22:22:24Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-16",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-03-16",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-16",
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
          "date": "2026-03-16T16:01:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
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
      "bioguideId": "P000607",
      "district": "2",
      "firstName": "Mark",
      "fullName": "Rep. Pocan, Mark [D-WI-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Pocan",
      "party": "D",
      "sponsorshipDate": "2026-03-16",
      "state": "WI"
    },
    {
      "bioguideId": "W000829",
      "district": "8",
      "firstName": "Tony",
      "fullName": "Rep. Wied, Tony [R-WI-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Wied",
      "party": "R",
      "sponsorshipDate": "2026-03-16",
      "state": "WI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7940ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7940\nIN THE HOUSE OF REPRESENTATIVES\nMarch 16, 2026 Mr. Grothman (for himself, Mr. Pocan , and Mr. Wied ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend the Federal Power Act to require the consideration of invasive species when prescribing fishways, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Safeguarding Aquatic Fisheries and Ecosystem Pathways Act or the SAFE Pathways Act .\n#### 2. Consideration of invasive species\nSection 18 of the Federal Power Act ( 16 U.S.C. 811 ) is amended by inserting after the Secretary of Commerce. the following: In prescribing a fishway, the Secretary of Commerce or the Secretary of the Interior, as appropriate, shall consider the threat of invasive species, in consultation with the State in which the fishway is to be located. .",
      "versionDate": "2026-03-16",
      "versionType": "Introduced in House"
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
        "name": "Public Lands and Natural Resources",
        "updateDate": "2026-04-02T22:22:24Z"
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
      "date": "2026-03-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7940ih.xml"
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
      "title": "SAFE Pathways Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-01T07:23:28Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "SAFE Pathways Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-01T07:23:28Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Safeguarding Aquatic Fisheries and Ecosystem Pathways Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-01T07:23:28Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Federal Power Act to require the consideration of invasive species when prescribing fishways, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-01T07:18:24Z"
    }
  ]
}
```
