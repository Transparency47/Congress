# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3533?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3533
- Title: Blockchain Regulatory Certainty Act
- Congress: 119
- Bill type: HR
- Bill number: 3533
- Origin chamber: House
- Introduced date: 2025-05-21
- Update date: 2026-03-19T08:07:15Z
- Update date including text: 2026-03-19T08:07:15Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-05-21: Introduced in House
- 2025-05-21 - IntroReferral: Introduced in House
- 2025-05-21 - IntroReferral: Introduced in House
- 2025-05-21 - IntroReferral: Referred to the House Committee on Financial Services.
- Latest action: 2025-05-21: Introduced in House

## Actions

- 2025-05-21 - IntroReferral: Introduced in House
- 2025-05-21 - IntroReferral: Introduced in House
- 2025-05-21 - IntroReferral: Referred to the House Committee on Financial Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-21",
    "latestAction": {
      "actionDate": "2025-05-21",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3533",
    "number": "3533",
    "originChamber": "House",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "E000294",
        "district": "6",
        "firstName": "Tom",
        "fullName": "Rep. Emmer, Tom [R-MN-6]",
        "lastName": "Emmer",
        "party": "R",
        "state": "MN"
      }
    ],
    "title": "Blockchain Regulatory Certainty Act",
    "type": "HR",
    "updateDate": "2026-03-19T08:07:15Z",
    "updateDateIncludingText": "2026-03-19T08:07:15Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-21",
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
      "actionDate": "2025-05-21",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-21",
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
          "date": "2025-05-21T14:00:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Financial Services Committee",
      "systemCode": "hsba00",
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
      "bioguideId": "T000486",
      "district": "15",
      "firstName": "Ritchie",
      "fullName": "Rep. Torres, Ritchie [D-NY-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Torres",
      "party": "D",
      "sponsorshipDate": "2025-05-21",
      "state": "NY"
    },
    {
      "bioguideId": "H001058",
      "district": "4",
      "firstName": "Bill",
      "fullName": "Rep. Huizenga, Bill [R-MI-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Huizenga",
      "party": "R",
      "sponsorshipDate": "2025-06-06",
      "state": "MI"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2025-06-23",
      "state": "NJ"
    },
    {
      "bioguideId": "D000626",
      "district": "8",
      "firstName": "Warren",
      "fullName": "Rep. Davidson, Warren [R-OH-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Davidson",
      "party": "R",
      "sponsorshipDate": "2025-12-01",
      "state": "OH"
    },
    {
      "bioguideId": "K000398",
      "district": "7",
      "firstName": "Thomas",
      "fullName": "Rep. Kean, Thomas H. [R-NJ-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Kean",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2026-03-18",
      "state": "NJ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3533ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3533\nIN THE HOUSE OF REPRESENTATIVES\nMay 21, 2025 Mr. Emmer (for himself and Mr. Torres of New York ) introduced the following bill; which was referred to the Committee on Financial Services\nA BILL\nTo provide a safe harbor from licensing and registration for certain non-controlling blockchain developers and providers of blockchain services.\n#### 1. Short title\nThis Act may be cited as the Blockchain Regulatory Certainty Act .\n#### 2. Safe harbor for non-controlling blockchain developers and providers of blockchain services\n##### (a) Protection for non-Controlling blockchain services and software developers\nNo blockchain developer or provider of a blockchain service shall be treated as a money transmitter or as engaging in money transmitting (as defined under any State or Federal law), a financial institution (as defined under section 5312 of title 31, United States Code), any other State or Federal legal designation requiring licensing or registration, or triggering liability for unlicensed or unregistered conduct, unless the developer or provider has, in the regular course of business, control over digital assets to which a user is entitled under the blockchain service or the software created, maintained, or disseminated by the blockchain developer or provider.\n##### (b) Effect on other laws\n**(1) Intellectual property law**\nNothing in this section shall be construed to limit or expand any law pertaining to intellectual property.\n**(2) State law**\nNothing in this section shall be construed to prevent any State from enforcing any State law that is consistent with this section. No cause of action may be brought and no liability may be imposed under any State or local law that is inconsistent with this section.\n##### (c) Definitions\nAs used in this section:\n**(1) Blockchain developer**\nThe term blockchain developer means any person or business that creates, maintains, or disseminates software facilitating the creation or maintenance of a blockchain network or a blockchain service.\n**(2) Blockchain network**\nThe term blockchain network means any system of networked computers that cooperates to reach consensus over the state of a computer program and allows users to participate in the consensus-making process without the need to license proprietary software or obtain permission from any other user. The term blockchain network includes, specifically, a public network of computers that cooperates to reach consensus over the state of a distributed ledger describing transactions in a digital asset.\n**(3) Blockchain service**\nThe term blockchain service means any information, transaction, or computing service or system that provides or enables access to a blockchain network by multiple users, including specifically a service or system that enables users to send, receive, exchange, or store digital assets described by blockchain networks.\n**(4) Control**\nThe term control means the unilateral and independent legal right, authority, or ability to obtain upon demand data sufficient to initiate transactions spending an amount of digital assets, without requiring the approval, consent, or direction of any other third party.\n**(5) Digital asset**\nThe term digital asset means any form of intangible personal property that can be exclusively possessed and transferred person to person without necessary reliance on an intermediary.",
      "versionDate": "2025-05-21",
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
        "name": "Finance and Financial Sector",
        "updateDate": "2025-05-30T13:51:35Z"
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
      "date": "2025-05-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3533ih.xml"
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
      "title": "Blockchain Regulatory Certainty Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-28T04:08:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Blockchain Regulatory Certainty Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-28T04:08:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To provide a safe harbor from licensing and registration for certain non-controlling blockchain developers and providers of blockchain services.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-28T04:03:43Z"
    }
  ]
}
```
