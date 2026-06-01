# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7482?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7482
- Title: LymeX Authorization Act
- Congress: 119
- Bill type: HR
- Bill number: 7482
- Origin chamber: House
- Introduced date: 2026-02-11
- Update date: 2026-04-14T08:05:42Z
- Update date including text: 2026-04-14T08:05:42Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-02-11: Introduced in House
- 2026-02-11 - IntroReferral: Introduced in House
- 2026-02-11 - IntroReferral: Introduced in House
- 2026-02-11 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2026-02-11: Introduced in House

## Actions

- 2026-02-11 - IntroReferral: Introduced in House
- 2026-02-11 - IntroReferral: Introduced in House
- 2026-02-11 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-11",
    "latestAction": {
      "actionDate": "2026-02-11",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7482",
    "number": "7482",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "S000522",
        "district": "4",
        "firstName": "Christopher",
        "fullName": "Rep. Smith, Christopher H. [R-NJ-4]",
        "lastName": "Smith",
        "party": "R",
        "state": "NJ"
      }
    ],
    "title": "LymeX Authorization Act",
    "type": "HR",
    "updateDate": "2026-04-14T08:05:42Z",
    "updateDateIncludingText": "2026-04-14T08:05:42Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-11",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-02-11",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-02-11",
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
          "date": "2026-02-11T16:01:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
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
      "bioguideId": "D000399",
      "district": "37",
      "firstName": "Lloyd",
      "fullName": "Rep. Doggett, Lloyd [D-TX-37]",
      "isOriginalCosponsor": "True",
      "lastName": "Doggett",
      "party": "D",
      "sponsorshipDate": "2026-02-11",
      "state": "TX"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2026-02-23",
      "state": "NJ"
    },
    {
      "bioguideId": "M001223",
      "district": "2",
      "firstName": "Seth",
      "fullName": "Rep. Magaziner, Seth [D-RI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Magaziner",
      "party": "D",
      "sponsorshipDate": "2026-04-13",
      "state": "RI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7482ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7482\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 11, 2026 Mr. Smith of New Jersey (for himself and Mr. Doggett ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo authorize the Secretary of Health and Human Services to fund prize competitions to accelerate innovation in the prevention, diagnosis, and treatment of Lyme disease, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the LymeX Authorization Act .\n#### 2. Policy\nIt is the policy of the United States to\u2014\n**(1)**\nengage stakeholders, including academia, nonprofits, industry, small business, entrepreneurs, and government to facilitate patient-centered innovations in Lyme disease care;\n**(2)**\nfoster breakthroughs in health education and public awareness initiatives focused on Lyme disease patients; and\n**(3)**\naccelerate development of next-gen diagnostics that are rapid and patient focused.\n#### 3. Authorization of appropriations\nThere is authorized to be appropriated to the Secretary of Health and Human Services $5,000,000 to carry out prize competitions (as defined in section 24 of the Stevenson-Wydler Technology Innovation Act of 1980 ( 15 U.S.C. 3719 )) to accelerate innovation in the prevention, diagnosis, and treatment of Lyme disease.",
      "versionDate": "2026-02-11",
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
        "name": "Health",
        "updateDate": "2026-02-19T19:11:26Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7482ih.xml"
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
      "title": "LymeX Authorization Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-18T09:53:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "LymeX Authorization Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-18T09:53:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To authorize the Secretary of Health and Human Services to fund prize competitions to accelerate innovation in the prevention, diagnosis, and treatment of Lyme disease, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-18T09:48:24Z"
    }
  ]
}
```
