# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/159?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/159
- Title: Standing Against Houthi Aggression Act
- Congress: 119
- Bill type: S
- Bill number: 159
- Origin chamber: Senate
- Introduced date: 2025-01-21
- Update date: 2025-10-08T11:03:14Z
- Update date including text: 2025-10-08T11:03:14Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-21: Introduced in Senate
- 2025-01-21 - IntroReferral: Introduced in Senate
- 2025-01-21 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.
- Latest action: 2025-01-21: Introduced in Senate

## Actions

- 2025-01-21 - IntroReferral: Introduced in Senate
- 2025-01-21 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-21",
    "latestAction": {
      "actionDate": "2025-01-21",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/159",
    "number": "159",
    "originChamber": "Senate",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "D000618",
        "district": "",
        "firstName": "Steve",
        "fullName": "Sen. Daines, Steve [R-MT]",
        "lastName": "Daines",
        "party": "R",
        "state": "MT"
      }
    ],
    "title": "Standing Against Houthi Aggression Act",
    "type": "S",
    "updateDate": "2025-10-08T11:03:14Z",
    "updateDateIncludingText": "2025-10-08T11:03:14Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-21",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Foreign Relations.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-01-21",
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
          "date": "2025-01-21T19:24:29Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Foreign Relations Committee",
      "systemCode": "ssfr00",
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
      "bioguideId": "G000386",
      "firstName": "Chuck",
      "fullName": "Sen. Grassley, Chuck [R-IA]",
      "isOriginalCosponsor": "True",
      "lastName": "Grassley",
      "party": "R",
      "sponsorshipDate": "2025-01-21",
      "state": "IA"
    },
    {
      "bioguideId": "C001095",
      "firstName": "Tom",
      "fullName": "Sen. Cotton, Tom [R-AR]",
      "isOriginalCosponsor": "True",
      "lastName": "Cotton",
      "party": "R",
      "sponsorshipDate": "2025-01-21",
      "state": "AR"
    },
    {
      "bioguideId": "S001232",
      "firstName": "Tim",
      "fullName": "Sen. Sheehy, Tim [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sheehy",
      "party": "R",
      "sponsorshipDate": "2025-01-21",
      "state": "MT"
    },
    {
      "bioguideId": "B001305",
      "firstName": "Ted",
      "fullName": "Sen. Budd, Ted [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Budd",
      "party": "R",
      "sponsorshipDate": "2025-01-21",
      "state": "NC"
    },
    {
      "bioguideId": "C001056",
      "firstName": "John",
      "fullName": "Sen. Cornyn, John [R-TX]",
      "isOriginalCosponsor": "True",
      "lastName": "Cornyn",
      "party": "R",
      "sponsorshipDate": "2025-01-21",
      "state": "TX"
    },
    {
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2025-01-21",
      "state": "TN"
    },
    {
      "bioguideId": "H001061",
      "firstName": "John",
      "fullName": "Sen. Hoeven, John [R-ND]",
      "isOriginalCosponsor": "True",
      "lastName": "Hoeven",
      "party": "R",
      "sponsorshipDate": "2025-01-21",
      "state": "ND"
    },
    {
      "bioguideId": "R000618",
      "firstName": "Pete",
      "fullName": "Sen. Ricketts, Pete [R-NE]",
      "isOriginalCosponsor": "True",
      "lastName": "Ricketts",
      "party": "R",
      "sponsorshipDate": "2025-01-21",
      "state": "NE"
    },
    {
      "bioguideId": "C000880",
      "firstName": "Mike",
      "fullName": "Sen. Crapo, Mike [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Crapo",
      "party": "R",
      "sponsorshipDate": "2025-01-21",
      "state": "ID"
    },
    {
      "bioguideId": "L000571",
      "firstName": "Cynthia",
      "fullName": "Sen. Lummis, Cynthia M. [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Lummis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-01-21",
      "state": "WY"
    },
    {
      "bioguideId": "C001047",
      "firstName": "Shelley",
      "fullName": "Sen. Capito, Shelley Moore [R-WV]",
      "isOriginalCosponsor": "True",
      "lastName": "Capito",
      "middleName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-01-21",
      "state": "WV"
    },
    {
      "bioguideId": "L000575",
      "firstName": "James",
      "fullName": "Sen. Lankford, James [R-OK]",
      "isOriginalCosponsor": "True",
      "lastName": "Lankford",
      "party": "R",
      "sponsorshipDate": "2025-01-21",
      "state": "OK"
    },
    {
      "bioguideId": "S001227",
      "firstName": "Eric",
      "fullName": "Sen. Schmitt, Eric [R-MO]",
      "isOriginalCosponsor": "True",
      "lastName": "Schmitt",
      "middleName": "S.",
      "party": "R",
      "sponsorshipDate": "2025-01-21",
      "state": "MO"
    },
    {
      "bioguideId": "F000463",
      "firstName": "Deb",
      "fullName": "Sen. Fischer, Deb [R-NE]",
      "isOriginalCosponsor": "True",
      "lastName": "Fischer",
      "party": "R",
      "sponsorshipDate": "2025-01-21",
      "state": "NE"
    },
    {
      "bioguideId": "S001217",
      "firstName": "Rick",
      "fullName": "Sen. Scott, Rick [R-FL]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-01-21",
      "state": "FL"
    },
    {
      "bioguideId": "B001319",
      "firstName": "Katie",
      "fullName": "Sen. Britt, Katie Boyd [R-AL]",
      "isOriginalCosponsor": "True",
      "lastName": "Britt",
      "party": "R",
      "sponsorshipDate": "2025-01-21",
      "state": "AL"
    },
    {
      "bioguideId": "C001035",
      "firstName": "Susan",
      "fullName": "Sen. Collins, Susan M. [R-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "Collins",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-01-21",
      "state": "ME"
    },
    {
      "bioguideId": "C001075",
      "firstName": "Bill",
      "fullName": "Sen. Cassidy, Bill [R-LA]",
      "isOriginalCosponsor": "True",
      "lastName": "Cassidy",
      "party": "R",
      "sponsorshipDate": "2025-01-21",
      "state": "LA"
    },
    {
      "bioguideId": "E000295",
      "firstName": "Joni",
      "fullName": "Sen. Ernst, Joni [R-IA]",
      "isOriginalCosponsor": "True",
      "lastName": "Ernst",
      "party": "R",
      "sponsorshipDate": "2025-01-21",
      "state": "IA"
    },
    {
      "bioguideId": "M001243",
      "firstName": "David",
      "fullName": "Sen. McCormick, David [R-PA]",
      "isOriginalCosponsor": "False",
      "lastName": "McCormick",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-10-07",
      "state": "PA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s159is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 159\nIN THE SENATE OF THE UNITED STATES\nJanuary 21, 2025 Mr. Daines (for himself, Mr. Grassley , Mr. Cotton , Mr. Sheehy , Mr. Budd , Mr. Cornyn , Mrs. Blackburn , Mr. Hoeven , Mr. Ricketts , Mr. Crapo , Ms. Lummis , Mrs. Capito , Mr. Lankford , Mr. Schmitt , Mrs. Fischer , Mr. Scott of Florida , Mrs. Britt , Ms. Collins , Mr. Cassidy , and Ms. Ernst ) introduced the following bill; which was read twice and referred to the Committee on Foreign Relations\nA BILL\nTo designate Ansarallah as a foreign terrorist organization and impose certain sanctions on Ansarallah, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Standing Against Houthi Aggression Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nIt was reported by Reuters on March 21, 2017, that Iran, a designated state sponsor of terror, sent advanced weapons and military advisers to assist and support Yemen\u2019s Ansarallah, commonly referred to as the Houthis .\n**(2)**\nOn January 19, 2021, the Trump Administration designated Ansarallah as a foreign terrorist organization and a specially designated global terrorist.\n**(3)**\nOn February 16, 2021, Secretary of State Blinken revoked the designation of Ansarallah as a foreign terrorist organization pursuant to section 219(a)(6)(A) of the Immigration and Nationality Act ( 8 U.S.C. 1189(a)(6)(A) ).\n**(4)**\nOn March 7, 2021, an Ansarallah drone strike had been intercepted by Saudi Arabia, which targeted an oil storage yard at Ras Tanura.\n**(5)**\nOn March 19, 2021, another Ansarallah drone strike hit a Riyadh oil refinery, which caused a fire that was brought under control.\n**(6)**\nAfter the March 19, 2021, attack, Ansarallah proclaimed that they launched six drones at a Saudi Aramco facility, and vowed to continue operations against Saudi Arabia as long as its aggression against Yemen would continue .\n#### 3. Designation as foreign terrorist organization; imposition of sanctions\n##### (a) Designation as foreign terrorist organization\nNot later than 90 days after the date of the enactment of this Act, the Secretary of State shall designate Ansarallah as a foreign terrorist organization pursuant to section 219(a) of the Immigration and Nationality Act ( 8 U.S.C. 1189(a) ).\n##### (b) Imposition of sanctions\n**(1) In general**\nNot later than 90 days after the date of the enactment of this Act, the President shall impose the sanctions described in paragraph (2) with respect to\u2014\n**(A)**\nAnsarallah; and\n**(B)**\nany foreign person that is a member, agent, or affiliate of, or owned or controlled by, Ansarallah.\n**(2) Sanctions described**\nThe sanctions described in this paragraph are\u2014\n**(A)**\nsanctions applicable with respect to a foreign person pursuant to Executive Order 13224 ( 50 U.S.C. 1701 note; relating to blocking property and prohibiting transactions with persons who commit, threaten to commit, or support terrorism); and\n**(B)**\nsanctions described in Executive Order 13780 ( 8 U.S.C. 1182 note; relating to protecting the Nation from foreign terrorist entry into the United States), as in effect on January 19, 2021, with respect to nationals of Yemen.",
      "versionDate": "2025-01-21",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "International Affairs",
        "updateDate": "2025-02-27T16:48:22Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-21",
    "originChamber": "Senate",
    "payload": {
      "dublinCore": {
        "contributor": "Congressional Research Service, Library of Congress",
        "description": "This file contains bill summaries for federal legislation. A bill summary describes the most significant provisions of a piece of legislation and details the effects the legislative text may have on current law and federal programs. Bill summaries are authored by the Congressional Research Service (CRS) of the Library of Congress. As stated in Public Law 91-510 (2 USC 166 (d)(6)), one of the duties of CRS is \"to prepare summaries and digests of bills and resolutions of a public general nature introduced in the Senate or House of Representatives\". For more information, refer to the User Guide that accompanies this file.",
        "format": "text/xml",
        "language": "EN",
        "rights": "Pursuant to Title 17 Section 105 of the United States Code, this file is not subject to copyright protection and is in the public domain."
      },
      "item": {
        "@attributes": {
          "congress": "119",
          "measure-id": "id119s159",
          "measure-number": "159",
          "measure-type": "s",
          "orig-publish-date": "2025-01-21",
          "originChamber": "SENATE",
          "update-date": "2025-03-14"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s159v00",
            "update-date": "2025-03-14"
          },
          "action-date": "2025-01-21",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Standing Against Houthi Aggression Act</strong></p><p>This bill requires (1) the Department of State to designate Ansarallah, the\u00a0Iran-backed movement in Yemen also known as the Houthis, as a foreign terrorist organization; and (2) the President to impose property- and visa-blocking sanctions with respect to Ansarallah and any foreign person who is a member, agent, or affiliate of, or owned or controlled by, Ansarallah.</p>"
        },
        "title": "Standing Against Houthi Aggression Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s159.xml",
    "summary": {
      "actionDate": "2025-01-21",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Standing Against Houthi Aggression Act</strong></p><p>This bill requires (1) the Department of State to designate Ansarallah, the\u00a0Iran-backed movement in Yemen also known as the Houthis, as a foreign terrorist organization; and (2) the President to impose property- and visa-blocking sanctions with respect to Ansarallah and any foreign person who is a member, agent, or affiliate of, or owned or controlled by, Ansarallah.</p>",
      "updateDate": "2025-03-14",
      "versionCode": "id119s159"
    },
    "title": "Standing Against Houthi Aggression Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-21",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Standing Against Houthi Aggression Act</strong></p><p>This bill requires (1) the Department of State to designate Ansarallah, the\u00a0Iran-backed movement in Yemen also known as the Houthis, as a foreign terrorist organization; and (2) the President to impose property- and visa-blocking sanctions with respect to Ansarallah and any foreign person who is a member, agent, or affiliate of, or owned or controlled by, Ansarallah.</p>",
      "updateDate": "2025-03-14",
      "versionCode": "id119s159"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s159is.xml"
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
      "title": "Standing Against Houthi Aggression Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-08T11:03:14Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Standing Against Houthi Aggression Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-21T03:23:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to designate Ansarallah as a foreign terrorist organization and impose certain sanctions on Ansarallah, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-21T03:18:29Z"
    }
  ]
}
```
