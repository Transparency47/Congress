# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hconres/74?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-concurrent-resolution/74
- Title: Providing for a joint session of Congress to receive a message from the President.
- Congress: 119
- Bill type: HCONRES
- Bill number: 74
- Origin chamber: House
- Introduced date: 2026-02-10
- Update date: 2026-02-13T18:51:56Z
- Update date including text: 2026-02-13T18:51:56Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, fullTexts, subjects, text, titles

## Timeline

- 2026-02-10: Introduced in House
- 2026-02-10 - IntroReferral: Submitted in House
- 2026-02-10 00:00:00 - Floor: Submitted in House
- 2026-02-10 21:57:35 - Floor: Considered as privileged matter. (consideration: CR H2116-2117)
- 2026-02-10 21:58:11 - Floor: On agreeing to the resolution Agreed to without objection. (text: CR H2116-2117)
- 2026-02-10 21:58:11 - Floor: Passed/agreed to in House: On agreeing to the resolution Agreed to without objection. (text: CR H2116-2117)
- 2026-02-10 21:58:15 - Floor: Motion to reconsider laid on the table Agreed to without objection.
- 2026-02-11 - IntroReferral: Received in the Senate.
- 2026-02-12 - Floor: Message on Senate action sent to the House.
- 2026-02-12 - Floor: Passed/agreed to in Senate: Resolution agreed to in Senate without amendment by Unanimous Consent.
- 2026-02-12 - Floor: Resolution agreed to in Senate without amendment by Unanimous Consent. (consideration: CR S616)
- Latest action: 2026-02-10: Submitted in House

## Actions

