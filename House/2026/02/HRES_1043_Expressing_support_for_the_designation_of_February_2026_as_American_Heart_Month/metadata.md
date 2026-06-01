# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/1043?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/1043
- Title: Expressing support for the designation of February 2026 as "American Heart Month".
- Congress: 119
- Bill type: HRES
- Bill number: 1043
- Origin chamber: House
- Introduced date: 2026-02-09
- Update date: 2026-02-18T19:25:03Z
- Update date including text: 2026-02-18T19:25:03Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-02-09: Introduced in House
- 2026-02-09 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2026-02-09 - IntroReferral: Submitted in House
- 2026-02-09 - IntroReferral: Submitted in House
- Latest action: 2026-02-09: Submitted in House

## Actions

- 2026-02-09 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2026-02-09 - IntroReferral: Submitted in House
- 2026-02-09 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-09",
    "latestAction": {
      "actionDate": "2026-02-09",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/1043",
    "number": "1043",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "B001281",
        "district": "3",
        "firstName": "Joyce",
        "fullName": "Rep. Beatty, Joyce [D-OH-3]",
        "lastName": "Beatty",
        "party": "D",
        "state": "OH"
      }
    ],
    "title": "Expressing support for the designation of February 2026 as \"American Heart Month\".",
    "type": "HRES",
    "updateDate": "2026-02-18T19:25:03Z",
    "updateDateIncludingText": "2026-02-18T19:25:03Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-09",
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
      "actionCode": "H11100",
      "actionDate": "2026-02-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2026-02-09",
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
          "date": "2026-02-09T17:02:20Z",
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
      "bioguideId": "S000522",
      "district": "4",
      "firstName": "Christopher",
      "fullName": "Rep. Smith, Christopher H. [R-NJ-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2026-02-09",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1043ih.xml",
      "text": "IV\n119th CONGRESS\n2d Session\nH. RES. 1043\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 9, 2026 Mrs. Beatty (for herself and Mr. Smith of New Jersey ) submitted the following resolution; which was referred to the Committee on Energy and Commerce\nRESOLUTION\nExpressing support for the designation of February 2026 as American Heart Month .\nThat the House of Representatives\u2014\n**(1)**\nexpresses support for the designation of American Heart Month ;\n**(2)**\nsupports the goals and ideals of American Heart Month;\n**(3)**\nrecognizes and reaffirms the commitment of the United States to fighting cardiovascular disease\u2014\n**(A)**\nby promoting awareness about the causes, risks, and prevention of cardiovascular disease;\n**(B)**\nby supporting research on cardiovascular disease; and\n**(C)**\nby improving access to affordable, quality care to reduce long-term disability and mortality;\n**(4)**\ncommends the efforts of States, territories, and possessions of the United States, localities, nonprofit organizations, businesses, and other entities, and the people of the United States who support American Heart Month; and\n**(5)**\nencourages every individual in the United States to learn about their risk for cardiovascular disease.",
      "versionDate": "2026-02-09",
      "versionType": "IH"
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
        "updateDate": "2026-02-18T19:25:03Z"
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
      "date": "2026-02-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1043ih.xml"
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
      "title": "Expressing support for the designation of February 2026 as \"American Heart Month\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-10T09:18:27Z"
    },
    {
      "title": "Expressing support for the designation of February 2026 as \"American Heart Month\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-10T09:05:41Z"
    }
  ]
}
```
