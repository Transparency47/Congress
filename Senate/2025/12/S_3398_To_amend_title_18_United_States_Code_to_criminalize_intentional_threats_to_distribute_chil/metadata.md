# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3398?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3398
- Title: Stop Sextortion Act
- Congress: 119
- Bill type: S
- Bill number: 3398
- Origin chamber: Senate
- Introduced date: 2025-12-09
- Update date: 2026-05-22T19:48:25Z
- Update date including text: 2026-05-22T19:48:25Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-12-09: Introduced in Senate
- 2025-12-09 - IntroReferral: Introduced in Senate
- 2025-12-09 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-12-09: Introduced in Senate

## Actions

- 2025-12-09 - IntroReferral: Introduced in Senate
- 2025-12-09 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-09",
    "latestAction": {
      "actionDate": "2025-12-09",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3398",
    "number": "3398",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "G000386",
        "district": "",
        "firstName": "Chuck",
        "fullName": "Sen. Grassley, Chuck [R-IA]",
        "lastName": "Grassley",
        "party": "R",
        "state": "IA"
      }
    ],
    "title": "Stop Sextortion Act",
    "type": "S",
    "updateDate": "2026-05-22T19:48:25Z",
    "updateDateIncludingText": "2026-05-22T19:48:25Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-09",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-12-09",
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
            "date": "2025-12-09T19:39:31Z",
            "name": "Referred To"
          },
          {
            "date": "2025-12-09T19:39:31Z",
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
      "bioguideId": "D000563",
      "firstName": "Richard",
      "fullName": "Sen. Durbin, Richard J. [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Durbin",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
      "state": "IL"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
      "state": "MN"
    },
    {
      "bioguideId": "C001056",
      "firstName": "John",
      "fullName": "Sen. Cornyn, John [R-TX]",
      "isOriginalCosponsor": "True",
      "lastName": "Cornyn",
      "party": "R",
      "sponsorshipDate": "2025-12-09",
      "state": "TX"
    },
    {
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2025-12-09",
      "state": "TN"
    },
    {
      "bioguideId": "G000359",
      "firstName": "Lindsey",
      "fullName": "Sen. Graham, Lindsey [R-SC]",
      "isOriginalCosponsor": "True",
      "lastName": "Graham",
      "party": "R",
      "sponsorshipDate": "2025-12-09",
      "state": "SC"
    },
    {
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "False",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "NH"
    },
    {
      "bioguideId": "M001244",
      "firstName": "Ashley",
      "fullName": "Sen. Moody, Ashley [R-FL]",
      "isOriginalCosponsor": "False",
      "lastName": "Moody",
      "party": "R",
      "sponsorshipDate": "2025-12-18",
      "state": "FL"
    },
    {
      "bioguideId": "K000393",
      "firstName": "John",
      "fullName": "Sen. Kennedy, John [R-LA]",
      "isOriginalCosponsor": "False",
      "lastName": "Kennedy",
      "party": "R",
      "sponsorshipDate": "2026-01-27",
      "state": "LA"
    },
    {
      "bioguideId": "B001319",
      "firstName": "Katie",
      "fullName": "Sen. Britt, Katie Boyd [R-AL]",
      "isOriginalCosponsor": "False",
      "lastName": "Britt",
      "party": "R",
      "sponsorshipDate": "2026-02-25",
      "state": "AL"
    },
    {
      "bioguideId": "C001098",
      "firstName": "Ted",
      "fullName": "Sen. Cruz, Ted [R-TX]",
      "isOriginalCosponsor": "False",
      "lastName": "Cruz",
      "party": "R",
      "sponsorshipDate": "2026-02-26",
      "state": "TX"
    },
    {
      "bioguideId": "K000383",
      "firstName": "Angus",
      "fullName": "Sen. King, Angus S., Jr. [I-ME]",
      "isOriginalCosponsor": "False",
      "lastName": "King",
      "middleName": "S.",
      "party": "I",
      "sponsorshipDate": "2026-03-02",
      "state": "ME"
    },
    {
      "bioguideId": "C001113",
      "firstName": "Catherine",
      "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
      "isOriginalCosponsor": "False",
      "lastName": "Cortez Masto",
      "party": "D",
      "sponsorshipDate": "2026-03-03",
      "state": "NV"
    },
    {
      "bioguideId": "K000377",
      "firstName": "Mark",
      "fullName": "Sen. Kelly, Mark [D-AZ]",
      "isOriginalCosponsor": "False",
      "lastName": "Kelly",
      "party": "D",
      "sponsorshipDate": "2026-03-04",
      "state": "AZ"
    },
    {
      "bioguideId": "G000574",
      "firstName": "Ruben",
      "fullName": "Sen. Gallego, Ruben [D-AZ]",
      "isOriginalCosponsor": "False",
      "lastName": "Gallego",
      "party": "D",
      "sponsorshipDate": "2026-03-09",
      "state": "AZ"
    },
    {
      "bioguideId": "S001208",
      "firstName": "Elissa",
      "fullName": "Sen. Slotkin, Elissa [D-MI]",
      "isOriginalCosponsor": "False",
      "lastName": "Slotkin",
      "party": "D",
      "sponsorshipDate": "2026-04-15",
      "state": "MI"
    },
    {
      "bioguideId": "G000555",
      "firstName": "Kirsten",
      "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
      "isOriginalCosponsor": "False",
      "lastName": "Gillibrand",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2026-05-21",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3398is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3398\nIN THE SENATE OF THE UNITED STATES\nDecember 9, 2025 Mr. Grassley (for himself, Mr. Durbin , Ms. Klobuchar , Mr. Cornyn , Mrs. Blackburn , and Mr. Graham ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo amend title 18, United States Code, to criminalize intentional threats to distribute child sexual abuse material, and to provide appropriate penalties for the use of child sexual abuse material to extort or coerce victims.\n#### 1. Short title\nThis Act may be cited as the Stop Sextortion Act .\n#### 2. Criminalizing threats to distribute child sexual abuse material\nTitle 18, United States Code, is amended\u2014\n**(1)**\nin section 2252\u2014\n**(A)**\nin subsection (a)(2)\u2014\n**(i)**\nin the matter preceding subparagraph (A)\u2014\n**(I)**\nby inserting , or threatens to distribute any visual depiction with intent to intimidate, coerce, extort, or cause substantial emotional distress to any person, after distributes, any visual depiction ;\n**(II)**\nby striking foreign commerce or that and inserting foreign commerce, or involving a visual depiction that ; and\n**(III)**\nby striking , or which contains materials which have been mailed or so shipped or transported, ; and\n**(B)**\nin subsection (b)\u2014\n**(i)**\nin paragraph (1), by striking Whoever and inserting Except as provided in paragraph (3), whoever ; and\n**(ii)**\nby adding at the end the following:\n(3) Whoever violates, or attempts or conspires to violate, subsection (a)(2) for threatening to distribute any visual depiction, as described in that subsection, shall be punished as provided in paragraph (2) of this subsection if no such visual depiction existed. ; and\n**(2)**\nin section 2252A\u2014\n**(A)**\nin subsection (a)(2)(A)\u2014\n**(i)**\nby inserting , or threatens to distribute any child pornography with intent to intimidate, coerce, extort, or cause substantial emotional distress to any person, after any child pornography ; and\n**(ii)**\nby striking foreign commerce or that and inserting foreign commerce, or involving any child pornography that ; and\n**(B)**\nin subsection (b)\u2014\n**(i)**\nin paragraph (1), by striking Whoever and inserting Except as provided in paragraph (4), whoever ; and\n**(ii)**\nby adding at the end the following:\n(4) Whoever violates, or attempts or conspires to violate, subsection (a)(2)(A) for threatening to distribute any child pornography, as described in that subsection, shall be punished as provided in paragraph (2) of this subsection if no such child pornography existed. .\n#### 3. Penalties for threats to distribute child sexual abuse material\n##### (a) In general\nTitle 18, United States Code, is amended\u2014\n**(1)**\nin section 1466A\u2014\n**(A)**\nin subsection (a), in the matter preceding subsection (b), by inserting , but if the offense involves the knowing use of a visual depiction of a minor engaged in sexually explicit conduct, with the intent to intimidate, coerce, extort, or cause substantial emotional distress to any person, the maximum term of imprisonment provided in section 2252A(b)(1) shall be increased by 10 years before the period at the end; and\n**(B)**\nin subsection (b), in the matter preceding subsection (c), by inserting , but if the offense involves the knowing use of a visual depiction of a minor engaged in sexually explicit conduct, with the intent to intimidate, coerce, extort, or cause substantial emotional distress to any person, the maximum term of imprisonment provided in section 2252A(b)(2) shall be increased by 10 years before the period at the end; and\n**(2)**\nin section 2260A\u2014\n**(A)**\nin the section heading, by striking Penalties for registered sex offenders and inserting Other offenses and penalties ;\n**(B)**\nby striking Whoever and inserting the following:\n(1) Offenses by registered sex offenders Whoever ; and\n**(C)**\nby adding at the end the following:\n(2) Additional penalties If any offense under section 875(d), 2251, 2252, 2252A, or 2260 involves the knowing use of child pornography with the intent to intimidate, coerce, extort, or cause substantial emotional distress to any person, the maximum term of imprisonment provided in section 875(d), 2251(e), 2252(b), 2252A(b), or 2260(c) shall be increased by 10 years. .\n##### (b) Clerical amendment\nThe table of sections for chapter 110 of title 18, United States Code, is amended by striking the item relating to section 2260A and inserting the following:\n2260A. Other offenses and penalties. .\n#### 4. Severability\nIf any provision of this Act, an amendment made by this Act, or the application of such provision or amendment to any person or circumstance is held to be unconstitutional, the remainder of this Act, the amendments made by this Act, and the application of the provisions of such to any person or circumstance shall not be affected thereby.",
      "versionDate": "2025-12-09",
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
        "actionDate": "2026-03-02",
        "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 346."
      },
      "number": "6719",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "James T. Woods Act",
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
        "name": "Crime and Law Enforcement",
        "updateDate": "2026-01-07T17:01:59Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-12-09",
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
          "measure-id": "id119s3398",
          "measure-number": "3398",
          "measure-type": "s",
          "orig-publish-date": "2025-12-09",
          "originChamber": "SENATE",
          "update-date": "2026-03-02"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s3398v00",
            "update-date": "2026-03-02"
          },
          "action-date": "2025-12-09",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Stop Sextortion Act</strong></p><p>This bill criminalizes threats to distribute child sexual abuse material to intimidate, coerce, extort, or cause substantial emotional distress. This practice is commonly referred to as <em>sextortion</em>. The bill also increases criminal penalties for related offenses that involve the use of child sexual abuse material to intimidate, coerce, extort, or cause substantial emotional distress.</p><p>Specifically, the bill establishes new federal criminal offenses for threatening to distribute child pornography or a visual depiction of a minor engaging in sexually explicit conduct with intent to intimidate, coerce, extort, or cause substantial emotional distress. An offense, or an attempt or conspiracy to commit the offense, is subject to criminal penalties.</p><p>Additionally, the bill increases the maximum prison term for various offenses involving the sexual exploitation of children if those offenses involve the use of child pornography or a visual depiction of a minor engaged in sexually explicit conduct with intent to intimidate, coerce, extort, or cause substantial emotional distress.</p>"
        },
        "title": "Stop Sextortion Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s3398.xml",
    "summary": {
      "actionDate": "2025-12-09",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Stop Sextortion Act</strong></p><p>This bill criminalizes threats to distribute child sexual abuse material to intimidate, coerce, extort, or cause substantial emotional distress. This practice is commonly referred to as <em>sextortion</em>. The bill also increases criminal penalties for related offenses that involve the use of child sexual abuse material to intimidate, coerce, extort, or cause substantial emotional distress.</p><p>Specifically, the bill establishes new federal criminal offenses for threatening to distribute child pornography or a visual depiction of a minor engaging in sexually explicit conduct with intent to intimidate, coerce, extort, or cause substantial emotional distress. An offense, or an attempt or conspiracy to commit the offense, is subject to criminal penalties.</p><p>Additionally, the bill increases the maximum prison term for various offenses involving the sexual exploitation of children if those offenses involve the use of child pornography or a visual depiction of a minor engaged in sexually explicit conduct with intent to intimidate, coerce, extort, or cause substantial emotional distress.</p>",
      "updateDate": "2026-03-02",
      "versionCode": "id119s3398"
    },
    "title": "Stop Sextortion Act"
  },
  "summaries": [
    {
      "actionDate": "2025-12-09",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Stop Sextortion Act</strong></p><p>This bill criminalizes threats to distribute child sexual abuse material to intimidate, coerce, extort, or cause substantial emotional distress. This practice is commonly referred to as <em>sextortion</em>. The bill also increases criminal penalties for related offenses that involve the use of child sexual abuse material to intimidate, coerce, extort, or cause substantial emotional distress.</p><p>Specifically, the bill establishes new federal criminal offenses for threatening to distribute child pornography or a visual depiction of a minor engaging in sexually explicit conduct with intent to intimidate, coerce, extort, or cause substantial emotional distress. An offense, or an attempt or conspiracy to commit the offense, is subject to criminal penalties.</p><p>Additionally, the bill increases the maximum prison term for various offenses involving the sexual exploitation of children if those offenses involve the use of child pornography or a visual depiction of a minor engaged in sexually explicit conduct with intent to intimidate, coerce, extort, or cause substantial emotional distress.</p>",
      "updateDate": "2026-03-02",
      "versionCode": "id119s3398"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-12-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3398is.xml"
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
      "title": "Stop Sextortion Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-22T19:48:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Stop Sextortion Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-31T03:53:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title 18, United States Code, to criminalize intentional threats to distribute child sexual abuse material, and to provide appropriate penalties for the use of child sexual abuse material to extort or coerce victims.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-31T03:48:18Z"
    }
  ]
}
```
