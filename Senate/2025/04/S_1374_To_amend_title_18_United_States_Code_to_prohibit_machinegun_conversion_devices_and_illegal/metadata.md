# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1374?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1374
- Title: BUMP Act
- Congress: 119
- Bill type: S
- Bill number: 1374
- Origin chamber: Senate
- Introduced date: 2025-04-09
- Update date: 2026-03-23T18:28:56Z
- Update date including text: 2026-03-23T18:28:56Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-04-09: Introduced in Senate
- 2025-04-09 - IntroReferral: Introduced in Senate
- 2025-04-09 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-04-09: Introduced in Senate

## Actions

- 2025-04-09 - IntroReferral: Introduced in Senate
- 2025-04-09 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-09",
    "latestAction": {
      "actionDate": "2025-04-09",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1374",
    "number": "1374",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "H001046",
        "district": "",
        "firstName": "Martin",
        "fullName": "Sen. Heinrich, Martin [D-NM]",
        "lastName": "Heinrich",
        "party": "D",
        "state": "NM"
      }
    ],
    "title": "BUMP Act",
    "type": "S",
    "updateDate": "2026-03-23T18:28:56Z",
    "updateDateIncludingText": "2026-03-23T18:28:56Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-09",
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
      "actionDate": "2025-04-09",
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
            "date": "2025-04-09T16:36:57Z",
            "name": "Referred To"
          },
          {
            "date": "2025-04-09T16:36:57Z",
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
      "bioguideId": "C001035",
      "firstName": "Susan",
      "fullName": "Sen. Collins, Susan M. [R-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "Collins",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-04-09",
      "state": "ME"
    },
    {
      "bioguideId": "C001113",
      "firstName": "Catherine",
      "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Cortez Masto",
      "party": "D",
      "sponsorshipDate": "2025-04-09",
      "state": "NV"
    },
    {
      "bioguideId": "R000608",
      "firstName": "Jacky",
      "fullName": "Sen. Rosen, Jacky [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Rosen",
      "party": "D",
      "sponsorshipDate": "2025-04-09",
      "state": "NV"
    },
    {
      "bioguideId": "F000479",
      "firstName": "John",
      "fullName": "Sen. Fetterman, John [D-PA]",
      "isOriginalCosponsor": "True",
      "lastName": "Fetterman",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-04-09",
      "state": "PA"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-04-09",
      "state": "DE"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-04-09",
      "state": "MN"
    },
    {
      "bioguideId": "K000384",
      "firstName": "Timothy",
      "fullName": "Sen. Kaine, Tim [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Kaine",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-04-09",
      "state": "VA"
    },
    {
      "bioguideId": "R000122",
      "firstName": "John",
      "fullName": "Sen. Reed, Jack [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Reed",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-04-09",
      "state": "RI"
    },
    {
      "bioguideId": "W000802",
      "firstName": "Sheldon",
      "fullName": "Sen. Whitehouse, Sheldon [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Whitehouse",
      "party": "D",
      "sponsorshipDate": "2025-04-09",
      "state": "RI"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-04-09",
      "state": "CT"
    },
    {
      "bioguideId": "D000563",
      "firstName": "Richard",
      "fullName": "Sen. Durbin, Richard J. [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Durbin",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-04-09",
      "state": "IL"
    },
    {
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2025-04-09",
      "state": "NH"
    },
    {
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2025-04-09",
      "state": "CA"
    },
    {
      "bioguideId": "S001203",
      "firstName": "Tina",
      "fullName": "Sen. Smith, Tina [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-04-09",
      "state": "MN"
    },
    {
      "bioguideId": "K000383",
      "firstName": "Angus",
      "fullName": "Sen. King, Angus S., Jr. [I-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "King",
      "middleName": "S.",
      "party": "I",
      "sponsorshipDate": "2025-04-09",
      "state": "ME"
    },
    {
      "bioguideId": "K000377",
      "firstName": "Mark",
      "fullName": "Sen. Kelly, Mark [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kelly",
      "party": "D",
      "sponsorshipDate": "2025-04-09",
      "state": "AZ"
    },
    {
      "bioguideId": "B001267",
      "firstName": "Michael",
      "fullName": "Sen. Bennet, Michael F. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Bennet",
      "party": "D",
      "sponsorshipDate": "2025-04-09",
      "state": "CO"
    },
    {
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2025-04-09",
      "state": "IL"
    },
    {
      "bioguideId": "M000133",
      "firstName": "Edward",
      "fullName": "Sen. Markey, Edward J. [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Markey",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-04-09",
      "state": "MA"
    },
    {
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2025-04-09",
      "state": "MD"
    },
    {
      "bioguideId": "S000033",
      "firstName": "Bernie",
      "fullName": "Sen. Sanders, Bernard [I-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sanders",
      "party": "I",
      "sponsorshipDate": "2025-04-09",
      "state": "VT"
    },
    {
      "bioguideId": "M001111",
      "firstName": "Patty",
      "fullName": "Sen. Murray, Patty [D-WA]",
      "isOriginalCosponsor": "True",
      "lastName": "Murray",
      "party": "D",
      "sponsorshipDate": "2025-04-09",
      "state": "WA"
    },
    {
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2025-04-09",
      "state": "OR"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-04-09",
      "state": "NJ"
    },
    {
      "bioguideId": "H001042",
      "firstName": "Mazie",
      "fullName": "Sen. Hirono, Mazie K. [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Hirono",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-04-09",
      "state": "HI"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-04-09",
      "state": "VT"
    },
    {
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2025-04-09",
      "state": "CA"
    },
    {
      "bioguideId": "S001194",
      "firstName": "Brian",
      "fullName": "Sen. Schatz, Brian [D-HI]",
      "isOriginalCosponsor": "False",
      "lastName": "Schatz",
      "party": "D",
      "sponsorshipDate": "2025-07-22",
      "state": "HI"
    },
    {
      "bioguideId": "K000394",
      "firstName": "Andy",
      "fullName": "Sen. Kim, Andy [D-NJ]",
      "isOriginalCosponsor": "False",
      "lastName": "Kim",
      "party": "D",
      "sponsorshipDate": "2025-10-07",
      "state": "NJ"
    },
    {
      "bioguideId": "W000817",
      "firstName": "Elizabeth",
      "fullName": "Sen. Warren, Elizabeth [D-MA]",
      "isOriginalCosponsor": "False",
      "lastName": "Warren",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-01-29",
      "state": "MA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1374is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1374\nIN THE SENATE OF THE UNITED STATES\nApril 9, 2025 Mr. Heinrich (for himself, Ms. Collins , Ms. Cortez Masto , Ms. Rosen , Mr. Fetterman , Mr. Coons , Ms. Klobuchar , Mr. Kaine , Mr. Reed , Mr. Whitehouse , Mr. Blumenthal , Mr. Durbin , Mrs. Shaheen , Mr. Padilla , Ms. Smith , Mr. King , Mr. Kelly , Mr. Bennet , Ms. Duckworth , Mr. Markey , Mr. Van Hollen , Mr. Sanders , Mrs. Murray , Mr. Wyden , Mr. Booker , Ms. Hirono , Mr. Welch , and Mr. Schiff ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo amend title 18, United States Code, to prohibit machinegun conversion devices and illegal modifications of semiautomatic firearms, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Banning Unlawful Machinegun Parts Act or the BUMP Act .\n#### 2. Prohibition\n##### (a) In general\nChapter 44 of title 18, United States Code, is amended\u2014\n**(1)**\nin section 921(a), by inserting after paragraph (30) the following:\n(31) The term semiautomatic firearm means any firearm that\u2014 (A) upon initiating the firing sequence, fires the first chambered cartridge and uses a portion of the energy of the firing cartridge to\u2014 (i) extract the expended cartridge case; (ii) chamber the next round; and (iii) prepare the firing mechanism to fire again; (B) requires a separate pull, release, push, or initiation of the trigger to fire each cartridge; and (C) is not a machinegun. ;\n**(2)**\nin section 922, by inserting after subsection (u) the following:\n(v) (1) Except as provided in paragraphs (3) and (4), on and after the date that is 120 days after the date of enactment of this subsection, it shall be unlawful for any person to import, sell, manufacture, transfer, receive, or possess, in or affecting interstate or foreign commerce\u2014 (A) any manual, power-driven, or electronic device primarily designed, or redesigned, so that when the device is attached to a semiautomatic firearm the device\u2014 (i) materially increases the rate of fire of the firearm; or (ii) approximates the action or rate of fire of a machinegun; (B) any device, part, or combination of parts, that is designed or functions to materially increase the rate of fire of a firearm, by eliminating the need for the operator of the firearm to make a separate movement for each individual function of the trigger; or (C) a semiautomatic firearm that has been modified in any way that\u2014 (i) materially increases the rate of fire of the firearm; or (ii) approximates the action or rate of fire of a machinegun. (2) Except as provided in paragraph (3), not later than 120 days after the date of enactment of this subsection, any person who lawfully owns or possesses a semiautomatic firearm that was modified as described in paragraph (1)(C) before such date of enactment shall register the semiautomatic firearm in accordance with section 5841 of the Internal Revenue Code of 1986. (3) This subsection does not apply with respect to the importation for, manufacture for, sale to, transfer to, or possession by or under the authority of, the United States or any department or agency thereof or a State or Tribe, or a department, agency, or political subdivision thereof. (4) Paragraph (1) shall not apply to any lawful transfer or possession of a semiautomatic firearm described in paragraph (1)(C) that\u2014 (A) was lawfully modified and possessed before the date of enactment of this subsection; and (B) is registered in accordance with paragraph (2). ; and\n**(3)**\nin section 924(a)(2), by striking , or (o) and inserting (o), or (v) .\n##### (b) Amendment to the National Firearms Act\nSection 5845(a) of the Internal Revenue Code of 1986 is amended by striking and (8) a destructive device and inserting (8) a destructive device; and (9) a semiautomatic firearm, as defined in section 921 of title 18, United States Code, that is modified as described in section 922(v)(1)(C) of such title .",
      "versionDate": "2025-04-09",
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
        "actionDate": "2025-04-09",
        "text": "Referred to the Committee on the Judiciary, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "2799",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Closing the Bump Stock Loophole Act of 2025",
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
        "updateDate": "2025-05-16T17:43:32Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-04-09",
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
          "measure-id": "id119s1374",
          "measure-number": "1374",
          "measure-type": "s",
          "orig-publish-date": "2025-04-09",
          "originChamber": "SENATE",
          "update-date": "2026-03-23"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s1374v00",
            "update-date": "2026-03-23"
          },
          "action-date": "2025-04-09",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Banning Unlawful Machinegun Parts Act or the BUMP Act</strong></p><p>This bill\u00a0generally prohibits the import, sale, manufacture, transfer, receipt, or possession of</p><ul><li>a device that is primarily designed, or redesigned, to increase the rate of fire when attached to a semiautomatic firearm;</li><li>a device, part, or combination of parts that is designed and functions to increase the rate of fire of a firearm; or</li><li>a semiautomatic firearm that has been modified to materially increase the rate of fire or to approximate the action or rate of fire of a machine gun.</li></ul><p>Additionally, the bill adds to the list of firearms subject to regulation under the National Firearms Act\u00a0semiautomatic firearms\u00a0that have been modified to materially increase the rate of fire or approximate the action or rate of fire of a machine gun.</p>"
        },
        "title": "BUMP Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s1374.xml",
    "summary": {
      "actionDate": "2025-04-09",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Banning Unlawful Machinegun Parts Act or the BUMP Act</strong></p><p>This bill\u00a0generally prohibits the import, sale, manufacture, transfer, receipt, or possession of</p><ul><li>a device that is primarily designed, or redesigned, to increase the rate of fire when attached to a semiautomatic firearm;</li><li>a device, part, or combination of parts that is designed and functions to increase the rate of fire of a firearm; or</li><li>a semiautomatic firearm that has been modified to materially increase the rate of fire or to approximate the action or rate of fire of a machine gun.</li></ul><p>Additionally, the bill adds to the list of firearms subject to regulation under the National Firearms Act\u00a0semiautomatic firearms\u00a0that have been modified to materially increase the rate of fire or approximate the action or rate of fire of a machine gun.</p>",
      "updateDate": "2026-03-23",
      "versionCode": "id119s1374"
    },
    "title": "BUMP Act"
  },
  "summaries": [
    {
      "actionDate": "2025-04-09",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Banning Unlawful Machinegun Parts Act or the BUMP Act</strong></p><p>This bill\u00a0generally prohibits the import, sale, manufacture, transfer, receipt, or possession of</p><ul><li>a device that is primarily designed, or redesigned, to increase the rate of fire when attached to a semiautomatic firearm;</li><li>a device, part, or combination of parts that is designed and functions to increase the rate of fire of a firearm; or</li><li>a semiautomatic firearm that has been modified to materially increase the rate of fire or to approximate the action or rate of fire of a machine gun.</li></ul><p>Additionally, the bill adds to the list of firearms subject to regulation under the National Firearms Act\u00a0semiautomatic firearms\u00a0that have been modified to materially increase the rate of fire or approximate the action or rate of fire of a machine gun.</p>",
      "updateDate": "2026-03-23",
      "versionCode": "id119s1374"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-04-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1374is.xml"
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
      "title": "BUMP Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-31T13:48:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "BUMP Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-23T02:53:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Banning Unlawful Machinegun Parts Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-23T02:53:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title 18, United States Code, to prohibit machinegun conversion devices and illegal modifications of semiautomatic firearms, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-23T02:48:28Z"
    }
  ]
}
```
