# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8372?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8372
- Title: El Paso VA Medical Center Activation Readiness Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 8372
- Origin chamber: House
- Introduced date: 2026-04-20
- Update date: 2026-05-23T08:07:22Z
- Update date including text: 2026-05-23T08:07:22Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-04-20: Introduced in House
- 2026-04-20 - IntroReferral: Introduced in House
- 2026-04-20 - IntroReferral: Introduced in House
- 2026-04-20 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2026-05-07 - Committee: Referred to the Subcommittee on Oversight and Investigations.
- Latest action: 2026-04-20: Introduced in House

## Actions

- 2026-04-20 - IntroReferral: Introduced in House
- 2026-04-20 - IntroReferral: Introduced in House
- 2026-04-20 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2026-05-07 - Committee: Referred to the Subcommittee on Oversight and Investigations.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-20",
    "latestAction": {
      "actionDate": "2026-04-20",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8372",
    "number": "8372",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "E000299",
        "district": "16",
        "firstName": "Veronica",
        "fullName": "Rep. Escobar, Veronica [D-TX-16]",
        "lastName": "Escobar",
        "party": "D",
        "state": "TX"
      }
    ],
    "title": "El Paso VA Medical Center Activation Readiness Act of 2026",
    "type": "HR",
    "updateDate": "2026-05-23T08:07:22Z",
    "updateDateIncludingText": "2026-05-23T08:07:22Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-05-07",
      "committees": {
        "item": {
          "name": "Oversight and Investigations Subcommittee",
          "systemCode": "hsvr08"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Oversight and Investigations.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-20",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "hsvr00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Veterans' Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-04-20",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-04-20",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
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
          "date": "2026-04-20T16:00:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2026-05-07T13:12:25Z",
              "name": "Referred to"
            }
          },
          "name": "Oversight and Investigations Subcommittee",
          "systemCode": "hsvr08"
        }
      },
      "systemCode": "hsvr00",
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
      "bioguideId": "L000603",
      "district": "8",
      "firstName": "Morgan",
      "fullName": "Rep. Luttrell, Morgan [R-TX-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Luttrell",
      "party": "R",
      "sponsorshipDate": "2026-04-20",
      "state": "TX"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8372ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8372\nIN THE HOUSE OF REPRESENTATIVES\nApril 20, 2026 Ms. Escobar (for herself and Mr. Luttrell ) introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo direct the Secretary of Veterans Affairs to provide to certain congressional committees a briefing on the medical center of the Department of Veterans Affairs in El Paso, Texas, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the El Paso VA Medical Center Activation Readiness Act of 2026 .\n#### 2. Briefing on medical center of Department of Veterans Affairs in El Paso, Texas\n##### (a) In general\nNot later than 180 days after the date of the enactment of this Act, the Secretary of Veterans Affairs shall provide to the appropriate congressional committees a briefing on the medical center of the Department of Veterans Affairs under construction in El Paso, Texas, which shall include information on the following with respect to such center:\n**(1)**\nStaffing requirements and recruitment plans, including with respect to both clinical and support staff.\n**(2)**\nWorkforce stability and hiring capacity, including any impacts of workforce restructuring, hiring limitations, or reductions in force on the ability of the Secretary to recruit, retain, and fully staff the medical center.\n**(3)**\nThe timeline for the procurement and installation of medical equipment.\n**(4)**\nThe specialty care services to be furnished to veterans.\n**(5)**\nThe demand for care in the area to be served.\n**(6)**\nAny plans to transfer the care of veterans from other facilities or providers.\n**(7)**\nAny plans to coordinate with medical facilities of the Department of Defense, including the William Beaumont Army Medical Center, to ensure continuity of care.\n**(8)**\nAny access or travel issues for recipients of care from both rural and urban communities and plans to address such issues, including through coordination with transportation providers and municipalities and other government entities.\n##### (b) Appropriate congressional committees defined\nIn this section, the term appropriate congressional committees means\u2014\n**(1)**\nthe Committees on Veterans\u2019 Affairs of the Senate and House of Representatives; and\n**(2)**\nthe Committees on Appropriations of the Senate and House of Representatives.",
      "versionDate": "2026-04-20",
      "versionType": "Introduced in House"
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
        "updateDate": "2026-04-27T22:37:39Z"
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
      "date": "2026-04-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8372ih.xml"
        }
      ],
      "type": "Introduced in House"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "El Paso VA Medical Center Activation Readiness Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-23T12:23:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "El Paso VA Medical Center Activation Readiness Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-23T12:23:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Secretary of Veterans Affairs to provide to certain congressional committees a briefing on the medical center of the Department of Veterans Affairs in El Paso, Texas, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-23T12:18:37Z"
    }
  ]
}
```
