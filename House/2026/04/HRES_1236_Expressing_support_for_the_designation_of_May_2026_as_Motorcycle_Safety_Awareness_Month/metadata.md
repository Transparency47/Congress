# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/1236?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/1236
- Title: Expressing support for the designation of May 2026 as "Motorcycle Safety Awareness Month".
- Congress: 119
- Bill type: HRES
- Bill number: 1236
- Origin chamber: House
- Introduced date: 2026-04-29
- Update date: 2026-05-14T17:51:40Z
- Update date including text: 2026-05-14T17:51:40Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-04-29: Introduced in House
- 2026-04-29 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2026-04-29 - IntroReferral: Submitted in House
- Latest action: 2026-04-29: Submitted in House

## Actions

- 2026-04-29 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2026-04-29 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-29",
    "latestAction": {
      "actionDate": "2026-04-29",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/1236",
    "number": "1236",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "W000798",
        "district": "5",
        "firstName": "Tim",
        "fullName": "Rep. Walberg, Tim [R-MI-5]",
        "lastName": "Walberg",
        "party": "R",
        "state": "MI"
      }
    ],
    "title": "Expressing support for the designation of May 2026 as \"Motorcycle Safety Awareness Month\".",
    "type": "HRES",
    "updateDate": "2026-05-14T17:51:40Z",
    "updateDateIncludingText": "2026-05-14T17:51:40Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-29",
      "committees": {
        "item": {
          "name": "Transportation and Infrastructure Committee",
          "systemCode": "hspw00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Transportation and Infrastructure.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2026-04-29",
      "committees": {
        "item": {
          "name": "Transportation and Infrastructure Committee",
          "systemCode": "hspw00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
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
          "date": "2026-04-29T13:00:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "systemCode": "hspw00",
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
      "bioguideId": "B001306",
      "district": "12",
      "firstName": "Troy",
      "fullName": "Rep. Balderson, Troy [R-OH-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Balderson",
      "party": "R",
      "sponsorshipDate": "2026-04-29",
      "state": "OH"
    },
    {
      "bioguideId": "V000135",
      "district": "3",
      "firstName": "Derrick",
      "fullName": "Rep. Van Orden, Derrick [R-WI-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Orden",
      "party": "R",
      "sponsorshipDate": "2026-04-29",
      "state": "WI"
    },
    {
      "bioguideId": "N000188",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Norcross, Donald [D-NJ-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Norcross",
      "party": "D",
      "sponsorshipDate": "2026-04-29",
      "state": "NJ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1236ih.xml",
      "text": "IV\n119th CONGRESS\n2d Session\nH. RES. 1236\nIN THE HOUSE OF REPRESENTATIVES\nApril 29, 2026 Mr. Walberg (for himself, Mr. Balderson , Mr. Van Orden , and Mr. Norcross ) submitted the following resolution; which was referred to the Committee on Transportation and Infrastructure\nRESOLUTION\nExpressing support for the designation of May 2026 as Motorcycle Safety Awareness Month .\nThat the House of Representatives\u2014\n**(1)**\nsupports the designation of Motorcycle Safety Awareness Month ;\n**(2)**\nrecognizes the contribution of motorcycles to the transportation mix;\n**(3)**\nencourages motorcycle awareness by all road users;\n**(4)**\nrecognizes that motorcyclists have a right to the road and that all motorists should safely share the roadways;\n**(5)**\nencourages rider safety education, training, and proper gear for safe motorcycle operation; and\n**(6)**\nsupports the goals of Motorcycle Safety Awareness Month.",
      "versionDate": "2026-04-29",
      "versionType": "IH"
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
        "actionDate": "2025-05-01",
        "text": "Referred to the Subcommittee on Highways and Transit."
      },
      "number": "367",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Expressing support for the designation of May 2025 as \"Motorcycle Safety Awareness Month\".",
      "type": "HRES"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-05-13",
        "text": "Submitted in the Senate, considered, and agreed to without amendment and with a preamble by Unanimous Consent. (consideration: CR S2901; text: CR S2900)"
      },
      "number": "222",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "A resolution expressing support for the designation of May 2025 as \"Motorcycle Safety Awareness Month\".",
      "type": "SRES"
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
        "updateDate": "2026-05-14T17:51:40Z"
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
      "date": "2026-04-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1236ih.xml"
        }
      ],
      "type": "IH"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Expressing support for the designation of May 2026 as \"Motorcycle Safety Awareness Month\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-01T08:48:38Z"
    },
    {
      "title": "Expressing support for the designation of May 2026 as \"Motorcycle Safety Awareness Month\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-30T08:06:42Z"
    }
  ]
}
```
