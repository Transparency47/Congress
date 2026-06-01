# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/1111?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/1111
- Title: Recognizing the 245th anniversary of the Battle of Guilford Courthouse and encouraging all United States citizens to visit the Guilford Courthouse National Military Park in Guilford County, North Carolina.
- Congress: 119
- Bill type: HRES
- Bill number: 1111
- Origin chamber: House
- Introduced date: 2026-03-12
- Update date: 2026-03-17T18:16:50Z
- Update date including text: 2026-03-17T18:16:50Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-03-12: Introduced in House
- 2026-03-12 - IntroReferral: Referred to the House Committee on Natural Resources.
- 2026-03-12 - IntroReferral: Submitted in House
- 2026-03-12 - IntroReferral: Submitted in House
- Latest action: 2026-03-12: Submitted in House

## Actions

- 2026-03-12 - IntroReferral: Referred to the House Committee on Natural Resources.
- 2026-03-12 - IntroReferral: Submitted in House
- 2026-03-12 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-12",
    "latestAction": {
      "actionDate": "2026-03-12",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/1111",
    "number": "1111",
    "originChamber": "House",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "M001240",
        "district": "6",
        "firstName": "Addison",
        "fullName": "Rep. McDowell, Addison P. [R-NC-6]",
        "lastName": "McDowell",
        "party": "R",
        "state": "NC"
      }
    ],
    "title": "Recognizing the 245th anniversary of the Battle of Guilford Courthouse and encouraging all United States citizens to visit the Guilford Courthouse National Military Park in Guilford County, North Carolina.",
    "type": "HRES",
    "updateDate": "2026-03-17T18:16:50Z",
    "updateDateIncludingText": "2026-03-17T18:16:50Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-12",
      "committees": {
        "item": {
          "name": "Natural Resources Committee",
          "systemCode": "hsii00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Natural Resources.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-12",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2026-03-12",
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
          "date": "2026-03-12T13:31:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Natural Resources Committee",
      "systemCode": "hsii00",
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
      "bioguideId": "H001067",
      "district": "9",
      "firstName": "Richard",
      "fullName": "Rep. Hudson, Richard [R-NC-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Hudson",
      "party": "R",
      "sponsorshipDate": "2026-03-12",
      "state": "NC"
    },
    {
      "bioguideId": "F000450",
      "district": "5",
      "firstName": "Virginia",
      "fullName": "Rep. Foxx, Virginia [R-NC-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Foxx",
      "party": "R",
      "sponsorshipDate": "2026-03-12",
      "state": "NC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1111ih.xml",
      "text": "IV\n119th CONGRESS\n2d Session\nH. RES. 1111\nIN THE HOUSE OF REPRESENTATIVES\nMarch 12, 2026 Mr. McDowell (for himself, Mr. Hudson , and Ms. Foxx ) submitted the following resolution; which was referred to the Committee on Natural Resources\nRESOLUTION\nRecognizing the 245th anniversary of the Battle of Guilford Courthouse and encouraging all United States citizens to visit the Guilford Courthouse National Military Park in Guilford County, North Carolina.\nThat the House of Representatives\u2014\n**(1)**\nrecognizes the 245th anniversary of the Battle of Guilford Courthouse in Guilford County, North Carolina;\n**(2)**\nhonors the bravery and sacrifice of the American and North Carolinian patriots who fought and died at the Battle of Guilford Courthouse;\n**(3)**\nrecognizes the significant role that the Battle of Guilford Courthouse played in our country\u2019s successful fight for independence; and\n**(4)**\nencourages all United States citizens to visit Guilford County, North Carolina, and tour the Guilford Courthouse National Military Park to celebrate the 250th anniversary of our independence.",
      "versionDate": "2026-03-12",
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
        "name": "Public Lands and Natural Resources",
        "updateDate": "2026-03-17T18:16:50Z"
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
      "date": "2026-03-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1111ih.xml"
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
      "title": "Recognizing the 245th anniversary of the Battle of Guilford Courthouse and encouraging all United States citizens to visit the Guilford Courthouse National Military Park in Guilford County, North Carolina.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-13T08:19:31Z"
    },
    {
      "title": "Recognizing the 245th anniversary of the Battle of Guilford Courthouse and encouraging all United States citizens to visit the Guilford Courthouse National Military Park in Guilford County, North Carolina.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-13T08:05:46Z"
    }
  ]
}
```
