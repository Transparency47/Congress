# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/214?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/214
- Title: A resolution recognizing the significance of Asian American, Native Hawaiian, and Pacific Islander Heritage Month as an important time to celebrate the significant contributions of Asian Americans, Native Hawaiians, and Pacific Islanders to the history of the United States.
- Congress: 119
- Bill type: SRES
- Bill number: 214
- Origin chamber: Senate
- Introduced date: 2025-05-08
- Update date: 2026-05-12T13:35:52Z
- Update date including text: 2026-05-12T13:35:52Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-05-08: Introduced in Senate
- 2025-05-08 - IntroReferral: Introduced in Senate
- 2025-05-08 - IntroReferral: Referred to the Committee on the Judiciary.
- 2025-05-22 - Floor: Passed/agreed to in Senate: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent.
- 2025-05-22 - Floor: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent. (consideration: CR S3142; text: 05/08/2025 CR S2844-2845)
- 2025-05-22 - Discharge: Senate Committee on the Judiciary discharged by Unanimous Consent.
- 2025-05-22 - Committee: Senate Committee on the Judiciary discharged by Unanimous Consent.
- Latest action: 2025-05-08: Introduced in Senate

## Actions

- 2025-05-08 - IntroReferral: Introduced in Senate
- 2025-05-08 - IntroReferral: Referred to the Committee on the Judiciary.
- 2025-05-22 - Floor: Passed/agreed to in Senate: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent.
- 2025-05-22 - Floor: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent. (consideration: CR S3142; text: 05/08/2025 CR S2844-2845)
- 2025-05-22 - Discharge: Senate Committee on the Judiciary discharged by Unanimous Consent.
- 2025-05-22 - Committee: Senate Committee on the Judiciary discharged by Unanimous Consent.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-08",
    "latestAction": {
      "actionDate": "2025-05-08",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/214",
    "number": "214",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Native Americans"
    },
    "sponsors": [
      {
        "bioguideId": "H001042",
        "district": "",
        "firstName": "Mazie",
        "fullName": "Sen. Hirono, Mazie K. [D-HI]",
        "lastName": "Hirono",
        "party": "D",
        "state": "HI"
      }
    ],
    "title": "A resolution recognizing the significance of Asian American, Native Hawaiian, and Pacific Islander Heritage Month as an important time to celebrate the significant contributions of Asian Americans, Native Hawaiians, and Pacific Islanders to the history of the United States.",
    "type": "SRES",
    "updateDate": "2026-05-12T13:35:52Z",
    "updateDateIncludingText": "2026-05-12T13:35:52Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-22",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent. (consideration: CR S3142; text: 05/08/2025 CR S2844-2845)",
      "type": "Floor"
    },
    {
      "actionCode": "17000",
      "actionDate": "2025-05-22",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Passed/agreed to in Senate: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent.",
      "type": "Floor"
    },
    {
      "actionDate": "2025-05-22",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Senate Committee on the Judiciary discharged by Unanimous Consent.",
      "type": "Discharge"
    },
    {
      "actionCode": "14500",
      "actionDate": "2025-05-22",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Senate Committee on the Judiciary discharged by Unanimous Consent.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-05-08",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-05-08",
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
        "item": [
          {
            "date": "2025-05-22T20:40:59Z",
            "name": "Discharged From"
          },
          {
            "date": "2025-05-08T19:38:35Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Judiciary Committee",
      "systemCode": "ssju00",
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
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2025-05-08",
      "state": "IL"
    },
    {
      "bioguideId": "K000394",
      "firstName": "Andy",
      "fullName": "Sen. Kim, Andy [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kim",
      "party": "D",
      "sponsorshipDate": "2025-05-08",
      "state": "NJ"
    },
    {
      "bioguideId": "C001035",
      "firstName": "Susan",
      "fullName": "Sen. Collins, Susan M. [R-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "Collins",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-05-08",
      "state": "ME"
    },
    {
      "bioguideId": "B001230",
      "firstName": "Tammy",
      "fullName": "Sen. Baldwin, Tammy [D-WI]",
      "isOriginalCosponsor": "True",
      "lastName": "Baldwin",
      "party": "D",
      "sponsorshipDate": "2025-05-08",
      "state": "WI"
    },
    {
      "bioguideId": "B001267",
      "firstName": "Michael",
      "fullName": "Sen. Bennet, Michael F. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Bennet",
      "party": "D",
      "sponsorshipDate": "2025-05-08",
      "state": "CO"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-05-08",
      "state": "CT"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-05-08",
      "state": "NJ"
    },
    {
      "bioguideId": "C000127",
      "firstName": "Maria",
      "fullName": "Sen. Cantwell, Maria [D-WA]",
      "isOriginalCosponsor": "True",
      "lastName": "Cantwell",
      "party": "D",
      "sponsorshipDate": "2025-05-08",
      "state": "WA"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-05-08",
      "state": "DE"
    },
    {
      "bioguideId": "C001113",
      "firstName": "Catherine",
      "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Cortez Masto",
      "party": "D",
      "sponsorshipDate": "2025-05-08",
      "state": "NV"
    },
    {
      "bioguideId": "D000563",
      "firstName": "Richard",
      "fullName": "Sen. Durbin, Richard J. [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Durbin",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-05-08",
      "state": "IL"
    },
    {
      "bioguideId": "F000479",
      "firstName": "John",
      "fullName": "Sen. Fetterman, John [D-PA]",
      "isOriginalCosponsor": "True",
      "lastName": "Fetterman",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-05-08",
      "state": "PA"
    },
    {
      "bioguideId": "G000555",
      "firstName": "Kirsten",
      "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
      "isOriginalCosponsor": "True",
      "lastName": "Gillibrand",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-05-08",
      "state": "NY"
    },
    {
      "bioguideId": "H001076",
      "firstName": "Maggie",
      "fullName": "Sen. Hassan, Margaret Wood [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Hassan",
      "party": "D",
      "sponsorshipDate": "2025-05-08",
      "state": "NH"
    },
    {
      "bioguideId": "K000384",
      "firstName": "Timothy",
      "fullName": "Sen. Kaine, Tim [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Kaine",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-05-08",
      "state": "VA"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-05-08",
      "state": "MN"
    },
    {
      "bioguideId": "M000133",
      "firstName": "Edward",
      "fullName": "Sen. Markey, Edward J. [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Markey",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-05-08",
      "state": "MA"
    },
    {
      "bioguideId": "M001111",
      "firstName": "Patty",
      "fullName": "Sen. Murray, Patty [D-WA]",
      "isOriginalCosponsor": "True",
      "lastName": "Murray",
      "party": "D",
      "sponsorshipDate": "2025-05-08",
      "state": "WA"
    },
    {
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2025-05-08",
      "state": "CA"
    },
    {
      "bioguideId": "R000122",
      "firstName": "John",
      "fullName": "Sen. Reed, Jack [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Reed",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-05-08",
      "state": "RI"
    },
    {
      "bioguideId": "R000608",
      "firstName": "Jacky",
      "fullName": "Sen. Rosen, Jacky [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Rosen",
      "party": "D",
      "sponsorshipDate": "2025-05-08",
      "state": "NV"
    },
    {
      "bioguideId": "S001194",
      "firstName": "Brian",
      "fullName": "Sen. Schatz, Brian [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Schatz",
      "party": "D",
      "sponsorshipDate": "2025-05-08",
      "state": "HI"
    },
    {
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2025-05-08",
      "state": "CA"
    },
    {
      "bioguideId": "S001203",
      "firstName": "Tina",
      "fullName": "Sen. Smith, Tina [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-05-08",
      "state": "MN"
    },
    {
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2025-05-08",
      "state": "MD"
    },
    {
      "bioguideId": "W000805",
      "firstName": "Mark",
      "fullName": "Sen. Warner, Mark R. [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warner",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-05-08",
      "state": "VA"
    },
    {
      "bioguideId": "W000790",
      "firstName": "Raphael",
      "fullName": "Sen. Warnock, Raphael G. [D-GA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warnock",
      "party": "D",
      "sponsorshipDate": "2025-05-08",
      "state": "GA"
    },
    {
      "bioguideId": "W000817",
      "firstName": "Elizabeth",
      "fullName": "Sen. Warren, Elizabeth [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warren",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-05-08",
      "state": "MA"
    },
    {
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2025-05-08",
      "state": "OR"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres214is.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 214\nIN THE SENATE OF THE UNITED STATES\nMay 8, 2025 Ms. Hirono (for herself, Ms. Duckworth , Mr. Kim , Ms. Collins , Ms. Baldwin , Mr. Bennet , Mr. Blumenthal , Mr. Booker , Ms. Cantwell , Mr. Coons , Ms. Cortez Masto , Mr. Durbin , Mr. Fetterman , Mrs. Gillibrand , Ms. Hassan , Mr. Kaine , Ms. Klobuchar , Mr. Markey , Mrs. Murray , Mr. Padilla , Mr. Reed , Ms. Rosen , Mr. Schatz , Mr. Schiff , Ms. Smith , Mr. Van Hollen , Mr. Warner , Mr. Warnock , Ms. Warren , and Mr. Wyden ) submitted the following resolution; which was referred to the Committee on the Judiciary\nRESOLUTION\nRecognizing the significance of Asian American, Native Hawaiian, and Pacific Islander Heritage Month as an important time to celebrate the significant contributions of Asian Americans, Native Hawaiians, and Pacific Islanders to the history of the United States.\nThat the Senate\u2014\n**(1)**\nrecognizes the significance of Asian American, Native Hawaiian, and Pacific Islander Heritage Month as an important time to celebrate the significant contributions of Asian Americans, Native Hawaiians, and Pacific Islanders to the history of the United States; and\n**(2)**\nrecognizes that Asian American, Native Hawaiian, and Pacific Islander communities enhance the rich diversity of and strengthen the United States.",
      "versionDate": "2025-05-08",
      "versionType": "IS"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres214ats.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 214\nIN THE SENATE OF THE UNITED STATES\nMay 8, 2025 Ms. Hirono (for herself, Ms. Duckworth , Mr. Kim , Ms. Collins , Ms. Baldwin , Mr. Bennet , Mr. Blumenthal , Mr. Booker , Ms. Cantwell , Mr. Coons , Ms. Cortez Masto , Mr. Durbin , Mr. Fetterman , Mrs. Gillibrand , Ms. Hassan , Mr. Kaine , Ms. Klobuchar , Mr. Markey , Mrs. Murray , Mr. Padilla , Mr. Reed , Ms. Rosen , Mr. Schatz , Mr. Schiff , Ms. Smith , Mr. Van Hollen , Mr. Warner , Mr. Warnock , Ms. Warren , and Mr. Wyden ) submitted the following resolution; which was referred to the Committee on the Judiciary\nMay 22, 2025 Committee discharged; considered and agreed to\nRESOLUTION\nRecognizing the significance of Asian American, Native Hawaiian, and Pacific Islander Heritage Month as an important time to celebrate the significant contributions of Asian Americans, Native Hawaiians, and Pacific Islanders to the history of the United States.\nThat the Senate\u2014\n**(1)**\nrecognizes the significance of Asian American, Native Hawaiian, and Pacific Islander Heritage Month as an important time to celebrate the significant contributions of Asian Americans, Native Hawaiians, and Pacific Islanders to the history of the United States; and\n**(2)**\nrecognizes that Asian American, Native Hawaiian, and Pacific Islander communities enhance the rich diversity of and strengthen the United States.",
      "versionDate": "2025-05-22",
      "versionType": "ATS"
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
        "actionDate": "2026-04-30",
        "text": "Referred to the House Committee on Oversight and Government Reform."
      },
      "number": "1243",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Recognizing the significance of Asian American, Native Hawaiian, and Pacific Islander Heritage Month as an important time to celebrate the significant contributions of Asian Americans, Native Hawaiians, and Pacific Islanders to the history of the United States.",
      "type": "HRES"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2026-04-30",
        "text": "Submitted in the Senate, considered, and agreed to without amendment and with a preamble by Unanimous Consent. (consideration: CR S2160; text: CR S2180-2181)"
      },
      "number": "720",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "A resolution recognizing the significance of Asian American, Native Hawaiian, and Pacific Islander Heritage Month as an important time to celebrate the significant contributions of Asian Americans, Native Hawaiians, and Pacific Islanders to the history of the United States.",
      "type": "SRES"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-05-08",
        "text": "Referred to the House Committee on Oversight and Government Reform."
      },
      "number": "400",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Recognizing the significance of Asian American, Native Hawaiian, and Pacific Islander Heritage Month as an important time to celebrate the significant contributions of Asian Americans, Native Hawaiians, and Pacific Islanders to the history of the United States.",
      "type": "HRES"
    }
  ]
}
```

## API Data: subjects

```json
{
  "subjects": [
    {
      "legislativeSubjects": {
        "item": [
          {
            "name": "Alaska Natives and Hawaiians",
            "updateDate": "2025-06-04T13:35:26Z"
          },
          {
            "name": "Asia",
            "updateDate": "2025-06-04T13:35:26Z"
          },
          {
            "name": "Commemorative events and holidays",
            "updateDate": "2025-06-04T13:35:26Z"
          },
          {
            "name": "Congressional tributes",
            "updateDate": "2025-06-04T13:35:26Z"
          },
          {
            "name": "Racial and ethnic relations",
            "updateDate": "2025-06-04T13:35:26Z"
          },
          {
            "name": "U.S. history",
            "updateDate": "2025-06-04T13:35:26Z"
          }
        ]
      },
      "policyArea": {
        "name": "Native Americans",
        "updateDate": "2025-06-04T10:37:22Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-05-08",
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
          "measure-id": "id119sres214",
          "measure-number": "214",
          "measure-type": "sres",
          "orig-publish-date": "2025-05-08",
          "originChamber": "SENATE",
          "update-date": "2025-08-08"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119sres214v00",
            "update-date": "2025-08-08"
          },
          "action-date": "2025-05-08",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p>This resolution recognizes the significance of Asian American, Native Hawaiian, and Pacific Islander Heritage Month as an important time to celebrate the significant contributions of Asian Americans, Native Hawaiians, and Pacific Islanders to the history of the United States.</p>"
        },
        "title": "A resolution recognizing the significance of Asian American, Native Hawaiian, and Pacific Islander Heritage Month as an important time to celebrate the significant contributions of Asian Americans, Native Hawaiians, and Pacific Islanders to the history of the United States."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/sres/BILLSUM-119sres214.xml",
    "summary": {
      "actionDate": "2025-05-08",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This resolution recognizes the significance of Asian American, Native Hawaiian, and Pacific Islander Heritage Month as an important time to celebrate the significant contributions of Asian Americans, Native Hawaiians, and Pacific Islanders to the history of the United States.</p>",
      "updateDate": "2025-08-08",
      "versionCode": "id119sres214"
    },
    "title": "A resolution recognizing the significance of Asian American, Native Hawaiian, and Pacific Islander Heritage Month as an important time to celebrate the significant contributions of Asian Americans, Native Hawaiians, and Pacific Islanders to the history of the United States."
  },
  "summaries": [
    {
      "actionDate": "2025-05-08",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This resolution recognizes the significance of Asian American, Native Hawaiian, and Pacific Islander Heritage Month as an important time to celebrate the significant contributions of Asian Americans, Native Hawaiians, and Pacific Islanders to the history of the United States.</p>",
      "updateDate": "2025-08-08",
      "versionCode": "id119sres214"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-05-08",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres214is.xml"
        }
      ],
      "type": "IS"
    },
    {
      "date": "2025-05-22",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres214ats.xml"
        }
      ],
      "type": "ATS"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A resolution recognizing the significance of Asian American, Native Hawaiian, and Pacific Islander Heritage Month as an important time to celebrate the significant contributions of Asian Americans, Native Hawaiians, and Pacific Islanders to the history of the United States.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-10T04:33:28Z"
    },
    {
      "title": "A resolution recognizing the significance of Asian American, Native Hawaiian, and Pacific Islander Heritage Month as an important time to celebrate the significant contributions of Asian Americans, Native Hawaiians, and Pacific Islanders to the history of the United States.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-09T10:56:23Z"
    }
  ]
}
```
