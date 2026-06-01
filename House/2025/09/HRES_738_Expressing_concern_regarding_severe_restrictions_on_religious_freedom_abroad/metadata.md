# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/738?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/738
- Title: Expressing concern regarding severe restrictions on religious freedom abroad.
- Congress: 119
- Bill type: HRES
- Bill number: 738
- Origin chamber: House
- Introduced date: 2025-09-18
- Update date: 2025-10-25T08:05:42Z
- Update date including text: 2025-10-25T08:05:42Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-09-18: Introduced in House
- 2025-09-18 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2025-09-18 - IntroReferral: Submitted in House
- 2025-09-18 - IntroReferral: Submitted in House
- Latest action: 2025-09-18: Submitted in House

## Actions

- 2025-09-18 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2025-09-18 - IntroReferral: Submitted in House
- 2025-09-18 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-18",
    "latestAction": {
      "actionDate": "2025-09-18",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/738",
    "number": "738",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "H001072",
        "district": "2",
        "firstName": "J.",
        "fullName": "Rep. Hill, J. French [R-AR-2]",
        "lastName": "Hill",
        "party": "R",
        "state": "AR"
      }
    ],
    "title": "Expressing concern regarding severe restrictions on religious freedom abroad.",
    "type": "HRES",
    "updateDate": "2025-10-25T08:05:42Z",
    "updateDateIncludingText": "2025-10-25T08:05:42Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-18",
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
      "actionCode": "H11100",
      "actionDate": "2025-09-18",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-09-18",
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
          "date": "2025-09-18T14:06:30Z",
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
      "bioguideId": "M000312",
      "district": "2",
      "firstName": "James",
      "fullName": "Rep. McGovern, James P. [D-MA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "McGovern",
      "middleName": "P.",
      "party": "D",
      "sponsorshipDate": "2025-09-18",
      "state": "MA"
    },
    {
      "bioguideId": "P000197",
      "district": "11",
      "firstName": "Nancy",
      "fullName": "Rep. Pelosi, Nancy [D-CA-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Pelosi",
      "party": "D",
      "sponsorshipDate": "2025-10-21",
      "state": "CA"
    },
    {
      "bioguideId": "M001218",
      "district": "7",
      "firstName": "Richard",
      "fullName": "Rep. McCormick, Richard [R-GA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "McCormick",
      "party": "R",
      "sponsorshipDate": "2025-10-24",
      "state": "GA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres738ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 738\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 18, 2025 Mr. Hill of Arkansas (for himself and Mr. McGovern ) submitted the following resolution; which was referred to the Committee on Foreign Affairs\nRESOLUTION\nExpressing concern regarding severe restrictions on religious freedom abroad.\nThat the House of Representatives\u2014\n**(1)**\naffirms that the United States should actively maintain its position of global leadership in the advancement of freedom of religion abroad;\n**(2)**\nurges the Secretary of State to engage robustly with allies and partners on religious freedom; and\n**(3)**\naffirms the importance of the offices of the Ambassador-at-Large for International Religious Freedom and the Special Envoy to Monitor and Combat Antisemitism.",
      "versionDate": "2025-09-18",
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
        "updateDate": "2025-09-19T16:33:27Z"
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
      "date": "2025-09-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres738ih.xml"
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
      "title": "Expressing concern regarding severe restrictions on religious freedom abroad.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-19T08:18:17Z"
    },
    {
      "title": "Expressing concern regarding severe restrictions on religious freedom abroad.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-19T08:07:52Z"
    }
  ]
}
```
