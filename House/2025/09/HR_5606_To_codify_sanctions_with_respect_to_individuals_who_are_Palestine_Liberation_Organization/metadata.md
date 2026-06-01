# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5606?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5606
- Title: Return to PEACE Act
- Congress: 119
- Bill type: HR
- Bill number: 5606
- Origin chamber: House
- Introduced date: 2025-09-26
- Update date: 2025-11-19T21:46:47Z
- Update date including text: 2025-11-19T21:46:47Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-09-26: Introduced in House
- 2025-09-26 - IntroReferral: Introduced in House
- 2025-09-26 - IntroReferral: Introduced in House
- 2025-09-26 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-09-26: Introduced in House

## Actions

- 2025-09-26 - IntroReferral: Introduced in House
- 2025-09-26 - IntroReferral: Introduced in House
- 2025-09-26 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-26",
    "latestAction": {
      "actionDate": "2025-09-26",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5606",
    "number": "5606",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "S001224",
        "district": "3",
        "firstName": "Keith",
        "fullName": "Rep. Self, Keith [R-TX-3]",
        "lastName": "Self",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Return to PEACE Act",
    "type": "HR",
    "updateDate": "2025-11-19T21:46:47Z",
    "updateDateIncludingText": "2025-11-19T21:46:47Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-26",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-09-26",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-26",
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
          "date": "2025-09-26T14:05:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
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
      "bioguideId": "O000175",
      "district": "5",
      "firstName": "Andrew",
      "fullName": "Rep. Ogles, Andrew [R-TN-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Ogles",
      "party": "R",
      "sponsorshipDate": "2025-09-26",
      "state": "TN"
    },
    {
      "bioguideId": "S001196",
      "district": "21",
      "firstName": "Elise",
      "fullName": "Rep. Stefanik, Elise M. [R-NY-21]",
      "isOriginalCosponsor": "False",
      "lastName": "Stefanik",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-10-03",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5606ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5606\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 26, 2025 Mr. Self (for himself and Mr. Ogles ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo codify sanctions with respect to individuals who are Palestine Liberation Organization members and Palestinian Authority officials.\n#### 1. Short title\nThis Act may be cited as the Return to Palestinian Entities Accountability and Counterterrorism Enforcement Act or Return to PEACE Act .\n#### 2. Codification of sanctions with respect to individuals who are Palestine Liberation Organization members and Palestinian Authority officials\n##### (a) In general\nOn and after the date of the enactment of this Act, the sanctions that deny visas to individuals who are members of the Palestine Liberation Organization (PLO) and officials of the Palestinian Authority (PA) pursuant to section 604(a)(1) of the Middle East Peace Facilitation Act, as in effect on July 31, 2025, shall remain in effect and continue to apply except for as provided in subsection (b).\n##### (b) Applicability of waiver\nNotwithstanding section 604(c) of the Foreign Relations Authorization Act, Fiscal Year 2003 ( Public Law 107\u2013228 ), the Secretary of State may, on a case-by-base basis not to exceed renewable periods of 180 days, waive the application of the sanctions codified in subsection (a) with respect to an individual or individuals if the Secretary transmits to the appropriate congressional committees the determination described in subsection (c).\n##### (c) Determination\nA determination described in this subsection is a determination that the PLO and the PA are not\u2014\n**(1)**\ninitiating or supporting actions at international organizations that undermine and contradict prior commitments in support of United Nations Security Council Resolution 242 and 338;\n**(2)**\ntaking actions to internationalize its conflict with Israel such as through the International Criminal Court and International Court of Justice;\n**(3)**\ncontinuing to support terrorism, including incitement and glorification of violence (especially in textbooks); and\n**(4)**\nproviding payments and benefits in support of terrorism to Palestinian terrorists and their families.\n##### (d) Sunset\nThis section shall terminate on the date that is seven years after the date of the enactment of this Act.",
      "versionDate": "2025-09-26",
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
        "name": "International Affairs",
        "updateDate": "2025-11-19T21:46:47Z"
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
      "date": "2025-09-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5606ih.xml"
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
      "title": "Return to PEACE Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-03T07:38:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Return to PEACE Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-03T07:38:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Return to Palestinian Entities Accountability and Counterterrorism Enforcement Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-03T07:38:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To codify sanctions with respect to individuals who are Palestine Liberation Organization members and Palestinian Authority officials.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-03T07:33:38Z"
    }
  ]
}
```
