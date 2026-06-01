# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/664?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/664
- Title: Observing the 20th anniversary of the dates on which Hurricane Katrina and Hurricane Rita devastated the Gulf Coast and recognizing the progress of efforts to rebuild the affected Gulf Coast region.
- Congress: 119
- Bill type: HRES
- Bill number: 664
- Origin chamber: House
- Introduced date: 2025-08-29
- Update date: 2025-10-07T08:05:36Z
- Update date including text: 2025-10-07T08:05:36Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-08-29: Introduced in House
- 2025-08-29 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-08-29 - IntroReferral: Submitted in House
- 2025-08-29 - IntroReferral: Submitted in House
- 2025-08-30 - Committee: Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management.
- Latest action: 2025-08-29: Submitted in House

## Actions

- 2025-08-29 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-08-29 - IntroReferral: Submitted in House
- 2025-08-29 - IntroReferral: Submitted in House
- 2025-08-30 - Committee: Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-08-29",
    "latestAction": {
      "actionDate": "2025-08-29",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/664",
    "number": "664",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "E000235",
        "district": "4",
        "firstName": "Mike",
        "fullName": "Rep. Ezell, Mike [R-MS-4]",
        "lastName": "Ezell",
        "party": "R",
        "state": "MS"
      }
    ],
    "title": "Observing the 20th anniversary of the dates on which Hurricane Katrina and Hurricane Rita devastated the Gulf Coast and recognizing the progress of efforts to rebuild the affected Gulf Coast region.",
    "type": "HRES",
    "updateDate": "2025-10-07T08:05:36Z",
    "updateDateIncludingText": "2025-10-07T08:05:36Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-08-30",
      "committees": {
        "item": {
          "name": "Economic Development, Public Buildings, and Emergency Management Subcommittee",
          "systemCode": "hspw13"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-08-29",
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
      "actionCode": "H11100",
      "actionDate": "2025-08-29",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-08-29",
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
          "date": "2025-08-29T17:30:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-08-30T21:37:09Z",
              "name": "Referred to"
            }
          },
          "name": "Economic Development, Public Buildings, and Emergency Management Subcommittee",
          "systemCode": "hspw13"
        }
      },
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
      "bioguideId": "H001077",
      "district": "3",
      "firstName": "Clay",
      "fullName": "Rep. Higgins, Clay [R-LA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Higgins",
      "party": "R",
      "sponsorshipDate": "2025-08-29",
      "state": "LA"
    },
    {
      "bioguideId": "L000595",
      "district": "5",
      "firstName": "Julia",
      "fullName": "Rep. Letlow, Julia [R-LA-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Letlow",
      "party": "R",
      "sponsorshipDate": "2025-08-29",
      "state": "LA"
    },
    {
      "bioguideId": "G000591",
      "district": "3",
      "firstName": "Michael",
      "fullName": "Rep. Guest, Michael [R-MS-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Guest",
      "party": "R",
      "sponsorshipDate": "2025-08-29",
      "state": "MS"
    },
    {
      "bioguideId": "K000388",
      "district": "1",
      "firstName": "Trent",
      "fullName": "Rep. Kelly, Trent [R-MS-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Kelly",
      "party": "R",
      "sponsorshipDate": "2025-08-29",
      "state": "MS"
    },
    {
      "bioguideId": "C001125",
      "district": "2",
      "firstName": "Troy",
      "fullName": "Rep. Carter, Troy A. [D-LA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Carter",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-08-29",
      "state": "LA"
    },
    {
      "bioguideId": "F000110",
      "district": "6",
      "firstName": "Cleo",
      "fullName": "Rep. Fields, Cleo [D-LA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Fields",
      "party": "D",
      "sponsorshipDate": "2025-08-29",
      "state": "LA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres664ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 664\nIN THE HOUSE OF REPRESENTATIVES\nAugust 29, 2025 Mr. Ezell (for himself, Mr. Higgins of Louisiana , Ms. Letlow , Mr. Guest , Mr. Kelly of Mississippi , Mr. Carter of Louisiana , and Mr. Fields ) submitted the following resolution; which was referred to the Committee on Transportation and Infrastructure\nRESOLUTION\nObserving the 20th anniversary of the dates on which Hurricane Katrina and Hurricane Rita devastated the Gulf Coast and recognizing the progress of efforts to rebuild the affected Gulf Coast region.\nThat the House of Representatives\u2014\n**(1)**\nexpresses its support to the victims of Hurricane Katrina and Hurricane Rita;\n**(2)**\ncommends the courageous efforts of those who assisted in the recovery progress;\n**(3)**\nrecognizes the contributions of communities in Louisiana, Mississippi, Alabama, Florida, Texas, and Georgia to the United States; and\n**(4)**\nreaffirms its commitment to rebuild, renew, and restore the Gulf Coast region.",
      "versionDate": "2025-08-29",
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
        "name": "Government Operations and Politics",
        "updateDate": "2025-09-19T18:58:50Z"
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
      "date": "2025-08-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres664ih.xml"
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
      "title": "Observing the 20th anniversary of the dates on which Hurricane Katrina and Hurricane Rita devastated the Gulf Coast and recognizing the progress of efforts to rebuild the affected Gulf Coast region.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-30T08:18:20Z"
    },
    {
      "title": "Observing the 20th anniversary of the dates on which Hurricane Katrina and Hurricane Rita devastated the Gulf Coast and recognizing the progress of efforts to rebuild the affected Gulf Coast region.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-30T08:05:31Z"
    }
  ]
}
```
