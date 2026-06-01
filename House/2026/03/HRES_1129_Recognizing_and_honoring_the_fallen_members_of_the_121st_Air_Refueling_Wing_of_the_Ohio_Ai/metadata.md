# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/1129?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/1129
- Title: Recognizing and honoring the fallen members of the 121st Air Refueling Wing of the Ohio Air National Guard.
- Congress: 119
- Bill type: HRES
- Bill number: 1129
- Origin chamber: House
- Introduced date: 2026-03-20
- Update date: 2026-03-31T20:35:58Z
- Update date including text: 2026-03-31T20:35:58Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-03-20: Introduced in House
- 2026-03-20 - IntroReferral: Referred to the House Committee on Armed Services.
- 2026-03-20 - IntroReferral: Submitted in House
- 2026-03-20 - IntroReferral: Submitted in House
- Latest action: 2026-03-20: Submitted in House

## Actions

- 2026-03-20 - IntroReferral: Referred to the House Committee on Armed Services.
- 2026-03-20 - IntroReferral: Submitted in House
- 2026-03-20 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-20",
    "latestAction": {
      "actionDate": "2026-03-20",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/1129",
    "number": "1129",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "B001306",
        "district": "12",
        "firstName": "Troy",
        "fullName": "Rep. Balderson, Troy [R-OH-12]",
        "lastName": "Balderson",
        "party": "R",
        "state": "OH"
      }
    ],
    "title": "Recognizing and honoring the fallen members of the 121st Air Refueling Wing of the Ohio Air National Guard.",
    "type": "HRES",
    "updateDate": "2026-03-31T20:35:58Z",
    "updateDateIncludingText": "2026-03-31T20:35:58Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-20",
      "committees": {
        "item": {
          "name": "Armed Services Committee",
          "systemCode": "hsas00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Armed Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-20",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2026-03-20",
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
          "date": "2026-03-20T14:30:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Armed Services Committee",
      "systemCode": "hsas00",
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
      "bioguideId": "T000490",
      "district": "2",
      "firstName": "David",
      "fullName": "Rep. Taylor, David J. [R-OH-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Taylor",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2026-03-20",
      "state": "OH"
    },
    {
      "bioguideId": "C001126",
      "district": "15",
      "firstName": "Mike",
      "fullName": "Rep. Carey, Mike [R-OH-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Carey",
      "party": "R",
      "sponsorshipDate": "2026-03-20",
      "state": "OH"
    },
    {
      "bioguideId": "K000009",
      "district": "9",
      "firstName": "Marcy",
      "fullName": "Rep. Kaptur, Marcy [D-OH-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Kaptur",
      "party": "D",
      "sponsorshipDate": "2026-03-24",
      "state": "OH"
    },
    {
      "bioguideId": "L000601",
      "district": "1",
      "firstName": "Greg",
      "fullName": "Rep. Landsman, Greg [D-OH-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Landsman",
      "party": "D",
      "sponsorshipDate": "2026-03-24",
      "state": "OH"
    },
    {
      "bioguideId": "L000566",
      "district": "5",
      "firstName": "Robert",
      "fullName": "Rep. Latta, Robert E. [R-OH-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Latta",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2026-03-24",
      "state": "OH"
    },
    {
      "bioguideId": "J000289",
      "district": "4",
      "firstName": "Jim",
      "fullName": "Rep. Jordan, Jim [R-OH-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Jordan",
      "party": "R",
      "sponsorshipDate": "2026-03-24",
      "state": "OH"
    },
    {
      "bioguideId": "M001222",
      "district": "7",
      "firstName": "Max",
      "fullName": "Rep. Miller, Max L. [R-OH-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Miller",
      "middleName": "L.",
      "party": "R",
      "sponsorshipDate": "2026-03-24",
      "state": "OH"
    },
    {
      "bioguideId": "R000619",
      "district": "6",
      "firstName": "Michael",
      "fullName": "Rep. Rulli, Michael A. [R-OH-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Rulli",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2026-03-24",
      "state": "OH"
    },
    {
      "bioguideId": "D000626",
      "district": "8",
      "firstName": "Warren",
      "fullName": "Rep. Davidson, Warren [R-OH-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Davidson",
      "party": "R",
      "sponsorshipDate": "2026-03-24",
      "state": "OH"
    },
    {
      "bioguideId": "J000295",
      "district": "14",
      "firstName": "David",
      "fullName": "Rep. Joyce, David P. [R-OH-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Joyce",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2026-03-27",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1129ih.xml",
      "text": "IV\n119th CONGRESS\n2d Session\nH. RES. 1129\nIN THE HOUSE OF REPRESENTATIVES\nMarch 20, 2026 Mr. Balderson (for himself, Mr. Taylor , and Mr. Carey ) submitted the following resolution; which was referred to the Committee on Armed Services\nRESOLUTION\nRecognizing and honoring the fallen members of the 121st Air Refueling Wing of the Ohio Air National Guard.\nThat the House of Representatives\u2014\n**(1)**\nhonors the lives, service, and sacrifice of such members of the Ohio Air National Guard from the 121st Air Refueling Wing who were killed in Iraq during Operation Epic Fury;\n**(2)**\non behalf of a grateful Nation, stands together to pledge that their selfless sacrifice shall not be forgotten; and\n**(3)**\nexpresses our deepest condolences to the families and loved ones left behind, with continued prayers for them in this harrowing time.",
      "versionDate": "2026-03-20",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2026-03-31T20:35:58Z"
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
      "date": "2026-03-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1129ih.xml"
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
      "title": "Recognizing and honoring the fallen members of the 121st Air Refueling Wing of the Ohio Air National Guard.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-21T08:18:35Z"
    },
    {
      "title": "Recognizing and honoring the fallen members of the 121st Air Refueling Wing of the Ohio Air National Guard.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-21T08:05:52Z"
    }
  ]
}
```
