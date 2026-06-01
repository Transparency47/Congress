# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/164?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/164
- Title: Providing for the consideration of the resolution (H. Res. 23) permitting parental remote voting by proxy, and for other purposes.
- Congress: 119
- Bill type: HRES
- Bill number: 164
- Origin chamber: House
- Introduced date: 2025-02-25
- Update date: 2026-01-07T16:22:05Z
- Update date including text: 2026-01-07T16:22:05Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-02-25: Introduced in House
- 2025-02-25 - IntroReferral: Referred to the House Committee on Rules.
- 2025-03-10 - Discharge: Motion to Discharge Committee filed by Mrs. Luna. Petition No: 119-1. (<a href="https://clerk.house.gov/DischargePetition/2025031001">Discharge petition</a> text with signatures.)
- 2025-03-11 - Discharge: Motion to discharge the Committee on Rules filed by Mrs. Luna. Assigned to the Discharge Calendar, Calendar No. 1. (consideration: CR H1146)
- 2025-04-01 12:01:49 - Floor: NOTIFICATION OF INTENT TO OFFER MOTION TO DISCHARGE - Mrs. Luna notified the House of her intent to offer a motion to discharge the Committee on Rules pursuant to clause 2(c) of rule XV. The Chair announced that the House will entertain the gentlewoman's motion within two legislative days.
- 2025-04-08 12:03:00 - Floor: NOTIFICATION OF INTENT TO OFFER MOTION TO DISCHARGE - Ms. Pettersen notified the House of her intent to offer a motion to discharge the Committee on Rules pursuant to clause 2(c) of rule XV. The Chair announced that the House will entertain the gentlewoman's motion within two legislative days.
- 2025-04-08 15:23:31 - Floor: Pursuant to the provisions of H. Res. 294, H. Res. 164 is laid on the table.
- Latest action: 2025-02-25: Referred to the House Committee on Rules.

## Actions

