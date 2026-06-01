# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/408?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/408
- Title: A resolution recognizing September 20, 2025, as "National LGBTQ+ Servicemembers and Veterans Day".
- Congress: 119
- Bill type: SRES
- Bill number: 408
- Origin chamber: Senate
- Introduced date: 2025-09-18
- Update date: 2026-04-08T12:15:35Z
- Update date including text: 2026-04-08T12:15:35Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-09-18: Introduced in Senate
- 2025-09-18 - IntroReferral: Introduced in Senate
- 2025-09-18 - IntroReferral: Referred to the Committee on Veterans' Affairs. (text: CR S6738)
- Latest action: 2025-09-18: Introduced in Senate

## Actions

- 2025-09-18 - IntroReferral: Introduced in Senate
- 2025-09-18 - IntroReferral: Referred to the Committee on Veterans' Affairs. (text: CR S6738)

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
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/408",
    "number": "408",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "M001176",
        "district": "",
        "firstName": "Jeff",
        "fullName": "Sen. Merkley, Jeff [D-OR]",
        "lastName": "Merkley",
        "party": "D",
        "state": "OR"
      }
    ],
    "title": "A resolution recognizing September 20, 2025, as \"National LGBTQ+ Servicemembers and Veterans Day\".",
    "type": "SRES",
    "updateDate": "2026-04-08T12:15:35Z",
    "updateDateIncludingText": "2026-04-08T12:15:35Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-09-18",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "ssva00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on Veterans' Affairs. (text: CR S6738)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-09-18",
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
          "date": "2025-09-18T21:07:46Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Veterans' Affairs Committee",
      "systemCode": "ssva00",
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
      "bioguideId": "B001230",
      "firstName": "Tammy",
      "fullName": "Sen. Baldwin, Tammy [D-WI]",
      "isOriginalCosponsor": "True",
      "lastName": "Baldwin",
      "party": "D",
      "sponsorshipDate": "2025-09-18",
      "state": "WI"
    },
    {
      "bioguideId": "B001267",
      "firstName": "Michael",
      "fullName": "Sen. Bennet, Michael F. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Bennet",
      "party": "D",
      "sponsorshipDate": "2025-09-18",
      "state": "CO"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-09-18",
      "state": "CT"
    },
    {
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2025-09-18",
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
      "sponsorshipDate": "2025-09-18",
      "state": "PA"
    },
    {
      "bioguideId": "H001042",
      "firstName": "Mazie",
      "fullName": "Sen. Hirono, Mazie K. [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Hirono",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-09-18",
      "state": "HI"
    },
    {
      "bioguideId": "L000570",
      "firstName": "Ben",
      "fullName": "Sen. Luj\u00e1n, Ben Ray [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Luj\u00e1n",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-09-18",
      "state": "NM"
    },
    {
      "bioguideId": "M001111",
      "firstName": "Patty",
      "fullName": "Sen. Murray, Patty [D-WA]",
      "isOriginalCosponsor": "True",
      "lastName": "Murray",
      "party": "D",
      "sponsorshipDate": "2025-09-18",
      "state": "WA"
    },
    {
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2025-09-18",
      "state": "CA"
    },
    {
      "bioguideId": "S000033",
      "firstName": "Bernie",
      "fullName": "Sen. Sanders, Bernard [I-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sanders",
      "party": "I",
      "sponsorshipDate": "2025-09-18",
      "state": "VT"
    },
    {
      "bioguideId": "S001194",
      "firstName": "Brian",
      "fullName": "Sen. Schatz, Brian [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Schatz",
      "party": "D",
      "sponsorshipDate": "2025-09-18",
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
      "sponsorshipDate": "2025-09-18",
      "state": "CA"
    },
    {
      "bioguideId": "S001203",
      "firstName": "Tina",
      "fullName": "Sen. Smith, Tina [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-09-18",
      "state": "MN"
    },
    {
      "bioguideId": "W000817",
      "firstName": "Elizabeth",
      "fullName": "Sen. Warren, Elizabeth [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warren",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-09-18",
      "state": "MA"
    },
    {
      "bioguideId": "W000802",
      "firstName": "Sheldon",
      "fullName": "Sen. Whitehouse, Sheldon [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Whitehouse",
      "party": "D",
      "sponsorshipDate": "2025-09-18",
      "state": "RI"
    },
    {
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2025-09-18",
      "state": "OR"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-09-18",
      "state": "NJ"
    },
    {
      "bioguideId": "D000563",
      "firstName": "Richard",
      "fullName": "Sen. Durbin, Richard J. [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Durbin",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-09-18",
      "state": "IL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres408is.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 408\nIN THE SENATE OF THE UNITED STATES\nSeptember 18 (legislative day, September 16), 2025 Mr. Merkley (for himself, Ms. Baldwin , Mr. Bennet , Mr. Blumenthal , Ms. Duckworth , Mr. Fetterman , Ms. Hirono , Mr. Luj\u00e1n , Mrs. Murray , Mr. Padilla , Mr. Sanders , Mr. Schatz , Mr. Schiff , Ms. Smith , Ms. Warren , Mr. Whitehouse , Mr. Wyden , Mr. Booker , and Mr. Durbin ) submitted the following resolution; which was referred to the Committee on Veterans' Affairs\nRESOLUTION\nRecognizing September 20, 2025, as National LGBTQ+ Servicemembers and Veterans Day .\nThat the Senate\u2014\n**(1)**\nrecognizes September 20, 2025, as National LGBTQ+ Servicemembers and Veterans Day ;\n**(2)**\ncelebrates the contributions of lesbian, gay, bisexual, transgender, and queer (referred to in this resolution as LGBTQ+ ) servicemembers and veterans who have served in the Armed Forces;\n**(3)**\nregrets the harm done to LGBTQ+ servicemembers and veterans under the Don\u2019t Ask, Don\u2019t Tell policy and earlier policies, bans on transgender servicemembers, and other policies that discriminate based on sexual orientation and gender identity;\n**(4)**\nrecognizes how other than honorable and dishonorable discharges given to LGBTQ+ servicemembers on the basis of sexual orientation and gender identity\u2014\n**(A)**\nprematurely terminated the careers of LGBTQ+ servicemembers in the Armed Forces;\n**(B)**\nsubjected LGBTQ+ servicemembers to the trauma of investigations and criminal charges;\n**(C)**\nunfairly denied LGBTQ+ servicemembers the honor associated with military service;\n**(D)**\ndeprived LGBTQ+ servicemembers of benefits those servicemembers have earned and deserve as veterans; and\n**(E)**\ncontinue to cause LGBTQ+ servicemembers dignitary harm;\n**(5)**\nurges the Department of Veterans Affairs and the Department of Defense\u2014\n**(A)**\nto implement policy changes that restore justice and right wrongs caused by past and present government-sponsored discrimination; and\n**(B)**\nto conduct further outreach to LGBTQ+ service member and veteran communities to ensure that those discharged based on their sexual orientation and gender identity can receive their benefits;\n**(6)**\nurges the Department of Veterans Affairs and the Department of Defense to ensure that transgender veterans and servicemembers and their families have access to the full range of health care, including gender-affirming care; and\n**(7)**\nurges the Department of Veterans Affairs to remove the exclusion of gender-affirming surgery from the Veterans Affairs Medical Benefits Package.",
      "versionDate": "2025-09-18",
      "versionType": "IS"
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
        "name": "Armed Forces and National Security",
        "updateDate": "2025-09-23T18:29:25Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-09-18",
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
          "measure-id": "id119sres408",
          "measure-number": "408",
          "measure-type": "sres",
          "orig-publish-date": "2025-09-18",
          "originChamber": "SENATE",
          "update-date": "2026-04-08"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119sres408v00",
            "update-date": "2026-04-08"
          },
          "action-date": "2025-09-18",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p>This resolution recognizes September 20, 2025, as National LGBTQ+ Servicemembers and Veterans Day and celebrates the contributions of lesbian, gay, bisexual, transgender, and queer servicemembers and veterans who have served in the Armed Forces.</p><p>Additionally, the resolution (1) regrets the harm done to such servicemembers and veterans under policies that discriminate based on sexual orientation and gender identity, and (2) urges the Department of Veterans Affairs and Department of Defense to ensure transgender veterans and servicemembers and their families have access to a full range of health care.</p>"
        },
        "title": "A resolution recognizing September 20, 2025, as \"National LGBTQ+ Servicemembers and Veterans Day\"."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/sres/BILLSUM-119sres408.xml",
    "summary": {
      "actionDate": "2025-09-18",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This resolution recognizes September 20, 2025, as National LGBTQ+ Servicemembers and Veterans Day and celebrates the contributions of lesbian, gay, bisexual, transgender, and queer servicemembers and veterans who have served in the Armed Forces.</p><p>Additionally, the resolution (1) regrets the harm done to such servicemembers and veterans under policies that discriminate based on sexual orientation and gender identity, and (2) urges the Department of Veterans Affairs and Department of Defense to ensure transgender veterans and servicemembers and their families have access to a full range of health care.</p>",
      "updateDate": "2026-04-08",
      "versionCode": "id119sres408"
    },
    "title": "A resolution recognizing September 20, 2025, as \"National LGBTQ+ Servicemembers and Veterans Day\"."
  },
  "summaries": [
    {
      "actionDate": "2025-09-18",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This resolution recognizes September 20, 2025, as National LGBTQ+ Servicemembers and Veterans Day and celebrates the contributions of lesbian, gay, bisexual, transgender, and queer servicemembers and veterans who have served in the Armed Forces.</p><p>Additionally, the resolution (1) regrets the harm done to such servicemembers and veterans under policies that discriminate based on sexual orientation and gender identity, and (2) urges the Department of Veterans Affairs and Department of Defense to ensure transgender veterans and servicemembers and their families have access to a full range of health care.</p>",
      "updateDate": "2026-04-08",
      "versionCode": "id119sres408"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres408is.xml"
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
      "title": "A resolution recognizing September 20, 2025, as \"National LGBTQ+ Servicemembers and Veterans Day\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-20T06:03:32Z"
    },
    {
      "title": "A resolution recognizing September 20, 2025, as \"National LGBTQ+ Servicemembers and Veterans Day\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-19T10:56:41Z"
    }
  ]
}
```
