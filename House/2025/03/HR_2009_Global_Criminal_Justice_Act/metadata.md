# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2009?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/2009
- Title: Global Criminal Justice Act
- Congress: 119
- Bill type: HR
- Bill number: 2009
- Origin chamber: House
- Introduced date: 2025-03-10
- Update date: 2025-05-21T13:38:00Z
- Update date including text: 2025-05-21T13:38:00Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-03-10: Introduced in House
- 2025-03-10 - IntroReferral: Introduced in House
- 2025-03-10 - IntroReferral: Introduced in House
- 2025-03-10 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- Latest action: 2025-03-10: Introduced in House

## Actions

- 2025-03-10 - IntroReferral: Introduced in House
- 2025-03-10 - IntroReferral: Introduced in House
- 2025-03-10 - IntroReferral: Referred to the House Committee on Foreign Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-10",
    "latestAction": {
      "actionDate": "2025-03-10",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/2009",
    "number": "2009",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "O000173",
        "district": "5",
        "firstName": "Ilhan",
        "fullName": "Rep. Omar, Ilhan [D-MN-5]",
        "lastName": "Omar",
        "party": "D",
        "state": "MN"
      }
    ],
    "title": "Global Criminal Justice Act",
    "type": "HR",
    "updateDate": "2025-05-21T13:38:00Z",
    "updateDateIncludingText": "2025-05-21T13:38:00Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-10",
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
      "actionCode": "Intro-H",
      "actionDate": "2025-03-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-10",
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
          "date": "2025-03-10T16:01:05Z",
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
      "bioguideId": "J000305",
      "district": "51",
      "firstName": "Sara",
      "fullName": "Rep. Jacobs, Sara [D-CA-51]",
      "isOriginalCosponsor": "True",
      "lastName": "Jacobs",
      "party": "D",
      "sponsorshipDate": "2025-03-10",
      "state": "CA"
    },
    {
      "bioguideId": "C001091",
      "district": "20",
      "firstName": "Joaquin",
      "fullName": "Rep. Castro, Joaquin [D-TX-20]",
      "isOriginalCosponsor": "True",
      "lastName": "Castro",
      "party": "D",
      "sponsorshipDate": "2025-03-10",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2009ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2009\nIN THE HOUSE OF REPRESENTATIVES\nMarch 10, 2025 Ms. Omar (for herself, Ms. Jacobs , and Mr. Castro of Texas ) introduced the following bill; which was referred to the Committee on Foreign Affairs\nA BILL\nTo encourage the establishment in the Department of State of an Office of Global Criminal Justice, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Global Criminal Justice Act .\n#### 2. Office of Global Criminal Justice\n##### (a) In general\nThere is established within the Department of State an Office of Global Criminal Justice (referred to in this section as the Office ), which may be placed within the organizational structure of the Department at the discretion of the Secretary of State.\n##### (b) Duties\nThe duties of the Office are the following:\n**(1)**\nAdvise the Secretary of State and other relevant senior Federal officials on issues related to atrocities, including war crimes, crimes against humanity, and genocide.\n**(2)**\nAssist in formulating United States policy on the prevention of, responses to, and accountability for atrocities.\n**(3)**\nCoordinate, as appropriate and with other relevant Federal departments and agencies, United States Government positions relating to the international and hybrid courts currently prosecuting persons suspected of atrocities around the world.\n**(4)**\nWork with other governments, international organizations, and nongovernmental organizations, as appropriate, to establish and assist international and domestic commissions of inquiry, fact-finding missions, and tribunals to investigate, document, and prosecute atrocities around the world.\n**(5)**\nCoordinate, as appropriate and with other relevant Federal departments and agencies, the deployment of diplomatic, legal, economic, military, and other tools to help collect evidence of atrocities, judge those responsible, protect and assist victims, enable reconciliation, prevent and deter atrocities, and promote the rule of law.\n**(6)**\nProvide advice and expertise on transitional justice mechanisms to United States personnel operating in conflict and post-conflict environments.\n**(7)**\nAct as a point of contact for international, hybrid, and domestic tribunals exercising jurisdiction over atrocities committed around the world.\n**(8)**\nRepresent the Department of State on any interagency whole-of-government coordinating entities addressing genocide and other atrocities.\n**(9)**\nPerform any additional duties and exercise such powers as the Secretary of State may prescribe.\n##### (c) Supervision\nThe Office shall be led by an Ambassador-at-Large for Global Criminal Justice, who shall be nominated by the President and appointed by and with the advice and consent of the Senate.",
      "versionDate": "2025-03-10",
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
        "updateDate": "2025-05-21T13:38:00Z"
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
      "date": "2025-03-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2009ih.xml"
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
      "title": "Global Criminal Justice Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-26T02:08:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Global Criminal Justice Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-26T02:08:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To encourage the establishment in the Department of State of an Office of Global Criminal Justice, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-26T02:03:36Z"
    }
  ]
}
```
