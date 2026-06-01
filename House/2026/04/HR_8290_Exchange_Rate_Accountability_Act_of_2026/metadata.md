# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8290?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8290
- Title: Exchange Rate Accountability Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 8290
- Origin chamber: House
- Introduced date: 2026-04-15
- Update date: 2026-04-29T13:50:24Z
- Update date including text: 2026-04-29T13:50:24Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-04-15: Introduced in House
- 2026-04-15 - IntroReferral: Introduced in House
- 2026-04-15 - IntroReferral: Introduced in House
- 2026-04-15 - IntroReferral: Referred to the House Committee on Financial Services.
- 2026-04-21 - Committee: Committee Consideration and Mark-up Session Held
- 2026-04-21 - Committee: Ordered to be Reported by the Yeas and Nays: 32 - 20.
- Latest action: 2026-04-15: Introduced in House

## Actions

- 2026-04-15 - IntroReferral: Introduced in House
- 2026-04-15 - IntroReferral: Introduced in House
- 2026-04-15 - IntroReferral: Referred to the House Committee on Financial Services.
- 2026-04-21 - Committee: Committee Consideration and Mark-up Session Held
- 2026-04-21 - Committee: Ordered to be Reported by the Yeas and Nays: 32 - 20.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-15",
    "latestAction": {
      "actionDate": "2026-04-15",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8290",
    "number": "8290",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "S000250",
        "district": "17",
        "firstName": "Pete",
        "fullName": "Rep. Sessions, Pete [R-TX-17]",
        "lastName": "Sessions",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Exchange Rate Accountability Act of 2026",
    "type": "HR",
    "updateDate": "2026-04-29T13:50:24Z",
    "updateDateIncludingText": "2026-04-29T13:50:24Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-04-21",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Ordered to be Reported by the Yeas and Nays: 32 - 20.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-04-21",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Committee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-15",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Financial Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-04-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-04-15",
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
        "item": [
          {
            "date": "2026-04-21T15:04:00Z",
            "name": "Markup By"
          },
          {
            "date": "2026-04-15T14:03:00Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "House",
      "name": "Financial Services Committee",
      "systemCode": "hsba00",
      "type": "Standing"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8290ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8290\nIN THE HOUSE OF REPRESENTATIVES\nApril 15, 2026 Mr. Sessions introduced the following bill; which was referred to the Committee on Financial Services\nA BILL\nTo require the use of the voice and vote of the United States to oppose any quota increase at the International Monetary Fund for member countries that employ certain exchange rate practices, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Exchange Rate Accountability Act of 2026 .\n#### 2. Opposition to IMF quota increase for countries that undermine the balanced growth of international trade\nThe Bretton Woods Agreements Act ( 22 U.S.C. 286\u2013286aaa ) is amended\u2014\n**(1)**\nby redesignating the 2nd section 73 (as added by section 1901 of division P of Public Law 116\u201394 ) as section 74; and\n**(2)**\nby adding at the end the following:\n75. Opposition to quota increase for countries that undermine the balanced growth of international trade (a) In general Not less than 7 days before consideration of any proposal to increase the quota of a foreign member of the Fund that is one of the 10 largest shareholders in the Fund, the Secretary of the Treasury shall submit a report to the Committee on Financial Services of the House of Representatives and the Committee on Foreign Relations of the Senate that sets forth a determination by the Secretary as to whether the foreign member meets the following criteria: (1) The member, in the preceding 12 months, does not appear to have been in violation of the obligations of the member under Article VIII of the Articles of Agreement of the Fund, based on publicly available data. (2) The member\u2014 (A) maintains transparent exchange rate policies and practices; and (B) publishes credible balance of payments data. (3) To the extent that the member, in the preceding 12 months, has recorded a current account surplus, the member has not persistently managed the rate of exchange between its currency and the United States dollar for purposes of preventing effective balance of payments adjustments or gaining unfair competitive advantage in international trade. (b) Effect of determination On determining that a foreign member of the Fund has failed to meet any of the criteria set forth in subsection (a), the Secretary shall instruct the Governor of the Fund to use the voice and vote of the United States to oppose the proposal to increase the quota of the member in the Fund. (c) Waiver The President may waive subsection (b) with respect to a member of the Fund on reporting to the Committee on Financial Services of the House of Representatives and the Committee on Foreign Relations of the Senate that the waiver is important to the national interest of the United States, with an explanation of the reasons therefor. (d) Proposal consideration For purposes of this section, consideration of a proposal to increase the quota of a foreign member of the Fund does not include consent to an amendment to the Articles of Agreement of the Fund that has been authorized by law. (e) Sunset This section shall cease to have force or effect 7 years after the date of the enactment of this Act. .",
      "versionDate": "2026-04-15",
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
        "updateDate": "2026-04-20T22:29:56Z"
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
      "date": "2026-04-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8290ih.xml"
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
      "title": "Exchange Rate Accountability Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-16T08:23:32Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Exchange Rate Accountability Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-16T08:23:31Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the use of the voice and vote of the United States to oppose any quota increase at the International Monetary Fund for member countries that employ certain exchange rate practices, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-16T08:18:30Z"
    }
  ]
}
```
