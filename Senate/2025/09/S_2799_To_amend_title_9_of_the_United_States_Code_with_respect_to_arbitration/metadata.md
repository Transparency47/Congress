# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2799?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2799
- Title: Forced Arbitration Injustice Repeal Act
- Congress: 119
- Bill type: S
- Bill number: 2799
- Origin chamber: Senate
- Introduced date: 2025-09-15
- Update date: 2026-03-31T15:42:40Z
- Update date including text: 2026-03-31T15:42:40Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-09-15: Introduced in Senate
- 2025-09-15 - IntroReferral: Introduced in Senate
- 2025-09-15 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-09-15: Introduced in Senate

## Actions

- 2025-09-15 - IntroReferral: Introduced in Senate
- 2025-09-15 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-15",
    "latestAction": {
      "actionDate": "2025-09-15",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2799",
    "number": "2799",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Law"
    },
    "sponsors": [
      {
        "bioguideId": "B001277",
        "district": "",
        "firstName": "Richard",
        "fullName": "Sen. Blumenthal, Richard [D-CT]",
        "lastName": "Blumenthal",
        "party": "D",
        "state": "CT"
      }
    ],
    "title": "Forced Arbitration Injustice Repeal Act",
    "type": "S",
    "updateDate": "2026-03-31T15:42:40Z",
    "updateDateIncludingText": "2026-03-31T15:42:40Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-09-15",
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
      "actionDate": "2025-09-15",
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
          "date": "2025-09-15T19:43:25Z",
          "name": "Referred To"
        }
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
      "bioguideId": "B001230",
      "firstName": "Tammy",
      "fullName": "Sen. Baldwin, Tammy [D-WI]",
      "isOriginalCosponsor": "True",
      "lastName": "Baldwin",
      "party": "D",
      "sponsorshipDate": "2025-09-15",
      "state": "WI"
    },
    {
      "bioguideId": "B001267",
      "firstName": "Michael",
      "fullName": "Sen. Bennet, Michael F. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Bennet",
      "party": "D",
      "sponsorshipDate": "2025-09-15",
      "state": "CO"
    },
    {
      "bioguideId": "B001303",
      "firstName": "Lisa",
      "fullName": "Sen. Blunt Rochester, Lisa [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Blunt Rochester",
      "party": "D",
      "sponsorshipDate": "2025-09-15",
      "state": "DE"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-09-15",
      "state": "NJ"
    },
    {
      "bioguideId": "C000127",
      "firstName": "Maria",
      "fullName": "Sen. Cantwell, Maria [D-WA]",
      "isOriginalCosponsor": "True",
      "lastName": "Cantwell",
      "party": "D",
      "sponsorshipDate": "2025-09-15",
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
      "sponsorshipDate": "2025-09-15",
      "state": "DE"
    },
    {
      "bioguideId": "C001113",
      "firstName": "Catherine",
      "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Cortez Masto",
      "party": "D",
      "sponsorshipDate": "2025-09-15",
      "state": "NV"
    },
    {
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2025-09-15",
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
      "sponsorshipDate": "2025-09-15",
      "state": "IL"
    },
    {
      "bioguideId": "G000555",
      "firstName": "Kirsten",
      "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
      "isOriginalCosponsor": "True",
      "lastName": "Gillibrand",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-09-15",
      "state": "NY"
    },
    {
      "bioguideId": "H001076",
      "firstName": "Maggie",
      "fullName": "Sen. Hassan, Margaret Wood [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Hassan",
      "party": "D",
      "sponsorshipDate": "2025-09-15",
      "state": "NH"
    },
    {
      "bioguideId": "H001046",
      "firstName": "Martin",
      "fullName": "Sen. Heinrich, Martin [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Heinrich",
      "party": "D",
      "sponsorshipDate": "2025-09-15",
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
      "sponsorshipDate": "2025-09-15",
      "state": "HI"
    },
    {
      "bioguideId": "K000384",
      "firstName": "Timothy",
      "fullName": "Sen. Kaine, Tim [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Kaine",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-09-15",
      "state": "VA"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-09-15",
      "state": "MN"
    },
    {
      "bioguideId": "L000570",
      "firstName": "Ben",
      "fullName": "Sen. Luj\u00e1n, Ben Ray [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Luj\u00e1n",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-09-15",
      "state": "NM"
    },
    {
      "bioguideId": "M000133",
      "firstName": "Edward",
      "fullName": "Sen. Markey, Edward J. [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Markey",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-09-15",
      "state": "MA"
    },
    {
      "bioguideId": "M001169",
      "firstName": "Christopher",
      "fullName": "Sen. Murphy, Christopher [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Murphy",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-09-15",
      "state": "CT"
    },
    {
      "bioguideId": "M001111",
      "firstName": "Patty",
      "fullName": "Sen. Murray, Patty [D-WA]",
      "isOriginalCosponsor": "True",
      "lastName": "Murray",
      "party": "D",
      "sponsorshipDate": "2025-09-15",
      "state": "WA"
    },
    {
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2025-09-15",
      "state": "CA"
    },
    {
      "bioguideId": "P000595",
      "firstName": "Gary",
      "fullName": "Sen. Peters, Gary C. [D-MI]",
      "isOriginalCosponsor": "True",
      "lastName": "Peters",
      "party": "D",
      "sponsorshipDate": "2025-09-15",
      "state": "MI"
    },
    {
      "bioguideId": "R000122",
      "firstName": "John",
      "fullName": "Sen. Reed, Jack [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Reed",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-09-15",
      "state": "RI"
    },
    {
      "bioguideId": "R000608",
      "firstName": "Jacky",
      "fullName": "Sen. Rosen, Jacky [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Rosen",
      "party": "D",
      "sponsorshipDate": "2025-09-15",
      "state": "NV"
    },
    {
      "bioguideId": "S000033",
      "firstName": "Bernie",
      "fullName": "Sen. Sanders, Bernard [I-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sanders",
      "party": "I",
      "sponsorshipDate": "2025-09-15",
      "state": "VT"
    },
    {
      "bioguideId": "S001194",
      "firstName": "Brian",
      "fullName": "Sen. Schatz, Brian [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Schatz",
      "party": "D",
      "sponsorshipDate": "2025-09-15",
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
      "sponsorshipDate": "2025-09-15",
      "state": "CA"
    },
    {
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2025-09-15",
      "state": "NH"
    },
    {
      "bioguideId": "S001203",
      "firstName": "Tina",
      "fullName": "Sen. Smith, Tina [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-09-15",
      "state": "MN"
    },
    {
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2025-09-15",
      "state": "MD"
    },
    {
      "bioguideId": "W000790",
      "firstName": "Raphael",
      "fullName": "Sen. Warnock, Raphael G. [D-GA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warnock",
      "party": "D",
      "sponsorshipDate": "2025-09-15",
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
      "sponsorshipDate": "2025-09-15",
      "state": "MA"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-09-15",
      "state": "VT"
    },
    {
      "bioguideId": "W000802",
      "firstName": "Sheldon",
      "fullName": "Sen. Whitehouse, Sheldon [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Whitehouse",
      "party": "D",
      "sponsorshipDate": "2025-09-15",
      "state": "RI"
    },
    {
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2025-09-15",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2799is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2799\nIN THE SENATE OF THE UNITED STATES\nSeptember 15, 2025 Mr. Blumenthal (for himself, Ms. Baldwin , Mr. Bennet , Ms. Blunt Rochester , Mr. Booker , Ms. Cantwell , Mr. Coons , Ms. Cortez Masto , Ms. Duckworth , Mr. Durbin , Mrs. Gillibrand , Ms. Hassan , Mr. Heinrich , Ms. Hirono , Mr. Kaine , Ms. Klobuchar , Mr. Luj\u00e1n , Mr. Markey , Mr. Murphy , Mrs. Murray , Mr. Padilla , Mr. Peters , Mr. Reed , Ms. Rosen , Mr. Sanders , Mr. Schatz , Mr. Schiff , Mrs. Shaheen , Ms. Smith , Mr. Van Hollen , Mr. Warnock , Ms. Warren , Mr. Welch , Mr. Whitehouse , and Mr. Wyden ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo amend title 9 of the United States Code with respect to arbitration.\n#### 1. Short title\nThis Act may be cited as the Forced Arbitration Injustice Repeal Act .\n#### 2. Purposes\nThe purposes of this Act are to\u2014\n**(1)**\nprohibit predispute arbitration agreements that force arbitration of future employment, consumer, antitrust, or civil rights disputes; and\n**(2)**\nprohibit agreements and practices that interfere with the right of individuals, workers, and small businesses to participate in a joint, class, or collective action related to an employment, consumer, antitrust, or civil rights dispute.\n#### 3. Arbitration of employment, consumer, antitrust, and civil rights disputes\n##### (a) In general\nTitle 9 of the United States Code is amended by adding at the end the following:\n5 Arbitration of Employment, Consumer, Antitrust, and Civil Rights Disputes Sec. 501. Definitions. 502. No validity or enforceability. 501. Definitions In this chapter\u2014 (1) the term antitrust dispute means a dispute\u2014 (A) arising from an alleged violation of the antitrust laws (as defined in subsection (a) of the first section of the Clayton Act ( 15 U.S.C. 12(a) )) or State antitrust laws; and (B) in which the plaintiffs seek certification as a class under rule 23 of the Federal Rules of Civil Procedure or a comparable rule or provision of State law; (2) the term civil rights dispute means a dispute\u2014 (A) arising from an alleged violation of\u2014 (i) the Constitution of the United States or the constitution of a State; or (ii) any Federal, State, or local law that prohibits discrimination on the basis of race, sex, age, gender identity, sexual orientation, disability, religion, national origin, or any legally protected status in education, employment, credit, housing, public accommodations and facilities, voting, veterans or servicemembers, health care, or a program funded or conducted by the Federal Government or a State government, including any law referred to or described in section 62(e) of the Internal Revenue Code of 1986, including parts of such law not explicitly referenced in such section but that relate to protecting individuals on any such basis; and (B) in which at least 1 party alleging a violation described in subparagraph (A) is an individual (or an authorized representative of an individual), including an individual seeking certification as a class under rule 23 of the Federal Rules of Civil Procedure or a comparable rule or provision of State law; (3) the term consumer dispute means a dispute between\u2014 (A) 1 or more individuals, including an individual who seeks certification as a class under rule 23 of the Federal Rules of Civil Procedure or a comparable rule or provision of State law, who seek or acquire real or personal property, services (including services related to digital technology), securities or other investments, money, or credit for personal, family, or household purposes; and (B) (i) the seller or provider of such property, services, securities or other investments, money, or credit; or (ii) a third party involved in the selling, providing of, payment for, receipt or use of information about, or other relationship to any such property, services, securities or other investments, money, or credit; (4) the term employment dispute \u2014 (A) means a dispute between 1 or more individuals (or their authorized representative) and a person arising out of or related to the work relationship or prospective work relationship between them, including a dispute regarding the terms of or payment for, advertising of, recruiting for, referring of, arranging for, or discipline or discharge in connection with, such work, regardless of whether the individual is or would be classified as an employee or an independent contractor with respect to such work; and (B) includes\u2014 (i) a dispute arising under any law referred to or described in section 62(e) of the Internal Revenue Code of 1986, including parts of such law not explicitly referenced in such section but that relate to protecting individuals on any such basis; and (ii) a dispute in which an individual seeks certification as a class under rule 23 of the Federal Rules of Civil Procedure or as a collective action under section 16(b) of the Fair Labor Standards Act ( 29 U.S.C. 216(b) ), or a comparable rule or provision of State law; (5) the term predispute arbitration agreement means an agreement to arbitrate a dispute that has not yet arisen at the time of the making of the agreement; and (6) the term predispute joint-action waiver means an agreement, whether or not part of a predispute arbitration agreement, that would prohibit, or waive the right of, one of the parties to the agreement to participate in a joint, class, or collective action in a judicial, arbitral, administrative, or other forum, concerning a dispute that has not yet arisen at the time of the making of the agreement. 502. No validity or enforceability (a) In general Notwithstanding any other provision of this title, no predispute arbitration agreement or predispute joint-action waiver shall be valid or enforceable with respect to an employment dispute, consumer dispute, antitrust dispute, or civil rights dispute. (b) Applicability (1) In general An issue as to whether this chapter applies with respect to a dispute shall be determined under Federal law. The applicability of this chapter to an agreement to arbitrate and the validity and enforceability of an agreement to which this chapter applies shall be determined by a court, rather than an arbitrator, irrespective of whether the party resisting arbitration challenges the arbitration agreement specifically or in conjunction with other terms of the contract containing such agreement, and irrespective of whether the agreement purports to delegate such determinations to an arbitrator. (2) Collective bargaining agreements Nothing in this chapter shall apply to any arbitration provision in a contract between an employer and a labor organization or between labor organizations, except that no such arbitration provision shall have the effect of waiving the right of a worker to seek judicial enforcement of a right arising under a provision of the Constitution of the United States, a State constitution, or a Federal or State statute, or public policy arising therefrom. .\n##### (b) Technical and conforming amendments\n**(1) In general**\nTitle 9 of the United States Code is amended\u2014\n**(A)**\nin section 1, by striking of seamen, and all that follows through interstate commerce and inserting of individuals, regardless of whether the individuals are designated as employees or independent contractors for other purposes ;\n**(B)**\nin section 2, by inserting or 5 before the period at the end;\n**(C)**\nin section 208, in the second sentence, by inserting or 5 before the period at the end; and\n**(D)**\nin section 307, in the second sentence, by inserting or 5 before the period at the end.\n**(2) Table of chapters**\nThe table of chapters of title 9, United States Code, is amended by adding at the end the following:\n5. Arbitration of employment, consumer, antitrust, and civil rights disputes 501 .\n#### 4. Effective date\nThis Act, and the amendments made by this Act, shall take effect on the date of enactment of this Act and shall apply with respect to any dispute or claim that arises or accrues on or after such date.",
      "versionDate": "2025-09-15",
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
        "actionDate": "2025-09-15",
        "text": "Referred to the House Committee on the Judiciary."
      },
      "number": "5350",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "FAIR Act of 2025",
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
        "name": "Law",
        "updateDate": "2025-09-29T13:33:00Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-09-15",
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
          "measure-id": "id119s2799",
          "measure-number": "2799",
          "measure-type": "s",
          "orig-publish-date": "2025-09-15",
          "originChamber": "SENATE",
          "update-date": "2026-03-31"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s2799v00",
            "update-date": "2026-03-31"
          },
          "action-date": "2025-09-15",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><b>Forced Arbitration Injustice Repeal Act</b></p> <p>This bill prohibits a predispute arbitration agreement from being valid or enforceable if it requires arbitration of an employment, consumer, antitrust, or civil rights dispute.</p>"
        },
        "title": "Forced Arbitration Injustice Repeal Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s2799.xml",
    "summary": {
      "actionDate": "2025-09-15",
      "actionDesc": "Introduced in Senate",
      "text": "<p><b>Forced Arbitration Injustice Repeal Act</b></p> <p>This bill prohibits a predispute arbitration agreement from being valid or enforceable if it requires arbitration of an employment, consumer, antitrust, or civil rights dispute.</p>",
      "updateDate": "2026-03-31",
      "versionCode": "id119s2799"
    },
    "title": "Forced Arbitration Injustice Repeal Act"
  },
  "summaries": [
    {
      "actionDate": "2025-09-15",
      "actionDesc": "Introduced in Senate",
      "text": "<p><b>Forced Arbitration Injustice Repeal Act</b></p> <p>This bill prohibits a predispute arbitration agreement from being valid or enforceable if it requires arbitration of an employment, consumer, antitrust, or civil rights dispute.</p>",
      "updateDate": "2026-03-31",
      "versionCode": "id119s2799"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-09-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2799is.xml"
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
      "title": "Forced Arbitration Injustice Repeal Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-27T03:38:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Forced Arbitration Injustice Repeal Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-27T03:38:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title 9 of the United States Code with respect to arbitration.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-27T03:33:23Z"
    }
  ]
}
```