- 2026-02-10 - IntroReferral: Submitted in House
- 2026-02-10 00:00:00 - Floor: Submitted in House
- 2026-02-10 21:57:35 - Floor: Considered as privileged matter. (consideration: CR H2116-2117)
- 2026-02-10 21:58:11 - Floor: On agreeing to the resolution Agreed to without objection. (text: CR H2116-2117)
- 2026-02-10 21:58:11 - Floor: Passed/agreed to in House: On agreeing to the resolution Agreed to without objection. (text: CR H2116-2117)
- 2026-02-10 21:58:15 - Floor: Motion to reconsider laid on the table Agreed to without objection.
- 2026-02-11 - IntroReferral: Received in the Senate.
- 2026-02-12 - Floor: Message on Senate action sent to the House.
- 2026-02-12 - Floor: Passed/agreed to in Senate: Resolution agreed to in Senate without amendment by Unanimous Consent.
- 2026-02-12 - Floor: Resolution agreed to in Senate without amendment by Unanimous Consent. (consideration: CR S616)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-10",
    "latestAction": {
      "actionDate": "2026-02-10",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-concurrent-resolution/74",
    "number": "74",
    "originChamber": "House",
    "policyArea": {
      "name": "Congress"
    },
    "sponsors": [
      {
        "bioguideId": "M001199",
        "district": "21",
        "firstName": "Brian",
        "fullName": "Rep. Mast, Brian J. [R-FL-21]",
        "lastName": "Mast",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "Providing for a joint session of Congress to receive a message from the President.",
    "type": "HCONRES",
    "updateDate": "2026-02-13T18:51:56Z",
    "updateDateIncludingText": "2026-02-13T18:51:56Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-02-12",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Message on Senate action sent to the House.",
      "type": "Floor"
    },
    {
      "actionDate": "2026-02-12",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Resolution agreed to in Senate without amendment by Unanimous Consent. (consideration: CR S616)",
      "type": "Floor"
    },
    {
      "actionCode": "17000",
      "actionDate": "2026-02-12",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Passed/agreed to in Senate: Resolution agreed to in Senate without amendment by Unanimous Consent.",
      "type": "Floor"
    },
    {
      "actionDate": "2026-02-11",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Received in the Senate.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H38310",
      "actionDate": "2026-02-10",
      "actionTime": "21:58:15",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Motion to reconsider laid on the table Agreed to without objection.",
      "type": "Floor"
    },
    {
      "actionCode": "H37100",
      "actionDate": "2026-02-10",
      "actionTime": "21:58:11",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "On agreeing to the resolution Agreed to without objection. (text: CR H2116-2117)",
      "type": "Floor"
    },
    {
      "actionCode": "8000",
      "actionDate": "2026-02-10",
      "actionTime": "21:58:11",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Passed/agreed to in House: On agreeing to the resolution Agreed to without objection. (text: CR H2116-2117)",
      "type": "Floor"
    },
    {
      "actionCode": "H30000",
      "actionDate": "2026-02-10",
      "actionTime": "21:57:35",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Considered as privileged matter. (consideration: CR H2116-2117)",
      "type": "Floor"
    },
    {
      "actionCode": "H30000",
      "actionDate": "2026-02-10",
      "actionTime": "00:00:00",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "Floor"
    },
    {
      "actionCode": "1025",
      "actionDate": "2026-02-10",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hconres/BILLS-119hconres74rds.xml",
      "text": "III\n119th CONGRESS\n2d Session\nH. CON. RES. 74\nIN THE SENATE OF THE UNITED STATES\nFebruary 11, 2026 Received\nCONCURRENT RESOLUTION\nProviding for a joint session of Congress to receive a message from the President.\nThat the two Houses of Congress assemble in the Hall of the House of Representatives on Tuesday, February 24, 2026, at 9 p.m., for the purpose of receiving such communication as the President of the United States shall be pleased to make to them.",
      "versionDate": "2026-02-11",
      "versionType": "RDS"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hconres/BILLS-119hconres74eh.xml",
      "text": "IV\n119th CONGRESS\n2d Session\nH. CON. RES. 74\nIN THE HOUSE OF REPRESENTATIVES\nCONCURRENT RESOLUTION\nProviding for a joint session of Congress to receive a message from the President.\nThat the two Houses of Congress assemble in the Hall of the House of Representatives on Tuesday, February 24, 2026, at 9 p.m., for the purpose of receiving such communication as the President of the United States shall be pleased to make to them.",
      "versionDate": "",
      "versionType": "EH"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hconres/BILLS-119hconres74enr.xml",
      "text": "IV\nOne Hundred Nineteenth Congress of the United States of America\nAt the Second Session\nBegun and held at the City of Washington on Saturday, the third day of January, two thousand and twenty-six\nH. CON. RES. 74\nFebruary 12, 2026 Agreed to\nCONCURRENT RESOLUTION\nProviding for a joint session of Congress to receive a message from the President.\nThat the two Houses of Congress assemble in the Hall of the House of Representatives on Tuesday, February 24, 2026, at 9 p.m., for the purpose of receiving such communication as the President of the United States shall be pleased to make to them.",
      "versionDate": "2026-02-12",
      "versionType": "ENR"
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
        "updateDate": "2026-02-13T13:29:44Z"
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
      "date": "2026-02-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hconres/BILLS-119hconres74rds.xml"
        }
      ],
      "type": "RDS"
    },
    {
      "date": "",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hconres/BILLS-119hconres74eh.xml"
        }
      ],
      "type": "EH"
    },
    {
      "date": "2026-02-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hconres/BILLS-119hconres74enr.xml"
        }
      ],
      "type": "ENR"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "EH",
      "billTextVersionName": "Engrossed in House",
      "chamberCode": "H",
      "chamberName": "House",
      "title": "Providing for a joint session of Congress to receive a message from the President.",
      "titleType": "Official Titles from EH (Engrossed in House) bill text",
      "titleTypeCode": "259",
      "updateDate": "2026-02-12T04:08:24Z"
    },
    {
      "title": "Providing for a joint session of Congress to receive a message from the President.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-11T09:06:23Z"
    },
    {
      "title": "Providing for a joint session of Congress to receive a message from the President.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-11T09:06:23Z"
    }
  ]
}
```
