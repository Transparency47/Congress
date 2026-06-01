# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hconres/106?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-concurrent-resolution/106
- Title: To direct the removal of United States Armed Forces from hostilities within or against the Republic of Cuba that have not been authorized by Congress.
- Congress: 119
- Bill type: HCONRES
- Bill number: 106
- Origin chamber: House
- Introduced date: 2026-05-22
- Update date: 2026-05-30T08:06:09Z
- Update date including text: 2026-05-30T08:06:09Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-05-22: Introduced in House
- 2026-05-22 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2026-05-22 - IntroReferral: Submitted in House
- Latest action: 2026-05-22: Submitted in House

## Actions

- 2026-05-22 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2026-05-22 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-22",
    "latestAction": {
      "actionDate": "2026-05-22",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-concurrent-resolution/106",
    "number": "106",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "V000081",
        "district": "7",
        "firstName": "Nydia",
        "fullName": "Rep. Vel\u00e1zquez, Nydia M. [D-NY-7]",
        "lastName": "Vel\u00e1zquez",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "To direct the removal of United States Armed Forces from hostilities within or against the Republic of Cuba that have not been authorized by Congress.",
    "type": "HCONRES",
    "updateDate": "2026-05-30T08:06:09Z",
    "updateDateIncludingText": "2026-05-30T08:06:09Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-05-22",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Foreign Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2026-05-22",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
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
          "date": "2026-05-22T14:31:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Foreign Affairs Committee",
      "systemCode": "hsfa00",
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
      "bioguideId": "M001137",
      "district": "5",
      "firstName": "Gregory",
      "fullName": "Rep. Meeks, Gregory W. [D-NY-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Meeks",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2026-05-22",
      "state": "NY"
    },
    {
      "bioguideId": "C001091",
      "district": "20",
      "firstName": "Joaquin",
      "fullName": "Rep. Castro, Joaquin [D-TX-20]",
      "isOriginalCosponsor": "False",
      "lastName": "Castro",
      "party": "D",
      "sponsorshipDate": "2026-05-26",
      "state": "TX"
    },
    {
      "bioguideId": "M000312",
      "district": "2",
      "firstName": "James",
      "fullName": "Rep. McGovern, James P. [D-MA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "McGovern",
      "middleName": "P.",
      "party": "D",
      "sponsorshipDate": "2026-05-26",
      "state": "MA"
    },
    {
      "bioguideId": "C001131",
      "district": "35",
      "firstName": "Greg",
      "fullName": "Rep. Casar, Greg [D-TX-35]",
      "isOriginalCosponsor": "False",
      "lastName": "Casar",
      "party": "D",
      "sponsorshipDate": "2026-05-29",
      "state": "TX"
    },
    {
      "bioguideId": "M000687",
      "district": "7",
      "firstName": "Kweisi",
      "fullName": "Rep. Mfume, Kweisi [D-MD-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Mfume",
      "party": "D",
      "sponsorshipDate": "2026-05-29",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hconres/BILLS-119hconres106ih.xml",
      "text": "IV\n119th CONGRESS\n2d Session\nH. CON. RES. 106\nIN THE HOUSE OF REPRESENTATIVES\nMay 22, 2026 Ms. Vel\u00e1zquez (for herself and Mr. Meeks ) submitted the following concurrent resolution; which was referred to the Committee on Foreign Affairs\nCONCURRENT RESOLUTION\nTo direct the removal of United States Armed Forces from hostilities within or against the Republic of Cuba that have not been authorized by Congress.\nThat, pursuant to section 5(c) of the War Powers Resolution ( 50 U.S.C. 1544(c) ), Congress hereby directs the President to remove the United States Armed Forces from hostilities within or against Cuba, unless explicitly authorized by a declaration of war or a specific authorization for use of military force.",
      "versionDate": "2026-05-22",
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
        "name": "International Affairs",
        "updateDate": "2026-05-28T21:02:57Z"
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
      "date": "2026-05-22",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hconres/BILLS-119hconres106ih.xml"
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
      "title": "To direct the removal of United States Armed Forces from hostilities within or against the Republic of Cuba that have not been authorized by Congress.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-23T08:18:28Z"
    },
    {
      "title": "To direct the removal of United States Armed Forces from hostilities within or against the Republic of Cuba that have not been authorized by Congress.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-23T08:07:32Z"
    }
  ]
}
```
