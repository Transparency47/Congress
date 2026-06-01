# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6449?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6449
- Title: DO NOT Call Act
- Congress: 119
- Bill type: HR
- Bill number: 6449
- Origin chamber: House
- Introduced date: 2025-12-04
- Update date: 2026-03-25T08:05:30Z
- Update date including text: 2026-03-25T08:05:30Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-12-04: Introduced in House
- 2025-12-04 - IntroReferral: Introduced in House
- 2025-12-04 - IntroReferral: Introduced in House
- 2025-12-04 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-12-04: Introduced in House

## Actions

- 2025-12-04 - IntroReferral: Introduced in House
- 2025-12-04 - IntroReferral: Introduced in House
- 2025-12-04 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-04",
    "latestAction": {
      "actionDate": "2025-12-04",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6449",
    "number": "6449",
    "originChamber": "House",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "K000392",
        "district": "8",
        "firstName": "David",
        "fullName": "Rep. Kustoff, David [R-TN-8]",
        "lastName": "Kustoff",
        "party": "R",
        "state": "TN"
      }
    ],
    "title": "DO NOT Call Act",
    "type": "HR",
    "updateDate": "2026-03-25T08:05:30Z",
    "updateDateIncludingText": "2026-03-25T08:05:30Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-04",
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
      "actionDate": "2025-12-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-04",
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
          "date": "2025-12-04T14:02:50Z",
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
      "bioguideId": "R000305",
      "district": "2",
      "firstName": "Deborah",
      "fullName": "Rep. Ross, Deborah K. [D-NC-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Ross",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-12-04",
      "state": "NC"
    },
    {
      "bioguideId": "M001217",
      "district": "23",
      "firstName": "Jared",
      "fullName": "Rep. Moskowitz, Jared [D-FL-23]",
      "isOriginalCosponsor": "True",
      "lastName": "Moskowitz",
      "party": "D",
      "sponsorshipDate": "2025-12-04",
      "state": "FL"
    },
    {
      "bioguideId": "F000459",
      "district": "3",
      "firstName": "Charles",
      "fullName": "Rep. Fleischmann, Charles J. \"Chuck\" [R-TN-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Fleischmann",
      "middleName": "J. \"Chuck\"",
      "party": "R",
      "sponsorshipDate": "2025-12-04",
      "state": "TN"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-12-04",
      "state": "PA"
    },
    {
      "bioguideId": "G000600",
      "district": "3",
      "firstName": "Marie",
      "fullName": "Rep. Perez, Marie Gluesenkamp [D-WA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Perez",
      "middleName": "Gluesenkamp",
      "party": "D",
      "sponsorshipDate": "2025-12-04",
      "state": "WA"
    },
    {
      "bioguideId": "P000613",
      "district": "19",
      "firstName": "Jimmy",
      "fullName": "Rep. Panetta, Jimmy [D-CA-19]",
      "isOriginalCosponsor": "True",
      "lastName": "Panetta",
      "party": "D",
      "sponsorshipDate": "2025-12-04",
      "state": "CA"
    },
    {
      "bioguideId": "S001220",
      "district": "5",
      "firstName": "Dale",
      "fullName": "Rep. Strong, Dale W. [R-AL-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Strong",
      "middleName": "W.",
      "party": "R",
      "sponsorshipDate": "2025-12-04",
      "state": "AL"
    },
    {
      "bioguideId": "R000622",
      "district": "19",
      "firstName": "Josh",
      "fullName": "Rep. Riley, Josh [D-NY-19]",
      "isOriginalCosponsor": "False",
      "lastName": "Riley",
      "party": "D",
      "sponsorshipDate": "2025-12-15",
      "state": "NY"
    },
    {
      "bioguideId": "M001237",
      "district": "8",
      "firstName": "Kristen",
      "fullName": "Rep. McDonald Rivet, Kristen [D-MI-8]",
      "isOriginalCosponsor": "False",
      "lastName": "McDonald Rivet",
      "party": "D",
      "sponsorshipDate": "2025-12-16",
      "state": "MI"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-12-23",
      "state": "VA"
    },
    {
      "bioguideId": "G000602",
      "district": "4",
      "firstName": "Laura",
      "fullName": "Rep. Gillen, Laura [D-NY-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Gillen",
      "party": "D",
      "sponsorshipDate": "2025-12-23",
      "state": "NY"
    },
    {
      "bioguideId": "D000629",
      "district": "3",
      "firstName": "Sharice",
      "fullName": "Rep. Davids, Sharice [D-KS-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Davids",
      "party": "D",
      "sponsorshipDate": "2026-01-12",
      "state": "KS"
    },
    {
      "bioguideId": "P000614",
      "district": "1",
      "firstName": "Chris",
      "fullName": "Rep. Pappas, Chris [D-NH-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Pappas",
      "party": "D",
      "sponsorshipDate": "2026-03-24",
      "state": "NH"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6449ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6449\nIN THE HOUSE OF REPRESENTATIVES\nDecember 4, 2025 Mr. Kustoff (for himself, Ms. Ross , Mr. Moskowitz , Mr. Fleischmann , Mr. Fitzpatrick , Ms. Perez , Mr. Panetta , and Mr. Strong ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo modify the penalties for violations of the Telephone Consumer Protection Act of 1993.\n#### 1. Short title\nThis Act may be cited as the Deter Obnoxious, Nefarious, and Outrageous Telephone Calls Act of 2025 or the DO NOT Call Act .\n#### 2. Penalties for violations of the Telephone Consumer Protection Act of 1993\n##### (a) Criminal penalties\n**(1) In general**\nSection 227 of the Communications Act of 1934 ( 47 U.S.C. 227 ) is amended by adding at the end the following:\n(k) Criminal penalties (1) In general Except as provided in paragraph (2), any person who willfully and knowingly violates this section shall be imprisoned for not more than 1 year, fined under title 18, United States Code, or both. (2) Aggravated offense Any person who willfully and knowingly violates this section shall be imprisoned for not more than 3 years, fined under title 18, United States Code, or both if\u2014 (A) the person has previously been convicted under this subsection; (B) the offense involved initiating more than\u2014 (i) 100,000 calls in a 24-hour period; (ii) 1,000,000 calls in a 30-day period; or (iii) 10,000,000 calls in a 1-year period; (C) the person committed the offense with the intent to use the calls in furtherance of a felony or conspiracy to commit a felony; or (D) the offense caused loss to 1 or more persons aggregating $5,000 or more in value during any 1-year period. (3) Definitions For purposes of this subsection\u2014 (A) the term call includes a message or other communication sent to any North American Numbering Plan number, including an emergency telephone number, that is\u2014 (i) initiated to communicate with or attempt to communicate with a person by telephone using an automatic telephone dialing system or artificial or prerecorded voice; or (ii) a text message sent to a mobile phone using an automatic telephone dialing system\u2014 (I) without the prior consent of the recipient to receive the message; or (II) as an emergency message; and (B) the term initiate , with respect to a call, includes the act of sending, making, or transmitting the call. .\n**(2) Technical and conforming amendment**\nSection 227(e)(5)(B) of the Communications Act of 1934 ( 47 U.S.C. 227(e)(5)(B) ) is amended, in the second sentence, by striking section 501 and inserting subsection (k) .\n##### (b) Increased penalties for provision of inaccurate caller identification information\nSection 227(e)(5) of the Communications Act of 1934 ( 47 U.S.C. 227(e)(5) ) is amended\u2014\n**(1)**\nin subparagraph (A)(i), by striking $10,000 and inserting $20,000 ; and\n**(2)**\nin subparagraph (B), in the first sentence, by striking $10,000 and inserting $20,000 .",
      "versionDate": "2025-12-04",
      "versionType": "Introduced in House"
    }
  ]
}
```

## API Data: relatedbills

```json
{
  "relatedBills": [
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-12-04",
        "text": "Read twice and referred to the Committee on Commerce, Science, and Transportation."
      },
      "number": "3370",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "DO NOT Call Act",
      "type": "S"
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
        "name": "Commerce",
        "updateDate": "2026-01-05T16:20:00Z"
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
      "date": "2025-12-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6449ih.xml"
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
      "title": "DO NOT Call Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-23T05:38:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "DO NOT Call Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-23T05:38:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Deter Obnoxious, Nefarious, and Outrageous Telephone Calls Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-23T05:38:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To modify the penalties for violations of the Telephone Consumer Protection Act of 1993.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-23T05:33:19Z"
    }
  ]
}
```
