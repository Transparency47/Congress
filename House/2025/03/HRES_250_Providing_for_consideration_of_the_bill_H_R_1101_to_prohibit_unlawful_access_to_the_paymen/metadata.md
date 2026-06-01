# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/250?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hres/250
- Title: Providing for consideration of the bill (H.R. 1101) to prohibit unlawful access to the payment system of the Bureau of the Fiscal Service within the Department of the Treasury, and for other purposes.
- Congress: 119
- Bill type: HRES
- Bill number: 250
- Origin chamber: House
- Introduced date: 2025-03-25
- Update date: 2025-05-01T12:11:35Z
- Update date including text: 2025-05-01T12:11:35Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-03-25: Introduced in House
- 2025-03-25 - IntroReferral: Referred to the House Committee on Rules.
- 2025-03-25 - IntroReferral: Submitted in House
- 2025-03-25 - IntroReferral: Submitted in House
- 2025-04-09 - Discharge: Motion to Discharge Committee filed by Mr. Casten. Petition No: 119-2. (<a href="https://clerk.house.gov/DischargePetition/2025040902">Discharge petition</a> text with signatures.)
- Latest action: 2025-03-25: Submitted in House

## Actions

- 2025-03-25 - IntroReferral: Referred to the House Committee on Rules.
- 2025-03-25 - IntroReferral: Submitted in House
- 2025-03-25 - IntroReferral: Submitted in House
- 2025-04-09 - Discharge: Motion to Discharge Committee filed by Mr. Casten. Petition No: 119-2. (<a href="https://clerk.house.gov/DischargePetition/2025040902">Discharge petition</a> text with signatures.)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-25",
    "latestAction": {
      "actionDate": "2025-03-25",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hres/250",
    "number": "250",
    "originChamber": "House",
    "policyArea": {
      "name": "Congress"
    },
    "sponsors": [
      {
        "bioguideId": "C001117",
        "district": "6",
        "firstName": "Sean",
        "fullName": "Rep. Casten, Sean [D-IL-6]",
        "lastName": "Casten",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "Providing for consideration of the bill (H.R. 1101) to prohibit unlawful access to the payment system of the Bureau of the Fiscal Service within the Department of the Treasury, and for other purposes.",
    "type": "HRES",
    "updateDate": "2025-05-01T12:11:35Z",
    "updateDateIncludingText": "2025-05-01T12:11:35Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H17000",
      "actionDate": "2025-04-09",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Motion to Discharge Committee filed by Mr. Casten. Petition No: 119-2. (<a href=\"https://clerk.house.gov/DischargePetition/2025040902\">Discharge petition</a> text with signatures.)",
      "type": "Discharge"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-25",
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
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-25",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-03-25",
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
          "date": "2025-03-25T14:05:00Z",
          "name": "Referred To"
        }
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
      "bioguideId": "S001215",
      "district": "11",
      "firstName": "Haley",
      "fullName": "Rep. Stevens, Haley M. [D-MI-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Stevens",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-03-25",
      "state": "MI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres250ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 250\nIN THE HOUSE OF REPRESENTATIVES\nMarch 25, 2025 Mr. Casten (for himself and Ms. Stevens ) submitted the following resolution; which was referred to the Committee on Rules\nRESOLUTION\nProviding for consideration of the bill (H.R. 1101) to prohibit unlawful access to the payment system of the Bureau of the Fiscal Service within the Department of the Treasury, and for other purposes.\nThat immediately upon adoption of this resolution, the House shall proceed to the consideration in the House of the bill (H.R. 1101) to prohibit unlawful access to the payment system of the Bureau of the Fiscal Service within the Department of the Treasury, and for other purposes. All points of order against consideration of the bill are waived. The bill shall be considered as read. All points of order against provisions in the bill are waived. The previous question shall be considered as ordered on the bill and on any amendment thereto to final passage without intervening motion except: (1) one hour of debate equally divided and controlled by the chair and ranking minority member of the Committee on Financial Services or their respective designees; and (2) one motion to recommit.\n#### 2.\nClause 1(c) of rule XIX and clause 8 of rule XX shall not apply to the consideration of H.R. 1101.\n#### 3.\nThe Clerk shall transmit to the Senate a message that the House has passed H.R. 1101 no later than one week after passage.",
      "versionDate": "2025-03-25",
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
        "updateDate": "2025-05-01T12:11:35Z"
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
      "date": "2025-03-25",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres250ih.xml"
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
      "title": "Providing for consideration of the bill (H.R. 1101) to prohibit unlawful access to the payment system of the Bureau of the Fiscal Service within the Department of the Treasury, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-26T08:18:24Z"
    },
    {
      "title": "Providing for consideration of the bill (H.R. 1101) to prohibit unlawful access to the payment system of the Bureau of the Fiscal Service within the Department of the Treasury, and for other purposes.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-26T08:06:37Z"
    }
  ]
}
```
