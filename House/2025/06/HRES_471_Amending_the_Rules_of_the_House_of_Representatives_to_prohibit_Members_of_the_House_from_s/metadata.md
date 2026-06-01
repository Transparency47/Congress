# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/471?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/471
- Title: Restoring Integrity in Democracy Resolution
- Congress: 119
- Bill type: HRES
- Bill number: 471
- Origin chamber: House
- Introduced date: 2025-06-04
- Update date: 2025-09-19T08:07:11Z
- Update date including text: 2025-09-19T08:07:11Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-06-04: Introduced in House
- 2025-06-04 - IntroReferral: Referred to the House Committee on Ethics.
- 2025-06-04 - IntroReferral: Submitted in House
- 2025-06-04 - IntroReferral: Submitted in House
- Latest action: 2025-06-04: Submitted in House

## Actions

- 2025-06-04 - IntroReferral: Referred to the House Committee on Ethics.
- 2025-06-04 - IntroReferral: Submitted in House
- 2025-06-04 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-04",
    "latestAction": {
      "actionDate": "2025-06-04",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/471",
    "number": "471",
    "originChamber": "House",
    "policyArea": {
      "name": "Congress"
    },
    "sponsors": [
      {
        "bioguideId": "C001119",
        "district": "2",
        "firstName": "Angie",
        "fullName": "Rep. Craig, Angie [D-MN-2]",
        "lastName": "Craig",
        "party": "D",
        "state": "MN"
      }
    ],
    "title": "Restoring Integrity in Democracy Resolution",
    "type": "HRES",
    "updateDate": "2025-09-19T08:07:11Z",
    "updateDateIncludingText": "2025-09-19T08:07:11Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-04",
      "committees": {
        "item": {
          "name": "Ethics Committee",
          "systemCode": "hsso00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Ethics.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-06-04",
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
          "date": "2025-06-04T14:01:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ethics Committee",
      "systemCode": "hsso00",
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
      "bioguideId": "D000530",
      "district": "17",
      "firstName": "Christopher",
      "fullName": "Rep. Deluzio, Christopher R. [D-PA-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Deluzio",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-06-04",
      "state": "PA"
    },
    {
      "bioguideId": "N000191",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Neguse, Joe [D-CO-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Neguse",
      "party": "D",
      "sponsorshipDate": "2025-06-04",
      "state": "CO"
    },
    {
      "bioguideId": "R000579",
      "district": "18",
      "firstName": "Patrick",
      "fullName": "Rep. Ryan, Patrick [D-NY-18]",
      "isOriginalCosponsor": "True",
      "lastName": "Ryan",
      "party": "D",
      "sponsorshipDate": "2025-06-04",
      "state": "NY"
    },
    {
      "bioguideId": "S001221",
      "district": "3",
      "firstName": "Hillary",
      "fullName": "Rep. Scholten, Hillary J. [D-MI-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Scholten",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-06-04",
      "state": "MI"
    },
    {
      "bioguideId": "M001223",
      "district": "2",
      "firstName": "Seth",
      "fullName": "Rep. Magaziner, Seth [D-RI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Magaziner",
      "party": "D",
      "sponsorshipDate": "2025-06-05",
      "state": "RI"
    },
    {
      "bioguideId": "L000593",
      "district": "49",
      "firstName": "Mike",
      "fullName": "Rep. Levin, Mike [D-CA-49]",
      "isOriginalCosponsor": "False",
      "lastName": "Levin",
      "party": "D",
      "sponsorshipDate": "2025-07-14",
      "state": "CA"
    },
    {
      "bioguideId": "S001223",
      "district": "13",
      "firstName": "Emilia",
      "fullName": "Rep. Sykes, Emilia Strong [D-OH-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Sykes",
      "middleName": "Strong",
      "party": "D",
      "sponsorshipDate": "2025-09-18",
      "state": "OH"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres471ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 471\nIN THE HOUSE OF REPRESENTATIVES\nJune 4, 2025 Ms. Craig (for herself, Mr. Deluzio , Mr. Neguse , Mr. Ryan , and Ms. Scholten ) submitted the following resolution; which was referred to the Committee on Ethics\nRESOLUTION\nAmending the Rules of the House of Representatives to prohibit Members of the House from serving on the boards of for-profit entities.\n#### 1. Short title\nThis resolution may be cited as the Restoring Integrity in Democracy Resolution .\n#### 2. Prohibiting Members of the House of Representatives from serving on boards of for-profit entities\nRule XXIII of the Rules of the House of Representatives is amended\u2014\n**(1)**\nby redesignating clauses 19 through 22 as clauses 20 through 23, respectively; and\n**(2)**\nby inserting after clause 18 the following new clause:\n19. A Member, Delegate, or Resident Commissioner may not serve on the board of directors of any for-profit entity. .",
      "versionDate": "2025-06-04",
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
        "name": "Congress",
        "updateDate": "2025-06-18T13:23:27Z"
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
      "date": "2025-06-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres471ih.xml"
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
      "title": "Restoring Integrity in Democracy Resolution",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-05T08:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Restoring Integrity in Democracy Resolution",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-05T08:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Amending the Rules of the House of Representatives to prohibit Members of the House from serving on the boards of for-profit entities.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-05T08:18:24Z"
    }
  ]
}
```