- 2025-02-25 - IntroReferral: Referred to the House Committee on Rules.
- 2025-03-10 - Discharge: Motion to Discharge Committee filed by Mrs. Luna. Petition No: 119-1. (<a href="https://clerk.house.gov/DischargePetition/2025031001">Discharge petition</a> text with signatures.)
- 2025-03-11 - Discharge: Motion to discharge the Committee on Rules filed by Mrs. Luna. Assigned to the Discharge Calendar, Calendar No. 1. (consideration: CR H1146)
- 2025-04-01 12:01:49 - Floor: NOTIFICATION OF INTENT TO OFFER MOTION TO DISCHARGE - Mrs. Luna notified the House of her intent to offer a motion to discharge the Committee on Rules pursuant to clause 2(c) of rule XV. The Chair announced that the House will entertain the gentlewoman's motion within two legislative days.
- 2025-04-08 12:03:00 - Floor: NOTIFICATION OF INTENT TO OFFER MOTION TO DISCHARGE - Ms. Pettersen notified the House of her intent to offer a motion to discharge the Committee on Rules pursuant to clause 2(c) of rule XV. The Chair announced that the House will entertain the gentlewoman's motion within two legislative days.
- 2025-04-08 15:23:31 - Floor: Pursuant to the provisions of H. Res. 294, H. Res. 164 is laid on the table.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-25",
    "latestAction": {
      "actionDate": "2025-02-25",
      "text": "Referred to the House Committee on Rules."
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/164",
    "number": "164",
    "originChamber": "House",
    "policyArea": {
      "name": "Families"
    },
    "sponsors": [
      {
        "bioguideId": "L000596",
        "district": "13",
        "firstName": "Anna Paulina",
        "fullName": "Rep. Luna, Anna Paulina [R-FL-13]",
        "lastName": "Luna",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "Providing for the consideration of the resolution (H. Res. 23) permitting parental remote voting by proxy, and for other purposes.",
    "type": "HRES",
    "updateDate": "2026-01-07T16:22:05Z",
    "updateDateIncludingText": "2026-01-07T16:22:05Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H1B000",
      "actionDate": "2025-04-08",
      "actionTime": "15:23:31",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Pursuant to the provisions of H. Res. 294, H. Res. 164 is laid on the table.",
      "type": "Floor"
    },
    {
      "actionCode": "H8D000",
      "actionDate": "2025-04-08",
      "actionTime": "12:03:00",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "NOTIFICATION OF INTENT TO OFFER MOTION TO DISCHARGE - Ms. Pettersen notified the House of her intent to offer a motion to discharge the Committee on Rules pursuant to clause 2(c) of rule XV. The Chair announced that the House will entertain the gentlewoman's motion within two legislative days.",
      "type": "Floor"
    },
    {
      "actionCode": "H8D000",
      "actionDate": "2025-04-01",
      "actionTime": "12:01:49",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "NOTIFICATION OF INTENT TO OFFER MOTION TO DISCHARGE - Mrs. Luna notified the House of her intent to offer a motion to discharge the Committee on Rules pursuant to clause 2(c) of rule XV. The Chair announced that the House will entertain the gentlewoman's motion within two legislative days.",
      "type": "Floor"
    },
    {
      "actionCode": "H12450",
      "actionDate": "2025-03-11",
      "committees": {
        "item": {
          "name": "Rules Committee",
          "systemCode": "hsru00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Motion to discharge the Committee on Rules filed by Mrs. Luna. Assigned to the Discharge Calendar, Calendar No. 1. (consideration: CR H1146)",
      "type": "Discharge"
    },
    {
      "actionCode": "H17000",
      "actionDate": "2025-03-10",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Motion to Discharge Committee filed by Mrs. Luna. Petition No: 119-1. (<a href=\"https://clerk.house.gov/DischargePetition/2025031001\">Discharge petition</a> text with signatures.)",
      "type": "Discharge"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-25",
      "committees": {
        "item": {
          "name": "Rules Committee",
          "systemCode": "hsru00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Rules.",
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
        "item": [
          {
            "date": "2025-03-11T22:01:33Z",
            "name": "Unknown"
          },
          {
            "date": "2025-02-25T15:04:00Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "House",
      "name": "Rules Committee",
      "systemCode": "hsru00",
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
      "bioguideId": "P000620",
      "district": "7",
      "firstName": "Brittany",
      "fullName": "Rep. Pettersen, Brittany [D-CO-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Pettersen",
      "party": "D",
      "sponsorshipDate": "2025-02-25",
      "state": "CO"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-02-25",
      "state": "NY"
    },
    {
      "bioguideId": "J000305",
      "district": "51",
      "firstName": "Sara",
      "fullName": "Rep. Jacobs, Sara [D-CA-51]",
      "isOriginalCosponsor": "True",
      "lastName": "Jacobs",
      "party": "D",
      "sponsorshipDate": "2025-02-25",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres164ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 164\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 25, 2025 Mrs. Luna (for herself, Ms. Pettersen , Mr. Lawler , and Ms. Jacobs ) submitted the following resolution; which was referred to the Committee on Rules\nRESOLUTION\nProviding for the consideration of the resolution (H. Res. 23) permitting parental remote voting by proxy, and for other purposes.\nThat immediately upon adoption of this resolution, without intervention of any point of order, the House shall proceed to the consideration in the House of the resolution (H. Res. 23) permitting parental remote voting by proxy, and for other purposes. The resolution shall be considered as read. The previous question shall be considered as ordered on the resolution to adoption without intervening motion or demand for division of the question except one hour of debate equally divided and controlled by the chair and ranking minority member of the Committee on Rules or their respective designees.\n#### 2.\nClause 1(c) of rule XIX shall not apply to the consideration of H. Res. 23.",
      "versionDate": "2025-02-25",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "House of Representatives",
            "updateDate": "2025-03-21T18:44:44Z"
          },
          {
            "name": "Legislative rules and procedure",
            "updateDate": "2025-03-21T18:44:48Z"
          }
        ]
      },
      "policyArea": {
        "name": "Families",
        "updateDate": "2025-03-01T17:27:41Z"
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
      "date": "2025-02-25",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres164ih.xml"
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
      "title": "Providing for the consideration of the resolution (H. Res. 23) permitting parental remote voting by proxy, and for other purposes.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-03T13:58:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Providing for the consideration of the resolution (H. Res. 23) permitting parental remote voting by proxy, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-26T11:18:31Z"
    }
  ]
}
```
