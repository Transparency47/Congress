# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3370?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3370
- Title: DO NOT Call Act
- Congress: 119
- Bill type: S
- Bill number: 3370
- Origin chamber: Senate
- Introduced date: 2025-12-04
- Update date: 2026-02-24T22:26:18Z
- Update date including text: 2026-02-24T22:26:18Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-12-04: Introduced in Senate
- 2025-12-04 - IntroReferral: 
- 2025-12-04 - IntroReferral: Introduced in Senate
- 2025-12-04 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- Latest action: 2025-12-04: Introduced in Senate

## Actions

- 2025-12-04 - IntroReferral: 
- 2025-12-04 - IntroReferral: Introduced in Senate
- 2025-12-04 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.

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
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3370",
    "number": "3370",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "C001113",
        "district": "",
        "firstName": "Catherine",
        "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
        "lastName": "Cortez Masto",
        "party": "D",
        "state": "NV"
      }
    ],
    "title": "DO NOT Call Act",
    "type": "S",
    "updateDate": "2026-02-24T22:26:18Z",
    "updateDateIncludingText": "2026-02-24T22:26:18Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-04",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Commerce, Science, and Transportation.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-S",
      "actionDate": "2025-12-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-12-04",
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
        "item": {
          "date": "2025-12-04T20:13:55Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Commerce, Science, and Transportation Committee",
      "systemCode": "sscm00",
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
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-12-04",
      "state": "MN"
    },
    {
      "bioguideId": "G000555",
      "firstName": "Kirsten",
      "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
      "isOriginalCosponsor": "True",
      "lastName": "Gillibrand",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-12-04",
      "state": "NY"
    },
    {
      "bioguideId": "K000383",
      "firstName": "Angus",
      "fullName": "Sen. King, Angus S., Jr. [I-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "King",
      "middleName": "S.",
      "party": "I",
      "sponsorshipDate": "2025-12-04",
      "state": "ME"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3370is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3370\nIN THE SENATE OF THE UNITED STATES\nDecember 4, 2025 Ms. Cortez Masto (for herself, Ms. Klobuchar , Mrs. Gillibrand , and Mr. King ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo modify the penalties for violations of the Telephone Consumer Protection Act of 1993.\n#### 1. Short title\nThis Act may be cited as the Deter Obnoxious, Nefarious, and Outrageous Telephone Calls Act of 2025 or the DO NOT Call Act .\n#### 2. Penalties for violations of the Telephone Consumer Protection Act of 1993\n##### (a) Criminal penalties\n**(1) In general**\nSection 227 of the Communications Act of 1934 ( 47 U.S.C. 227 ) is amended by adding at the end the following:\n(k) Criminal penalties (1) In general Except as provided in paragraph (2), any person who willfully and knowingly violates this section shall be imprisoned for not more than 1 year, fined under title 18, United States Code, or both. (2) Aggravated offense Any person who willfully and knowingly violates this section shall be imprisoned for not more than 3 years, fined under title 18, United States Code, or both if\u2014 (A) the person has previously been convicted under this subsection; (B) the offense involved initiating more than\u2014 (i) 100,000 calls in a 24-hour period; (ii) 1,000,000 calls in a 30-day period; or (iii) 10,000,000 calls in a 1-year period; (C) the person committed the offense with the intent to use the calls in furtherance of a felony or conspiracy to commit a felony; or (D) the offense caused loss to 1 or more persons aggregating $5,000 or more in value during any 1-year period. (3) Definitions For purposes of this subsection\u2014 (A) the term call includes a message or other communication sent to any North American Numbering Plan number, including an emergency telephone number, that is\u2014 (i) initiated to communicate with or attempt to communicate with a person by telephone using an automatic telephone dialing system or artificial or prerecorded voice; or (ii) a text message sent to a mobile phone using an automatic telephone dialing system\u2014 (I) without the prior consent of the recipient to receive the message; or (II) as an emergency message; and (B) the term initiate , with respect to a call, includes the act of sending, making, or transmitting the call. .\n**(2) Technical and conforming amendment**\nSection 227(e)(5)(B) of the Communications Act of 1934 ( 47 U.S.C. 227(e)(5)(B) ) is amended, in the second sentence, by striking section 501 and inserting subsection (k) .\n##### (b) Increased penalties for provision of inaccurate caller identification information\nSection 227(e)(5) of the Communications Act of 1934 ( 47 U.S.C. 227(e)(5) ) is amended\u2014\n**(1)**\nin subparagraph (A)(i), by striking $10,000 and inserting $20,000 ; and\n**(2)**\nin subparagraph (B), in the first sentence, by striking $10,000 and inserting $20,000 .",
      "versionDate": "2025-12-04",
      "versionType": "Introduced in Senate"
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
        "text": "Referred to the House Committee on Energy and Commerce."
      },
      "number": "6449",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "DO NOT Call Act",
      "type": "HR"
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
        "updateDate": "2026-01-05T16:20:39Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3370is.xml"
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
      "title": "DO NOT Call Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-30T05:38:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "DO NOT Call Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-30T05:38:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Deter Obnoxious, Nefarious, and Outrageous Telephone Calls Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-30T05:38:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to modify the penalties for violations of the Telephone Consumer Protection Act of 1993.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-30T05:33:16Z"
    }
  ]
}
```
