# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/473?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/473
- Title: A resolution commemorating the seventh anniversary of the murder of Jamal Khashoggi and calling for accountability.
- Congress: 119
- Bill type: SRES
- Bill number: 473
- Origin chamber: Senate
- Introduced date: 2025-10-29
- Update date: 2025-12-05T22:08:36Z
- Update date including text: 2025-12-05T22:08:36Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-10-29: Introduced in Senate
- 2025-10-29 - IntroReferral: Introduced in Senate
- 2025-10-29 - IntroReferral: Referred to the Committee on Foreign Relations. (text: CR S7829)
- Latest action: 2025-10-29: Introduced in Senate

## Actions

- 2025-10-29 - IntroReferral: Introduced in Senate
- 2025-10-29 - IntroReferral: Referred to the Committee on Foreign Relations. (text: CR S7829)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-29",
    "latestAction": {
      "actionDate": "2025-10-29",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/473",
    "number": "473",
    "originChamber": "Senate",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "K000384",
        "district": "",
        "firstName": "Timothy",
        "fullName": "Sen. Kaine, Tim [D-VA]",
        "lastName": "Kaine",
        "party": "D",
        "state": "VA"
      }
    ],
    "title": "A resolution commemorating the seventh anniversary of the murder of Jamal Khashoggi and calling for accountability.",
    "type": "SRES",
    "updateDate": "2025-12-05T22:08:36Z",
    "updateDateIncludingText": "2025-12-05T22:08:36Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-10-29",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on Foreign Relations. (text: CR S7829)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-10-29",
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
          "date": "2025-10-29T19:05:38Z",
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
      "bioguideId": "W000805",
      "firstName": "Mark",
      "fullName": "Sen. Warner, Mark R. [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warner",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-10-29",
      "state": "VA"
    },
    {
      "bioguideId": "B001267",
      "firstName": "Michael",
      "fullName": "Sen. Bennet, Michael F. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Bennet",
      "party": "D",
      "sponsorshipDate": "2025-10-29",
      "state": "CO"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-10-29",
      "state": "NJ"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-10-29",
      "state": "DE"
    },
    {
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2025-10-29",
      "state": "IL"
    },
    {
      "bioguideId": "D000563",
      "firstName": "Richard",
      "fullName": "Sen. Durbin, Richard J. [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Durbin",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-10-29",
      "state": "IL"
    },
    {
      "bioguideId": "H001046",
      "firstName": "Martin",
      "fullName": "Sen. Heinrich, Martin [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Heinrich",
      "party": "D",
      "sponsorshipDate": "2025-10-29",
      "state": "NM"
    },
    {
      "bioguideId": "H001042",
      "firstName": "Mazie",
      "fullName": "Sen. Hirono, Mazie K. [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Hirono",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-10-29",
      "state": "HI"
    },
    {
      "bioguideId": "K000394",
      "firstName": "Andy",
      "fullName": "Sen. Kim, Andy [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kim",
      "party": "D",
      "sponsorshipDate": "2025-10-29",
      "state": "NJ"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-10-29",
      "state": "MN"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2025-10-29",
      "state": "OR"
    },
    {
      "bioguideId": "M001169",
      "firstName": "Christopher",
      "fullName": "Sen. Murphy, Christopher [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Murphy",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-10-29",
      "state": "CT"
    },
    {
      "bioguideId": "M001111",
      "firstName": "Patty",
      "fullName": "Sen. Murray, Patty [D-WA]",
      "isOriginalCosponsor": "True",
      "lastName": "Murray",
      "party": "D",
      "sponsorshipDate": "2025-10-29",
      "state": "WA"
    },
    {
      "bioguideId": "S000033",
      "firstName": "Bernie",
      "fullName": "Sen. Sanders, Bernard [I-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sanders",
      "party": "I",
      "sponsorshipDate": "2025-10-29",
      "state": "VT"
    },
    {
      "bioguideId": "S001194",
      "firstName": "Brian",
      "fullName": "Sen. Schatz, Brian [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Schatz",
      "party": "D",
      "sponsorshipDate": "2025-10-29",
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
      "sponsorshipDate": "2025-10-29",
      "state": "CA"
    },
    {
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2025-10-29",
      "state": "MD"
    },
    {
      "bioguideId": "W000817",
      "firstName": "Elizabeth",
      "fullName": "Sen. Warren, Elizabeth [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warren",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-10-29",
      "state": "MA"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-10-29",
      "state": "VT"
    },
    {
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2025-10-29",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres473is.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 473\nIN THE SENATE OF THE UNITED STATES\nOctober 29, 2025 Mr. Kaine (for himself, Mr. Warner , Mr. Bennet , Mr. Booker , Mr. Coons , Ms. Duckworth , Mr. Durbin , Mr. Heinrich , Ms. Hirono , Mr. Kim , Ms. Klobuchar , Mr. Merkley , Mr. Murphy , Mrs. Murray , Mr. Sanders , Mr. Schatz , Mr. Schiff , Mr. Van Hollen , Ms. Warren , Mr. Welch , and Mr. Wyden ) submitted the following resolution; which was referred to the Committee on Foreign Relations\nRESOLUTION\nCommemorating the seventh anniversary of the murder of Jamal Khashoggi and calling for accountability.\nThat the Senate\u2014\n**(1)**\nacknowledges the Government of the United States has sanctioned 17 Saudi individuals under the Global Magnitsky Human Rights Accountability Act (subtitle F of title XII of Public Law 114\u2013328 ; 22 U.S.C. 10101 et seq. ) for their roles in the murder of Jamal Khashoggi; and\n**(2)**\ncalls for the Government of Saudi Arabia to\u2014\n**(A)**\nensure appropriate accountability for all individuals responsible for the murder of Jamal Khashoggi, including the individuals sanctioned by the United States;\n**(B)**\nrelease all individuals wrongfully detained, including Nourah al-Qahtani, Abdulrahman Alsadhan, Salman Alodah, Waleed Abu al-Khair, and Sarah and Omar Aljabri; and\n**(C)**\nrespect the rights of Saudi citizens and ensure the protection of the freedoms of assembly, association, and the press.",
      "versionDate": "2025-10-29",
      "versionType": "IS"
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
        "actionDate": "2025-10-31",
        "text": "Referred to the House Committee on Foreign Affairs."
      },
      "number": "854",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Commemorating the seventh anniversary of the murder of Jamal Khashoggi and calling for accountability.",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "International Affairs",
        "updateDate": "2025-11-20T17:25:40Z"
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
      "date": "2025-10-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres473is.xml"
        }
      ],
      "type": "IS"
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
      "title": "A resolution commemorating the seventh anniversary of the murder of Jamal Khashoggi and calling for accountability.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-01T03:48:20Z"
    },
    {
      "title": "A resolution commemorating the seventh anniversary of the murder of Jamal Khashoggi and calling for accountability.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-30T10:56:14Z"
    }
  ]
}
```
