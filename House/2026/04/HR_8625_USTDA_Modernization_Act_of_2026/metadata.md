# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8625?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8625
- Title: USTDA Modernization Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 8625
- Origin chamber: House
- Introduced date: 2026-04-30
- Update date: 2026-05-12T19:40:07Z
- Update date including text: 2026-05-12T19:40:07Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-04-30: Introduced in House
- 2026-04-30 - IntroReferral: Introduced in House
- 2026-04-30 - IntroReferral: Introduced in House
- 2026-04-30 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- Latest action: 2026-04-30: Introduced in House

## Actions

- 2026-04-30 - IntroReferral: Introduced in House
- 2026-04-30 - IntroReferral: Introduced in House
- 2026-04-30 - IntroReferral: Referred to the House Committee on Foreign Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-30",
    "latestAction": {
      "actionDate": "2026-04-30",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8625",
    "number": "8625",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "M001219",
        "district": "",
        "firstName": "James",
        "fullName": "Del. Moylan, James C. [R-GU-At Large]",
        "lastName": "Moylan",
        "party": "R",
        "state": "GU"
      }
    ],
    "title": "USTDA Modernization Act of 2026",
    "type": "HR",
    "updateDate": "2026-05-12T19:40:07Z",
    "updateDateIncludingText": "2026-05-12T19:40:07Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-30",
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
      "actionDate": "2026-04-30",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-04-30",
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
          "date": "2026-04-30T13:05:10Z",
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
      "bioguideId": "T000487",
      "district": "2",
      "firstName": "Jill",
      "fullName": "Rep. Tokuda, Jill N. [D-HI-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Tokuda",
      "middleName": "N.",
      "party": "D",
      "sponsorshipDate": "2026-04-30",
      "state": "HI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8625ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8625\nIN THE HOUSE OF REPRESENTATIVES\nApril 30, 2026 Mr. Moylan (for himself and Ms. Tokuda ) introduced the following bill; which was referred to the Committee on Foreign Affairs\nA BILL\nTo amend the Foreign Assistance Act of 1961 to authorize assistance for certain development activities in high-income countries, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the United States Trade and Development Agency Modernization Act of 2026 or the USTDA Modernization Act of 2026 .\n#### 2. Sense of Congress\nIt is the sense of Congress that the United States Trade and Development Agency plays a critical role in advancing United States commercial, energy, digital, and infrastructure interests in priority emerging markets by supporting early-stage project preparation and technical assistance and should be authorized to allocate some of its annual program funds for activities in high-income countries that directly affect United States economic and national security.\n#### 3. Expansion of country eligibility\nSection 661(b) of the Foreign Assistance Act of 1961 ( 22 U.S.C. 2421(b) ) is amended\u2014\n**(1)**\nby redesignating paragraphs (3), (4), and (5) as paragraphs (4), (5), and (6), respectively; and\n**(2)**\nby inserting after paragraph (2) the following:\n(3) Assistance in high-income countries Notwithstanding any other provision of law, the Director of the Trade and Development Agency is authorized to provide not more than 15 percent of the total amount of funds appropriated in a fiscal year for assistance under this section for\u2014 (A) activities described in paragraph (2) in high-income countries; or (B) projects in high-income countries that serve United States strategic interests in the energy, critical minerals, transport, or telecommunications sectors. .\n#### 4. Personnel authorities\nSection 661(c) of such Act ( 22 U.S.C. 2421(c) ) is amended\u2014\n**(1)**\nin paragraph (2)(C), by striking 2 and inserting 5 before may be appointed ; and\n**(2)**\nby adding at the end the following:\n(3) Personal services contractors (A) The Trade and Development Agency may contract with individuals for personal services, and such individuals may not be considered Federal employees for the purpose of any provision of law administered by the Director of the Office of Personnel Management. (B) The Director shall submit to Congress an annual report describing the number of individuals contracted for personal services by the Trade and Development Agency, the roles of such contractors, and the costs associated with such contracts. .",
      "versionDate": "2026-04-30",
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
        "updateDate": "2026-05-12T19:40:06Z"
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
      "date": "2026-04-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8625ih.xml"
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
      "title": "USTDA Modernization Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-07T09:23:42Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "USTDA Modernization Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-07T09:23:40Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "United States Trade and Development Agency Modernization Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-07T09:23:40Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Foreign Assistance Act of 1961 to authorize assistance for certain development activities in high-income countries, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-07T09:18:38Z"
    }
  ]
}
```
