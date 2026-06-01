# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2264?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2264
- Title: Advancing VA’s Emergency Response to (AVERT) Crises Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 2264
- Origin chamber: Senate
- Introduced date: 2025-07-14
- Update date: 2026-04-01T19:06:12Z
- Update date including text: 2026-04-01T19:06:12Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-07-14: Introduced in Senate
- 2025-07-14 - IntroReferral: Introduced in Senate
- 2025-07-14 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.
- 2025-12-10 - Committee: Committee on Veterans' Affairs. Hearings held.
- 2026-03-18 - Committee: Committee on Veterans' Affairs. Ordered to be reported with an amendment in the nature of a substitute favorably.
- Latest action: 2025-07-14: Introduced in Senate

## Actions

- 2025-07-14 - IntroReferral: Introduced in Senate
- 2025-07-14 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.
- 2025-12-10 - Committee: Committee on Veterans' Affairs. Hearings held.
- 2026-03-18 - Committee: Committee on Veterans' Affairs. Ordered to be reported with an amendment in the nature of a substitute favorably.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-14",
    "latestAction": {
      "actionDate": "2025-07-14",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2264",
    "number": "2264",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "B001277",
        "district": "",
        "firstName": "Richard",
        "fullName": "Sen. Blumenthal, Richard [D-CT]",
        "lastName": "Blumenthal",
        "party": "D",
        "state": "CT"
      }
    ],
    "title": "Advancing VA\u2019s Emergency Response to (AVERT) Crises Act of 2025",
    "type": "S",
    "updateDate": "2026-04-01T19:06:12Z",
    "updateDateIncludingText": "2026-04-01T19:06:12Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-18",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "ssva00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Veterans' Affairs. Ordered to be reported with an amendment in the nature of a substitute favorably.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-12-10",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "ssva00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Veterans' Affairs. Hearings held.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-07-14",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "ssva00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Veterans' Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-07-14",
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
        "item": [
          {
            "date": "2026-03-18T20:00:16Z",
            "name": "Markup By"
          },
          {
            "date": "2025-12-10T21:00:20Z",
            "name": "Hearings By (full committee)"
          },
          {
            "date": "2025-07-14T20:47:06Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Veterans' Affairs Committee",
      "systemCode": "ssva00",
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
      "sponsorshipDate": "2025-07-14",
      "state": "HI"
    },
    {
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "False",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2025-07-16",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2264is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2264\nIN THE SENATE OF THE UNITED STATES\nJuly 14, 2025 Mr. Blumenthal (for himself and Ms. Hirono ) introduced the following bill; which was read twice and referred to the Committee on Veterans\u2019 Affairs\nA BILL\nTo improve the emergency management capabilities of the Department of Veterans Affairs, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Advancing VA\u2019s Emergency Response to (AVERT) Crises Act of 2025 .\n#### 2. Report on emergency management roles for Department of Veterans Affairs\n##### (a) In general\nNot later than 180 days after the date of the enactment of this Act, the Secretary of Veterans Affairs shall submit to the Committee on Veterans\u2019 Affairs of the Senate and the Committee on Veterans\u2019 Affairs of the House of Representatives a report outlining the roles and responsibilities of all offices of the Department of Veterans Affairs involved with emergency management.\n##### (b) Consultation\nIn preparing the report required by subsection (a), the Secretary of Veterans Affairs shall consult with the Comptroller General of the United States, the Inspector General of the Department of Veterans Affairs, the Secretary of Homeland Security, and such other Federal agencies as the Secretary of Veterans Affairs considers relevant, to obtain insights from their experience and trends that they have found, and such recommendations as they may have with respect to the management by the Department of Veterans Affairs of emergency management functions.\n##### (c) Contents\nThe report submitted pursuant to subsection (a) shall include the following:\n**(1)**\nA description of the organizational structure of each office, both during normal operations and during emergency or disaster operations.\n**(2)**\nThe roles and responsibilities of each office.\n**(3)**\nA detailed description of roles and responsibilities that are shared by both the Office of Emergency Management of the Department and the Office of Operations, Security, and Preparedness of the Department, including an analysis of how each office plays a part in emergency management functions.\n**(4)**\nRecommendations for improving the structure and alignment of relevant offices to better prepare the Department for emergencies, remove redundancies, and improve accountability.\n**(5)**\nAn analysis of the feasibility and advisability of consolidating relevant offices into one centralized emergency management office to improve communication and streamline emergency preparedness and response efforts of the Department.\n#### 3. Report on Regional Readiness Centers of Department of Veterans Affairs\n##### (a) In general\nNot later than 180 days after the date of the enactment of this Act, the Secretary of Veterans Affairs shall submit to the Committee on Veterans\u2019 Affairs of the Senate and the Committee on Veterans\u2019 Affairs of the House of Representatives a report on the Regional Readiness Centers of the Department of Veterans Affairs.\n##### (b) Contents\nThe report submitted pursuant to subsection (a) shall include the following:\n**(1)**\nThe number of requests made by facilities of the Department to obtain supplies from a Regional Readiness Center since the inception of the Regional Readiness Center program, disaggregated by Regional Readiness Center.\n**(2)**\nInformation on types and amounts of material distributed since the inception of the Regional Readiness Center program, disaggregated by Regional Readiness Center.\n**(3)**\nCurrent inventory, disaggregated by Regional Readiness Center.\n**(4)**\nAn overview of the change in inventory in each Regional Readiness Center during the two-year period ending on the date of the enactment of this Act.\n**(5)**\nThe percentage of inventory that is expired or that will expire in the next month, disaggregated by Regional Readiness Center.\n**(6)**\nOperational costs since the inception of the Regional Readiness Center program, disaggregated by Regional Readiness Center.\n**(7)**\nAn analysis of the types and sizes of emergencies, including natural disasters, public health emergencies, or Fourth Mission activations of the Department, with respect to which each Regional Readiness Center would be able to provide sufficient resources to respond to, based on the current capacity of the Regional Readiness Center.\n**(8)**\nAny plans of the Secretary to realign or change the number of Regional Readiness Centers.\n#### 4. Plan to allow fuel sharing and increased coordination between the Federal Emergency Management Agency and the Department of Veterans Affairs\nNot later than 90 days after the date of the enactment of this Act, the Secretary of Veterans Affairs shall, after consulting with the Administrator of the Federal Emergency Management Agency, submit to the Committee on Veterans\u2019 Affairs of the Senate, the Committee on Veterans\u2019 Affairs of the House of Representatives, the Committee on Homeland Security and Government Affairs of the Senate, and the Committee on Homeland Security of the House of Representatives a report regarding\u2014\n**(1)**\nthe current limitations preventing the Federal Emergency Management Agency from providing fuel or other resources to the Department of Veterans Affairs during emergencies;\n**(2)**\nwhether the Department requires action by Congress to allow such resource provision to occur;\n**(3)**\nwhether the Secretary has been unable to coordinate with the Administrator during prior emergencies or Fourth Mission activations due to a lack of authority for such coordination; and\n**(4)**\nwhether the Secretary requires action by Congress to address any of the issues mentioned under paragraph (3).",
      "versionDate": "2025-07-14",
      "versionType": "Introduced in Senate"
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
            "name": "Congressional oversight",
            "updateDate": "2026-01-05T16:11:37Z"
          },
          {
            "name": "Department of Homeland Security",
            "updateDate": "2026-01-05T16:11:52Z"
          },
          {
            "name": "Department of Veterans Affairs",
            "updateDate": "2026-01-05T16:11:45Z"
          },
          {
            "name": "Emergency planning and evacuation",
            "updateDate": "2026-01-05T16:11:41Z"
          },
          {
            "name": "Federal Emergency Management Agency (FEMA)",
            "updateDate": "2026-01-05T16:11:48Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-07-31T22:26:50Z"
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
      "date": "2025-07-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2264is.xml"
        }
      ],
      "type": "Introduced in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Advancing VA\u2019s Emergency Response to (AVERT) Crises Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-19T11:03:27Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Advancing VA\u2019s Emergency Response to (AVERT) Crises Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-31T04:23:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to improve the emergency management capabilities of the Department of Veterans Affairs, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-31T04:18:20Z"
    }
  ]
}
```
