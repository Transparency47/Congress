# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2803?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/2803
- Title: Protecting Election Administration from Interference Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 2803
- Origin chamber: House
- Introduced date: 2025-04-09
- Update date: 2025-07-02T16:27:26Z
- Update date including text: 2025-07-02T16:27:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-04-09: Introduced in House
- 2025-04-09 - IntroReferral: Introduced in House
- 2025-04-09 - IntroReferral: Introduced in House
- 2025-04-09 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on House Administration, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-04-09 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on House Administration, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-04-09: Introduced in House

## Actions

- 2025-04-09 - IntroReferral: Introduced in House
- 2025-04-09 - IntroReferral: Introduced in House
- 2025-04-09 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on House Administration, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-04-09 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on House Administration, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

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
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/2803",
    "number": "2803",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "V000131",
        "district": "33",
        "firstName": "Marc",
        "fullName": "Rep. Veasey, Marc A. [D-TX-33]",
        "lastName": "Veasey",
        "party": "D",
        "state": "TX"
      }
    ],
    "title": "Protecting Election Administration from Interference Act of 2025",
    "type": "HR",
    "updateDate": "2025-07-02T16:27:26Z",
    "updateDateIncludingText": "2025-07-02T16:27:26Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-09",
      "committees": {
        "item": {
          "name": "Committee on House Administration",
          "systemCode": "hsha00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on the Judiciary, and in addition to the Committee on House Administration, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-09",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on the Judiciary, and in addition to the Committee on House Administration, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-04-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-09",
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
          "date": "2025-04-09T16:01:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Committee on House Administration",
      "systemCode": "hsha00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-04-09T16:01:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
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
      "bioguideId": "E000299",
      "district": "16",
      "firstName": "Veronica",
      "fullName": "Rep. Escobar, Veronica [D-TX-16]",
      "isOriginalCosponsor": "True",
      "lastName": "Escobar",
      "party": "D",
      "sponsorshipDate": "2025-04-09",
      "state": "TX"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-04-09",
      "state": "DC"
    },
    {
      "bioguideId": "T000469",
      "district": "20",
      "firstName": "Paul",
      "fullName": "Rep. Tonko, Paul [D-NY-20]",
      "isOriginalCosponsor": "True",
      "lastName": "Tonko",
      "party": "D",
      "sponsorshipDate": "2025-04-09",
      "state": "NY"
    },
    {
      "bioguideId": "G000553",
      "district": "9",
      "firstName": "Al",
      "fullName": "Rep. Green, Al [D-TX-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Green",
      "party": "D",
      "sponsorshipDate": "2025-04-09",
      "state": "TX"
    },
    {
      "bioguideId": "D000530",
      "district": "17",
      "firstName": "Christopher",
      "fullName": "Rep. Deluzio, Christopher R. [D-PA-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Deluzio",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-04-09",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2803ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2803\nIN THE HOUSE OF REPRESENTATIVES\nApril 9, 2025 Mr. Veasey (for himself, Ms. Escobar , Ms. Norton , Mr. Tonko , Mr. Green of Texas , and Mr. Deluzio ) introduced the following bill; which was referred to the Committee on the Judiciary , and in addition to the Committee on House Administration , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo enhance protections for election records.\n#### 1. Short title\nThis Act may be cited as the Protecting Election Administration from Interference Act of 2025 .\n#### 2. Enhancement of protections for election records, papers, and equipment\n##### (a) Preservation of records, paper, and equipment\nSection 301 of the Civil Rights Act of 1960 ( 52 U.S.C. 20701 ) is amended\u2014\n**(1)**\nby striking Every officer and inserting the following:\n(a) In general Every officer ;\n**(2)**\nby striking records and papers and inserting records (including electronic records), papers, and election equipment each place the term appears;\n**(3)**\nby striking record or paper and inserting record (including electronic record), paper, or election equipment ;\n**(4)**\nby inserting (but only under the direct administrative supervision of an election officer). Notwithstanding any other provision of this section, the paper record of a voter\u2019s cast ballot shall remain the official record of the cast ballot for purposes of this title after upon such custodian ;\n**(5)**\nby inserting , or acts in reckless disregard of, after fails to comply with ; and\n**(6)**\nby inserting after subsection (a) the following:\n(b) Election equipment The requirement in subsection (a) to preserve election equipment shall not be construed to prevent the reuse of such equipment in any election that takes place within twenty-two months of a Federal election described in subsection (a), provided that all electronic records, files, and data from such equipment related to such Federal election are retained and preserved. (c) Guidance Not later than 1 year after the date of the enactment of this subsection, the Director of the Cybersecurity and Infrastructure Security Agency of the Department of Homeland Security, in consultation with the Election Assistance Commission and the Attorney General, shall issue guidance regarding compliance with subsections (a) and (b), including minimum standards and best practices for retaining and preserving records (including electronic records), papers, and election equipment in compliance with subsections (a) and (b). Such guidance shall also include protocols for enabling the observation of the preservation, security, and transfer of records (including electronic records), papers, and election equipment described in subsection (a) by the Attorney General and by a representative of each party, as defined by the Attorney General. .\n##### (b) Penalty\nSection 302 of the Civil Rights Act of 1960 ( 52 U.S.C. 20702 ) is amended\u2014\n**(1)**\nby inserting , or whose reckless disregard of section 301 results in the theft, destruction, concealment, mutilation, or alteration of, after or alters ; and\n**(2)**\nby striking record or paper and inserting record (including electronic record), paper, or election equipment .\n##### (c) Inspection, reproduction, and copying\nSection 303 of the Civil Rights Act of 1960 ( 52 U.S.C. 20703 ) is amended by striking record or paper and inserting \u201crecord (including electronic record), paper, or election equipment\u201d each place the term appears.\n##### (d) Nondisclosure\nSection 304 of the Civil Rights Act of 1960 ( 52 U.S.C. 20704 ) is amended by striking record or paper and inserting \u201crecord (including electronic record), paper, or election equipment\u201d.\n##### (e) Jurisdiction To compel production\nSection 305 of the Civil Rights Act of 1960 ( 52 U.S.C. 20705 ) is amended by striking record or paper and inserting \u201crecord (including electronic record), paper, or election equipment\u201d each place the term appears.\n#### 3. Judicial review for election records\nTitle III of the Civil Rights Act of 1960 ( 52 U.S.C. 20701 et seq. ), is amended\u2014\n**(1)**\nby redesignating section 306 as section 307; and\n**(2)**\nby inserting after section 305 the following:\n306. Judicial review to ensure compliance (a) Right of action The Attorney General, a representative of the Attorney General, or a candidate in a Federal election described in section 301 may bring an action in the district court of the United States for the judicial district in which a record (including electronic record), paper, or election equipment is located, or in the United States District Court for the District of Columbia, to compel compliance with the requirements of section 301. (b) Duty To expedite It shall be the duty of the court to advance on the docket, and to expedite to the greatest possible extent the disposition of, the action and appeal under this section. .\n#### 4. Criminal penalties for intimidation of tabulation, canvass, or certification efforts\nSection 12(1) of the National Voter Registration Act of 1993 ( 52 U.S.C. 20511(1) ) is amended\u2014\n**(1)**\nin subparagraph (B), by striking or at the end; and\n**(2)**\nby adding at the end the following:\n(D) processing or scanning ballots, or tabulating, canvassing, or certifying voting results; or .",
      "versionDate": "2025-04-09",
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
        "name": "Government Operations and Politics",
        "updateDate": "2025-05-23T14:21:28Z"
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
    "originChamber": "House",
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
          "measure-id": "id119hr2803",
          "measure-number": "2803",
          "measure-type": "hr",
          "orig-publish-date": "2025-04-09",
          "originChamber": "HOUSE",
          "update-date": "2025-07-02"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr2803v00",
            "update-date": "2025-07-02"
          },
          "action-date": "2025-04-09",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Protecting Election Administration from Interference Act of </strong><strong>2025</strong></p><p>This bill revises preservation and retention requirements for federal election records. It also revises criminal penalties related to election records and the voting process.</p><p>Under current law, election officials must, for a period of 22 months from the federal election, retain and preserve all election-related records and papers. This bill extends the requirement to electronic records and election equipment.</p><p>Next, the bill directs the Cybersecurity and Infrastructure Security Agency to issue minimum standards and best practices for retaining and preserving records (including electronic records), papers, and election equipment, including protocols for observing their preservation, security, and transfer by the Department of Justice (DOJ) and a representative of each political party.</p><p>In addition, the bill revises the federal criminal offense related to election records or papers to include reckless disregard of election record requirements resulting in the theft, destruction, concealment, mutilation, or alteration of a record, paper, or election equipment.</p><p>Further, the bill allows DOJ to demand electronic records and election equipment be made available for inspection and generally prohibits DOJ from disclosing this information.</p><p>The bill allows DOJ and candidates for federal office to bring an action in a district court to compel compliance with election record requirements.</p><p>Finally, the bill extends criminal penalties related to voting interference to include intimidating, threatening, or coercing (or attempting to do so) an individual for processing or scanning ballots, tabulating, canvassing, or certifying voting results.</p>"
        },
        "title": "Protecting Election Administration from Interference Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr2803.xml",
    "summary": {
      "actionDate": "2025-04-09",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Protecting Election Administration from Interference Act of </strong><strong>2025</strong></p><p>This bill revises preservation and retention requirements for federal election records. It also revises criminal penalties related to election records and the voting process.</p><p>Under current law, election officials must, for a period of 22 months from the federal election, retain and preserve all election-related records and papers. This bill extends the requirement to electronic records and election equipment.</p><p>Next, the bill directs the Cybersecurity and Infrastructure Security Agency to issue minimum standards and best practices for retaining and preserving records (including electronic records), papers, and election equipment, including protocols for observing their preservation, security, and transfer by the Department of Justice (DOJ) and a representative of each political party.</p><p>In addition, the bill revises the federal criminal offense related to election records or papers to include reckless disregard of election record requirements resulting in the theft, destruction, concealment, mutilation, or alteration of a record, paper, or election equipment.</p><p>Further, the bill allows DOJ to demand electronic records and election equipment be made available for inspection and generally prohibits DOJ from disclosing this information.</p><p>The bill allows DOJ and candidates for federal office to bring an action in a district court to compel compliance with election record requirements.</p><p>Finally, the bill extends criminal penalties related to voting interference to include intimidating, threatening, or coercing (or attempting to do so) an individual for processing or scanning ballots, tabulating, canvassing, or certifying voting results.</p>",
      "updateDate": "2025-07-02",
      "versionCode": "id119hr2803"
    },
    "title": "Protecting Election Administration from Interference Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-04-09",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Protecting Election Administration from Interference Act of </strong><strong>2025</strong></p><p>This bill revises preservation and retention requirements for federal election records. It also revises criminal penalties related to election records and the voting process.</p><p>Under current law, election officials must, for a period of 22 months from the federal election, retain and preserve all election-related records and papers. This bill extends the requirement to electronic records and election equipment.</p><p>Next, the bill directs the Cybersecurity and Infrastructure Security Agency to issue minimum standards and best practices for retaining and preserving records (including electronic records), papers, and election equipment, including protocols for observing their preservation, security, and transfer by the Department of Justice (DOJ) and a representative of each political party.</p><p>In addition, the bill revises the federal criminal offense related to election records or papers to include reckless disregard of election record requirements resulting in the theft, destruction, concealment, mutilation, or alteration of a record, paper, or election equipment.</p><p>Further, the bill allows DOJ to demand electronic records and election equipment be made available for inspection and generally prohibits DOJ from disclosing this information.</p><p>The bill allows DOJ and candidates for federal office to bring an action in a district court to compel compliance with election record requirements.</p><p>Finally, the bill extends criminal penalties related to voting interference to include intimidating, threatening, or coercing (or attempting to do so) an individual for processing or scanning ballots, tabulating, canvassing, or certifying voting results.</p>",
      "updateDate": "2025-07-02",
      "versionCode": "id119hr2803"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2803ih.xml"
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
      "title": "Protecting Election Administration from Interference Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-24T02:53:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Protecting Election Administration from Interference Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-24T02:53:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To enhance protections for election records.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-24T02:48:22Z"
    }
  ]
}
```
