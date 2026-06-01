# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/386?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/386
- Title: A resolution designating the week of September 14 through September 20, 2025, as "Community School Coordinators Appreciation Week".
- Congress: 119
- Bill type: SRES
- Bill number: 386
- Origin chamber: Senate
- Introduced date: 2025-09-15
- Update date: 2025-09-24T16:58:39Z
- Update date including text: 2025-09-24T16:58:39Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-09-15: Introduced in Senate
- 2025-09-15 - IntroReferral: Introduced in Senate
- 2025-09-15 - IntroReferral: Referred to the Committee on the Judiciary. (text: CR S6601)
- Latest action: 2025-09-15: Introduced in Senate

## Actions

- 2025-09-15 - IntroReferral: Introduced in Senate
- 2025-09-15 - IntroReferral: Referred to the Committee on the Judiciary. (text: CR S6601)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-15",
    "latestAction": {
      "actionDate": "2025-09-15",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/386",
    "number": "386",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "V000128",
        "district": "",
        "firstName": "Chris",
        "fullName": "Sen. Van Hollen, Chris [D-MD]",
        "lastName": "Van Hollen",
        "party": "D",
        "state": "MD"
      }
    ],
    "title": "A resolution designating the week of September 14 through September 20, 2025, as \"Community School Coordinators Appreciation Week\".",
    "type": "SRES",
    "updateDate": "2025-09-24T16:58:39Z",
    "updateDateIncludingText": "2025-09-24T16:58:39Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-09-15",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on the Judiciary. (text: CR S6601)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-09-15",
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
          "date": "2025-09-15T23:11:37Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Judiciary Committee",
      "systemCode": "ssju00",
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
      "bioguideId": "H001042",
      "firstName": "Mazie",
      "fullName": "Sen. Hirono, Mazie K. [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Hirono",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-09-15",
      "state": "HI"
    },
    {
      "bioguideId": "D000563",
      "firstName": "Richard",
      "fullName": "Sen. Durbin, Richard J. [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Durbin",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-09-15",
      "state": "IL"
    },
    {
      "bioguideId": "S000033",
      "firstName": "Bernie",
      "fullName": "Sen. Sanders, Bernard [I-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sanders",
      "party": "I",
      "sponsorshipDate": "2025-09-15",
      "state": "VT"
    },
    {
      "bioguideId": "H001046",
      "firstName": "Martin",
      "fullName": "Sen. Heinrich, Martin [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Heinrich",
      "party": "D",
      "sponsorshipDate": "2025-09-15",
      "state": "NM"
    },
    {
      "bioguideId": "A000382",
      "firstName": "Angela",
      "fullName": "Sen. Alsobrooks, Angela D. [D-MD]",
      "isOriginalCosponsor": "False",
      "lastName": "Alsobrooks",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "MD"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres386is.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 386\nIN THE SENATE OF THE UNITED STATES\nSeptember 15, 2025 Mr. Van Hollen (for himself, Ms. Hirono , Mr. Durbin , Mr. Sanders , and Mr. Heinrich ) submitted the following resolution; which was referred to the Committee on the Judiciary\nRESOLUTION\nDesignating the week of September 14 through September 20, 2025, as Community School Coordinators Appreciation Week .\nThat the Senate\u2014\n**(1)**\ndesignates the week of September 14 through September 20, 2025, as Community School Coordinators Appreciation Week ;\n**(2)**\ngives thanks to community school coordinators for the work they do to serve students, families, and communities; and\n**(3)**\nencourages students, parents, school administrators, and public officials to participate in events that celebrate Community School Coordinators Appreciation Week.",
      "versionDate": "2025-09-15",
      "versionType": "IS"
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
        "name": "Education",
        "updateDate": "2025-09-23T15:55:09Z"
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
      "date": "2025-09-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres386is.xml"
        }
      ],
      "type": "IS"
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
      "title": "A resolution designating the week of September 14 through September 20, 2025, as \"Community School Coordinators Appreciation Week\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-18T04:48:34Z"
    },
    {
      "title": "A resolution designating the week of September 14 through September 20, 2025, as \"Community School Coordinators Appreciation Week\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-16T10:56:16Z"
    }
  ]
}
```
